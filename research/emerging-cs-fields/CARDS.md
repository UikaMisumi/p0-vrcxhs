# 领域卡片（由 score.py 自动生成，勿手改；内容来自 evidence/*.json）

## 1. LLM驱动的形式化验证 / 可验证代码生成 — 80.5（A 强烈关注）

*LLM-driven Formal Verification & Verified Code Generation ("vericoding": Verus/Dafny/Lean code with proofs)* · AI-可信与推理 · `G4.5 S5 C4 E4 R3.5 H5 X4 P3` · 排名区间 1–2

**拐点事件**：2025-09 MIT/Tegmark等发布Vericoding基准，显示现成LLM在Dafny上已达82%、一年内纯验证从68%升至96%；2026年Certora用LLM两周完成zlib关键函数内存安全形式化证明。待到来的“GPT-3时刻”：AI智能体端到端产出真实规模（万行级）带完整证明的软件仓库。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | 纯Dafny验证成功率一年内从68%升至96%；2025-2026相继出现Vericoding基准（12,504个规约）、VeriSoftBench（500个仓库级Lean义务）、Vero（43个多模块仓库）、VeruSyn（690万条已验证Rust程序）、KVerus等；未找到论文总量统计，按定性证据评4.5。 |
| 阶段窗口 S | 5 | 社区很小（PL/FM与ML交叉），POPL 2026 Dafny workshop、新基准刚成形，顶会占比远低于1%，尚无共识范式（规约生成、证明搜索、语言选择均未定），处于典型“2021窗口”。 |
| 能力拐点 C | 4 | 现成LLM在Vericoding基准上Dafny 82%、Verus 44%、Lean 27%；AutoVerus在150个任务上>90%；Certora借助LLM两周内完成zlib inflate_table内存安全证明（约2万行Lean）——强存在性证明，但仓库级与规约侧扩展性未明。 |
| 使能条件 E | 4 | Dafny/Verus/Lean工具链开源，基准与合成数据（VeruSyn）可得；瓶颈是高质量规约与真实工程级训练数据。 |
| 资源注入 R | 3.5 | Microsoft Research（Verus/AutoVerus）、AWS、Certora投入；Axiom以“可验证AI代码”为目标获2亿美元；Atlas Computing、Schmidt Sciences等资助；前沿实验室尚未作为核心方向。 |
| 学术空间 H | 5 | 规约获取与验证、仓库级证明、证明修复与维护、跨语言验证等根本问题开放，且以PL方法+中等算力即可取得成果。 |
| 外溢平台性 X | 4 | 若成熟可重塑软件工程与安全（AI写代码+机器可检证明），也为AI安全提供可信执行基础，是潜在通用底座。 |
| 风险扣分 P | 3 | “规约即正确”问题（错误规约下的已验证代码）、工业采纳门槛高，可能被AI数学/通用编码智能体方向吸收；扣3分。 |

**关键证据**：

- 2025-09 Vericoding基准含12,504个形式化规约（Dafny 3,029 / Verus 2,334 / Lean 7,141）；现成LLM成功率Lean 27%、Verus 44%、Dafny 82%；纯Dafny验证一年内从68%升到96% [来源](https://arxiv.org/abs/2509.22908v1)
- 2024-09 AutoVerus（MSR）多智能体为Rust/Verus自动生成证明，在150个非平凡任务上成功率>90% [来源](https://www.microsoft.com/en-us/research/?p=1097760)
- 2026-02 VeruSyn数据合成管线生成690万条带规约与证明的已验证Rust程序 [来源](https://arxiv.org/abs/2602.04910v2)
- 2026-05 Certora借助Lean与LLM在两周内完成zlib inflate_table（266行C）的内存安全与终止性证明，约2万行Lean [来源](https://www.certora.com/blog/formally-verifying-zlib-memory-safety-with-lean)
- 2026-08 Vero基准评测AI智能体在Lean 4中联合合成实现与证明的仓库级能力（43个多模块实例）；VeriSoftBench含500个仓库级Lean证明义务 [来源](https://www.alphaxiv.org/abs/2608.13522)
- 2026-03 Axiom以“Verified AI”定位融资2亿美元，目标是证明AI生成代码可安全使用 [来源](https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/)

**开放问题**：

- 从自然语言意图得到正确且完整的形式化规约，并评估规约本身的质量
- 仓库级/跨模块验证：证明的组合、维护与随代码演化的自动修复
- 将验证扩展到并发、系统级代码与C/Rust等主流语言，并降低证明体积与验证时间

**切入点**：

- 在Vericoding/VerusBench/VeriSoftBench上研究检索增强+验证器反馈的证明修复与规约生成，用小模型+RL验证可奖励信号
- 选一个真实开源组件（如解析器、压缩库、密码库函数）做LLM辅助的端到端验证案例研究，并沉淀为新基准

---

## 2. 自我改进与自博弈（LLM引导的进化搜索/开放式学习） — 79.0（A 强烈关注）

*Self-Improvement & Self-Play (LLM-guided Evolutionary Search, Open-Endedness)* · AI-模型与方法 · `G4.5 S4.5 C4 E4 R4.5 H5 X5 P6` · 排名区间 1–4

**拐点事件**：2025年5月DeepMind发布AlphaEvolve：LLM引导的进化代码搜索在数学（4x4复矩阵乘法48次）与生产系统中产生超越人类的新结果；同月Darwin Gödel Machine与Absolute Zero展示自修改智能体与零数据自博弈推理。下一个拐点将是闭环自动化AI研究产生可复现的模型级改进。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | 2025年AlphaEvolve、Darwin Gödel Machine、Absolute Zero、SEAL等集中出现，并迅速有开源复现（OpenEvolve、ShinkaEvolve，背景知识）；2026年出现专门公司。未找到精确论文计数，定性判断60-100%+/年。 |
| 阶段窗口 S | 4.5 | 无共识范式（进化搜索、自博弈课程、自奖励、自修改代码智能体并存），顶会份额小、处于起飞期；但已有大额资本与概念热度，给4.5。 |
| 能力拐点 C | 4 | AlphaEvolve在50+数学开放问题中约20%找到优于已知的新构造，4x4复矩阵乘法48次乘法（56年来首次改进），并部署于Google数据中心调度与训练内核；DGM把SWE-bench从20%提升到50%；AZR零外部数据达到SOTA。强存在性证明，但仅限有自动评估器的领域，scaling规律不清，给4。 |
| 使能条件 E | 4 | 前沿LLM API与开源模型、开源进化框架可用；关键瓶颈是可靠的自动评估器与API调用成本。 |
| 资源注入 R | 4.5 | DeepMind（AlphaEvolve）、Sakana（DGM）、Recursive Superintelligence 2026-05融资6.5亿美元（估值46.5亿，GV/NVIDIA/AMD参投）；接近但未明确达到多家前沿实验室+>$1B。 |
| 学术空间 H | 5 | 评估器设计、开放式探索的理论、防止奖励作弊、自改进的收敛/安全性等基础问题大量开放，用API级算力即可做出成果。 |
| 外溢平台性 X | 5 | 可成为算法设计、数学、科学发现、AI研究自动化的通用方法，外溢面极广。 |
| 风险扣分 P | 6 | '递归自我改进/超级智能'叙事炒作严重；收益受限于可验证评估器，开放域效果未证；结果依赖闭源前沿模型且算力成本高、复现性一般；存在安全与失控担忧。 |

**关键证据**：

- 2025-05 AlphaEvolve在50+数学开放问题中约75%复现最佳已知构造、约20%找到更优新构造；4x4复矩阵乘法用48次标量乘法（56年来首次改进） [来源](https://spectrum.ieee.org/amp/deepmind-alphaevolve-2672018683)
- 2025-05 AlphaEvolve已部署优化Google数据中心调度与LLM训练内核 [来源](https://towardsdatascience.com/googles-alphaevolve-is-evolving-new-algorithms-and-it-could-be-a-game-changer/)
- 2025-05 Darwin Gödel Machine 自修改编码智能体把SWE-bench从20.0%提升至50.0%，Polyglot从14.2%到30.7%（ICLR 2026） [来源](https://sakana.ai/dgm/)
- 2025-05 Absolute Zero Reasoner 完全不用外部数据，自提任务+代码执行器验证，在代码/数学推理达到零设置SOTA（NeurIPS 2025） [来源](https://neurips.cc/virtual/2025/poster/116121)
- 2026-05 Recursive Superintelligence（Socher、Rocktäschel、Clune、田渊栋等）融资6.5亿美元，估值46.5亿美元，GV/Greycroft领投、NVIDIA与AMD参投 [来源](https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding)
- 2025-11 AlphaEvolve在数学问题上的大规模应用论文（Terence Tao等合作） [来源](https://www.alphaxiv.org/abs/2511.02864v1)

**开放问题**：

- 没有可靠自动评估器的开放领域如何自我改进（评估器本身的学习与防奖励作弊）
- 开放式探索的多样性/新颖性度量与长期不停滞（open-endedness）的理论与机制
- 自我改进循环的收敛性、可控性与安全边界：如何证明改进是真实且不引入有害行为

**切入点**：

- 用OpenEvolve/ShinkaEvolve等开源框架+开放模型，攻克组合数学、编译器优化、调度等有精确评估器的具体问题
- 研究自博弈课程生成（提出者-求解者）与自我奖励的失效模式，或为AI研究自动化构建小规模可复现基准

---

## 3. AI数学与形式化定理证明 — 78.9（A 强烈关注）

*AI for Mathematics & Formal Theorem Proving (Lean, AlphaProof, autoformalization, Seed-Prover, IMO gold, Erdős problems)* · AI-可信与推理 · `G5 S4 C5 E4 R5 H3.5 X4 P3` · 排名区间 1–5

**拐点事件**：2025-07 IMO 2025：GDM Gemini Deep Think与OpenAI实验模型达金牌水平，字节Seed-Prover/Harmonic Aristotle以Lean形式化证明获金牌级成绩；2026-05 OpenAI模型给出Erdős单位距离猜想反例，被Quanta称为数学界的“相变”。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | PutnamBench从Seed-Prover的50.4%到Seed-Prover 1.5的88%仅用数月，miniF2F已饱和（99.6%）；Harmonic、Axiom、Math Inc等融资密集；新基准（FrontierMath Erdős，68个Lean形式化开放问题）不断出现；按定性证据判断>100%/年。 |
| 阶段窗口 S | 4 | ICML/NeurIPS AI for Math workshop连续举办，Lean/Mathlib社区迅速扩张；在顶会占比仍小（约1-2%量级，背景判断），范式在收敛（Lean反馈+RL+引理式搜索）但非形式化LLM与形式化路线之争未定；已过最早期，评4。 |
| 能力拐点 C | 5 | 明确的“GPT-3时刻”：2025-07多家系统IMO金牌水平、Seed-Prover形式化证出5/6题；2025-12 AxiomProver Putnam 120/120；2026-05 OpenAI模型给出Erdős单位距离猜想（1946）的反例，被称为首个历史意义的AI证明；且有清晰的扩展趋势。 |
| 使能条件 E | 4 | Lean 4/Mathlib开源，DeepSeek-Prover、Goedel-Prover等开源模型可用；瓶颈是大规模RL所需算力与高质量形式化数据。 |
| 资源注入 R | 5 | GDM、OpenAI、字节Seed、DeepSeek均有大投入；Harmonic C轮1.2亿美元（估值14.5亿）、Axiom A轮2亿美元（估值16亿+）；DOE/DARPA等政府项目；合计超10亿美元级。 |
| 学术空间 H | 3.5 | 竞赛数学已成工业算力竞赛，但自动形式化、研究级数学库建设、证明可读性与人机协作仍为学术可为；评3.5。 |
| 外溢平台性 X | 4 | 形式化验证可作为可信推理的通用底座，外溢到可验证代码生成、物理/科学推理与AI对齐中的“可验证奖励”。 |
| 风险扣分 P | 3 | 存在数据污染与成果宣传口径问题（“GPT-5解决Erdős问题”被指部分为文献检索），非形式化LLM可能削弱形式化路线的必要性；扣3分。 |

**关键证据**：

- 2025-07 Seed-Prover证明78.1%历届IMO形式化题、miniF2F 99.6%、PutnamBench>50%，IMO 2025形式化证出5/6题；Seed-Prover 1.5在PutnamBench达88%，9小时内解出Putnam 2025的11/12题 [来源](https://arxiv.org/pdf/2507.23726)
- 2025-12 AxiomProver在Putnam 2025获120/120满分（人类最高110），证明经Lean机器校验 [来源](https://www.tamradar.com/funding-rounds/axiom-series-a-200m)
- 2026-08 2026-05-20 OpenAI内部模型给出1946年Erdős单位距离猜想的反例，被视为首个具有历史意义的AI证明；2026-08 未发布模型Astra再取得10项数学进展 [来源](https://www.quantamagazine.org/how-ai-tore-through-a-mathematical-community-20260803/)
- 2026-08 Epoch AI发布FrontierMath Erdős：68个截至2026-08仍开放、由Thomas Bloom整理并用Lean形式化的Erdős问题 [来源](https://epoch.ai/latest/announcing-frontiermath-erdos)
- 2025-11 Harmonic完成1.2亿美元C轮，估值14.5亿美元（2024-09 A轮估值3.25亿） [来源](https://siliconangle.com/2025/11/25/harmonic-ai-raises-120m-1-45b-valuation-advance-mathematical-reasoning/)
- 2026-03 Axiom完成2亿美元A轮，估值16亿美元以上，距6400万美元种子轮仅5个月 [来源](https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/)
- 2024-07 AlphaProof/AlphaGeometry 2在IMO 2024取得银牌水平（28/42） （background knowledge）

**开放问题**：

- 研究级数学的自动形式化（定义、陈述与大规模库的对齐），而非竞赛题
- 从“证明给定命题”走向“提出有意义的猜想与概念”，以及长程（数月级）证明项目的规划
- 非形式化证明的可靠自动检验，以及形式化与非形式化推理的结合与互相监督

**切入点**：

- 在Lean/Mathlib上做自动形式化基准与工具（如把论文/教科书定理转写为Lean），或为某一细分数学领域建设可供RL使用的形式化数据集
- 基于开源证明器（DeepSeek-Prover、Goedel-Prover）研究高效测试时搜索、引理复用与证明修复，在PutnamBench/FrontierMath Erdős上低成本报告结果

---

## 4. 机器人基础模型 / 视觉-语言-动作模型(VLA) — 77.7（A 强烈关注）

*Robot Foundation Models / Vision-Language-Action Models* · 具身/空间/生命科学交叉 · `G5 S4.5 C4 E3.5 R5 H4 X4 P4` · 排名区间 3–4

**拐点事件**：候选“GPT-3时刻”：2024-10 π0与2025-04 π0.5（开放世界家庭任务泛化）、2025-03 Gemini Robotics与GR00T N1；真正的拐点将是某个VLA在大规模未见环境中以>90%可靠性完成长时程任务并呈现清晰的数据规模化定律（尚未发生）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | 对1228篇cs.RO VLA论文的统计显示发文量同比约5倍，为机器人最快子方向（次快的操作/抓取仅1.6倍）；ICLR 2026 VLA投稿从个位数增至164篇（约18倍）。 |
| 阶段窗口 S | 4.5 | ICLR 2026投稿约164篇，仍仅占总投稿约1%量级；专门综述、benchmark（LIBERO、SimplerEnv、RoboArena等）和workshop正在形成，动作表示（离散token/flow/扩散）、是否引入世界模型与RL后训练尚无共识范式；但热度上升极快，扣0.5。 |
| 能力拐点 C | 4 | π0.5在未见过的家庭中完成长时程清理任务、Gemini Robotics/GR00T N1展示跨本体泛化，是强存在性证明；但成功率与可靠性仍远未达到“GPT-3式”普适能力，数据规模化曲线尚不清晰。 |
| 使能条件 E | 3.5 | 开源模型（openpi/π0、OpenVLA、SmolVLA、GR00T N1）、LeRobot工具链、Open X-Embodiment数据和低成本机械臂齐备；真实机器人数据规模与可复现的真实世界评测是主要瓶颈。 |
| 资源注入 R | 5 | Physical Intelligence 2025-11 B轮6亿美元（估值56亿），2026年传出约10亿美元新一轮；Skild AI融资14亿美元估值140亿；Google DeepMind、NVIDIA、Tesla、Figure均有大型项目，2025年机器人融资超100亿美元。 |
| 学术空间 H | 4 | 跨本体迁移、数据配方、动作tokenization、RL后训练、评测方法学等大量基础问题可用开源VLA+小规模真实数据研究；但预训练前沿仍被工业数据垄断。 |
| 外溢平台性 X | 4 | 有望成为“物理AI”的通用底座，重塑机器人学、具身智能、世界模型与多模态大模型研究；对CS之外（制造、物流）亦有外溢。 |
| 风险扣分 P | 4 | 估值与真实部署能力差距大、真实世界评测难复现（demo挑选）；有被视频世界模型/通用多模态模型吸收的可能。扣4分。 |

**关键证据**：

- 2026-06 对2023-02至2026-06的1228篇cs.RO VLA论文分析：VLA发文量同比增长5倍，是机器人最快增长子领域，而机器人整体增长127% [来源](https://arxiv.org/html/2512.11362v1)
- 2025-10 ICLR 2026 VLA相关投稿从上一年个位数增至164篇（约18倍）；机器人/VLA相关录用约210篇，2025年不足100篇 [来源](https://eu.36kr.com/en/p/3532732628769664)
- 2026-03 Physical Intelligence 2025-11完成6亿美元B轮（CapitalG领投，估值56亿美元），2026-03传洽谈10亿美元新一轮，目标估值约110亿 [来源](https://www.aicerts.ai/news/physical-intelligence-secures-massive-robotics-war-chest/)
- 2026-01 Skild AI融资14亿美元，估值超140亿美元（SoftBank领投，NVentures参与），打造“全本体大脑” [来源](https://fintool.com/news/skild-ai-14-billion-valuation-robotics)
- 2026-02 2025年机器人行业融资超过103亿美元，由人形机器人和跨硬件基础模型驱动 [来源](https://landbase.com/blog/fastest-growing-robotics-companies)
- 2025-04 π0(2024-10)开源于2025-02，π0.5(2025-04)面向开放世界泛化；Gemini Robotics(2025-03)、GR00T N1(2025-03)、RT-2(2023-07)、Open X-Embodiment(2023-10)构成主线 （background knowledge）

**开放问题**：

- 机器人数据的规模化定律与数据配方：仿真、人类视频、遥操作数据如何混合，是否存在类似LLM的可预测scaling曲线
- 动作表示与推理：离散token、flow matching、扩散头与世界模型/潜在动作的统一，以及长时程任务中的推理与记忆
- 可复现的真实世界评测与RL后训练：如何低成本、统计可信地评估泛化与可靠性，并用在线RL提升成功率

**切入点**：

- 基于openpi/OpenVLA/SmolVLA和LeRobot在低成本机械臂（如SO-100/ALOHA）上做微调、数据效率和失败模式分析研究
- 聚焦评测与方法学：构建分布外泛化benchmark、真实-仿真相关性研究，或研究VLA的RL后训练与安全约束

---

## 5. 世界模型 / 可交互视频生成 — 75.8（A 强烈关注）

*World Models & Interactive Video Generation* · AI-模型与方法 · `G5 S4.5 C4 E3 R5 H4 X4 P5` · 排名区间 5–7

**拐点事件**：2025年8月DeepMind发布Genie 3：首个通用实时可交互世界模型（文本→可游玩3D世界，720p/24fps，数分钟一致）；2026年1月以Project Genie向用户开放，标志从'视频生成'跨入'可交互模拟器'。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | 未找到精确论文计数；但ICLR 2025首届World Models workshop超1500人参会，ICLR 2026办第2届，NeurIPS 2026同时出现'World Models in Physical AI'与'Continual World Models'等多个专门workshop，2025-2026一年内由1个分裂为多个，定性判断>100%/年。 |
| 阶段窗口 S | 4.5 | 专门workshop/基准刚成形，范式未统一（JEPA式表征预测 vs 生成式视频 vs 3D/空间生成三派并立），在顶会中仍为小份额；但热度已接近主流边缘，故4.5而非5。 |
| 能力拐点 C | 4 | Genie 3（2025-08）实现720p/24fps实时可交互、数分钟一致性、约1分钟视觉记忆，是质变的存在性证明；V-JEPA 2用62小时机器人数据做零样本规划。Genie 1→2→3有规模化趋势，但物理正确性与可控性仍缺定量scaling law，给4。 |
| 使能条件 E | 3 | NVIDIA Cosmos、V-JEPA 2、Matrix-Game等开放权重可用；但训练需大规模视频+动作标注数据与巨量算力，评测标准缺失，是一个主要瓶颈。 |
| 资源注入 R | 5 | AMI Labs（LeCun）2026年种子轮10.3亿美元；World Labs（李飞飞）2026-02融资10亿美元、估值50亿；DeepMind、NVIDIA、Meta均有旗舰项目，远超>$1B门槛。 |
| 学术空间 H | 4 | 长时一致性/记忆、动作条件化、物理一致性评测、用世界模型训练智能体的sim-to-real等问题大量开放；大模型训练偏工业，但评测、小规模机理与下游规划学术可做。 |
| 外溢平台性 X | 4 | 可成为机器人、自动驾驶、游戏/内容生成、智能体训练环境乃至科学模拟的通用底座。 |
| 风险扣分 P | 5 | 概念边界模糊（'world model'被泛化营销）、炒作与可靠性差距大、物理正确性难验证、训练高度依赖少数大厂算力。 |

**关键证据**：

- 2025-08 Genie 3 实时生成可交互环境，720p/24fps，数分钟一致性，视觉记忆可回溯约1分钟 [来源](https://techcrunch.com/2025/08/05/deepmind-reveals-genie-3-a-world-model-that-could-be-the-key-to-reaching-agi)
- 2026-01 Project Genie（基于Genie 3）于2026-01-29通过Google Labs向美国AI Ultra用户开放 [来源](https://dataconomy.com/2026/01/30/google-launches-project-genie-create-interactive-worlds-with-ai/)
- 2025-06 V-JEPA 2 自监督视频世界模型，仅用62小时Droid机器人数据微调即可零样本规划抓取/放置 [来源](https://arxiv.org/pdf/2506.09985)
- 2026-03 LeCun创立AMI Labs，种子轮10.3亿美元（估值35亿美元），聚焦JEPA世界模型 [来源](https://futurumgroup.com/insights/yann-lecuns-ami-raises-1bn-seed-round-is-the-world-model-era-finally-here)
- 2026-02 World Labs 融资10亿美元、估值50亿美元，累计融资12.3亿美元；首个产品Marble于2025-11发布 [来源](https://www.crowdfundinsider.com/2026/02/262836-ai-firm-world-labs-raises-1-billion-at-5-billion-valuation/)
- 2026-04 ICLR 2025首届World Models workshop超1500名参与者，2026年办第2届；NeurIPS 2026另有'World Models in Physical AI'与'Continual World Models' workshop [来源](https://iclr.cc/virtual/2026/workshop/10000799)
- 2026-01 NVIDIA Cosmos世界基础模型扩展至机器人控制（Cosmos Policy）、自动驾驶与工业视觉 [来源](https://metavert.io/world-models-for-robotics)

**开放问题**：

- 如何在分钟到小时尺度上保持空间/物体一致性与长期记忆，而不是靠上下文窗口硬撑
- 如何定量评测世界模型的物理正确性与可控性（而非视觉质量），并证明其对下游智能体/机器人策略有增益
- 生成式像素预测 vs JEPA式潜空间预测哪条路线更可扩展，动作标签稀缺时如何从无标注视频学习可控动态（latent action）

**切入点**：

- 基于开放权重（Cosmos、V-JEPA 2、Matrix-Game等）做世界模型评测基准：物理一致性、反事实动作响应、长时记忆探针
- 在小规模可控领域（Atari/Procgen/MineRL、桌面机械臂）研究潜动作学习与基于世界模型的规划，验证'想象训练'对策略的增益

---

## 6. 持续学习与测试时训练 / 测试时记忆 — 75.5（A 强烈关注）

*Continual Learning & Test-Time Training / Test-Time Memory* · AI-模型与方法 · `G4.5 S5 C3 E3.5 R4 H5 X4.5 P5` · 排名区间 3–8

**拐点事件**：尚未发生的'GPT-3时刻'：一个前沿规模模型在部署中通过测试时权重更新持续积累技能并显著超越冻结权重版本。先兆事件：2024-12 Google Titans、2025-06 MIT SEAL、2025-11 Google Nested Learning/HOPE、2025-12 TTT-E2E（Stanford/NVIDIA）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | 未找到精确计数；定性：2025-2026出现Titans、Nested Learning/HOPE、SEAL、TTT-E2E、CL-Bench（2026-06）等密集成果，NeurIPS 2026出现'Continual World Models' workshop，arXiv 2026年多篇'LLM持续学习'综述/基准，估计60-100%+/年。 |
| 阶段窗口 S | 5 | 被普遍视为'缺失的关键能力'（Sutskever 2025-11访谈、Dwarkesh），但无共识范式（测试时梯度更新、神经记忆模块、自生成数据微调、嵌套优化并存），顶会份额小，处起飞前沿。 |
| 能力拐点 C | 3 | TTT-E2E在128K上下文以全注意力精度、2.7x速度，并随上下文长度像全注意力一样scale；SEAL在一项拼图任务上0%→72.5%；HOPE困惑度优于Transformer。均为窄域存在性证明，尚无'部署后持续变强'的质变演示，给3。 |
| 使能条件 E | 3.5 | 开放基座模型、学术可训练的小规模设置充足；但缺乏公认的持续学习评测（CL-Bench刚出现）与长期部署数据，是主要瓶颈。 |
| 资源注入 R | 4 | Google Research（Titans/Nested Learning）、NVIDIA+Stanford（TTT-E2E）、SSI明确押注持续学习；多家前沿实验室公开表态，但专项资金额度不明。 |
| 学术空间 H | 5 | 灾难性遗忘、更新规则的元学习、记忆与权重的分工、评测协议、安全性等基础问题开放，且大多可在1-3B规模用学术算力研究。 |
| 外溢平台性 X | 4.5 | 若突破，将成为所有智能体/个性化/科学发现系统的通用底座（模型部署后从经验中学习）。 |
| 风险扣分 P | 5 | 尚无GPT-3式突破，存在被长上下文+检索+RL后训练'够用替代'的风险；评测不统一导致结果难比较；部署时权重更新带来安全/对齐风险。 |

**关键证据**：

- 2025-11 Google提出Nested Learning范式与HOPE架构（Titans的自修改变体，含连续记忆系统CMS），语言建模困惑度优于Transformer与现代循环模型 [来源](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning)
- 2025-11 MIT SEAL用RL训练LLM生成'self-edit'来更新自身权重，一项拼图任务成功率0%→72.5% [来源](https://news.mit.edu/2025/teaching-large-language-models-to-absorb-new-knowledge-1112)
- 2025-12 TTT-E2E：滑窗Transformer在测试时用next-token预测更新权重，128K上下文达到全注意力精度且快2.7x；3B/164B tokens下随上下文长度的scaling与全注意力一致，而Mamba 2/Gated DeltaNet不然 [来源](https://arxiv.org/html/2512.23675v1)
- 2025-11 Sutskever（SSI）在2025-11访谈中称'缺失的要素是部署后能从经验中持续改进的学习者' [来源](https://bretkerr.substack.com/p/the-sentence-that-survived)
- 2026-06 CL-Bench：基于专家验证任务评测前沿AI系统能否通过序列经验改进 [来源](https://arxiv.org/pdf/2606.05661)
- 2026-09 NeurIPS 2026 设立'Continual World Models' workshop，聚焦训练后持续更新的模型 [来源](https://neurips.cc/virtual/2026/workshop/137499)

**开放问题**：

- 如何在不发生灾难性遗忘与对齐漂移的前提下，让LLM在部署中安全地更新权重
- 测试时记忆（快权重/神经记忆）与慢权重、外部检索之间的最优分工与理论刻画
- 缺乏标准化、可防作弊的持续学习评测协议（时间序列任务流、知识更新、技能积累）

**切入点**：

- 在1B级开放模型上复现并对比TTT层、Titans记忆、SEAL式自编辑在同一任务流上的遗忘-可塑性曲线，构建统一基准
- 研究测试时更新的元学习初始化与更新规则（learned optimizer），或面向智能体的'经验→权重'蒸馏方案

---

## 7. 智能体系统基础设施 — 75.1（A 强烈关注）

*Agent Systems Infrastructure* · 系统与硬件 · `G5 S4 C4 E4 R5 H4 X4.5 P5` · 排名区间 6–7

**拐点事件**：2024 年 11 月 Anthropic 发布 MCP，2025 年编码智能体（Claude Code、Codex 等）进入大规模生产，让“智能体工作负载”变成数据中心的一类新负载。2026 年 5 月首届 ACM CAIS 会议召开，标志着这个系统社区开始成形。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | MCP 公共注册表从 2025 年 Q1 末约 1,200 个服务器增至 2026 年 4 月 9,400+（约 8 倍）；PulseMCP 在 2026 年 7 月收录 20,115 个。智能体负载刻画类论文从 2025 年开始出现。增速远超 100%/年。 |
| 阶段窗口 S | 4 | 首届 ACM CAIS（AI 与智能体系统会议）于 2026 年 5 月召开，MLSys 2026 已把 agentic AI 列为热点，但在 OSDI/SOSP 中占比仍小。运行时、调度、隔离、状态管理都还没有共识范式，正处于“2021 年的 LLM”阶段。 |
| 能力拐点 C | 4 | 编码智能体（SWE-agent、Claude Code 等）已能完成长程多工具任务，这是新的工作负载形态的存在性证明；智能体可完成任务长度随模型代际快速增长（背景知识，METR 观测）。但系统层面的“能力拐点”还在形成。 |
| 使能条件 E | 4 | 开源模型、MCP 开放协议、SWE-bench/Terminal-Bench/GAIA 等基准和开源框架都可获得；主要短板是缺少真实生产级智能体 trace。 |
| 资源注入 R | 5 | 各大模型厂商、云厂商以及 Linux 基金会旗下的 Agentic AI Foundation 都在投入，智能体创业公司大量获得 VC 资金。 |
| 学术空间 H | 4 | 调度、沙箱隔离、工具调用开销、CPU-GPU 协同、容错/检查点等都是可用开源模型和小集群研究的基础问题。 |
| 外溢平台性 X | 4.5 | 可能成为新的“操作系统层”，同时影响 OS、数据库、网络、安全和软件工程。 |
| 风险扣分 P | 5 | 炒作重、框架快速更迭、可能被模型厂商的一体化产品吸收、评测可复现性差，因此扣 5 分。 |

> 校准：S 5 → 4，“智能体”已是 2026 年 AI 最热主题，MCP 生态已商业化，不再是小众起飞期；但系统顶会中的份额仍小，所以给 4 而非 3

> 校准：X 5 → 4.5，与“GUI/计算机使用智能体”的外溢效应部分重叠，避免重复计分

**关键证据**：

- 2026-04 MCP 公共注册表从 2025 年 Q1 末约 1,200 个服务器增至 2026 年 4 月中旬 9,400+ [来源](https://getknit.dev/blog/the-guide-to-the-mcp-ecosystem)
- 2026-07 PulseMCP 在 2026 年 7 月收录 20,115 个 MCP 服务器 [来源](https://tooldirectory.ai/blog/state-of-mcp-servers-2026)
- 2026-05 首届 ACM Conference on AI and Agentic Systems（CAIS）于 2026 年 5 月 27-29 日在圣何塞召开，Matei Zaharia 等担任主席，含 5 个联合研讨会 [来源](https://www.twosigma.com/articles/acm-cais-2026-what-to-watch-at-the-inaugural-conference-on-ai-agentic-systems/)
- 2025-11 CPU 视角的智能体负载刻画：工具处理最高占总延迟 90.6%，大批量时 CPU 动态能耗最高占 44% [来源](https://arxiv.org/abs/2511.00739)
- 2026-05 2026 年工具调用刻画：GAIA 最高 28.7% 时间花在 WebFetch/WebSearch 等工具上 [来源](https://www.alphaxiv.org/abs/2605.26297)
- 2026-05 MLSys 2026 的热门主题包括缓存管理、推测解码、RAG 和 agentic AI [来源](https://www.capitalone.com/tech/ai/mlsys-2026-highlights/)
- 2026-04 每个 MCP 服务器都会把整个工具目录注入上下文，4 个服务器的组合可消耗 1.2-2 万 token [来源](https://getknit.dev/blog/the-guide-to-the-mcp-ecosystem)

**开放问题**：

- 面向智能体的运行时/OS 抽象：长时运行任务的状态持久化、检查点、回滚和隔离沙箱
- LLM 推理与工具执行（CPU、I/O、网络）的协同调度，以及前缀/KV 在多轮工具调用之间的复用
- 大规模工具生态（上万 MCP 服务器）下的工具检索、上下文预算管理、权限与安全模型

**切入点**：

- 用开源模型 + SWE-bench/Terminal-Bench 搭建可复现的智能体负载基准，做系统级刻画（延迟分解、能耗、CPU/GPU 瓶颈）
- 在 vLLM/SGLang 之上实现“智能体感知”的调度器或工具调用缓存，以单机/小集群验证收益

---

## 8. 空间智能 / 3D基础模型（前馈式三维重建） — 73.0（B 值得投入）

*Spatial Intelligence / 3D Foundation Models (Feed-forward 3D Reconstruction)* · 具身/空间/生命科学交叉 · `G4.5 S4 C4 E4.5 R4 H4.5 X4 P3` · 排名区间 7–10

**拐点事件**：2023-12 DUSt3R首次证明无需标定的前馈双视图三维重建可行，2025-03 VGGT（CVPR 2025最佳论文）实现秒级多视图前馈重建并超越优化式方法，是该领域的“GPT-3时刻”；2026 VGGT-Ω显示数据规模化趋势。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | DUSt3R(CVPR 2024)不到一年被引>200、后续计数548+，衍生MASt3R、MUSt3R、CUT3R、π3、VGGT、MapAnything、Depth Anything 3等；VGGT获CVPR 2025最佳论文，VGGT-Ω成为CVPR 2026最佳论文候选；未找到精确论文计数，按定性估计>80%/年。 |
| 阶段窗口 S | 4 | 以pointmap/前馈Transformer为核心的范式正在快速形成，专题综述与workshop涌现，仍是CVPR中较小份额；但VGGT类架构已开始成为共识，略高于“首个workshop”阶段，给4。 |
| 能力拐点 C | 4 | 从需要标定和迭代优化的SfM/MVS转为秒级前馈重建（VGGT<1秒处理数百张视图）是质的变化；VGGT-Ω用15倍监督数据与1800万自监督视频扩展，显示初步scaling趋势，但精度在部分场景仍需BA后处理。 |
| 使能条件 E | 4.5 | 开源权重（DUSt3R/VGGT/MapAnything）、大规模多视图数据集、COLMAP伪标签与适中训练算力均可获得。 |
| 资源注入 R | 4 | Meta、Google DeepMind、NVIDIA、NAVER Labs投入；World Labs 2026-02获10亿美元融资（估值约50亿，累计12.3亿），Autodesk出资2亿美元。 |
| 学术空间 H | 4.5 | 动态场景、度量尺度、长序列/大场景、语义与物理属性、与生成模型统一等问题大量开放，学术算力可训练中等规模模型。 |
| 外溢平台性 X | 4 | 可成为机器人、自动驾驶、AR/VR、世界模型、VLM空间推理的通用几何底座。 |
| 风险扣分 P | 3 | “空间智能”品牌把生成式世界与几何重建混为一谈存在炒作；有被视频生成/世界模型吸收的风险。扣3分。 |

**关键证据**：

- 2025-06 VGGT获CVPR 2025最佳论文，前馈推断相机参数、点图、深度和3D轨迹，1秒内完成重建并超越需几何优化后处理的方法 [来源](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html)
- 2026-06 VGGT-Ω为CVPR 2026 oral与最佳论文候选，使用15倍监督数据和1800万自监督视频扩展 [来源](https://learnopencv.com/vggt-vs-vggt-%cf%89-vggt-omega-a-complete-guide-to-feed-forward-3d-reconstruction/)
- 2025-06 DUSt3R被548篇论文引用，Meta、Google DeepMind、NVIDIA均有衍生研究 [来源](https://www.naverlabs.com/en/storyDetail/328)
- 2025-09 MapAnything（Meta/CMU）用单一前馈模型统一SfM、MVS、单目深度、相机定位等任务 [来源](https://arxiv.org/abs/2509.13414v3)
- 2026-02 World Labs 2026-02宣布10亿美元融资（NVIDIA、AMD、Autodesk等），估值约50亿美元；首个产品Marble于2025-11发布 [来源](https://www.crowdfundinsider.com/2026/02/262836-ai-firm-world-labs-raises-1-billion-at-5-billion-valuation/)

**开放问题**：

- 动态与非刚性场景的前馈4D重建，以及长视频/城市级场景的可扩展记忆机制
- 几何基础模型的scaling规律：自监督视频数据能否替代昂贵的3D真值
- 几何表征与语义、物理属性及生成式世界模型的统一，并服务于机器人与VLM空间推理

**切入点**：

- 在开源VGGT/MASt3R/MapAnything上做微调与蒸馏，研究轻量化、动态场景或特定领域（医疗、遥感）适配
- 构建评测：针对度量精度、鲁棒性、空间推理的benchmark，或将前馈3D特征接入VLA/VLM做下游验证

---

## 9. 自动化科研 / AI科学家 — 71.9（B 值得投入）

*Automated Research / AI Scientist (AI Scientist, AlphaEvolve-style discovery, Co-Scientist, autonomous labs)* · AI-可信与推理 · `G5 S4 C3.5 E3 R5 H4 X5 P6` · 排名区间 8–12

**拐点事件**：2025-05 DeepMind AlphaEvolve以LLM驱动的进化搜索取得多项可验证数学/算法新纪录并在Google基础设施落地；同年AI Scientist v2首次以完全AI生成论文通过同行评审。尚待到来的“GPT-3时刻”：自主系统在湿实验或主流期刊层面独立产出被广泛认可的重要发现。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | 2024-08 AI Scientist v1后，AI Scientist v2、Google Co-Scientist、AlphaEvolve、Kosmos等相继发布，Agents4Science等新会议出现；未找到可靠论文计数，按系统发布与资金流判断>100%/年。 |
| 阶段窗口 S | 4 | 已有首个AI为第一作者的会议（Agents4Science 2025）与多场workshop，基准（如MLE-bench、PaperBench）形成中，但评估范式与“何为有效发现”无共识，顶会占比仍小；舆论热度高于学术沉淀，评4。 |
| 能力拐点 C | 3.5 | AlphaEvolve给出可验证新结果（56年来4×4复矩阵乘法改进、kissing number、2026-08将ω上界从2.371339降至2.371177）；AI Scientist v2论文以6.33均分通过ICLR workshop评审；但端到端自主科研产出质量仍以workshop级为主，评3.5。 |
| 使能条件 E | 3 | 纯计算领域（ML、算法、数学）工具齐全；湿实验自动化、可靠的新颖性/正确性评估是主要瓶颈。 |
| 资源注入 R | 5 | GDM、OpenAI for Science、FutureHouse；Lila Sciences估值超13亿美元并洽谈约20亿美元B轮、Periodic Labs融资3亿美元；DOE Genesis Mission首批3.2亿美元；总量远超10亿美元。 |
| 学术空间 H | 4 | 评测、可验证性、假设生成质量、实验设计与闭环优化等大量开放问题，计算类科学可用学术算力研究。 |
| 外溢平台性 X | 5 | 目标即为跨学科的科研基础设施，可外溢到材料、生物、数学、ML自身研究。 |
| 风险扣分 P | 6 | 炒作与结果落差大、AI生成论文污染同行评审、可复现性与“发现”认定争议、物理实验成本与速度限制；扣6分。 |

**关键证据**：

- 2025-05 AlphaEvolve（2025-05-14）改进4×4复矩阵乘法56年纪录、推进11维kissing number等开放问题并提升Google基础设施效率 [来源](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- 2026-08 借助AlphaEvolve将矩阵乘法指数ω上界从2.371339改进到2.371177（作者含Alman与Vassilevska Williams） [来源](https://www.alphaxiv.org/abs/2608.16884)
- 2025-03 Sakana AI Scientist v2的3篇完全自主论文投稿ICLR 2025 ICBINB workshop，1篇均分6.33超过录用线 [来源](https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that)
- 2025-10 Stanford与Together AI举办Agents4Science 2025，要求AI为第一作者并由AI初审，2025-10-22线上召开 [来源](https://agents4science.stanford.edu)
- 2026-06 Lila Sciences估值超13亿美元（Nvidia参投），2026-06洽谈约20亿美元B轮（投前估值约85亿美元）；Periodic Labs融资3亿美元建设AI科学家 [来源](https://news.bgov.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation)
- 2025-12 DOE Genesis Mission首批3.2亿美元，包括14个机器人与自动化实验室项目 [来源](https://insidehpc.com/2025/12/doe-awards-320m-for-genesis-mission-ai-for-science/)
- 2025-02 Google发布基于Gemini的AI Co-Scientist多智能体假设生成系统，部分假设经湿实验验证（如药物再利用、细菌基因转移机制） （background knowledge）

**开放问题**：

- 如何可靠评估AI产出的新颖性、正确性与重要性（避免同行评审被AI论文淹没）
- 开放式科研中的假设生成与实验选择（探索-利用）以及长时程闭环（含湿实验）的稳健性
- 从“可自动评分”的领域（算法/数学优化）推广到评价信号稀疏、噪声大的经验科学

**切入点**：

- 基于开源AlphaEvolve类框架（如OpenEvolve）在组合优化、编译器启发式、数值算法等可自动评分问题上寻找新纪录
- 构建AI科研流程的评测基准（复现、审稿、错误检测、新颖性判定），或研究AI审稿/AI生成论文检测

---

## 10. 量子纠错与容错量子计算软件栈 — 71.8（B 值得投入）

*Quantum Error Correction & Fault-Tolerant Quantum Computing Stack* · 量子/密码/网络/理论 · `G4.5 S4.5 C4.5 E3 R5 H4 X3.5 P7` · 排名区间 8–12

**拐点事件**：2024年12月 Google Willow 首次在超导处理器上实现低于表面码阈值的指数级逻辑错误抑制（Λ≈2.14）并配合实时解码——相当于QEC的“GPT-3时刻”；2025-2026年 Quantinuum/QuEra 数十个逻辑比特与 lattice surgery 演示正在把它推向“可编程逻辑计算”。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | Riverlane 报告：2025年1-10月同行评审 QEC 码论文120篇，2024全年仅36篇（>3倍）；2026年 lattice surgery、qLDPC 处理器、QEC 编译器（CircLS 等）预印本密集出现。 |
| 阶段窗口 S | 4.5 | 已有专门的 QEC 会议/报告与 SIGARCH/QCE 专场，但在 CS 顶会中占比仍很小；表面码 vs qLDPC vs 玻色码路线未收敛，解码器/编译器无共识范式——典型的“2021年LLM”位置。 |
| 能力拐点 C | 4.5 | Google Willow（2024-12）首次实现低于阈值：码距每+2逻辑错误率降低2.14倍，d=7逻辑错误0.143%/周期，实时解码延迟63μs；指数抑制本身即“缩放律”。Quantinuum Helios 48逻辑比特、QuEra 96逻辑比特。但尚无有用的容错计算。 |
| 使能条件 E | 3 | Stim/PyMatching 等开源模拟与解码工具完善，学界可做大规模数值实验；主要瓶颈是可做实时 QEC 的硬件访问受限于少数公司。 |
| 资源注入 R | 5 | Google、IBM（Starling 2029，200逻辑比特）、Quantinuum、Microsoft、AWS、QuEra 等全面投入；DARPA QBI 以2033年实用规模为目标分阶段评估；量子行业年融资数十亿美元。 |
| 学术空间 H | 4 | 解码算法（Relay-BP 等）、qLDPC 上的逻辑门/手术、magic state 制备、资源估计与编译均为可由小组以模拟推进的开放问题；但实验验证依赖工业界。 |
| 外溢平台性 X | 3.5 | 直接决定 Shor 威胁时间线（Gidney 2025：RSA-2048 <100万噪声比特），外溢到密码迁移、量子化学/材料模拟；但成为通用 CS 底座仍远。 |
| 风险扣分 P | 7 | 距离有用容错计算仍需5-10年、物理工程极限（布线、制冷、泄漏错误）、厂商路线图宣传与实际差距大、硬件集中于少数公司，扣7分。 |

**关键证据**：

- 2024-12 Willow：d=7 表面码（101比特）逻辑错误率0.143%/周期，码距+2错误率降低2.14倍，逻辑寿命为最佳物理比特2.4倍；d=5 实时解码平均延迟63μs，持续百万周期 [来源](https://postquantum.com/engineering-news/google-surface-code-threshold/)
- 2025-11 Riverlane QEC Report 2025：2025年1-10月同行评审 QEC 码论文120篇，2024全年36篇，“QEC code explosion”，并警告人才短缺 [来源](https://www.riverlane.com/quantum-error-correction-report-2025)
- 2025-06 IBM 提出 Relay-BP 解码器，适合 FPGA/ASIC 实时解码，在双变量自行车(BB) qLDPC 码上显著优于 BP+OSD；IBM Starling 规划200逻辑比特、1亿门 [来源](https://quantumcomputingreport.com/ibm-researchers-devise-relay-bp-algorithm-for-real-time-decoding-of-qldpc-codes/)
- 2025-11 Quantinuum Helios（98离子比特，双比特门保真度99.921%）演示48个纠错逻辑比特（2:1物理/逻辑比）；同月入选 DARPA QBI Stage B [来源](https://www.quantinuum.com/press-releases/quantinuum-selected-by-darpa-to-advance-to-stage-b-of-quantum-benchmarking-initiative)
- 2025-05 Gidney：2048位 RSA 可用<100万噪声比特、<1周分解，较2019年估计（2000万比特）降低20倍，依赖 yoked surface code 与 magic state cultivation [来源](https://arxiv.org/abs/2505.15917v1)
- 2026-06 QuEra 用高码率 [[16,6,4]] qLDPC 码编码至多96个逻辑比特并测得低于阈值运行；超导表面码处理器 lattice-surgery 逻辑操作预印本出现 [来源](https://postquantum.com/quantum-research/quera-qldpc-2-to-1-physical-logical-qubit-ratio/)

**开放问题**：

- 可扩展到数千逻辑比特的低延迟、高精度实时解码（尤其是 qLDPC 码的电路级噪声解码与硬件实现）
- qLDPC 码上的高效逻辑门、lattice/lifted surgery 与 magic state 生产的端到端架构与编译
- 面向泄漏、相关噪声、宇宙射线等非理想噪声的容错协议与可信资源估计

**切入点**：

- 基于 Stim + Sinter + PyMatching/BP-OSD 做新解码器或新码的电路级数值研究，并参与 Riverlane/Google 公开的解码数据集与基准对比
- 从编译器/体系结构角度切入：lattice surgery 调度、逻辑比特布局与资源估计工具（如 Azure Resource Estimator、Qualtran），以 PL/架构背景发表于 ISCA/MICRO/ASPLOS 量子专场

---

## 11. 扩散语言模型 / 非自回归LLM — 70.5（B 值得投入）

*Diffusion Language Models (non-autoregressive LLMs)* · AI-模型与方法 · `G4.5 S5 C3 E4 R3.5 H5 X3 P4` · 排名区间 9–13

**拐点事件**：2025年2月Inception发布Mercury（首个商用规模dLLM，>1000 tok/s）与同期LLaDA 8B追平LLaMA3 8B；2025年5月Google I/O展示Gemini Diffusion（1000-2000 tok/s）；真正的'GPT-3时刻'将是扩散模型在前沿质量上追平AR且保持5-10x速度优势（尚未发生）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | 未找到arXiv精确月度计数；定性证据：2025年LLaDA/Dream/Mercury后出现综述（2025-08、2026-06）、开源框架dLLM（2026-02）、ACL 2026 demo、NeurIPS 2026首个专门workshop，2025-12已扩展至100B（LLaDA2.0），判断增长约80-100%+/年。 |
| 阶段窗口 S | 5 | 首个专门workshop在2026年出现，顶会份额小，范式未收敛（masked离散扩散、block diffusion、AR转扩散、连续扩散并存），正处起飞窗口。 |
| 能力拐点 C | 3 | Mercury 2（2026-02）1009 tok/s、端到端1.7s，质量对标Haiku/GPT-5 mini级；LLaDA 8B≈LLaMA3 8B；LLaDA2.0达100B。核心是速度/双向性优势而非质变新能力，前沿质量仍落后AR，给3。 |
| 使能条件 E | 4 | LLaDA、Dream、LLaDA2.0等开放权重，开源训练框架dLLM，可由AR模型转换降低训练成本；推理引擎/KV缓存生态尚不成熟。 |
| 资源注入 R | 3.5 | Inception 2025-11融资5000万美元（Menlo、NVentures、M12等）；Google Gemini Diffusion；蚂蚁/inclusionAI LLaDA2.0；属1-2家大厂+创业公司级，未到>$1B。 |
| 学术空间 H | 5 | 采样调度、长度控制、KV缓存、扩散模型上的RL与推理、scaling law、理论（离散扩散ELBO）等大量问题，8B以下可用学术算力研究。 |
| 外溢平台性 X | 3 | 可重塑推理服务（低延迟）、代码编辑/填空、统一多模态生成；若质量追平则影响面更广，但目前属'更快的LLM'。 |
| 风险扣分 P | 4 | 可能被AR侧推测解码/多token预测等加速技术抵消；前沿质量差距；商业主导者单一（Inception）。 |

**关键证据**：

- 2025-02 Mercury Coder 在H100上>1000 tok/s，Mini版HumanEval 88.0%、MBPP 77.1%，约为速度优化AR模型的5倍 [来源](https://www.inceptionlabs.ai/introducing-mercury)
- 2025-05 Google I/O 2025演示Gemini Diffusion，约1000-2000 tok/s [来源](https://www.web3aiblog.com/blog/diffusion-llms-explained-mercury-gemini-diffusion-2026)
- 2026-02 Mercury 2：首个推理型dLLM，Blackwell上1009 tok/s、端到端1.7s（对比Claude 4.5 Haiku 89 tok/s） [来源](https://www.businesswire.com/news/home/20260224034496/en)
- 2025-11 Inception 融资5000万美元，Menlo领投，NVentures、M12、Snowflake、Databricks参投 [来源](https://www.businesswire.com/news/home/20251106570339/en/Inception-Raises-$50M-to-Power-Diffusion-LLMs-Increasing-LLM-Speed-and-Efficiency-by-up-to-10X-and-Unlocking-Real-Time-Accessible-AI-Applications)
- 2025-12 LLaDA2.0 通过AR→扩散转换把dLLM扩展到100B总参数（MoE），此前多数dLLM≤8B [来源](https://arxiv.org/abs/2512.15745v2)
- 2026-09 NeurIPS 2026 设立'Diffusion Language Models: Foundations, Efficiency, and Reasoning' workshop [来源](https://neurips.cc/virtual/2026/workshop/137483)
- 2026-02 开源框架 dLLM: Simple Diffusion Language Modeling 标准化dLLM训练/评测流水线 [来源](https://arxiv.org/html/2602.22661)

**开放问题**：

- 扩散LM的scaling law与AR是否同斜率：在相同算力下能否在前沿规模上追平AR的质量与推理能力
- 可变长度生成、KV缓存与高效并行采样（步数-质量权衡）的系统级方案
- 如何在扩散LM上做RL/可验证奖励训练与长链推理，利用其双向、可修改性优势（如反转诅咒、自我修订）

**切入点**：

- 基于LLaDA/Dream等8B开放权重研究采样策略、重掩码与自我纠错，学术算力即可产出顶会工作
- 研究扩散LM上的RL（如GRPO变体）或AR→扩散低成本转换方法，并建立速度-质量公平对比基准

---

## 12. 大模型驱动的芯片设计/EDA — 70.5（B 值得投入）

*LLM-Driven Chip Design / EDA* · 系统与硬件 · `G5 S5 C3.5 E3 R4 H4 X2.5 P4` · 排名区间 9–13

**拐点事件**：2023 年 ChipNeMo/VerilogEval 开启了这个方向；真正的“GPT-3 时刻”可能是 2025-2026 年智能体流程首次自主完成“规格→RTL→验证→GDS”的完整 CPU 设计（Agentrys 2026 年声明），并在工业基准 CVDP 上超过 90%。前提是这些结果能被独立复现。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | LLM 硬件设计/安全相关论文从 2023 年 21 篇增至 2024 年 86 篇（约 4 倍），2025 年预测 345 篇；Verilog 生成论文 6→29→64 篇（2023-2025）。年增速超过 100%。 |
| 阶段窗口 S | 5 | 已有专门的基准（VerilogEval v1/v2、RTLLM、CVDP、RealBench）和研讨会（如 IEEE LAD），但在 DAC/ICCAD 中占比仍小，从 RTL 生成、验证到物理设计的范式尚未统一。 |
| 能力拐点 C | 3.5 | 简单模块的 RTL 生成已基本可用（GPT-4o 在 VerilogEval-Human 上 pass@1 为 57.1%，后续模型更高）；Agentrys 声称从规格到 GDS 自主完成 32 位 CPU，并在 NVIDIA CVDP 上超过 90%（厂商声明）。IP 级真实设计（RealBench）仍很弱，属于“强存在性证明、可扩展性未明”。 |
| 使能条件 E | 3 | 开源模型和基准都可获得，OpenROAD 等开源流程存在；但商用 EDA 工具、先进 PDK 和高质量 RTL 数据稀缺，是一个主要瓶颈。 |
| 资源注入 R | 4 | NVIDIA（ChipNeMo、CVDP）、Synopsys/Cadence 的 agent 产品；ChipAgents 半年内累计融资 1.34 亿美元，Agentrys 2,450 万美元。 |
| 学术空间 H | 4 | 验证、规格理解、PPA 反馈闭环、数据合成等问题大多可用开源工具链和学术资源研究。 |
| 外溢平台性 X | 2.5 | 主要影响 EDA/体系结构，外溢到形式化验证和代码生成，属于中等偏窄。 |
| 风险扣分 P | 4 | 基准污染与简单题饱和、厂商声明难以复现，AlphaChip 可复现性争议说明这一方向的评测风险，因此扣 4 分。 |

**关键证据**：

- 2025-04 LLM 硬件设计与安全论文：2023 年 21 篇 → 2024 年 86 篇（4 倍），2025 年预测 345 篇 [来源](https://arxiv.org/pdf/2504.08854)
- 2025-12 Verilog 代码生成论文：2023 年 6 篇、2024 年 29 篇、2025 年 64 篇；系统综述覆盖 102 篇 [来源](https://arxiv.org/pdf/2512.00020)
- 2024-08 VerilogEval v2：GPT-4o 在 VerilogEval-Human 上 pass@1 为 57.1%；RealBench 首次面向真实 IP 级设计 [来源](https://arxiv.org/pdf/2408.11053)
- 2026-02 ChipAgents 在 A/A1/A2 轮累计融资 1.34 亿美元（首轮之后 6 个月内） [来源](https://siliconangle.com/2026/02/18/chipagents-secures-50m-funding-accelerate-agentic-chip-design/)
- 2026-06 Agentrys 融资 2,450 万美元（MediaTek 领投预种子轮）；声称多智能体流程自主完成 32 位 CPU 从规格到签核 GDS，并在 NVIDIA CVDP 上超过 90% [来源](https://pulse2.com/agentrys-raises-24-5-million-as-agentic-chip-design-platform-tops-90-on-nvidia-benchmark/amp/)
- 2024-09 AlphaChip（2021 Nature）可复现性争议；Nature 于 2024 年 9 月发布 Addendum 支持原结论，Google 开源 Circuit Training [来源](https://en.wikipedia.org/wiki/AlphaChip_(controversy))

**开放问题**：

- IP/SoC 级的设计与验证：长规格理解、跨模块一致性、形式化验证与 LLM 的结合
- 将 PPA（功耗、性能、面积）与时序反馈纳入智能体闭环，实现跨 RTL 和物理设计的优化
- 高质量硬件设计数据稀缺：数据合成、去污染的基准和可信评测

**切入点**：

- 基于开源模型 + OpenROAD/Yosys/Verilator 搭建智能体流程，在 VerilogEval/RTLLM/CVDP/RealBench 上做 RL 微调或验证驱动的迭代生成
- 构建去污染的新基准，或者面向断言生成/形式化验证的 LLM 方法（数据需求小、工业界关注度高）

---

## 13. GUI/计算机使用智能体 — 68.1（B 值得投入）

*GUI / Computer-Use Agents* · AI-模型与方法 · `G4.5 S3.5 C4.5 E4 R5 H3.5 X4 P5` · 排名区间 11–14

**拐点事件**：2024年10月Anthropic发布Claude computer use（首个前沿模型通用屏幕操作）与2025年1月OpenAI Operator；2025年12月至2026年初智能体在OSWorld-Verified上首次超过人类平均水平（72.4%）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4.5 | OSWorld从12.24%（2024-04）到72.6%（2025-12）仅20个月；一项综述统计的336篇GUI智能体论文主要集中于2024年后；NeurIPS 2025仅CUA相关就有约45篇；整体智能体论文一年近三倍。估计>80%/年。 |
| 阶段窗口 S | 3.5 | 专门基准（OSWorld、WindowsAgentArena、AndroidWorld等）与综述密集形成，但方法正趋于收敛（原生VLM智能体+多轮RL+数据飞轮），且前沿模型均已内置，正从起飞期迈向成熟，给4。 |
| 能力拐点 C | 4.5 | GPT-5.4在OSWorld-Verified 75.0%、Claude Opus 4.6 72.7%，超过人类平均72.4%；Claude Sonnet 4.0→4.5从42.2%到61.4%，scaling趋势清晰；但真实世界可靠性与效率仍远逊人类。 |
| 使能条件 E | 4 | 开放模型UI-TARS-2、开放基准与环境可用；但大规模并行虚拟机RL环境、轨迹数据和评测成本仍高。 |
| 资源注入 R | 5 | OpenAI（Operator/ChatGPT agent）、Anthropic、Google（Mariner）、字节、微软均在产品线投入，多家创业公司（Simular等）。 |
| 学术空间 H | 3.5 | 安全性（提示注入）、长程可靠性、效率、grounding仍开放；但训练前沿CUA需重度工业环境与算力，学术多做基准/分析。 |
| 外溢平台性 X | 4 | 影响软件自动化、RPA、测试、无障碍、科研工具操作等多个相邻领域。 |
| 风险扣分 P | 5 | 基准分数≠真实可靠性（72%仍意味大量失败、效率远低于人）；提示注入等安全风险；可能被API/MCP工具调用路线部分替代；结果高度依赖闭源前沿模型。 |

> 校准：S 4 → 3.5，OSWorld-Verified 已超过人类基线，基准趋于饱和，各前沿实验室均已产品化

**关键证据**：

- 2026-03 OSWorld 上智能体成功率从12.24%（2024-04）提升到72.6%（2025-12），用时20个月 [来源](https://www.buildmvpfast.com/blog/osworld-benchmark-ai-agents-passed-human-baseline-2026)
- 2026-03 GPT-5.4 在OSWorld-Verified得分75.0%，超过人类平均72.4% [来源](https://signalmesh.beehiiv.com/p/ai-crossed-the-human-line)
- 2026-02 Claude Sonnet 4.5 OSWorld 61.4%（Sonnet 4.0为42.2%）；Opus 4.6达72.7% [来源](https://www.longtermwiki.com/wiki/osworld)
- 2025-09 UI-TARS-2 开源：OSWorld 47.5、WindowsAgentArena 50.6、AndroidWorld 73.3，采用数据飞轮+多轮RL [来源](https://arxiv.org/abs/2509.02544v1)
- 2026-08 一项综述审阅2018-01至2026-04共336篇GUI智能体论文，领域自2024年起急剧扩张 [来源](https://www.alphaxiv.org/abs/2608.09278.md)
- 2025-12 NeurIPS 2025 约45篇计算机使用智能体论文（基准、安全、grounding等） [来源](https://cua.ai/blog/neurips-2025-cua-papers)

**开放问题**：

- 长程任务的可靠性与效率：从'能完成'到'稳定、快速、可恢复地完成'，以及基准之外的真实工作流评测
- 提示注入、越权操作等安全问题与可验证的权限/沙箱机制
- 可扩展的GUI环境与奖励构建（自动任务生成、结果验证器）以支撑大规模在线RL

**切入点**：

- 构建垂直领域（科研软件、企业应用、移动端）的可复现GUI基准与自动验证器，或研究CUA的安全攻击与防御
- 基于UI-TARS/Qwen-VL等开放模型研究视觉grounding、小模型高效动作执行或GUI+API混合调用策略

---

## 14. 智能体安全 — 67.0（C 观察）

*AI Agent Security (prompt-injection defenses, tool-use security, agent sandboxing, AgentDojo-style benchmarks)* · AI-可信与推理 · `G5 S4 C3 E5 R5 H4 X3 P5` · 排名区间 13–14

**拐点事件**：2023-02 Greshake等提出“间接提示注入”确立威胁模型；2024-06 AgentDojo成为统一基准；2025-03 CaMeL首次给出“设计上安全”的系统级防御。尚缺的“GPT-3时刻”是：在自适应攻击下仍保持高实用性的通用可证明防御。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 5 | 2024-2026涌现AgentDojo、WASP、PIArena、LongPIBench、AgentVigil等大量基准与攻防论文；未找到可靠的arXiv计数，但产业端2026年AI安全种子轮已达8.55亿美元/150+轮，按定性证据判断>100%/年。 |
| 阶段窗口 S | 4 | OWASP将提示注入列为LLM01:2025首要风险，RSAC 2026创新沙盒聚焦智能体安全，产业已大规模介入；学术界在安全四大会上已有专门session，但防御范式仍无共识（模型级防御被自适应攻击击穿，系统级方案仍在探索），处于起飞向成熟过渡段。 |
| 能力拐点 C | 3 | CaMeL等系统级设计在AgentDojo上实现77%任务的可证明安全，是重要的存在性证明；但“The Attacker Moves Second”用自适应攻击使12种防御中多数攻击成功率>90%，人类红队100%攻破，能力拐点更多来自威胁侧而非防御侧。 |
| 使能条件 E | 5 | 基准、开源模型、MCP/工具生态、沙箱均广泛可得，计算成本低。 |
| 资源注入 R | 5 | 智能体安全初创累计融资约36亿美元，Palo Alto收购Protect AI、Check Point收购Lakera、SentinelOne收购Prompt Security等密集并购；OpenAI/Anthropic/GDM均有专门团队。 |
| 学术空间 H | 4 | 指令-数据分离、面向智能体的信息流控制与能力系统、可证明防御、自适应评测方法论等根本问题开放，学术算力即可研究。 |
| 外溢平台性 X | 3 | 重塑系统安全、操作系统/浏览器安全、Web安全与软件供应链安全（MCP），但主要仍是安全子领域。 |
| 风险扣分 P | 5 | 攻防猫鼠游戏、大量防御论文评测不充分（自适应攻击下失效）、厂商炒作明显；可能被并入通用安全工程与模型安全训练；扣5分。 |

**关键证据**：

- 2025-03 CaMeL通过从可信查询中显式抽取控制/数据流，在AgentDojo上实现约67%–77%任务的可证明安全 [来源](https://liner.com/review/defeating-prompt-injections-by-design)
- 2025-10 OpenAI/Anthropic/GDM等14位作者的“The Attacker Moves Second”用自适应攻击绕过12种防御，多数攻击成功率>90%，500人红队竞赛100%攻破 [来源](https://arxiv.org/abs/2510.09023)
- 2026-07 Agent数据注入攻击成功率最高50%，仅CaMeL Strict完全阻止（0% ASR），其他防御仍有22.2%–50% [来源](https://arxiv.org/pdf/2607.05120)
- 2026-03 智能体AI安全初创合计融资36亿美元，2026年4–9月12笔融资共4.35亿美元；Palo Alto/Protect AI、Check Point/Lakera、SentinelOne/Prompt Security等并购 [来源](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/)
- 2026-06 2026年迄今AI安全种子轮融资8.55亿美元、150余轮；OWASP将提示注入列为LLM01:2025 [来源](https://aiweekly.co/alerts/ai-security-startups-pull-855m-across-150-seed-rounds-in-2026)
- 2026-04 PIArena（2026）、LongPIBench（2026）等新基准持续出现，说明评测体系仍在快速形成 [来源](https://arxiv.org/pdf/2604.08499)

**开放问题**：

- 在不牺牲实用性的前提下实现指令/数据的根本分离与可证明的信息流控制
- 针对自适应攻击者的标准化评测方法（避免“静态攻击集下接近0%”的虚假安全）
- 多智能体/MCP工具生态中的权限最小化、供应链投毒与长时程任务中的延迟触发攻击

**切入点**：

- 在AgentDojo/WASP上用自适应攻击（RL/搜索）系统重评现有防御，或设计基于能力/IFC的系统级防御并报告效用-安全权衡
- 研究MCP服务器与工具描述投毒、浏览器/计算机使用智能体的沙箱与权限策略，结合传统系统安全方法（形式化策略、引用监视器）

---

## 15. AI控制与可扩展监督 — 65.0（C 观察）

*AI Control & Scalable Oversight (control protocols, CoT monitoring, model organisms of misalignment, alignment auditing)* · AI-可信与推理 · `G4 S5 C3 E4 R4 H4 X2.5 P4` · 排名区间 15–16

**拐点事件**：2024-12 Anthropic/Redwood“Alignment Faking”首次在生产模型中观察到无训练诱导的策略性伪装对齐，配合2025-07多实验室CoT可监控性立场论文，标志该领域从思辨转为实证；真正的“GPT-3时刻”将是控制协议在真实前沿智能体部署中被量化证明能拦截内部破坏行为。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 2023-12 Redwood提出“AI Control”后，2025-2026出现ControlArena（14个设定）、BashArena（637个任务）、Ctrl-Z、Petri、CoT可监控性等一系列工作；未找到可靠的论文计数，按定性证据估计年增长60-100%。 |
| 阶段窗口 S | 5 | 社区小而聚焦（Redwood、UK AISI、Anthropic、GDM、OpenAI），基准与评测库刚形成，黑客松/专门会议起步，顶会占比远低于1%，尚无共识范式，符合“LLM在2021”的窗口。 |
| 能力拐点 C | 3 | CoT监控在实践中可发现奖励作弊、Petri等自动审计智能体可在前沿模型上发现失准行为，但这些是有前景的窄胜利，而非质变能力；能力进步主要来自底层模型。 |
| 使能条件 E | 4 | ControlArena开源、开源权重模型可做红蓝方，API成本可承受；主要瓶颈是缺少真正失准的前沿模型样本，只能依赖model organisms。 |
| 资源注入 R | 4 | 三大前沿实验室均有团队；40余名来自OpenAI/GDM/Anthropic/Meta的研究者联名CoT可监控性论文；UK AISI Alignment Project总额达£27m（含OpenAI £5.6m）；总量远小于10亿美元。 |
| 学术空间 H | 4 | 监控器-被监控者能力差、隐写/不忠实CoT、评测意识（eval awareness）、控制评估的红队充分性等问题大量开放，许多可用开源模型+API研究。 |
| 外溢平台性 X | 2.5 | 主要服务AI安全与部署治理，对安全运维、智能体安全、人机协作审批流程有一定外溢。 |
| 风险扣分 P | 4 | 可监控性依赖“模型用自然语言推理”这一脆弱前提，可能被潜空间推理/强结果RL破坏；评测真实性受eval-awareness影响；资金高度依赖安全导向机构；扣4分。 |

**关键证据**：

- 2025-07 40余名来自OpenAI、GDM、Anthropic、Meta的研究者联合发表“CoT Monitorability: A New and Fragile Opportunity”，Hinton、Sutskever等背书 [来源](https://arxiviq.substack.com/p/chain-of-thought-monitorability-a)
- 2025-10 UK AISI与Redwood发布ControlArena，含14个“正常任务+隐蔽恶意目标”设定，已被Anthropic、GDM等使用；BashArena含637个Linux运维任务与4类破坏目标 [来源](https://www.aisi.gov.uk/blog/introducing-controlarena-a-library-for-running-ai-control-experiments)
- 2026-02 UK AISI Alignment Project首批资助60个项目，总资金增至£27m，新增OpenAI(£5.6m)、Microsoft等出资方 [来源](https://www.aisi.gov.uk/blog/funding-60-projects-to-advance-ai-alignment-research)
- 2025-12 Anthropic开展“审计隐藏目标”的auditing game（4个人类团队），并开源Petri自动化行为审计工具，用于评估前沿模型失准程度 [来源](https://alignment.anthropic.com/)
- 2023-12 Redwood Research于2023-12发表“AI Control: Improving Safety Despite Intentional Subversion”，提出可信/不可信模型监控协议框架 （background knowledge）
- 2025-03 OpenAI报告用较弱模型监控推理模型CoT可有效发现奖励作弊，但对CoT施加优化压力会导致“隐藏意图” （background knowledge）

**开放问题**：

- 如何保证CoT忠实且可监控，以及在潜空间推理/强化学习下保持可监控性
- 当被监控模型强于监控器时的可扩展监督（辩论、递归监督、弱到强）是否有效
- 控制评估的红队是否充分（模型故意藏拙/sandbagging、评测意识）以及如何给出可信的安全论证（safety case）

**切入点**：

- 基于ControlArena/BashArena，用开源模型做新的监控协议（如多监控器集成、重采样Ctrl-Z）或新的攻击策略并报告安全-有用性帕累托曲线
- 构建小规模model organisms（如通过微调植入隐藏目标/奖励作弊），研究可解释性或黑盒审计方法的检出率

---

## 16. 学习增强算法 / 带预测的算法（含LLM驱动的算法发现） — 63.3（C 观察）

*Learning-Augmented Algorithms & LLM-Driven Algorithm Discovery* · 量子/密码/网络/理论 · `G4 S4.5 C3 E4 R3.5 H4.5 X3.5 P6` · 排名区间 15–17

**拐点事件**：2025年5月 DeepMind AlphaEvolve 以 LLM+自动评估的演化搜索改进多个数学/算法开放问题的已知界（接吻数、矩阵乘法、有限域 Kakeya），并于2025-11与 Tao 等合作系统化报告67个问题——LLM 成为算法发现工具的“GPT-3时刻”雏形。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | “带预测的算法”自2018年起稳定增长（论文列表早期已超100篇，现数百篇，精确数未知）；2025年 AlphaEvolve 后 LLM 演化搜索框架一年内涌现 OpenEvolve、ShinkaEvolve、CodeEvolve、GigaEvo、LoongFlow、ThetaEvolve 及多个基准，增速>60%/年。 |
| 阶段窗口 S | 4.5 | 经典“带预测的算法”已有一致性/鲁棒性框架（偏成熟，SIGMETRICS LATA、STOC 2026 ML for Algorithms 研讨会）；而 LLM 驱动算法发现处于急速起飞、无共识范式阶段，整体接近目标窗口。 |
| 能力拐点 C | 3 | FunSearch（2023-12）改进 cap set 下界；AlphaEvolve（2025-05）在67个问题中多数复现最优、部分改进，如11维接吻数592→593、4×4复矩阵乘法48次乘法（background knowledge）；Tao 等基于其输出发表新结果。但改进幅度小、领域窄，缩放规律未明。 |
| 使能条件 E | 4 | OpenEvolve/ShinkaEvolve 等开源，LLM API 可得；大规模演化搜索的 API/算力成本是限制但非致命。 |
| 资源注入 R | 3.5 | Google DeepMind（AlphaEvolve）、Sakana AI、OpenAI/各大实验室的 AI-for-math 投入；但专门面向算法设计的资金规模有限。 |
| 学术空间 H | 4.5 | 如何为 LLM 生成算法提供可证明保证、评测方法论、预测误差模型、与复杂性理论（硬度归约 gadget 搜索）结合，大量问题适合理论小组。 |
| 外溢平台性 X | 3.5 | 外溢到组合数学、TCS、系统优化（调度、编译器、数据中心）、科学计算，可能成为“算法设计的通用工具”。 |
| 风险扣分 P | 6 | 评测可能高估进展（2026-09 预印本《Evolution or Illusion?》质疑 LLM 演化搜索评测）、AlphaEvolve 的接吻数结果被人类反超、改进多为边际，并可能被通用 AI-for-math 吸收，扣6分。 |

> 校准：C 3.5 → 3，AlphaEvolve 的证据已计入“自我改进与进化搜索”和“AI 科学家”，此处只按理论侧（带预测的算法）计分，避免三重计分

> 校准：X 4 → 3.5，同上，去除与 AlphaEvolve 相关的重复外溢

**关键证据**：

- 2025-11 Georgiev、Tao、Gómez-Serrano、Wagner 用 AlphaEvolve 处理分析、组合、几何、数论67个问题，多数复现最优解并在若干问题上改进（如有限域 Kakeya 界） [来源](https://alphaxiv.org/overview/2511.02864v1)
- 2025-05 AlphaEvolve 将11维接吻数下界从592提高到593；FunSearch 曾改进 cap set 下界 [来源](https://www.popsci.com/science/human-outsmarts-ai-kissing-problem-math)
- 2025-09 开源复刻/改进框架 OpenEvolve、ShinkaEvolve（样本效率高数个量级，改进圆填充结果）、CodeEvolve、GigaEvo、ThetaEvolve 等快速出现 [来源](https://sakana.ai/shinka-evolve/)
- 2026-06 STOC 2026 举办 Machine Learning for Algorithms 研讨会；SIGMETRICS 2025/2026 连续举办学习增强算法研讨会 LATA；TAAP 2025 专门研讨会 [来源](https://www.mit.edu/~vakilian/stoc26-workshop.html)
- 2026-09 预印本《Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search》质疑现有评测方式 [来源](https://arxiv.org/pdf/2609.19799)
- 2025-09 Google 用 AlphaEvolve 搜索组合构造改进 MAX-4-CUT 等不可近似性结果与 Ramanujan 图相关界，属 TCS 应用 （background knowledge）

**开放问题**：

- 为 LLM/演化搜索发现的算法与构造提供可验证的正确性与最坏情况保证（与形式化证明助手结合）
- 建立防止过拟合与评测泄漏的算法发现基准与方法论，刻画搜索预算与改进幅度的缩放关系
- 统一“带预测的算法”理论（一致性-鲁棒性权衡、预测误差度量）与 LLM 作为预测器/设计者的新范式

**切入点**：

- 用 OpenEvolve/ShinkaEvolve 在组合优化、在线算法或硬度归约 gadget 等具有自动评估器的问题上做定向攻关，小算力即可产出可发表结果
- 在经典学习增强算法框架下研究以 LLM 输出为预测的在线/近似算法，给出一致性-鲁棒性理论保证（SODA/ICALP/NeurIPS）

---

## 17. 神经数据基础模型与脑机接口解码 — 62.9（C 观察）

*Neural Data Foundation Models and BCI Decoding* · 具身/空间/生命科学交叉 · `G4 S4.5 C3.5 E2.5 R4 H4.5 X3 P5` · 排名区间 16–18

**拐点事件**：解码侧拐点：2024-08 NEJM ALS语音BCI（~97%准确率）与2025-06 Nature实时语音合成神经假体；基础模型侧候选“GPT-3时刻”：跨被试、跨设备零样本解码的神经基础模型显示清晰scaling定律（OmniMouse 2026在1500亿神经token上的scaling研究为早期迹象）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | POYO(2023)→POYO+、NDT3、NEDS(约3万神经元/74 session)、OmniMouse(1500亿神经token，ICLR 2026)规模持续扩大；NeurIPS 2025首设“脑与身体基础模型”workshop和EEG Foundation Challenge；未找到精确论文计数，定性估计60-100%/年。 |
| 阶段窗口 S | 4.5 | 首批专门workshop、挑战赛和benchmark刚形成；分词方式、跨被试对齐等无共识范式；在ML顶会中份额很小，符合起飞期特征。 |
| 能力拐点 C | 3.5 | 语音神经假体是明确拐点：2025-06 Nature报道约30ms延迟实时语音合成，125k词表词准确率达97.5%；但其驱动力主要是解码器与植入技术而非通用基础模型，神经基础模型的scaling收益仍有限，EEG基础模型常不优于简单模型。 |
| 使能条件 E | 2.5 | 侵入式数据稀缺且受伦理/隐私限制，记录设备与协议异构；DANDI、IBL等开放数据与EEG benchmark正在出现，但关键数据规模远不及其他模态。 |
| 资源注入 R | 4 | Neuralink 2025年E轮6.5亿美元（估值约90亿）；OpenAI参投Merge Labs约2.5亿美元种子轮；Synchron D轮2亿美元；BRAIN Initiative等政府资助。 |
| 学术空间 H | 4.5 | 跨被试/跨设备泛化、神经tokenization、多模态神经-行为建模、闭环自适应解码等基础问题可在公开数据和学术算力上研究。 |
| 外溢平台性 X | 3 | 主要影响神经科学、医疗设备与人机交互；对通用CS外溢中等。 |
| 风险扣分 P | 5 | 临床样本量极小（Neuralink约26名受试者），监管与手术是硬性物理限制；Musk/Altman带来的炒作与EEG基础模型可复现性问题。扣5分。 |

**关键证据**：

- 2025-06 Nature报道实时语音合成神经假体，延迟约30ms，可调语调甚至唱歌 [来源](https://ideas.repec.org/a/nat/nature/v644y2025i8075d10.1038_s41586-025-09127-3.html)
- 2026-04 OmniMouse：在1500亿神经token上研究多模态多任务脑模型的scaling性质（ICLR 2026） [来源](https://arxiv.org/pdf/2604.18827)
- 2025-04 NEDS在约3万神经元、74个session上进行多任务编解码，对比POYO+与NDT2，显示数据规模提升下游性能 [来源](https://arxiv.org/html/2504.08201v1)
- 2025-12 NeurIPS 2025举办“Foundation Models for the Brain and Body”workshop；EEG基础模型benchmark显示简单模型在临床分布偏移下仍有竞争力 [来源](https://neurips.cc/virtual/2025/workshop/109571)
- 2025-06 Neuralink 2025年E轮融资6.5亿美元，估值约90亿美元；2026年受试者达26人 [来源](https://news.bloombergtax.com/private-equity/neuralink-raises-650-million-in-late-stage-funding-round)
- 2026-01 OpenAI参投Sam Altman联合创立的BCI公司Merge Labs约2.5亿美元种子轮，估值约8.5亿美元 [来源](https://techinformed.com/openai-backs-merge-labs-in-250m-seed-round-led-by-sam-altman/)
- 2025-11 Synchron完成2亿美元D轮融资 [来源](https://app.dealroom.co/news/feed/synchron-raises-200m-for-bci-tech)

**开放问题**：

- 跨被试、跨脑区、跨记录设备的神经表征对齐与零样本迁移
- 神经数据的scaling定律：更多神经元/会话/物种能否带来可预测增益，tokenization如何设计
- 长期植入下的非平稳性与闭环自适应解码，以及非侵入式（EEG/MEG）基础模型的真实增益验证

**切入点**：

- 利用DANDI、IBL、NLB（Neural Latents Benchmark）和EEG Foundation Challenge等公开数据，在POYO/NDT开源代码上做跨会话迁移与scaling研究
- 与临床BCI团队合作，研究语言模型先验在语音/文本解码中的作用，或开发严格的EEG基础模型评测协议

---

## 18. 机制可解释性 — 61.7（C 观察）

*Mechanistic Interpretability (SAEs, transcoders, attribution graphs / circuit tracing, model diffing)* · AI-可信与推理 · `G4 S4 C3 E4 R4 H5 X3 P4` · 排名区间 17–19

**拐点事件**：2024-05 Anthropic “Scaling Monosemanticity” 在生产级模型Claude 3 Sonnet上提取数百万可解释特征（“金门大桥Claude”），再到2025-03 attribution graphs 追踪Claude 3.5 Haiku的完整计算电路；真正的“GPT-3时刻”尚待到来：能在前沿模型上可靠地发现并修复真实未知的错误行为。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 一项文献计量研究统计：主要会议中该主题论文2025年约100篇，同比约3.7倍；关键词计数2022→2023→2024为3→9→23，持续高速增长，但基数仍小。 |
| 阶段窗口 S | 4 | 已有ICML/NeurIPS专门workshop与Neuronpedia/Gemma Scope等公共基础设施，并入选MIT Technology Review 2026十大突破技术；在顶会论文中占比仍很小，且SAE与线性探针、神经元基等范式仍有争论，尚无共识范式，处于起飞期后段。 |
| 能力拐点 C | 3 | Anthropic的attribution graphs在Claude 3.5 Haiku上展示了提前规划、跨语言概念等电路（2025-03），属于较强的存在性证明；但GDM报告SAE在有害意图OOD检测上不如线性探针，并降低了基础SAE研究的优先级，实际可用收益较窄。 |
| 使能条件 E | 4 | Gemma Scope 2已覆盖到27B参数，circuit-tracing工具开源，TransformerLens/nnsight/Neuronpedia成熟；对前沿闭源模型无内部访问是主要瓶颈。 |
| 资源注入 R | 4 | Anthropic、GDM、OpenAI均设有专门团队；Goodfire于2026-02完成1.5亿美元B轮（估值12.5亿美元）；整体资金规模远低于10亿美元级的前沿方向。 |
| 学术空间 H | 5 | 特征完备性、叠加（superposition）、可解释性评估标准、电路的可扩展自动化等基础问题大量开放，且在7B以下开源模型上用学术算力即可研究。 |
| 外溢平台性 X | 3 | 可外溢到模型调试、对齐审计、科学模型（如生物基础模型）中的知识发现，但主要仍是服务于ML本身的工具学科。 |
| 风险扣分 P | 4 | 炒作与实际效果有落差（SAE负面结果），方法论的可复现性和“解释是否忠实”仍受质疑；扣4分。 |

**关键证据**：

- 2026-06 该主题在主要会议中2025年达到约100篇论文，同比增长约3.7倍；关键词计数2022/2023/2024为3/9/23篇 [来源](https://arxiv.org/pdf/2606.12828)
- 2025-03 Anthropic用attribution graphs追踪Claude 3.5 Haiku，发现诗歌写作中的提前规划、语言无关的概念电路，并开源circuit tracing工具 [来源](https://pub.towardsai.net/mechanistic-interpretability-is-having-its-moment-what-engineers-actually-need-to-know-e4421f305f84)
- 2025-12 DeepMind Gemma Scope 2 将SAE分析扩展到27B参数模型 [来源](https://pub.towardsai.net/mechanistic-interpretability-is-having-its-moment-what-engineers-actually-need-to-know-e4421f305f84)
- 2025-03 GDM机制可解释性团队报告：SAE在有害意图OOD检测上逊于线性探针，决定降低基础SAE研究优先级 [来源](https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/)
- 2026-02 Goodfire于2026年2月完成1.5亿美元B轮，估值12.5亿美元；MIT Technology Review将机制可解释性列为2026年突破技术 [来源](https://www.longtermwiki.com/wiki/goodfire)
- 2026-01 ICML 2026论文表明MLP神经元本身与SAE一样稀疏，约100个神经元的电路即可控制主谓一致行为——基础表示单元仍无共识 [来源](https://arxiv.org/abs/2601.22594)

**开放问题**：

- 如何评估解释的忠实性与完备性（缺少ground truth与统一的度量基准）
- SAE/transcoder的特征是否是模型的“自然单元”，以及如何处理特征分裂、吸收与暗物质（未解释方差）
- 将电路级分析扩展到长推理链、智能体轨迹与前沿规模模型，并转化为可靠的下游安全/调试收益

**切入点**：

- 基于Gemma Scope 2、Neuronpedia和开源circuit-tracer，在≤9B开源模型上做特征/电路的忠实性评测与对比（SAE vs 探针 vs 神经元基）
- 做“模型差分”（base vs 微调/RL后模型）找出训练引入的行为变化，或将可解释性方法用于生物/科学基础模型中的知识发现

---

## 19. 人形机器人全身控制与sim2real — 59.6（D 暂缓）

*Humanoid Whole-Body Control and Sim-to-Real* · 具身/空间/生命科学交叉 · `G4 S3.5 C4 E4.5 R4.5 H4 X2.5 P5` · 排名区间 18–22

**拐点事件**：拐点已于2024-2025年间发生：大规模并行RL+运动跟踪让人形机器人零样本sim2real完成高动态技能（2025-06 GMT、2025-08 BeyondMimic）；下一个“GPT-3时刻”应是统一全身控制器在真实环境中完成通用接触丰富的移动操作。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 2025年密集涌现BeyondMimic、GMT、ASAP、HumanPlus/OmniH2O后续、LangWBC、CLONE等工作，2026年继续有OmniXtreme、AnyBody等；未找到精确论文计数，按定性证据+Unitree出货（2025年>5500台，70%以上营收来自科研教育）估计约60-100%/年。 |
| 阶段窗口 S | 3.5 | 已形成共识范式：大规模并行仿真PPO（IsaacLab/MuJoCo）+域随机化+人体动作重定向的运动跟踪；RSS/CoRL已有专门workshop，进入“已建立方法”阶段而非早期起飞。 |
| 能力拐点 C | 4 | 2025年单一通用跟踪策略零样本迁移到真机完成侧手翻、旋转跳、冲刺等（BeyondMimic、GMT），是强存在性证明；但能力仍局限于运动技能，接触丰富的全身移动操作尚未突破。 |
| 使能条件 E | 4.5 | Unitree G1等平价人形平台大规模普及、IsaacLab/MuJoCo Playground开源、AMASS等人体动作数据可用；硬件可靠性仍是约束。 |
| 资源注入 R | 4.5 | Figure C轮10亿美元估值390亿美元；Tesla Optimus、NVIDIA GR00T、Boston Dynamics、中国大量政府与产业资本投入；但WBC本身更多由学术+创业团队推进。 |
| 学术空间 H | 4 | 移动操作、接触与力控、安全与鲁棒性、与VLA的层级接口等问题在学术算力下可做（单卡GPU+一台G1即可）。 |
| 外溢平台性 X | 2.5 | 主要外溢到机器人学与计算机动画/角色控制，对更广CS影响有限。 |
| 风险扣分 P | 5 | 人形机器人估值泡沫明显，demo与实际部署差距大；硬件耐久性与安全监管是物理约束；运动跟踪可能被统一的VLA/层级系统吸收。扣5分。 |

**关键证据**：

- 2025-08 BeyondMimic实现跳跃旋转、冲刺、侧手翻等高质量动作跟踪，并用引导扩散在测试时组合任务 [来源](https://arxiv.org/abs/2508.08241v2)
- 2025-06 GMT（UCSD/SFU）用自适应采样+运动MoE训练单一统一策略，在Unitree G1上稳健复现多样动作 [来源](https://arxiv.org/abs/2506.14770v2)
- 2026-01 Unitree 2025年人形机器人出货超5500台；截至2025Q3超70%人形营收来自科研与教育客户 [来源](https://en.jiemian.com/article/13924474.html)
- 2025-09 Figure完成10亿美元C轮，投后估值390亿美元 [来源](https://landbase.com/blog/fastest-growing-robotics-companies)
- 2026-02 RSS 2025设有全身控制与双臂操作workshop；CLONE全身遥操作发表于CoRL 2025 [来源](https://arxiv.org/pdf/2602.23843)
- 2026-06 2026年持续出现通用高动态控制（OmniXtreme）与任意关键点引导全身控制（AnyBody）等工作 [来源](https://arxiv.org/pdf/2606.29209)

**开放问题**：

- 接触丰富的全身移动操作：在保持平衡的同时进行力控交互与搬运
- 从运动跟踪到语言/视觉条件的通用控制器，以及与上层VLA的接口设计
- sim2real的系统性理论与安全性：执行器建模、跌倒恢复、长期可靠性保证

**切入点**：

- 采购Unitree G1等平价平台，基于开源BeyondMimic/GMT/IsaacLab代码复现并扩展到移动操作或新技能
- 研究动作数据侧：人体视频到机器人动作的重定向、物理可行性过滤和数据集构建

---

## 20. 虚拟细胞 / 单细胞基础模型 — 59.6（D 暂缓）

*Virtual Cell / Single-Cell Foundation Models* · 具身/空间/生命科学交叉 · `G4 S4.5 C2 E3 R4 H5 X3.5 P5` · 排名区间 18–22

**拐点事件**：尚未发生。候选“GPT-3时刻”：某模型在未见细胞类型/未见扰动上零样本预测转录组响应并稳定、显著超越线性基线（Arc 2026虚拟细胞挑战即以此为目标）；2025-06 Arc发布State与首届挑战赛是社区形成标志而非能力拐点。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | Arc虚拟细胞挑战赛2025年吸引5000+注册者、114国、1200+提交队伍，2026年第二届已启动；scGPT、Geneformer、scFoundation、State、TranscriptFormer等模型密集发布；未找到精确论文计数，估计60-100%/年。 |
| 阶段窗口 S | 4.5 | 处于典型起飞期：首届挑战赛、benchmark（PertEval-scFM等）刚形成，评测指标本身仍有争议，无共识范式，在ML顶会中份额很小。 |
| 能力拐点 C | 2 | 能力拐点尚未出现：Nature Methods(2025-08)显示5个基础模型+2个深度模型在扰动预测上均未超过简单线性基线；挑战赛冠军也承认纯AI方法未稳定超越统计基线。 |
| 使能条件 E | 3 | CELLxGENE、Tahoe-100M、Billion Cells Project等观测数据丰富，但跨细胞类型的高质量扰动数据稀缺，评测指标（MAE/PDS/DES）可被操纵，是主要瓶颈。 |
| 资源注入 R | 4 | CZI建设1万GPU集群并与NVIDIA扩大合作、Arc Institute、Xaira（>10亿美元）、Altos Labs、BioMap等投入；前沿LLM实验室参与有限。 |
| 学术空间 H | 5 | 表示学习、因果/扰动泛化、评测方法学、数据设计等基础问题大量开放，学术算力即可开展。 |
| 外溢平台性 X | 3.5 | 主要重塑计算生物学与药物发现，对通用CS外溢有限。 |
| 风险扣分 P | 5 | “虚拟细胞”叙事与实测结果差距显著，挑战赛出现指标被操纵与排行榜崩塌；扣5分。 |

**关键证据**：

- 2025-08 Nature Methods：5个单细胞基础模型和2个深度学习模型在单/双基因扰动预测上均未超越刻意简单的线性基线 [来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328236/)
- 2025-12 Arc虚拟细胞挑战（Arc/NVIDIA/10x/Ultima）吸引5000+注册者、1200+提交队伍，NeurIPS 2025公布结果，BioMap总冠军、Altos Labs获通用奖 [来源](https://www.genengnews.com/topics/artificial-intelligence/neurips-2025-altos-labs-wins-generalist-prize-at-arcs-virtual-cell-challenge)
- 2025-12 挑战赛MAE指标设计导致排行榜可被数据变换操纵，PDS榜首方法TransPert使用经典统计而非大模型 [来源](https://gmdbioinformatics.substack.com/p/arc-virtual-cell-challenge-has-the)
- 2025-10 CZI建设1万GPU集群、推进十亿细胞项目，并于2025-10与NVIDIA扩大虚拟细胞模型合作 [来源](https://www.rdworldonline.com/czi-and-nvidia-expand-virtual-cell-push-with-open-models-and-benchmarks/)
- 2026-06 Arc 2026虚拟细胞挑战聚焦模型从未见过的细胞上下文中的扰动响应预测（零样本） [来源](https://arcinstitute.org/news/virtual-cell-challenge-2026)
- 2025-06 Arc发布基线模型STATE（State Transition + State Embedding两部分） [来源](https://huggingface.co/blog/virtual-cell-challenge)

**开放问题**：

- 如何在未见细胞类型和未见扰动上实现可泛化的因果预测，而不仅是拟合平均表达
- 构建不可被操纵、与生物学意义一致的评测指标与基线体系
- 多模态整合（转录组、蛋白组、成像、空间组学）与主动实验设计以弥补扰动数据稀缺

**切入点**：

- 参加Arc 2026虚拟细胞挑战，系统性对比基础模型与强线性/统计基线，发表严谨的评测与消融研究
- 利用Tahoe-100M、Replogle Perturb-seq等公开数据研究表示质量与扰动预测的关系，或开发主动学习式实验设计方法

---

## 21. AI数据中心能效与电力感知计算 — 59.5（D 暂缓）

*AI Datacenter Energy and Power-Aware Computing* · 系统与硬件 · `G4 S4 C2.5 E3 R5 H4 X3.5 P4` · 排名区间 19–22

**拐点事件**：2025 年 5 月 Emerald AI 在凤凰城用 256 块 GPU 完成首次 AI 负载电网响应示范（持续削减 25% 功率）；2025 年 8 月 Microsoft/OpenAI/NVIDIA 发表《Power Stabilization for AI Training Datacenters》，确认吉瓦级训练的功率摆动可能损伤电网。可能的“GPT-3 时刻”是 AI 数据中心作为可调度柔性负载被规模化接入电网市场（2026-2027 年）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 需求侧爆发：2025 年数据中心用电增长 17%（是全球总用电增速的 5 倍以上），IEA 预计 2030 年从约 485 TWh 增至约 945 TWh；EPRI DCFlex 汇集了 60+ 机构。学术论文增长没有确切数字，估计 60-100%/年。 |
| 阶段窗口 S | 4 | HotCarbon 等研讨会已存在，但“电网交互/功率摆动/吉瓦级集群”的系统研究刚刚形成（2025 年 Microsoft/OpenAI/NVIDIA 功率稳定论文、Emerald AI 示范），尚无共识范式。 |
| 能力拐点 C | 2.5 | 这里的拐点主要体现在问题层面（吉瓦级同步训练带来的电网级功率摆动），而不是能力突破。已有初步方案：Emerald AI 在 256 GPU 上演示持续削减 25% 功率；全栈方案让功率过冲降低 40%。属于渐进到窄范围的胜利。 |
| 使能条件 E | 3 | GPU 功率遥测和开源能耗测量工具可用，但真实电网/设施数据和大规模集群需要与产业合作，是一个主要瓶颈。 |
| 资源注入 R | 5 | 超大规模云厂商 AI 基建投入超过 4,000 亿美元（2025 年），并有 NVIDIA、EPRI、各电力公司以及 SMR 购电协议（45 GW）。 |
| 学术空间 H | 4 | 电力感知调度、能耗建模、碳感知训练、功率平滑算法都可以用小集群和模拟研究。 |
| 外溢平台性 X | 3.5 | 连接 CS 与能源/电力系统，影响调度、体系结构和可持续计算等多个领域。 |
| 风险扣分 P | 4 | 受物理与监管约束（并网审批、变压器短缺），核心数据被少数厂商掌握，也有“漂绿”式指标风险，因此扣 4 分。 |

**关键证据**：

- 2026-04 2025 年数据中心用电增长 17%，是全球总用电增速（3%）的 5 倍以上；科技公司 AI 基建投入超过 4,000 亿美元，2026 年可能再增 75% [来源](https://letsdatascience.com/news/ai-drives-surge-in-data-centre-electricity-demand-16cbe703)
- 2026-04 IEA：全球数据中心用电从 2025 年约 485 TWh 增至 2030 年约 945 TWh，其中 AI 相关用电约增至 3 倍 [来源](https://datacentremagazine.com/data-centres/ai-boom-will-cause-data-centre-electricity-demand-to-double)
- 2025-07 Emerald AI 于 2025 年 5 月 3 日在凤凰城 Oracle 数据中心用 256 块 NVIDIA GPU 进行电网压力事件示范，目标是持续削减 25% 功率；EPRI DCFlex 汇集 60+ 机构 [来源](https://introl.com/blog/data-centers-grid-stabilizers-flexible-power-nvidia-epri-2026)
- 2025-08 Microsoft/OpenAI/NVIDIA：数万 GPU 同步训练产生的功率摆动可能与电网关键频率共振而损伤设备；全栈方案可让功率过冲降低 40%，但设置功率下限可能多耗 10% 以上能量 [来源](https://arxiv.org/html/2508.14318v1)
- 2026-04 与 SMR 项目相关的购电协议从 2024 年底 25 GW 增至 45 GW [来源](https://letsdatascience.com/news/ai-drives-surge-in-data-centre-electricity-demand-16cbe703)
- 2026-01 微软发表 PowerSlider：利用 LLM 服务的相位不对称性应对需求响应 [来源](https://www.microsoft.com/en-us/research/group/azure-research-systems/publications/)

**开放问题**：

- 吉瓦级同步训练的功率摆动平滑：软件（调度、通信重叠）与硬件（储能、功率封顶）的协同设计及其能量代价
- 训练/推理负载的电网柔性：在满足 SLO 和收敛的前提下，实现可证明的功率调节与需求响应
- 端到端能耗/碳排放的准确建模与归因（含冷却、嵌入碳、推理与智能体负载）

**切入点**：

- 用小规模 GPU 集群 + NVML 功率遥测，研究 LLM 训练/服务在功率封顶、DVFS 下的性能-能耗权衡与调度算法
- 构建开源的“AI 负载-电网”协同模拟器（结合公开电网价格/碳强度数据与 LLM 负载 trace），研究需求响应策略

---

## 22. 光计算与光互连 — 57.6（D 暂缓）

*Optical Interconnect and Photonic Computing* · 系统与硬件 · `G4 S4 C3.5 E2 R5 H3 X3 P5` · 排名区间 20–25

**拐点事件**：光互连侧：2025 年 3 月 NVIDIA 发布 Spectrum-X/Quantum-X Photonics CPO 交换机，2026 年下半年开始出货；光计算侧：2025 年 4 月 Nature 同期发表 Lightmatter 多芯片光子处理器（可运行 ResNet/BERT）和 Lightelligence PACE。真正的“GPT-3 时刻”可能是 2027 年 scale-up CPO 进入 NVLink 级互连。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 产业侧增长迅猛：Coherent 把 CPO 可服务市场上调至 150 亿美元，Ayar Labs 仅 2026 年就融资 6.5 亿美元。学术论文增速没有找到确切数字，估计 60-100%/年。 |
| 阶段窗口 S | 4 | 光互连在光学/通信社区已成熟，但在 CS 体系结构/系统社区（光交换拓扑、CPO 感知的集群设计）仍处早期；光计算仍以少数团队为主。 |
| 能力拐点 C | 3.5 | CPO 交换机（Spectrum-X Photonics，100Tb/s）于 2026 年下半年出货，是工程上的拐点。2025 年 Nature 两篇光计算论文（Lightmatter 65.5 TOPS@78W；Lightelligence PACE 16,000+ 器件）是存在性证明，但适用面窄，NLP 精度仍有差距。 |
| 使能条件 E | 2 | 流片/PDK、封装和测试成本高，学术界接触真实硬件很难，这是主要瓶颈。 |
| 资源注入 R | 5 | NVIDIA 向 Coherent/Lumentum 投资 40 亿美元，Lightmatter 估值 44 亿美元，Ayar Labs 2026 年融资 6.5 亿美元，超过 10 亿美元量级。 |
| 学术空间 H | 3 | 器件和封装问题由资本主导；学术界的空间主要在系统层（拓扑、调度、OCS 重配置）。 |
| 外溢平台性 X | 3 | 主要重塑 AI 集群网络、体系结构和数据中心设计，对 CS 整体外溢中等。 |
| 风险扣分 P | 5 | 光计算长期存在“炒作-结果”落差（非线性、精度、ADC/DAC 开销），激光可靠性和良率问题，依赖少数厂商，因此扣 5 分。 |

**关键证据**：

- 2026-03 NVIDIA Spectrum-X Photonics 交换机 2026 年下半年出货，总带宽 100Tb/s；NVIDIA 与 Coherent、Lumentum 签署供应协议并投资 40 亿美元 [来源](https://www.optics.org/news/nvidia-backs-lumentum-and-coherent-with-4bn-cash-investment)
- 2026-05 Coherent 将 CPO SAM 上调至 150 亿美元；scale-out CPO 收入 2026 年下半年开始，scale-up CPO 2027 年下半年开始 [来源](https://futurumgroup.com/insights/coherents-23-billion-growth-opportunity-lifted-by-nvidias-optical-ambitions/)
- 2026-06 Lightmatter 完成 4 亿美元 D 轮、估值 44 亿美元；2026 年 6 月加入 NVLink Fusion 生态 [来源](https://www.lightwaveonline.com/home/podcast/55397706/podcast-lightmatters-harris-on-electrical-bottlenecks-for-scaling-ai-with-optics)
- 2026-07 Ayar Labs 再融资 1.5 亿美元，2026 年累计融资 6.5 亿美元 [来源](https://futurumgroup.com/?p=87854)
- 2025-04 Lightmatter 在 Nature 发表多芯片光子处理器：4 个 128x128 光张量核，65.5 TOPS（ABFP16）、78W 电功率，ResNet/BERT 精度接近 FP32 [来源](https://physics.aps.org/articles/v18/84)
- 2025-04 Lightelligence PACE 发表于 Nature：16,000+ 光子器件、64x64 矩阵、1GHz，延迟最多降低 500 倍 [来源](https://physicsworld.com/a/photonic-computer-chips-perform-as-well-as-purely-electronic-counterparts-say-researchers/)

**开放问题**：

- CPO/OCS 时代的 AI 集群拓扑与可重配置网络调度（拓扑随作业动态变化）
- 光计算的精度、非线性与光电转换（ADC/DAC）开销问题，以及哪些算子真正适合光域
- 激光源可靠性、热管理和可维护性对大规模集群可用性的影响建模

**切入点**：

- 系统层研究：在网络模拟器（如 ASTRA-sim、ns-3）中建模 CPO/光交换，研究集合通信与拓扑协同设计
- 做光计算的“算法-硬件协同”：为噪声/低精度光张量核设计鲁棒训练与映射方法，用仿真验证

---

## 23. Transformer/大模型理论 — 56.6（D 暂缓）

*Theory of Transformers & Large Language Models* · 量子/密码/网络/理论 · `G4 S3.5 C2.5 E5 R3 H5 X3.5 P5` · 排名区间 21–26

**拐点事件**：尚无单一“GPT-3时刻”；候选为2023-2024年 CoT 表达力的精确复杂性刻画（Merrill & Sabharwal，ICLR 2024）与 ICL≈隐式梯度下降/贝叶斯推断系列结果。若出现能定量预测缩放律或推理时计算收益的理论，将构成真正拐点。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 无精确计数；自 Garg et al.(2022) ICL 线性函数实验与 Merrill-Sabharwal CoT 表达力结果后，ICL 理论、CoT 理论、电路复杂度表达力论文在 ICML/NeurIPS/COLT 快速增长，估计60-100%/年。 |
| 阶段窗口 S | 3.5 | 已有专门研讨会（NeurIPS 2025 “What Can('t) Transformers Do?”）、Simons 研究所 2024-25 LLM 专题年、ICML 2026 主题报告；部分共识结果（TC⁰ 上界、多项式步 CoT=P）已形成，但“为何能泛化/缩放律从何来”无共识范式。 |
| 能力拐点 C | 2.5 | 作为理论领域，已有精确刻画（Merrill & Sabharwal ICLR 2024：多项式步 CoT 的 decoder 恰好识别 P），但对实践的预测与指导能力仍有限，未出现理论版“GPT-3时刻”。 |
| 使能条件 E | 5 | 主要需要数学与小模型实验，算力门槛低，工具完全可得。 |
| 资源注入 R | 3 | DARPA AIQ（为生成式 AI 提供数学保证）、Simons/IVADO、NSF 资助；工业界投入以可解释性为主，理论资金中等。 |
| 学术空间 H | 5 | 大量根本性开放问题（ICL 样本复杂度、缩放律来源、CoT/推理时计算理论、长度泛化），非常适合学术小组。 |
| 外溢平台性 X | 3.5 | 可指导架构设计、推理时计算、可解释性与安全保证，并与复杂性理论、统计物理交叉。 |
| 风险扣分 P | 5 | 理论-实践差距大、玩具模型结论脆弱、易被经验进展超越或架构更替（如状态空间模型）削弱，扣5分。 |

**关键证据**：

- 2024-05 Merrill & Sabharwal：线性步 CoT 使 decoder 停留在上下文相关语言内，多项式步 CoT 恰好识别 P，是首个 Transformer 类与标准复杂性类的精确对应 [来源](https://proceedings.iclr.cc/paper_files/paper/2024/hash/1f59721c106ea80f613299039112f651-Abstract-Conference.html)
- 2022-08 Garg et al.：从零训练的 Transformer 可在上下文中学习线性函数，性能接近最小二乘，并可学稀疏线性、决策树、两层网络 [来源](https://arxiv.org/pdf/2208.01066)
- 2025-01 Simons 研究所举办2024-2025学年 LLM 与 Transformer 专题年（与 IVADO、DARPA 合作） [来源](https://simons.berkeley.edu/programs/special-year-large-language-models-transformers-part-2)
- 2024-05 DARPA AIQ 项目征集为生成式 AI 能力提供数学保证的理论与评测研究，ICML 2026 设主题报告 [来源](https://www.darpa.mil/research/programs/aiq-artificial-intelligence-quantified)
- 2025-11 NeurIPS 2025 研讨会 “What Can('t) Transformers Do?” 聚焦 Transformer 能力与极限 （background knowledge（检索摘要提及））
- 2025-11 ICL 的样本复杂度、预训练任务多样性与上下文长度要求等问题仍未解决（线性注意力可解模型的渐近理论） [来源](https://math.mcmaster.ca/events/deep-learning-theory-seminar-mary-i-letey-asymptotic-theory-of-in-context-learning-by-linear-attention/)

**开放问题**：

- 缩放律的第一性原理解释及其对数据、架构、推理时计算的定量预测
- 推理时计算/CoT/强化学习后训练的表达力与可学习性理论（何时 CoT 可被梯度下降学到、长度泛化）
- 上下文学习的样本复杂度与预训练分布条件，以及从玩具模型到真实 LLM 的可迁移性

**切入点**：

- 在可解析模型（线性注意力、随机特征、简化 Transformer）中研究 ICL/CoT 动力学，并以小规模实验验证，面向 COLT/ICML 理论轨道
- 从电路复杂度/形式语言角度研究新架构（SSM、带循环的 Transformer、推理时计算）的表达力上下界，与 FLaNN 等社区对接

---

## 24. 零知识证明系统与zkVM — 55.4（D 暂缓）

*Zero-Knowledge Proof Systems & zkVMs* · 量子/密码/网络/理论 · `G3.5 S3 C4 E4.5 R3.5 H4 X3.5 P5` · 排名区间 23–26

**拐点事件**：2025年5月 Succinct SP1 Hypercube 实现以太坊区块实时证明（93%区块<12s），随后以太坊基金会将 L1 zkEVM 纳入路线图并设定2026年128位可证明安全目标——通用计算“证明成本跌到实时”的拐点。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3.5 | 未检索到 ePrint SNARK 论文年增长的精确统计；定性看 zkVM（SP1、RISC Zero、Jolt、OpenVM、Pico、ZisK 等）2023-2025 年爆发、证明速度年提升一个数量级以上，zkML/安全测试等子方向论文快速增加，估计30-60%/年。 |
| 阶段窗口 S | 3 | SNARK 自 2016 年 Zcash 起已成密码学成熟方向，Plonkish/FRI-STARK/lookup 等已有共识方法，RISC-V zkVM 成为事实范式；处于“已建立赛道”阶段，而非起飞初期。 |
| 能力拐点 C | 4 | SP1 Hypercube（2025-05）在200张 RTX 4090 上为 93% 以太坊区块在12秒内生成证明（平均10.3s），实现“实时证明通用计算”这一质变；zkLLM/DeepProve 已可证明 GPT-2 推理。但应用仍主要限于区块链。 |
| 使能条件 E | 4.5 | SP1、RISC Zero、Jolt、Google longfellow-zk 等全部开源，消费级 GPU 即可实验，基准与 soundcalc 等工具出现。 |
| 资源注入 R | 3.5 | Succinct 融资5500万美元、RISC Zero 4000万美元、Ingonyama 2100万美元等，加上以太坊基金会路线图与 Google 开源 ZKP 用于欧盟年龄验证；但资金高度依赖加密货币 VC，大型科技公司投入有限。 |
| 学术空间 H | 4 | 后量子/哈希型 SNARK 的可证明安全（EF 要求2026年底128位可证明安全、证明≤300KiB）、递归架构形式化验证、prover 内存/时间、zkVM 健全性测试等，学术可做空间大。 |
| 外溢平台性 X | 3.5 | 可成为“可验证计算”通用底座：区块链扩容、数字身份/年龄验证、zkML、可验证 AI 推理；但跨 CS 渗透仍有限。 |
| 风险扣分 P | 5 | 与加密货币市场强绑定、健全性漏洞频出（Arguzz 在6个 zkVM 中发现11个 bug；Solana 机密转账 Fiat-Shamir 漏洞）、营销宣称多于独立评测，扣5分。 |

**关键证据**：

- 2025-05 SP1 Hypercube 在10,000个以太坊主网区块测试中93%在12秒内完成证明，平均10.3秒，使用200张 RTX 4090 [来源](https://www.theblock.co/post/355013/succinct-introduces-zkvm-sp1-hypercube-claims-real-time-ethereum-proving)
- 2025-07 以太坊基金会发布 realtime proving 规划，并设定 L1 zkEVM 2026年中100位、年底128位可证明安全，证明大小≤600KiB→≤300KiB [来源](https://blog.ethereum.org/2025/07/10/realtime-proving)
- 2025-07 Google 开源 ZKP 库 longfellow-zk，用于欧盟年龄验证等数字身份场景 [来源](https://blog.google/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/)
- 2024-03 Succinct 获 Paradigm 领投5500万美元；RISC Zero 获4000万美元 A 轮 [来源](https://www.theblock.co/post/284002/paradigm-leads-55-million-round-in-zk-proofs-startup-succinct-labs-with-participation-from-polygon-founders)
- 2025-09 Arguzz 测试 RISC Zero、Nexus、Jolt、SP1、OpenVM、Pico 六个 zkVM，在其中三个发现11个健全性/完备性 bug，其中一个获5万美元赏金 [来源](https://arxiv.org/abs/2509.10819v1)
- 2025-08 DeepProve-1 首次为完整 GPT-2 推理生成 ZK 证明；zkLLM 对至13B参数模型证明时间1-15分钟、证明<200kB [来源](https://lagrange.dev/blog/deepprove-1)

**开放问题**：

- 在保持128位可证明安全与小证明尺寸的前提下进一步降低 prover 成本（哈希/格基后量子 SNARK、递归与折叠方案的严格安全证明）
- zkVM/电路的系统化健全性保障：形式化验证、差分模糊测试与安全参数计算
- 面向大模型推理/训练的高效 zkML（非线性算子、浮点、量化）及其在可验证 AI 中的实际部署

**切入点**：

- 基于开源 SP1/RISC Zero/Jolt 做 prover 性能或安全研究：如 GPU 内核优化、zkVM 差分模糊测试（参考 Arguzz、zkvmBlast）
- 参与以太坊 L1 zkEVM 生态的 soundcalc/安全参数分析与形式化验证，或研究 ZK 在数字身份/年龄验证（longfellow-zk、EU 数字钱包）中的协议设计

---

## 25. 后Transformer架构：SSM/线性注意力/混合架构 — 55.0（D 暂缓）

*Post-Transformer Architectures: SSMs, Linear Attention & Hybrids* · AI-模型与方法 · `G3 S3 C3.5 E5 R4 H4 X3.5 P3` · 排名区间 23–26

**拐点事件**：2023-12 Mamba提出选择性SSM；真正的产业拐点为2025-09 Qwen3-Next与2026-02 Qwen3.5将Gated DeltaNet 3:1混合架构用于前沿规模开放模型全系（0.8B-397B），标志后Transformer混合架构进入主流生产。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3 | Mamba（2023-12）后已持续两年多高产出，2025-2026仍有Mamba-3（ICLR 2026 oral）、Kimi Delta Attention等，但增速已从爆发期回落，估计30-60%/年（未找到精确计数）。 |
| 阶段窗口 S | 3 | 已形成共识设计（约3:1线性注意力/全注意力混合，Gated DeltaNet为主流线性层），Qwen3-Next/Qwen3.5、Kimi Linear、Nemotron-H等生产级采用，属'已建立方向'而非起飞窗口。 |
| 能力拐点 C | 3.5 | Qwen3.5（2026-02）397B-A17B全系采用Gated DeltaNet混合，原生262K上下文；证明混合架构可在前沿规模不损质量地降低长上下文成本，但属效率提升而非质变能力。 |
| 使能条件 E | 5 | 开源内核（fla、mamba）、开放权重混合模型、学术可训练规模充足，几乎无瓶颈。 |
| 资源注入 R | 4 | 阿里Qwen、月之暗面、NVIDIA、AI21、MiniMax、Together/Cartesia等投入；多家大厂+创业公司。 |
| 学术空间 H | 4 | 状态追踪表达力理论、检索/复制能力缺陷、硬件感知内核、最佳混合比例等仍可用学术算力研究。 |
| 外溢平台性 X | 3.5 | 影响推理成本、长上下文智能体、端侧模型，以及基因组/时序等长序列科学任务。 |
| 风险扣分 P | 3 | 正被主流吸收为'工程默认选项'，独立研究空间被压缩；纯线性模型在检索类任务上的质量缺陷仍在。 |

**关键证据**：

- 2025-11 Qwen3-Next 采用Gated DeltaNet与Gated Attention 3:1混合，支撑原生262K上下文 [来源](https://magazine.sebastianraschka.com/p/beyond-standard-llms)
- 2025-10 Kimi Linear（2025-10）以通道级门控的Kimi Delta Attention改进Gated DeltaNet，提升长上下文推理 [来源](https://magazine.sebastianraschka.com/p/beyond-standard-llms)
- 2026-02 Qwen3.5（2026-02-16）全系8个模型（0.8B至397B-A17B）采用Gated DeltaNet混合+MoE，262K原生上下文 [来源](https://medium.com/@mlabonne/qwen3-5-nobody-agrees-on-attention-anymore-4709e1bd014b)
- 2026-03 Mamba-3（ICLR 2026 oral）：复数状态更新与MIMO，1.5B规模较Gated DeltaNet平均下游+1.8点，半数状态维度达到Mamba-2困惑度 [来源](https://arxiv.org/abs/2603.15569)
- 2025-04 NVIDIA Nemotron-H、AI21 Jamba 等Mamba-Transformer混合模型已开放（背景知识） （background knowledge）

**开放问题**：

- 固定大小状态的表达力极限：状态追踪、精确检索/复制任务上的理论与实证界限
- 最优混合比例与层放置的原则性方法，以及与MoE、稀疏注意力的联合设计
- 长上下文推理（RL长链思维）场景下线性层与全注意力的真实质量-成本权衡

**切入点**：

- 基于flash-linear-attention等开源内核，在≤1.5B规模做新的线性递归/delta规则变体与合成任务（MQAR、状态追踪）分析
- 研究混合模型在长链推理与智能体任务中的失效模式，提出可证明的表达力改进或蒸馏转换（Transformer→混合）方法

---

## 26. 全同态加密及其硬件加速 — 53.9（D 暂缓）

*Fully Homomorphic Encryption & Hardware Acceleration* · 量子/密码/网络/理论 · `G3 S4 C3.5 E3 R3.5 H4.5 X3 P6` · 排名区间 24–28

**拐点事件**：尚未出现明确的“GPT-3时刻”；最接近的是2026年2月 Intel Heracles 在 ISSCC 公布可工作的 FHE 加速芯片（千倍级加速）。若未来出现可交互速度（<1s/token）的完整加密 LLM 推理服务，则构成真正拐点。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3 | 未找到精确论文计数；定性看自 F1(2021)、CraterLake(2022) 后 ISCA/MICRO/HPCA 每年多篇 FHE 加速器论文，2024-2026 年 GPU-FHE 与加密 LLM 推理论文明显增多，估计30-60%/年。 |
| 阶段窗口 S | 4 | 体系结构界已有持续的 FHE 加速器研究线与 FHE.org 专门会议，但在顶会中占比仍小；CKKS vs TFHE、ASIC vs GPU vs 光子路线无共识，适合“起飞期”。 |
| 能力拐点 C | 3.5 | Intel Heracles（ISSCC 2026，Intel 3 工艺）对7种核心 FHE 运算较24核 Xeon 快1074-5547倍；GPU CKKS 自举从22.1ms(Cheddar)降至7.5-12.8ms；Llama3-8B 加密推理134s。进步显著但仍比明文慢数千倍，属“强存在性证明、缩放尚不明”。 |
| 使能条件 E | 3 | OpenFHE、Concrete、Lattigo 等开源库成熟，GPU 可用；但专用 ASIC 不可获得，硬件研究依赖仿真，构成一个主要瓶颈。 |
| 资源注入 R | 3.5 | DARPA DPRIVE（Intel、Duality、Niobium 等）；Zama 2025年成为首个 FHE 独角兽（累计>1.5亿美元）；Niobium 2300万美元、Optalysys 3100万美元；Apple 已在系统服务中使用同态加密（background knowledge）。 |
| 学术空间 H | 4.5 | 自举加速、非线性层近似、FHE 编译器与调度、算法-硬件协同设计均为学术小组可推进的根本性问题，不需巨额算力。 |
| 外溢平台性 X | 3 | 隐私计算、隐私 AI 推理、医疗/金融数据协作、区块链机密计算；影响若干相邻领域，但难成通用底座。 |
| 风险扣分 P | 6 | 相对明文开销仍达10³-10⁴倍、与 TEE/MPC 竞争、ASIC 商业化前景不确定、需求端尚未验证，扣6分。 |

**关键证据**：

- 2026-02 Intel Heracles FHE 加速器（Intel 3，197mm²，1.2GHz，176W，HBM）在7种核心 FHE 运算上较24核 Sapphire Rapids Xeon 快1074-5547倍 [来源](https://spectrum.ieee.org/fhe-intel)
- 2025-06 Zama 完成5700万美元 B 轮，累计融资>1.5亿美元，估值>10亿美元，成为首个 FHE 独角兽 [来源](https://www.theblock.co/post/359659/zama-raises-57m-in-series-b-to-bring-end-to-end-encryption-to-public-blockchains)
- 2025-12 Niobium 获2300万美元以上融资推进第二代 FHE 硬件；其 DARPA DPRIVE SoC 早期结果趋向较软件10,000倍加速 [来源](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/)
- 2026-02 Optalysys 获3100万美元 A 轮（含英国国家安全战略投资基金），用光子芯片加速 FHE [来源](https://www.optica-opn.org/home/industry/2026/february/optalysys_raises_us_$31_million_to_push_photonics_computing_toward_cloud_infrastructure/)
- 2025-12 多 GPU 加密大模型推理：BERT-Base 8秒、Llama3-8B 134秒；GPU CKKS 自举 Cheddar 22.1ms→Theodosian 12.8ms→<10ms [来源](https://www.alphaxiv.org/abs/2512.11269)
- 2021-03 DARPA DPRIVE 项目旨在设计 FHE 硬件加速器，使 FHE 计算速度接近明文 [来源](https://www.darpa.mil/program/data-protection-in-virtual-environments)

**开放问题**：

- 将自举与密钥切换开销再降1-2个数量级的算法-体系结构协同设计（内存带宽瓶颈、数据复用）
- Transformer 非线性层（Softmax/LayerNorm/GELU）的高精度低深度同态计算与方案混合（CKKS+TFHE）
- 自动化 FHE 编译器：参数选择、噪声管理、bootstrapping 放置与多后端（GPU/ASIC/光子）代码生成

**切入点**：

- 基于 OpenFHE/Phantom 等开源 GPU 库，针对加密 Transformer 推理做内核与调度优化，在 MLSys/HPCA/USENIX Security 发表
- 以周期级仿真器复现 F1/CraterLake/SHARP 等加速器，探索近存计算或 chiplet 化 FHE 架构，避开流片成本

---

## 27. 端侧/边缘大模型 — 53.4（D 暂缓）

*On-Device / Edge LLMs* · 系统与硬件 · `G4 S3 C3 E4 R5 H4 X3 P5` · 排名区间 24–28

**拐点事件**：2024 年 6 月 Apple Intelligence 发布、2025 年 6 月 WWDC 开放约 3B 端侧模型的 Foundation Models 框架，让端侧 LLM 成为操作系统级能力。真正的“GPT-3 时刻”是端侧模型达到 GPT-4 级通用能力，且 NPU 内存带宽足以流畅运行（预计 2027-2029 年）。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 端侧模型（MobileLLM、Gemma 3n、Qwen3 小模型）、框架（llama.cpp、ExecuTorch、MLC）和相关论文持续高速增长；小模型市场年复合增长约 36%（市场报告）。论文计数没有找到确切数字。 |
| 阶段窗口 S | 3 | 已在 MobiCom/MobiSys/MLSys 中形成稳定方向，量化、蒸馏、投机解码等共识方法已存在，且已进入 Apple/Google/Samsung 的产品，处于“既定方向”阶段。 |
| 能力拐点 C | 3 | 苹果约 3B 端侧模型（2-bit QAT、KV 共享省 37.5% 内存）随 Foundation Models 框架开放给开发者；但能力仍落后于 GPT-4o；手机 NPU 对解码的实际增益有限，2.7B 模型在骁龙 8 Elite 上约 21 tok/s。属于窄范围的胜利。 |
| 使能条件 E | 4 | 开源小模型和推理框架齐全；NPU 工具链碎片化、封闭，是主要短板。 |
| 资源注入 R | 5 | Apple、Google、Qualcomm、Samsung、Meta、MediaTek 均有大规模投入。 |
| 学术空间 H | 4 | 压缩、内存受限推理、端云协同、隐私等问题可在手机/笔记本上用学术资源研究。 |
| 外溢平台性 X | 3 | 影响移动系统、HCI 和隐私计算，外溢中等。 |
| 风险扣分 P | 5 | 产品体验不及预期（Apple Intelligence 落后于云端模型）、受内存与功耗的物理限制、可能被云端推理成本下降所替代，因此扣 5 分。 |

**关键证据**：

- 2025-07 WWDC 2025 发布 Foundation Models 框架，开发者可调用约 3B 参数的端侧模型（支持引导生成、工具调用） [来源](https://www.infoq.com/news/2025/07/apple-foundation-models-ios26)
- 2025-07 苹果端侧模型采用 KV 缓存共享（内存减少 37.5%）和 2-bit 量化感知训练 [来源](https://pr-mlr-shield-prod.apple.com/research/apple-foundation-models-tech-report-2025)
- 2025-07 苹果模型更新后仍落后于 OpenAI GPT-4o [来源](https://www.neowin.net/news/apples-ai-models-still-trail-behind-openais-gpt-4o-despite-latest-update/)
- 2026-05 移动端 LLM 分阶段分析：Prefill 阶段 CPU 甚至优于 NPU，NPU 在 Decode 阶段收益有限，调度开销和回退削弱了卸载收益 [来源](https://arxiv.org/pdf/2605.27435)
- 2026-07 2.7B 模型在骁龙 8 Elite 上用 ExecuTorch（CPU）达到 20.97 tok/s [来源](https://arxiv.org/pdf/2607.24585)
- 2025-01 小模型市场 2024-2029 年预计增长 246.8 亿美元，年复合增长率 36.1% [来源](https://www.technavio.com/report/small-language-model-slm-market-industry-analysis)

**开放问题**：

- NPU 上的高效 LLM 推理：解码阶段的带宽瓶颈、动态形状、异构 CPU/GPU/NPU 协同调度
- 端云协同推理与路由：何时在端侧、何时上云，同时兼顾隐私与延迟
- 极低比特（2-bit 及以下）量化与小模型能力上限，包括端侧个性化/持续学习

**切入点**：

- 基于 llama.cpp/ExecuTorch/MLC 在真实手机上做系统级测量与优化（如异构调度、内存换页），成本低、易复现
- 研究端侧的智能体/工具调用场景（结合 Apple Foundation Models 框架或 Gemma 3n），做端云混合推理策略

---

## 28. 推理时计算与可验证奖励强化学习 — 52.5（D 暂缓）

*Test-Time Compute & RL with Verifiable Rewards (RLVR)* · AI-模型与方法 · `G3.5 S1.5 C5 E5 R5 H3 X5 P5` · 排名区间 25–29

**拐点事件**：2024年9月OpenAI o1首次展示推理时计算scaling；2025年1月DeepSeek-R1开放权重并公开用纯RL（GRPO+可验证奖励）复现，引发全领域跟进——已发生且已主流化。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3.5 | 2025年爆发后基数已极大，ICLR 2026（19,809投稿）中'Reinforcement Learning'为第二高频关键词（796+404次），仍在增长但份额增速放缓。 |
| 阶段窗口 S | 1.5 | 已完全主流化：Raschka称'2025年LLM开发本质上被RLVR+GRPO主导'；是ICLR 2026头部关键词，所有前沿模型标配，早已过了'2021年LLM'的窗口。 |
| 能力拐点 C | 5 | o1（2024-09）与DeepSeek-R1（2025-01）是明确的'GPT-3时刻'：推理时计算成为新的scaling轴，并有清晰的训练/推理算力scaling曲线。 |
| 使能条件 E | 5 | 开放推理模型（R1、Qwen系列）、verl/OpenRLHF等框架、GRPO等简单算法、数学/代码验证器全部可用。 |
| 资源注入 R | 5 | 所有前沿实验室与大厂核心投入，资金远超$1B。 |
| 学术空间 H | 3 | RL是否真正扩展能力边界、非可验证领域的奖励、长程信用分配等仍开放，但前沿进展高度依赖工业级算力。 |
| 外溢平台性 X | 5 | 已外溢到代码、数学、智能体、科学推理等几乎所有LLM应用。 |
| 风险扣分 P | 5 | 已被主流LLM训练完全吸收（作为独立'新兴领域'的价值低），奖励作弊、评测污染与'RL仅锐化分布'争议。 |

**关键证据**：

- 2025-01 DeepSeek-R1 以开放权重达到与o1可比的推理性能，并公开RL训练配方 [来源](https://www.deeplearning.ai/the-batch/deepseek-r1-a-transparent-challenger-to-openai-o1)
- 2025-12 2025年LLM开发本质上由使用RLVR与GRPO的推理模型主导 [来源](https://magazine.sebastianraschka.com/p/state-of-llms-2025)
- 2026-01 ICLR 2026 共19,809投稿，'Reinforcement Learning'为第二高频关键词（796次，另小写404次），仅次于LLM [来源](https://papercopilot.com/venue-overview/iclr-2026-venue-overview/)
- 2024-09 OpenAI o1 展示随训练RL算力与推理时思考算力增加性能平滑提升（背景知识） （background knowledge）
- 2026-06 LLM相关arXiv论文从2021年91篇增至2025年33,569篇，占2025年arXiv约11.89%，RL子主题作为'次级浪潮'同步上升 [来源](https://arxiv.org/pdf/2606.12828)

**开放问题**：

- RLVR是扩展了模型能力边界还是仅锐化已有分布（pass@k争议），以及如何真正发现新策略
- 非可验证领域（开放式写作、科研、长程智能体任务）的可靠奖励信号与过程监督
- 推理效率：过度思考、自适应计算分配与长链推理的压缩

**切入点**：

- 在1.5-7B开放推理模型上用verl等框架做机理研究（探索、熵坍塌、数据选择），算力需求可控
- 转向奖励设计与评测：为非数学/代码领域构建可验证环境与rubric奖励，或研究奖励作弊检测

---

## 29. 大模型推理/服务系统 — 50.6（D 暂缓）

*LLM Serving Systems* · 系统与硬件 · `G4 S2 C4 E5 R5 H3 X3 P4` · 排名区间 28–29

**拐点事件**：2023 年 9 月 vLLM/PagedAttention（SOSP'23）让 LLM 服务吞吐提升数倍并迅速成为事实标准；2024 年 DistServe（OSDI'24）提出 PD 分离，到 2026 年已被全部主流框架采用。也就是说，这个领域的“GPT-3 时刻”已经过去。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 4 | 论文与开源仍在快速增长（vLLM 已部署在 40 万+ GPU 上；2026 年仍有大量 arXiv 服务类论文），但已从爆发期转入高基数增长期，估计年增长 60-100%。 |
| 阶段窗口 S | 2 | 已经主流化：2024 年系统类顶会 LLM 相关论文占比约 10%；PD 分离在 vLLM/SGLang/TensorRT-LLM/Dynamo 中均已产品化，已形成共识范式（PagedAttention、连续批处理、PD 分离、KV 缓存池）。 |
| 能力拐点 C | 4 | 拐点已发生在 2023 年（PagedAttention/vLLM 吞吐提升 2-24 倍），随后 DistServe（OSDI'24）和 Mooncake（FAST'25）带来 2-3 倍以上收益；SGLang 在 GB200 NVL72 上报告 2.7 倍解码吞吐。能力很强，但新增收益已经越来越渐进。 |
| 使能条件 E | 5 | 开源引擎（vLLM、SGLang）、开源权重模型、公开 trace 和云 GPU 都容易获得。 |
| 资源注入 R | 5 | NVIDIA Dynamo、各云厂商自研，加上 Inferact 获 1.5 亿美元种子轮（估值 8 亿美元）、RadixArk 估值 4 亿美元，资源非常充沛。 |
| 学术空间 H | 3 | 机架级（NVL72）、大规模 MoE 专家并行、多租户 SLO 等问题需要大量资本和集群，越来越由工业界主导；学术界只剩调度与建模类的切入空间。 |
| 外溢平台性 X | 3 | 主要影响 ML 系统、网络和存储（KV 缓存池），对整个 CS 的外溢有限。 |
| 风险扣分 P | 4 | 已商品化、同质化论文多、容易被框架厂商吸收，因此扣 4 分。 |

**关键证据**：

- 2026-06 2026 年 PD 分离已被 vLLM、SGLang、TensorRT-LLM 全面支持，NVIDIA Dynamo 于 2026 年 3 月 GA [来源](https://rdp.in/gpu-mart/knowledge-base/disaggregated-inference-prefill-decode-2026/)
- 2026-06 SGLang 在 GB200 NVL72 上，分离式解码吞吐是非分离基线的 2.7 倍；多 GPU vLLM 部署稳定获得 2-3 倍吞吐 [来源](https://rdp.in/gpu-mart/knowledge-base/disaggregated-inference-prefill-decode-2026/)
- 2026-01 vLLM 创始团队成立 Inferact，种子轮 1.5 亿美元、估值 8 亿美元；vLLM 运行在 40 万+ GPU 上 [来源](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/)
- 2026-01 SGLang 商业化实体 RadixArk 估值 4 亿美元，由 Accel 领投 [来源](https://diyhaven858.wasmer.app/?p=6419)
- 2025-04 系统领域（OSDI 等）的 LLM 论文占比到 2024 年升至约 10% [来源](https://arxiv.org/pdf/2504.08619)
- 2024-07 DistServe（OSDI'24）与 Mooncake（FAST'25）奠定了 PD 分离和 KV 缓存中心架构 [来源](https://usenix.org/biblio-14637)

**开放问题**：

- 超长上下文与智能体多轮会话下的 KV 缓存分层存储、迁移与淘汰策略（GPU-CPU-SSD-远端池）
- 大规模 MoE 专家并行推理中的负载均衡、通信重叠和容错
- 多 SLO、多租户、多模型混部下的成本与能耗最优调度，以及可验证的性能建模

**切入点**：

- 基于 vLLM/SGLang 开源代码和公开 trace（如 Azure LLM trace、Mooncake trace），研究面向智能体/推理模型负载的调度与 KV 复用策略
- 做轻量级性能建模/模拟器（不需要大集群），对 PD 分离、专家并行等配置做自动调优

---

## 30. 低轨卫星互联网与空天地一体化网络 — 48.0（D 暂缓）

*LEO Satellite Networking & Space-Air-Ground Integrated Networks* · 量子/密码/网络/理论 · `G3 S3.5 C3.5 E2.5 R5 H3 X2.5 P6` · 排名区间 30–30

**拐点事件**：2020-2022年 Starlink 规模化商用为部署拐点；2025年9月 SpaceX 收购 EchoStar 频谱（约170亿美元）及直连手机商用，标志卫星直接融入蜂窝网络的“第二拐点”，下一代直连手机卫星测试计划于2026年底开始。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3 | 未找到精确论文计数；LEO-NET 研讨会自2023年起已办到第4届（SIGCOMM 2026），Starlink 测量论文与仿真器（Hypatia、StarryNet 等）持续增长，估计30-60%/年。 |
| 阶段窗口 S | 3.5 | 已有专门研讨会和 SIGCOMM/NSDI/MobiCom 会议场次，但路由、拥塞控制、星间链路等无共识方案；对 CS 网络界而言处于起飞到建立之间。 |
| 能力拐点 C | 3.5 | Starlink 在轨超1万颗（2026-04）、用户超800万，直连手机（direct-to-cell）商用化，属部署层面的质变；但网络算法层面的“新能力”较少，多为工程规模化。 |
| 使能条件 E | 2.5 | 卫星系统封闭、内部数据不可得，学界只能靠用户终端测量与仿真；这是主要瓶颈。 |
| 资源注入 R | 5 | SpaceX 以约170-200亿美元收购 EchoStar 频谱用于直连手机；Amazon Leo（Kuiper）规模部署；中国千帆、国网星座国家级投入；3GPP NTN 标准化。 |
| 学术空间 H | 3 | 开放问题多（星间路由、移动性管理、TCP 适配、空间计算），但数据与实验设施被企业垄断，学术空间受限。 |
| 外溢平台性 X | 2.5 | 影响移动通信、边缘计算与遥感，但对整个 CS 外溢有限。 |
| 风险扣分 P | 6 | 单一主体依赖（SpaceX 占绝对主导）、频谱/监管与空间碎片等物理限制、学术难以获得系统访问，扣6分。 |

**关键证据**：

- 2025-09 SpaceX 与 EchoStar 达成约170亿美元（后增至约200亿美元）AWS-4/H-block 频谱交易，用于 Starlink Direct to Cell [来源](https://techcrunch.com/2025/09/08/spacex-strikes-17b-deal-to-buy-echostars-spectrum-for-starlinks-direct-to-phone-service/)
- 2026-04 Starlink 截至2026年4月在轨超10,300颗卫星，获批约15,000颗；Amazon Leo 已发射239颗（计划3,236颗）；国网星座近200颗、千帆超100颗 [来源](https://datatracker.ietf.org/meeting/126/materials/slides-126-space-york-beyond-starlink-understanding-the-coming-waves-of-leo-satellite-deployments-00)
- 2025-11 SpaceX 全球用户超过800万 （background knowledge（检索摘要提及，原始出处未核实））
- 2026-08 第4届 LEO-NET 研讨会在 SIGCOMM 2026 举办，主题含星座设计、LEO 路由、传输与拥塞控制、直连终端与多轨道协同 [来源](https://conferences.sigcomm.org/sigcomm/2026/workshops/leo-net/)
- 2023-06 迄今最大规模 Starlink 延迟研究覆盖13个国家2,400多名用户 [来源](https://arxiv.org/pdf/2306.07469)
- 2025-10 3GPP Rel-17 引入 NTN，Rel-18 增强，支撑大众市场手机直连卫星 （background knowledge）

**开放问题**：

- 大规模动态拓扑下的星间路由、流量工程与跨星座/跨地面网络的统一控制面
- 直连手机（D2D/NTN）场景下的链路预算受限传输、移动性与切换管理
- 在轨计算（space edge computing）与卫星网络的安全、韧性和可测量性

**切入点**：

- 利用 Starlink 用户终端与公开工具（如 LEOScope、Hypatia、StarryNet）开展测量和仿真研究，投稿 LEO-NET/IMC
- 与运营商或3GPP NTN 产业链合作研究直连手机的传输协议与切换算法，或基于开源 5G 栈（OpenAirInterface NTN 分支）做原型

---

## 31. 存内/近存计算 — 44.6（D 暂缓）

*Processing-in-Memory / Compute-in-Memory* · 系统与硬件 · `G3 S3 C3 E2.5 R3.5 H4 X3 P5` · 排名区间 31–32

**拐点事件**：尚无明确的“GPT-3 时刻”。可能的拐点是 PIM 进入 HBM4/LPDDR6 标准、并在主流 LLM 推理服务器中商用（例如某云厂商用 PIM 服务 LLM 解码），预计不早于 2027 年；d-Matrix Corsair 2025 年量产、2025 年 11 月获 20 亿美元估值，是数字存内计算的早期信号。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3 | LLM 解码的内存墙让 PIM 再度升温（AttAcc、NeuPIMs、IANUS、PAPI、LoL-PIM、HPIM 等），但 PIM/CIM 本身已有十多年历史，增长估计 30-60%/年（未找到确切计数）。 |
| 阶段窗口 S | 3 | 在 ISCA/HPCA/MICRO/ISSCC 已有稳定的分会场；“NPU/GPU 做 GEMM + PIM 做 GEMV/注意力”的异构方案已成为共识。 |
| 能力拐点 C | 3 | 多篇论文报告解码阶段数倍加速和能效提升，但大多基于模拟器；SK hynix GDDR6-AiM 展示了 LLM 演示（声称 16 倍加速、数据搬运功耗降低 80%），尚未进入主流部署。 |
| 使能条件 E | 2.5 | 缺乏可广泛获取的商用 PIM 硬件（UPMEM 除外），主要依赖模拟器；模拟 CIM 需要流片。 |
| 资源注入 R | 3.5 | Samsung、SK hynix 在投入；d-Matrix C 轮 2.75 亿美元、估值 20 亿美元，EnCharge 累计 1.44 亿美元，但还没有到多巨头加数十亿美元的规模。 |
| 学术空间 H | 4 | 映射、编译、编程模型和噪声鲁棒性等问题可以用模拟器在学术资源下研究。 |
| 外溢平台性 X | 3 | 主要影响体系结构和内存系统，对 ML 系统有一定外溢。 |
| 风险扣分 P | 5 | 十余年“即将商用”的落差，模拟 CIM 存在噪声/精度问题，依赖存储厂商和 JEDEC 标准化，可能被 HBM 带宽升级吸收，因此扣 5 分。 |

**关键证据**：

- 2025-11 d-Matrix（数字存内计算 DIMC）2025 年 11 月完成 2.75 亿美元 C 轮，估值 20 亿美元，累计融资 4.5 亿美元 [来源](https://news.bgov.com/private-equity/microsoft-backed-d-matrix-hits-2-billion-value-as-qatar-invests)
- 2025-02 EnCharge AI（普林斯顿衍生，模拟存内计算）获超 1 亿美元 B 轮，累计 1.44 亿美元，声称能效比数字方案高 20 倍 [来源](https://datacenterdynamics.com/en/news/encharge-ai-closes-oversubscribed-100m-series-b-funding-round-for-development-of-analog-in-memory-chips)
- 2026-08 PIM 加速 LLM 推理的主要工作包括 NeuPIMs、IANUS、AttAcc、PAPI；业界共识是 NPU/GPU 做 GEMM、PIM 做访存受限的注意力 [来源](https://arxiv.org/pdf/2608.28048)
- 2025-09 HPIM 将 FC 层放到 HBM 近 bank PIM，注意力放到 SRAM-PIM，以缓解解码阶段的带宽瓶颈 [来源](https://arxiv.org/pdf/2509.12993)
- 2022-02 SK hynix GDDR6-AiM 针对特定计算声称 16 倍加速、数据搬运功耗降低 80%，已演示 LLM 应用 [来源](https://hothardware.com/news/sk-hynix-ai-accelerating-pim-memory)

**开放问题**：

- PIM 的编程模型与编译栈：如何在 vLLM 这类服务系统中透明地把 GEMV/注意力卸载到 PIM
- 模拟 CIM 的噪声、漂移与低比特精度下的 LLM 精度保持（训练感知与校准）
- 长上下文 KV 缓存在 PIM 上的布局、稀疏注意力映射以及与 GPU 的负载划分

**切入点**：

- 基于开源 PIM 模拟器（Ramulator-PIM、AttAcc 模拟器等）或 UPMEM 真机，做 LLM 解码/注意力卸载的软硬件协同研究
- 研究面向 CIM 的噪声鲁棒量化与训练方法，只需 GPU 仿真即可产出成果

---

## 32. 后量子密码迁移工程 — 42.9（D 暂缓）

*Post-Quantum Cryptography Migration Engineering* · 量子/密码/网络/理论 · `G3.5 S2.5 C2 E5 R5 H2.5 X2.5 P4` · 排名区间 31–32

**拐点事件**：2024年8月 NIST 发布 FIPS 203/204/205 正式标准，叠加2025年5月 Gidney 将 RSA-2048 破解资源降至<100万比特、2026年 Google/Caltech 等论文继续压缩 ECC 破解资源，使迁移从“规划”变为“截止日期驱动”的工程。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 3.5 | 部署侧增长迅猛：Cloudflare 观测到人类浏览器 TLS 流量中混合 ML-KEM 占比 >60%（2024初为个位数，background knowledge）；研究论文增长无精确数据，侧信道/迁移类论文持续增加，估计30-60%/年。 |
| 阶段窗口 S | 2.5 | FIPS 203/204/205 已于2024-08定稿，X25519MLKEM768 混合方案成为事实共识，迁移已进入主流工程阶段而非起飞期。 |
| 能力拐点 C | 2 | 本身不产生新能力，而是替换；能力拐点在于标准定稿与大规模部署可行（2024-2025），属增量型。 |
| 使能条件 E | 5 | 标准、开源实现（liboqs、OpenSSL 3.5、BoringSSL）、浏览器与 CDN 支持全部可得。 |
| 资源注入 R | 5 | 美国 OMB 估算联邦迁移成本约71亿美元（2025-2035）；NSA CNSA 2.0 要求2027年起新采购合规；欧盟路线图要求2030年前关键基础设施完成；全部大型科技公司参与。 |
| 学术空间 H | 2.5 | 侧信道/故障攻击（KyberSlash 后续功耗攻击30秒恢复密钥）、密码敏捷性、PQ 签名尺寸对协议的影响、迁移自动化工具仍有学术空间，但多为工程问题。 |
| 外溢平台性 X | 2.5 | 触及所有安全通信系统，但作为“替换件”外溢有限，不会开辟新研究范式。 |
| 风险扣分 P | 4 | 研究新颖性有限、量子威胁时间线不确定（但2025-2026资源估计骤降反而增强紧迫性）、格密码潜在密码分析风险；整体风险低，扣4分。 |

**关键证据**：

- 2026-03 Cloudflare：超过60%（另一口径约70%）的人类/浏览器 TLS 流量已使用混合 X25519MLKEM768；但仅约15%的源站支持；目标2029年全面后量子安全 [来源](https://blog.cloudflare.com/post-quantum-visibility/)
- 2025-03 NIST 于2025-03-11选定 HQC 作为基于编码的第五个 PQC 标准算法；IR 8547 规定 RSA/ECDSA 2030年弃用、2035年禁用 [来源](https://utimaco.com/news/blog-posts/pqc-news-nist-announces-hqc-fifth-algorithm-be-standardized)
- 2024-08 OMB 报告估算联邦政府优先系统 PQC 迁移成本约71亿美元（2025-2035） [来源](https://thequantuminsider.com/2024/08/12/white-house-report-u-s-federal-agencies-brace-for-7-1-billion-post-quantum-cryptography-migration)
- 2025-06 欧盟协调路线图：2026年底前各成员国启动，2030年前高风险系统完成，2035年尽可能全面完成 [来源](https://pqshield.com/eu-pqc-workstream-publishes-a-coordinated-implementation-roadmap-for-the-transition-to-post-quantum-cryptography/)
- 2025-01 KyberSlash 时序漏洞影响包括参考实现在内的多个 ML-KEM 实现；后续功耗分析在打补丁实现上30秒恢复密钥 [来源](https://tches.iacr.org/index.php/TCHES/article/view/12046)
- 2026-03 2026年3-6月多篇论文（Google 关于 secp256k1 的资源估计、Caltech/Oratomic 约1万原子比特运行 Shor）将破解所需资源再降一个数量级 [来源](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/)

**开放问题**：

- 大规模、异构系统中的自动化密码资产发现（cryptographic inventory）与可验证的密码敏捷性架构
- ML-KEM/ML-DSA/FN-DSA 在嵌入式与硬件上的低成本侧信道与故障防护、形式化验证的常数时间实现
- 大尺寸 PQ 签名/证书对 TLS、DNSSEC、物联网及区块链协议性能的影响与协议重设计（如 KEMTLS、Merkle Tree Certificates）

**切入点**：

- 利用 liboqs/OpenSSL 3.5 搭建测量平台，做互联网规模 PQC 部署测量或协议性能评估（IMC/NDSS 类工作）
- 在 Cortex-M4/FPGA 上对 ML-KEM/ML-DSA 实现做侧信道与故障攻击/防护研究（CHES/TCHES）

---

## 33. 3D/4D高斯泼溅与神经渲染 — 33.4（D 暂缓）

*3D/4D Gaussian Splatting and Neural Rendering* · 具身/空间/生命科学交叉 · `G2 S1.5 C3 E5 R3.5 H2.5 X3 P5` · 排名区间 33–33

**拐点事件**：拐点已于2023-08（SIGGRAPH 2023 3D Gaussian Splatting）发生，实时辐射场渲染；2026年glTF/OpenUSD标准化标志着从研究热点走向商品化，当前不再处于“2021年LLM”阶段。

| 维度 | 分 | 理由 |
|---|---|---|
| 增长动量 G | 2 | RadianceFields.com收录3333篇辐射场论文，2026年至今至少749篇（约每天4篇），总量高但未找到加速证据；按定性判断增速已放缓至约10-30%/年。 |
| 阶段窗口 S | 1.5 | 3DGS已是CVPR 2025头部研究主题之一；Khronos 2026-02发布glTF高斯泼溅扩展RC、OpenUSD 26.03原生支持3DGS，进入标准化/商品化阶段，已过峰值。 |
| 能力拐点 C | 3 | 2023年3DGS实现实时高质量辐射场渲染是真实拐点，但当前4DGS、前馈GS等多为增量改进，没有新的质变能力。 |
| 使能条件 E | 5 | 开源实现（gsplat、nerfstudio等）、数据集、消费级GPU、行业标准格式全部可得。 |
| 资源注入 R | 3.5 | NVIDIA、Niantic、Autodesk、Apple/Meta等产品化投入，Cesium、Babylon.js、PlayCanvas已支持；但缺乏前沿实验室把它作为核心战略。 |
| 学术空间 H | 2.5 | 论文高度拥挤、问题多为工程化；剩余开放问题（动态、可编辑性、压缩）正被前馈3D模型与视频世界模型分流。 |
| 外溢平台性 X | 3 | 影响图形学、AR/VR、数字孪生、机器人仿真等若干相邻领域。 |
| 风险扣分 P | 5 | 已过峰值、增量论文泛滥；可能被前馈3D基础模型与视频生成/世界模型替代或吸收。扣5分。 |

**关键证据**：

- 2026-09 RadianceFields.com收录3333篇辐射场研究论文，其中2026年至少749篇，约每天4篇 [来源](https://radiancefields.com/gaussian-splatting-statistics)
- 2025-06 3DGS是CVPR 2025头部研究主题之一 [来源](https://www.paperdigest.org/report/data/cvpr-2025-topics.html)
- 2026-02 Khronos 2026-02-03发布KHR_gaussian_splatting glTF扩展候选版，目标2026Q2正式批准；Cesium、Babylon.js、PlayCanvas已支持 [来源](https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release)
- 2026-03 OpenUSD 26.03加入原生3D高斯泼溅schema与参考渲染器 [来源](https://www.cgchannel.com/tag/usd-26-03)
- 2025-10 原作者Kerbl发表《The Impact and Outlook of 3D Gaussian Splatting》回顾性综述，标志领域进入总结期 [来源](https://arxiv.org/pdf/2510.26694)

**开放问题**：

- 前馈式、可泛化的4D高斯表示，与VGGT类几何基础模型的统一
- 可编辑、可物理仿真的高斯场景，用于机器人仿真与数字孪生
- 大规模场景的流式压缩、LOD与跨平台实时渲染标准化

**切入点**：

- 将3DGS作为工具而非研究对象：用于机器人real2sim数据生成或具身仿真场景构建
- 研究前馈GS与3D基础模型/视频生成模型的结合，避开拥挤的逐场景优化增量改进赛道

---
