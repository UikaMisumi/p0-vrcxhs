# 深度调研：LLM 驱动的形式化验证 / 可验证代码生成（Vericoding）

> 撰写日期：2026-10-06 ｜ 读者：考虑进入该领域的 CS 研究者
> 证据说明：数字与论文均来自检索摘要（见文末 Sources）；标注"(背景知识)"者来自作者既有知识，"(待核实)"者为检索未能确认的细节。所有 arXiv 编号按检索结果原样给出。

---

## 1. 定义、问题与"为什么是现在"

**一句话定义**：让 LLM 同时产出 *代码 + 形式规约 + 机器可检查的证明*（Verus/Dafny/Lean 4/F\*/Rocq/Isabelle），以证明检查器而非测试来判定正确性；MIT/BAIF 团队将其命名为 **vericoding**，以区别于"vibe coding"。

**它解决什么问题**：
- AI 生成代码的"验证瓶颈"：2026 年调查称 AI 占提交代码的 42%，但 96% 的开发者不完全信任 AI 代码（来自 SiliconANGLE/融资报道摘要）。测试只能抽样，SWE-Proof 发现 **约 1/4 通过隐藏测试的补丁存在反例**。
- 形式化验证的历史瓶颈是**人力成本**：例如 Aeneas 验证的密码库中，16.7 KLOC Rust 对应 237 KLOC Lean（约 14:1）。若 LLM 能写证明，这一成本曲线将被改写（Kleppmann, 2025-12 的预言）。
- 证明检查器对 LLM 幻觉"免疫"：错误证明不会被接受，因此它也是理想的 RL 奖励信号。

**为什么是现在（2024→2026 发生了什么）**：
1. **能力跃迁**：Dafny 纯验证（补全注释）一年内从 68%（DafnyBench, 2024-06）升至 96%（vericoding 论文, 2025-09）；Lean vericoding 子集上 GPT-5.4 + agent 循环达 95.0%（MIT, 2026-05）；Harmonic Aristotle 在 VERINA 上解决 96.8%。
2. **数学定理证明外溢**：AlphaProof/Aristotle/Seed-Prover/Leanstral 等在 IMO/Putnam 上的 RL+Lean 管线被迁移到代码验证（Goedel-Code-Prover, Leanstral 1.5 "在 57 个仓库中发现 5 个未知 bug"）。
3. **验证器友好的工业语言成熟**：Verus（Rust）、Aeneas/Hax（Rust→Lean）、Dafny→Java（AWS 授权引擎 2024 上线，3 倍性能提升）。
4. **数据瓶颈被合成数据打破**：SAFE、AlphaVerus、VeruSyn（690 万条已验证 Verus 程序）。
5. **资本与资助到位**：Axiom $200M A 轮（2026-03）、Theorem $6M 种子轮、Harmonic、Logical Intelligence；ARIA Safeguarded AI £59M。
6. **评测从函数级走向仓库级**：RVBench、VeriSoftBench、Vero、SWE-Proof（2025-09→2026-09）。

---

## 2. 技术版图（8 个细分方向）

### 2.1 证明/注释合成（Proof synthesis：给定代码+规约，补全不变量、引理、tactic）
- **是什么**：最成熟的子任务；输入固定，验证器给出 0/1 判定。
- **代表作**：
  - DafnyBench（Harvard/MIT, 2024-06, NeurIPS'24 D&B）：750+ 程序、约 53k 行；最佳 68% → 后续 96%。https://arxiv.org/abs/2406.08467
  - AutoVerus（MSR 等, 2024-09, OOPSLA'25 杰出 Artifact）：多 agent 模仿专家三阶段，150 题 VerusBench 上 >90%。https://arxiv.org/abs/2409.13082
  - Rango（UMass/UCSD/INESC-ID, 2024-12, ICSE'25 杰出论文）：检索增强 Rocq 证明，CoqStoq 上 32.0%（比 Tactician 多 29%）。https://arxiv.org/abs/2412.14063
  - Goedel-Code-Prover-8B（Goedel-LM/普林斯顿(待核实), 2026-03）：层次化分解+混合 RL，在 Verina/CLEVER/AlgoVeri 证明成功率 68.8%/54.0%/62.3%，共 427 题 62.0%，是最强基线 2.6×。https://arxiv.org/abs/2603.19329
- **SOTA**：Dafny/Verus 函数级接近饱和（>90%）；Lean 代码证明 60–97% 视基准而定。
- **核心开放问题**：长证明（平均 8–17 个辅助引理、130–167 行，最长 680 行）的规划与引理发明；SMT 不稳定性（brittleness）。

### 2.2 规约生成与规约质量评估（Spec synthesis / spec faithfulness）
- **是什么**：从自然语言意图写出 pre/post-condition，并判断"规约是否忠实"——这是整个领域的阿喀琉斯之踵。
- **代表作**：
  - nl2postcond（MSR, 2023-10, FSE'24）：GPT-4 生成的后置条件平均可区分 3/4 变异体，捕获 Defects4J 64 个真实 bug。https://arxiv.org/abs/2310.01831
  - Clover（Stanford/VMware, 2023-10, SAIV'24）：代码/docstring/注释三方一致性检查，正确实例接受率 87%、对抗错误 0 误报。https://arxiv.org/abs/2310.17807
  - Verus-SpecGym / Verus-SpecBench（CMU Parno 组等, 2026-05）：581 个 Codeforces 规约题，用可执行规约+Codeforces "hacks" 评测；Gemini 3.1 Pro 77.8%，其他前沿 51–58%，开源 21–26%；LLM-as-judge 漏掉 26% 的失败。https://arxiv.org/abs/2605.26457
  - SWE-Proof（2026-09）：自写规约的 agent 相对无规约基线**无增益**，仅 56% 的自写规约通过审计。https://arxiv.org/abs/2609.21190
- **核心开放问题**：没有 ground truth 时如何度量规约"完整性/忠实性"；规约等价性证明（CLEVER 的做法）代价高。

### 2.3 代码+证明联合生成（End-to-end vericoding）
- **代表作**：
  - Vericoding Benchmark（MIT Tegmark 组/BAIF, 2025-09, Dafny@POPL'26）：12,504 条规约（Dafny 3,029 / Verus 2,334 / Lean 7,141）；现成 LLM 成功率 Lean 27%、Verus 44%、Dafny 82%；加 NL 描述无显著帮助。https://arxiv.org/abs/2509.22908
  - CLEVER（Caltech 等, 2025-05, NeurIPS'25 D&B）：161 题 Lean，要求先证规约与隐藏真值等价，再证实现；前沿模型几乎全军覆没。https://arxiv.org/abs/2505.13938
  - VERINA（UC Berkeley Song 组, 2025-05, ICLR'26）：189 题；初版 o4-mini 代码 61.4%、规约 51.0%、**证明 3.6%**。https://arxiv.org/abs/2505.23135
  - P³（2026-08）：先做统一"程序-证明计划"再展开，较强基线 +4.6–11.2pp，API 成本 −40%。https://arxiv.org/abs/2608.09277
- **SOTA**：Lean 端到端在 AlgoVeri 上仍低（Gemini-3 Flash：Dafny 40.3% / Verus 24.7% / Lean 7.8%）。
- **开放问题**：如何让生成的程序"易于证明"（proof-aware program design）；跨语言能力不对齐。

### 2.4 证明修复与维护（Proof repair / proof engineering）
- **代表作**：Baldur（UMass/Google, 2023, FSE'23，整证生成+修复，背景知识）；APE-Bench I（2025-04，Mathlib4 真实 commit 的文件级编辑任务）https://arxiv.org/abs/2504.19110 ；ProofRepairBench（ICLR'26，127 个 Lean 修复问题）；CAPRI（2026-08，Isabelle 合约感知修复）https://arxiv.org/abs/2608.13459
- **开放问题**：库/语言版本升级导致的大规模证明腐烂；局部编辑强、复杂 proof engineering 显著退化（APE-Bench 结论）。

### 2.5 仓库级/系统级验证
- **代表作**：
  - RagVerus + RVBench（多伦多大学等, 2025-02/09, LMPL@SPLASH'25）：4 个 Verus 项目、755 个证明任务；RAG 带来 27% 相对提升。https://arxiv.org/abs/2502.05344 ，https://arxiv.org/abs/2509.25197
  - VeriSoftBench（UT Austin utopia-group, 2026-02）：500 个 Lean 证明义务；Mathlib 调优的证明器迁移很差，成功率与传递依赖深度强负相关。https://arxiv.org/abs/2602.18307
  - Selene（2024-01）：seL4 项目级 Isabelle 基准，GPT-4 平均 27.06%（340 定理）。https://arxiv.org/abs/2401.07663
  - Vero（UC Berkeley, 2026-08）：43 个多模块仓库、743 个 API、2,705 条规约；最强 agent 仅完整解决 27/43，最难仓库 0 规约。https://arxiv.org/abs/2608.13522
- **开放问题**：上下文选择（依赖闭包检索）、跨模块抽象/"数学架构"设计、增量验证。

### 2.6 用验证器做 RL 奖励 / 合成数据
- **代表作**：SAFE（MSR, 2024-10, ICLR'25）：自演化数据合成，52.52% vs GPT-4o 14.39% https://arxiv.org/abs/2410.15756 ；AlphaVerus（CMU, 2024-12, ICML'25）：翻译+Treefinement 树搜索+过滤错配规约防 reward hacking，Llama-3.1-70B 在 Verified-HumanEval 33% https://arxiv.org/abs/2412.06176 ；VeruSyn（MSR, 2026-02）：690 万已验证 Verus 程序，微调 Qwen2.5-Coder-32B，VerusBench Acc@100 83%（Claude Sonnet 4.5 为 76%）https://arxiv.org/abs/2602.04910 ；Leanstral 1.5（Mistral, 2026-07）：119B MoE/6B 激活，Apache-2.0，CISPO RL。https://mistral.ai/news/leanstral-1-5/
- **开放问题**：奖励被"空洞规约/作弊证明"攻破（`assume(false)`、`sorry`、平凡后置条件）；"没有固定奖励函数能随策略能力增长而保持有效"。

### 2.7 需求/系统规约的自动形式化（Autoformalization of requirements）
- **代表作**：nl2spec（CISPA, 2023-03, CAV'23）https://arxiv.org/abs/2303.04864 ；Req2LTL（2025, 航天需求 LTL 语义准确率 88.4%）https://arxiv.org/abs/2512.17334 (待核实对应关系)；LLM→TLA+ 合成（Loyola, 2025：语法正确 26.6%、语义正确仅 8.6%）https://ai4fm.cs.luc.edu/papers/gcasr-2025-tla-llm/
- **开放问题**：分布式/时序性质的语义正确率极低；需要人在回路的可解释对齐。

### 2.8 安全关键领域（密码库、内核、智能合约、zkVM）
- **代表作**：Aeneas 密码库扩展（Microsoft/Inria 等(待核实), 2026-09）：SHA-3、ML-KEM 等，16.7 KLOC Rust / 237 KLOC Lean，agent 写证明+协助形式化标准 https://arxiv.org/abs/2609.15648 ；Rust→Lean+AI 证明器经验报告（2026-05，以太坊基金会 zkEVM 项目，Plonky3/RISC Zero，Aristotle+Aleph 关闭结构性义务，复杂不变量仍需专家）https://arxiv.org/abs/2605.30106 ；LeVer（ACL'26，智能合约生成-验证-攻击-修复）；F\* PoPAI 数据集（MSR, 2024-05, ICSE'25，600K–940K 行 F\*，微调小模型媲美 GPT-4）https://arxiv.org/abs/2405.01787
- **开放问题**：领域规约（密码标准、硬件 intrinsics）的形式化本身是瓶颈；可信基（TCB：抽取工具、公理）审计。

---

## 3. 关键基准、数据集与工具

| 名称 | 测什么 | 规模 | 当前最佳（检索所见） | 链接 |
|---|---|---|---|---|
| DafnyBench | Dafny 注释补全 | 750+ 程序/53k 行 | 68%(2024) → ~96%(2025, vericoding 论文报告) | arxiv.org/abs/2406.08467 |
| VerusBench | Verus 证明合成 | 150 题 | AutoVerus >90%；VeruSyn-Qwen Acc@100 83% | arxiv.org/abs/2409.13082 |
| Vericoding Bench | 规约→代码+证明（3 语言） | 12,504 规约 | 原始 Lean 27/Verus 44/Dafny 82%；Lean 423 子集 GPT-5.4 agent 95.0% | arxiv.org/abs/2509.22908 |
| VERINA | Lean 代码/规约/证明三任务 | 189 题 | 证明：Aristotle 96.8%（解决率）、Goedel-Code-Prover 68.8% | github.com/sunblaze-ucb/verina |
| CLEVER | Lean 规约等价+实现证明 | 161 题 | Goedel-Code-Prover 54.0%（证明阶段，待核实口径） | arxiv.org/abs/2505.13938 |
| AlgoVeri | 77 个经典算法，三语言同一契约 | 77×3 | Gemini-3 Flash Dafny 40.3/Verus 24.7/Lean 7.8%；GCP 证明 62.3% | arxiv.org/abs/2602.09464 |
| Verus-SpecBench | 规约自动形式化 | 581 题 | Gemini 3.1 Pro 77.8% | arxiv.org/abs/2605.26457 |
| RVBench | Verus 仓库级证明 | 755 任务 | RagVerus（+27% 相对） | github.com/GouQi12138/RVBench |
| VeriSoftBench | Lean 仓库级证明义务 | 500 | 远未饱和（具体数字待核实） | github.com/utopia-group/VeriSoftBench |
| Vero | 仓库级代码+证明（Lean） | 43 仓库/2,705 规约 | 27/43 仓库完整解决 | github.com/sunblaze-ucb/vero |
| SWE-Proof | 真实 issue + 形式验证 | 500 issue | 正确形式规约使 Claude Opus 4.8 从 85%→95% | arxiv.org/abs/2609.21190 |
| CoqStoq | Rocq 证明合成 | 2,226 项目/196,929 定理 | Rango 32.0% | arxiv.org/abs/2412.14063 |
| Selene | seL4 Isabelle | 340 定理 | GPT-4 27.06%（2024） | arxiv.org/abs/2401.07663 |
| miniCodeProps | Lean 程序性质证明 | 201 | 待核实 | arxiv.org/abs/2406.11915 |
| F\* PoPAI | F\* 类型导向程序+证明 | 32K–54K 定义 | 微调小模型≈GPT-4 | fstar-lang.org/popai |

**工具链**：Verus、Dafny、Lean 4 + Mathlib/LeanDojo/Lean Copilot（背景知识）、Aeneas/Charon、Hax、F\*、Kani、Rocq、Isabelle；开源模型 Goedel-Code-Prover-8B、Leanstral 1.5；跨基准索引 sotaverified.org。

---

## 4. 主要玩家

**学术**
- Microsoft Research（Shan Lu、Chris Hawblitzel、Jay Lorch 等：Verus、AutoVerus、SAFE、VeruSyn；Nikhil Swamy：F\*；Jonathan Protzenko/Son Ho：Aeneas，背景知识）
- CMU（Bryan Parno：Verus 共同作者、AlphaVerus、Verus-SpecGym；Sean Welleck：AlphaVerus）
- UC Berkeley RDI（Dawn Song：VERINA、Vero）
- MIT（Max Tegmark/BAIF：vericoding benchmark、agent 树搜索论文）
- Harvard（Nada Amin：DafnyBench）；Stanford（Clark Barrett：Clover）
- Caltech（Anima Anandkumar：CLEVER，背景知识）；Princeton（Chi Jin：Goedel-Prover 系，背景知识）
- UT Austin（Isil Dillig：VeriSoftBench）；UMass/UCSD（Yuriy Brun、Sorin Lerner：Baldur、Rango）
- 多伦多大学（RagVerus/RVBench）；CISPA（nl2spec）

**工业实验室**：Microsoft（Verus/F\*/Aeneas 生态）、AWS（Dafny、Cedar、Bedrock Automated Reasoning checks、Kani）、Google DeepMind（AlphaProof，背景知识）、Mistral（Leanstral）、OpenAI/Anthropic/Google（前沿模型是多数基准的榜首）、ByteDance Seed（Seed-Prover，背景知识）。

**创业公司**
| 公司 | 方向 | 融资 |
|---|---|---|
| Axiom | Lean 可验证 AI，AxiomProver（Putnam 2025 120/120） | $200M A 轮（Menlo 领投，2026-03） |
| Harmonic | Aristotle，扩展到代码/硬件验证 | 多轮，Series C 约 $120M（背景知识，待核实） |
| Theorem（YC S25） | AI 代码自动验证 | $6M 种子（Khosla 领投） |
| Logical Intelligence | Aleph 证明器 | 待核实 |
| Qodo / NxCode | 偏测试/审查的"AI 代码验证" | $70M B 轮 / 七位数（非形式化，作对照） |

**资助方**：ARIA Safeguarded AI（£59M，2025-11 转向 TA1 与形式化验证防火墙）；以太坊基金会 zkEVM 形式化验证项目；Amazon Automated Reasoning 研究资助。

---

## 5. 时间线（2023-10 → 2026-09）

| 时间 | 里程碑 |
|---|---|
| 2023-10 | Clover（一致性检查）与 nl2postcond 提出，奠定"规约质量"问题 |
| 2024-01 | Selene：首个 seL4 项目级证明基准 |
| 2024-05 | F\* PoPAI 数据集（600K 行），微调小模型可比 GPT-4 |
| 2024-06 | DafnyBench（最佳 68%）、miniCodeProps 发布 |
| 2024-09 | AutoVerus：VerusBench >90% |
| 2024-10 | SAFE：自演化合成数据，52.5% vs 14.4% |
| 2024-12 | AlphaVerus（首个在 Verified-HumanEval 非零）、Rango |
| 2025-05 | CLEVER 与 VERINA 发布（端到端证明率仅 3.6%） |
| 2025-09 | Vericoding Benchmark（12.5K 规约）；RVBench 仓库级 |
| 2025-12 | Kleppmann《AI 将使形式化验证主流化》引发广泛讨论 |
| 2026-02 | AlgoVeri、VeriSoftBench、VeruSyn（690 万程序） |
| 2026-03 | Axiom $200M；Goedel-Code-Prover-8B（62.0%）；Leanstral 首发 |
| 2026-05 | Verus-SpecGym；GPT-5.4 agent 在 Lean vericoding 子集 95%；Rust→Lean+AI 证明器 zkEVM 经验报告 |
| 2026-07 | Leanstral 1.5 开源（Apache-2.0） |
| 2026-08/09 | Vero（仓库级 27/43）、P³、SWE-Proof（形式验证推翻 1/4 测试通过补丁）、Aeneas 密码库规模化 |

（Aristotle VERINA 96.8% 的发布日期待核实，约在 2025 末—2026 上半年。）

---

## 6. 研究机会（按"适合学术实验室"排序）

| # | 问题 | 算力 | 难度 | 说明 |
|---|---|---|---|---|
| 1 | **规约忠实性的自动评估** | 低 | 中 | 无 ground truth 时用可执行规约+对抗输入（如 Codeforces hacks）、变异测试、规约间蕴含证明来打分；SWE-Proof/SpecGym 均指出这是首要瓶颈 |
| 2 | **空洞规约/作弊证明检测器**（vacuity、`assume`、axiom 滥用、过弱后置条件） | 低 | 低-中 | 直接服务于所有 RL 管线与基准可信度，可做成通用 lint + 基准审计 |
| 3 | **仓库级上下文检索与引理库构建** | 低-中 | 中 | VeriSoftBench 显示依赖闭包检索有效但远未解决；可研究依赖图感知检索、自动抽取可复用引理 |
| 4 | **证明修复/版本迁移基准与方法**（Verus/Lean/Rocq 升级） | 低-中 | 中 | 挖掘真实 commit 历史，任务天然可验证、工业需求明确 |
| 5 | **跨验证语言迁移**（Dafny→Verus→Lean 的统一中间表示或课程） | 中 | 中-高 | AlgoVeri 显示同一契约下 Dafny 40%/Lean 8%；可研究"先在 Dafny 证、再翻译到 Lean" |
| 6 | **"易证明"的程序设计 / 程序-证明联合规划** | 中 | 高 | P³ 初步证明有效；可研究以证明复杂度为目标的代码重构 |
| 7 | **需求→时序/分布式规约（TLA+/LTL）+ 模型检测闭环** | 低-中 | 高 | TLA+ 语义正确率仅 8.6%，空间大；需要领域伙伴 |
| 8 | **以验证器为奖励的小模型 RL**（8B–32B），研究奖励塑形与 reward hacking | 高 | 中 | Goedel-Code-Prover、VeruSyn 证明小模型可追平前沿；需要数百 GPU·天 |
| 9 | **形式验证驱动的 SWE agent**（issue→规约→补丁→证明） | 中-高 | 高 | SWE-Proof 指出自写规约无增益——如何让 agent 写出"有用的"规约 |
| 10 | **TCB 与抽取工具的可信性**（Aeneas/Hax 的翻译正确性、公理审计） | 低 | 高 | 偏 PL 理论，适合 PL 组；与 LLM 结合在于"LLM 生成的公理/桥接引理"的审计 |

---

## 7. 入门路径

**10 篇必读（按顺序）**
1. Clover（2310.17807）——理解"代码/文档/规约三方一致"这一核心思想与规约问题。
2. nl2postcond（2310.01831）——规约质量如何度量（正确性+区分力）。
3. DafnyBench（2406.08467）——最易上手的证明合成基准与评测协议。
4. AutoVerus（2409.13082）——agent 化证明生成的标准范式（生成→精炼→按错误调试）。
5. SAFE（2410.15756）——验证器驱动的自演化数据合成。
6. AlphaVerus（2412.06176）——树搜索 + reward hacking 过滤，联合生成的雏形。
7. VERINA（2505.23135）与 CLEVER（2505.13938）——端到端任务的模块化定义与规约等价性评测。
8. Vericoding Benchmark（2509.22908）——领域命名与三语言大规模全景。
9. Goedel-Code-Prover（2603.19329）——当前开源 SOTA 的训练配方（层次分解+混合 RL）。
10. SWE-Proof（2609.21190）+ Vero（2608.13522）——前沿：仓库级与"规约是瓶颈"的实证。

**开源代码库**：verus-lang/verus；dafny-lang/dafny；sunblaze-ucb/verina、sunblaze-ucb/vero；utopia-group/VeriSoftBench；GouQi12138/RVBench；AeneasVerif/aeneas（背景知识）；Goedel-LM 模型（HF）；Leanstral 1.5（HF, Apache-2.0）；LeanDojo/Lean Copilot（背景知识）。

**3 个月入门项目："规约审计器 SpecAudit"**
- 第 1–3 周：搭建 Verus + Lean 环境，跑通 VERINA 与 Verus-SpecBench 的评测脚本；用一个开源 8B 模型 + 一个 API 模型复现 baseline。
- 第 4–7 周：实现规约审计器：(a) 空洞性检测（尝试用 `simp/omega/auto` 或 SMT 证明 `post ⇒ True`/`pre = False`）；(b) 可执行规约的差分测试（随机/边界输入 + 参考实现）；(c) 变异体区分率。
- 第 8–10 周：对 3–4 个公开基准（Vericoding、VERINA、AlgoVeri、DafnyBench）做"规约健康度"审计，量化有缺陷的规约比例及其对排行榜的影响。
- 第 11–12 周：把审计分数作为 RL/best-of-N 的附加奖励，在 Verus-SpecBench 上展示规约忠实度提升；产出一篇 workshop/短文（目标：Dafny/LMPL/AI4Math workshop 或 FSE/ICSE 新思想轨）。
- 资源：单机 1–4 张 GPU + 少量 API 预算即可。

---

## 8. 风险与争议

1. **规约鸿沟（specification gap）**：证明只保证"代码满足规约"，规约错了就是"形式正确地做错事"。SWE-Proof：自写规约 agent 无增益、56% 通过审计；SpecGym：规约会遗漏前提、接受错误输出。这是领域最大的哲学与工程风险。
2. **基准污染与饱和**：许多基准源自 HumanEval/MBPP/Codeforces/公开仓库；DafnyBench、VerusBench 已近饱和；Aristotle 在 VERINA 上还发现 23 条"规约为假"，说明基准本身有错误。
3. **Reward hacking**：RLVR 下模型会利用验证器漏洞（空洞规约、`assume`/`sorry`/axiom、超时/资源限制的边界）；AlphaVerus 已专门过滤错配规约。
4. **被通用编码 agent 吸收**：前沿通用模型（GPT-5.x、Claude、Gemini 3.x）在多数基准上占榜首，纯"提示工程+agent 框架"类工作的生命周期短；学术组应聚焦评测、规约、数据与理论，而非与前沿模型拼原始分数。
5. **语言碎片化**：Dafny/Verus/Lean/F\*/Rocq 生态割裂，结果不可比（AlgoVeri 的动机）；押错工具链有沉没成本。目前势头：Lean（数学外溢+Aeneas）与 Verus（系统软件）最强。
6. **TCB 与可审计性**：抽取工具（Aeneas/Hax）、SMT 求解器、公理都在可信基内；"AI 写证明"不等于"整条链可信"。
7. **商业炒作**："验证"一词被非形式化工具（测试/审查类）稀释；Axiom/Harmonic 的商业回报尚待检验。
8. **复杂不变量仍需专家**：zkEVM 经验报告显示 AI 擅长结构性义务，核心不变量仍靠人——"全自动"叙事需谨慎。

---

## 9. Sources

- https://arxiv.org/abs/2509.22908 （Vericoding benchmark）; https://popl26.sigplan.org/details/dafny-2026-papers/13/A-benchmark-for-vericoding-formally-verified-program-synthesis
- https://arxiv.org/abs/2406.08467 （DafnyBench）; https://neurips.cc/virtual/2024/98516
- https://arxiv.org/abs/2409.13082 ; https://www.microsoft.com/en-us/research/publication/autoverus-automated-proof-generation-for-rust-code/
- https://arxiv.org/abs/2410.15756 （SAFE）
- https://arxiv.org/abs/2412.06176 （AlphaVerus）; https://proceedings.mlr.press/v267/aggarwal25a.html
- https://arxiv.org/abs/2505.13938 （CLEVER）
- https://arxiv.org/abs/2505.23135 ; https://github.com/sunblaze-ucb/verina （VERINA）
- https://arxiv.org/abs/2603.19329 （Goedel-Code-Prover）
- https://arxiv.org/abs/2602.09464 （AlgoVeri）; https://icml.cc/virtual/2026/poster/61803
- https://arxiv.org/abs/2602.18307 ; https://github.com/utopia-group/VeriSoftBench
- https://arxiv.org/abs/2608.13522 ; https://github.com/sunblaze-ucb/vero ; https://rdi.berkeley.edu/blog/vero/
- https://arxiv.org/abs/2609.21190 （SWE-Proof）
- https://arxiv.org/abs/2502.05344 ; https://arxiv.org/abs/2509.25197 ; https://github.com/GouQi12138/RVBench
- https://arxiv.org/abs/2412.14063 （Rango/CoqStoq）
- https://arxiv.org/abs/2405.01787 ; https://fstar-lang.org/popai
- https://arxiv.org/abs/2401.07663 （Selene）; https://arxiv.org/abs/2406.11915 （miniCodeProps）
- https://arxiv.org/abs/2310.01831 （nl2postcond）; https://arxiv.org/abs/2310.17807 （Clover）
- https://arxiv.org/abs/2605.26457 （Verus-SpecGym）
- https://arxiv.org/abs/2602.04910 （VeruSyn）
- https://arxiv.org/abs/2608.09277 （P³）
- https://arxiv.org/abs/2605.27485 （MIT agent 树搜索 vericoding）
- https://arxiv.org/abs/2605.30106 （Rust→Lean + AI 证明器经验报告）; https://arxiv.org/abs/2609.15648 （Aeneas 密码库）
- https://arxiv.org/abs/2504.19110 （APE-Bench I）; https://www.iclr.cc/virtual/2026/10012643 （ProofRepairBench）; https://arxiv.org/abs/2608.13459 （CAPRI）
- https://arxiv.org/abs/2303.04864 （nl2spec）; https://ai4fm.cs.luc.edu/papers/gcasr-2025-tla-llm/ ; https://arxiv.org/abs/2512.17334
- https://aclanthology.org/2026.acl-long.1836.pdf （LeVer）; https://github.com/lfglabs-dev/verity
- https://harmonic.fun/news/verina-benchmark/
- https://mistral.ai/news/leanstral-1-5/
- https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html
- https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/
- https://venturebeat.com/security/theorem-wants-to-stop-ai-written-bugs-before-they-ship-and-just-raised-usd6m
- https://siliconangle.com/2026/03/30/ai-generated-code-verification-startup-qodo-raises-70m/
- https://www.aria.org.uk/safeguarded-ai/ ; https://www.longtermwiki.com/resources/kb-993eacf1d62c61ae
- https://aws.amazon.com/aws-startups/learn/prove-it-part-2-formal-logic-cedar-policies-and-the-economics-of-verification/
