#!/usr/bin/env python3
"""Emergence Score (新兴度评分) calculator.

Reads per-field evidence files (evidence/*.json) and historical back-test cases
(backtest.json), computes the Emergence Score, runs a weight-sensitivity
analysis, and writes results.json + results.md.

Usage: python3 score.py [--samples N] [--seed S]
Stdlib only.
"""
import argparse
import glob
import json
import math
import os
import random
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))

DIMS = ["G", "S", "C", "E", "R", "H", "X"]
WEIGHTS = {"G": 0.20, "S": 0.15, "C": 0.20, "E": 0.10, "R": 0.10, "H": 0.10, "X": 0.15}
DIM_NAMES = {
    "G": "增长动量", "S": "阶段窗口", "C": "能力拐点", "E": "使能条件",
    "R": "资源注入", "H": "学术空间", "X": "外溢平台性", "P": "风险扣分",
}
# Sub-indices: 势 = is it taking off now; 质 = will it matter / can you work on it.
MOMENTUM = ["G", "S", "C"]
SUBSTANCE = ["E", "R", "H", "X"]
# Dirichlet concentration for weight perturbation; 40 gives roughly ±0.05 on each weight.
CONCENTRATION = 40


def emergence_score(s, weights=WEIGHTS):
    return 20 * sum(weights[d] * s[d] for d in DIMS) - s.get("P", 0)


def sub_index(s, dims):
    total = sum(WEIGHTS[d] for d in dims)
    return 20 * sum(WEIGHTS[d] * s[d] for d in dims) / total


def growth_to_G(counts):
    """Map yearly paper counts {year: n} to a G score using 2-year CAGR + acceleration.

    Used when real bibliometric counts are available (e.g. arXiv keyword queries).
    """
    years = sorted(int(y) for y in counts)
    if len(years) < 3:
        raise ValueError("need >= 3 years of counts")
    c = [max(counts[str(y)] if str(y) in counts else counts[y], 1) for y in years[-3:]]
    cagr = math.sqrt(c[2] / c[0]) - 1
    accel = (c[2] / c[1]) > (c[1] / c[0])
    if cagr < 0:
        return 0
    for threshold, g in ((1.0, 4.5), (0.6, 4), (0.3, 3), (0.1, 2)):
        if cagr >= threshold:
            return min(5, g + (0.5 if accel else 0))
    return 1


def dirichlet(rng, alphas):
    xs = [rng.gammavariate(a, 1) for a in alphas]
    total = sum(xs)
    return [x / total for x in xs]


def sensitivity(fields, samples, seed):
    rng = random.Random(seed)
    alphas = [WEIGHTS[d] * CONCENTRATION for d in DIMS]
    ranks = {f["id"]: [] for f in fields}
    for _ in range(samples):
        w = dict(zip(DIMS, dirichlet(rng, alphas)))
        ordered = sorted(fields, key=lambda f: -emergence_score(f["scores"], w))
        for i, f in enumerate(ordered, 1):
            ranks[f["id"]].append(i)
    out = {}
    for fid, r in ranks.items():
        r.sort()
        out[fid] = {
            "median_rank": statistics.median(r),
            "rank_p10": r[int(0.1 * len(r))],
            "rank_p90": r[int(0.9 * len(r)) - 1],
            "p_top10": sum(1 for x in r if x <= 10) / len(r),
        }
    return out


def tier(score):
    if score >= 80:
        return "A 强烈关注"
    if score >= 72:
        return "B 值得投入"
    if score >= 64:
        return "C 观察"
    return "D 暂缓/已主流"


def load_fields():
    fields = []
    for path in sorted(glob.glob(os.path.join(HERE, "evidence", "*.json"))):
        with open(path, encoding="utf-8") as fh:
            for f in json.load(fh):
                if "counts" in f:
                    f["scores"]["G"] = growth_to_G(f["counts"])
                missing = [d for d in DIMS + ["P"] if d not in f["scores"]]
                if missing:
                    raise ValueError(f"{f['id']} missing scores {missing}")
                fields.append(f)
    ids = [f["id"] for f in fields]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise ValueError(f"duplicate field ids: {sorted(dupes)}")
    return fields


def fmt_scores(s):
    return " ".join(f"{d}{s[d]:g}" for d in DIMS + ["P"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20261006)
    args = ap.parse_args()

    fields = load_fields()
    for f in fields:
        f["score"] = round(emergence_score(f["scores"]), 1)
        f["momentum"] = round(sub_index(f["scores"], MOMENTUM), 1)
        f["substance"] = round(sub_index(f["scores"], SUBSTANCE), 1)
        f["tier"] = tier(f["score"])
    fields.sort(key=lambda f: -f["score"])
    sens = sensitivity(fields, args.samples, args.seed)

    with open(os.path.join(HERE, "backtest.json"), encoding="utf-8") as fh:
        backtest = json.load(fh)
    for b in backtest:
        b["score"] = round(emergence_score(b["scores"]), 1)
    backtest.sort(key=lambda b: -b["score"])

    results = {
        "weights": WEIGHTS,
        "fields": [
            {k: f[k] for k in ("id", "name_zh", "name_en", "domain", "scores",
                               "score", "momentum", "substance", "tier")}
            | {"sensitivity": sens[f["id"]]}
            for f in fields
        ],
        "backtest": backtest,
    }
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=2)

    lines = [
        "# 评分结果（由 score.py 自动生成，勿手改）",
        "",
        f"权重：{', '.join(f'{DIM_NAMES[d]} {d}={WEIGHTS[d]:.2f}' for d in DIMS)}；"
        "总分 = 20 × Σ(w·s) − P。",
        f"敏感性：Dirichlet(浓度 {CONCENTRATION}) 随机扰动权重 {args.samples} 次，"
        "报告排名中位数、10–90% 分位区间与进入前 10 的概率。",
        "",
        "## 候选领域排名",
        "",
        "| # | 领域 | 方向 | 总分 | 势(G,S,C) | 质(E,R,H,X) | 分项 | 排名区间 | P(前10) | 档位 |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, f in enumerate(fields, 1):
        s = sens[f["id"]]
        lines.append(
            f"| {i} | {f['name_zh']}<br><sub>{f['name_en']}</sub> | {f['domain']} | "
            f"**{f['score']}** | {f['momentum']} | {f['substance']} | "
            f"`{fmt_scores(f['scores'])}` | {s['rank_p10']}–{s['rank_p90']} | "
            f"{s['p_top10']:.0%} | {f['tier']} |"
        )
    lines += [
        "",
        "## 历史回测（事前视角打分 vs 实际走向）",
        "",
        "| 案例 | 时点 | 总分 | 分项 | 实际走向 |",
        "|---|---|---|---|---|",
    ]
    for b in backtest:
        lines.append(
            f"| {b['name']} | {b['as_of']} | **{b['score']}** | "
            f"`{fmt_scores(b['scores'])}` | {b['outcome']} |"
        )
    with open(os.path.join(HERE, "results.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"{len(fields)} fields scored; top 10:")
    for f in fields[:10]:
        print(f"  {f['score']:5.1f}  {f['name_zh']}  (P(top10)={sens[f['id']]['p_top10']:.0%})")


if __name__ == "__main__":
    main()
