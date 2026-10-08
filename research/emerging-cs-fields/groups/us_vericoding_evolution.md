# 美国学术界课题组清单：Vericoding / LLM 形式化验证 & 自我改进 / LLM 引导的进化搜索

> 编制日期：2026-10-08｜面向：有 ML/NLP 背景、计划申请美国 CS PhD（Fall 2027 申请季）的同学
> 方法：约 31 次 WebSearch（standard / extended）。WebFetch 对 arxiv 等域名被拦截，无法逐页打开主页核对；本轮搜索配额已用完，部分候选人未能核实，列在文末"未核实候选"中，**不在正表里**。
> 收录规则：只有当检索到 2024–2026 年的来源，能同时证明 (a) 目前在美国高校任教、(b) 确实在做该方向时才收录。职称或入职年份没有直接来源的，标"待核实"。论文标题都取自检索结果；无法确认的标"(待核实)"。
> 招生信号：除非来源明确写了 Fall 2026/2027 招生，一律写"未知"。**本轮没有找到任何一位 PI 的官方招生声明。**

图例：**青年教师** = 2022–2026 年入职的 Assistant Professor，且有来源支持入职时间。适配度指与 ML/NLP 背景的匹配程度。

---

## 一、LLM 驱动的形式化验证 / 可验证代码生成（Vericoding）& LLM 形式化定理证明

| 姓名（英文） | 学校 / 院系 | 职称 | 相关方向关键词 | 1–2 项 2024–2026 代表工作 | 主页 / 来源 URL | 招生信号 | 适配度 |
|---|---|---|---|---|---|---|---|
| Sean Welleck | Carnegie Mellon University / Language Technologies Institute (LTI) | Assistant Professor，**青年教师**（2024 年加入 CMU LTI） | Lean 定理证明、LLM 推理/inference-time 算法、可验证代码生成、AI for math | AlphaVerus: Bootstrapping Formally Verified Code Generation through Self-Improving Translation and Treefinement（ICML 2025，与 Bryan Parno 合作）；LeanHammer（与 Avigad 合作的 Lean 自动推理工具，论文标题待核实） | https://lti.cmu.edu/people/faculty/welleck-sean.html ；https://www.cmu.edu/hoskinson/people/sean-welleck.html ；https://proceedings.mlr.press/v267/aggarwal25a.html | 未知（只有一个第三方聚合页 researchersjob.com 提到他，不是官方来源） | **高**：院系属于 NLP（LTI），研究本身就是 LLM 推理 + Lean，NLP 背景可以直接对接 |
| Bryan Parno | Carnegie Mellon University / CSD & ECE | 教授（具体职级待核实） | Verus/Rust 验证、可验证代码生成、系统安全 | AlphaVerus（ICML 2025，合作者 Aggarwal、Welleck） | https://proceedings.mlr.press/v267/aggarwal25a.html ；https://www.alphaxiv.org/@bryan-parno | 未知 | **中**：主线是形式化方法/安全，需要一定 PL 基础；可以考虑和 Welleck 联合指导 |
| Jeremy Avigad | Carnegie Mellon University / Philosophy（兼 Math，Hoskinson Center） | Professor | Lean、形式化数学、神经+符号的 premise selection | 与 Welleck 联合指导 LeanHammer（神经 premise selector + 符号自动化，标题待核实）；参与 NSF ICARM 研究所 | https://www.siebelscholars.com/scholar-profile/3886/ ；https://www.cmu.edu/dietrich/ai/news/ai-mathematics-carnegie-mellon.html | 未知 | **低–中**：院系是哲学/数学，CS PhD 一般需要和 CS 教员联合指导 |
| Talia Ringer | University of Illinois Urbana-Champaign / Siebel School of Computing | 教员（职称待核实；2021 年 UW 博士毕业后入职） | 证明自动化、LLM for Rocq/Lean/Agda、proof repair | QEDCartographer: Automating Formal Verification Using Reward-Free Reinforcement Learning（ICSE 2025）；Cobblestone: A Divide-and-Conquer Approach for Automating Formal Verification（ICSE 2026） | https://conf.researchr.org/profile/talialilyringer ；https://siebelschool.illinois.edu/academics/graduate/phd-program/amazon-ai-phd-fellows/Kevin-Fisher | 未知 | **中**：组里专门做"让 LLM 用好证明助手"，但大本营在 PL/FM/SE |
| Emily First | Rutgers University–New Brunswick / Computer Science | Assistant Professor，**青年教师**（2025 年 3 月做 Rutgers 求职报告，应为 2025 年入职，具体入职日期待核实） | AI for 定理证明、LLM 证明合成、Coq/Rocq | Cobblestone（ICSE 2026）；Rango: Adaptive Retrieval-Augmented Proving for Automated Software Verification（ICSE 2025，获奖论文）；另有一篇 ACL 2024 论文（用 trial-and-error 数据微调 LLM 做直觉主义命题逻辑证明，标题待核实） | https://conf.researchr.org/profile/icse-2027/emilyfirst1 ；https://www.cs.rutgers.edu/events/icalrepeat.detail/2025/03/11/4818/-/machine-learning-for-formal-software-verification ；https://people.cs.umass.edu/~efirst | 未知（新组，大概率在招，但没有来源） | **中–高**：有 ACL 论文，对 NLP 背景友好；属于非 top-4、新建组，比较容易接触到导师 |
| Yuriy Brun | University of Massachusetts Amherst / CICS | Professor | 基于 LLM 的证明合成、软件验证、SE | Rango（ICSE 2025）；Cobblestone（ICSE 2026，合作） | https://people.cs.umass.edu/~brun ；https://conf.researchr.org/details/icse-2025/icse-2025-research-track/88/Rango-Adaptive-Retrieval-Augmented-Proving-for-Automated-Software-Verification | 未知 | **中**：属于 SE 组，做 LLM 证明合成方向成熟，需要愿意学 Coq |
| Swarat Chaudhuri | UT Austin / Computer Science | Professor（**目前在 Google DeepMind 伦敦休假**） | LLM 定理证明 agent、可验证代码生成基准、形式化数学推理 | CLEVER: A Curated Benchmark for Formally Verified Code Generation（NeurIPS 2025 D&B）；PutnamBench（NeurIPS 2024） | https://www.cs.utexas.edu/~swarat ；https://proceedings.neurips.cc/paper_files/paper/2025/hash/a7f67788f7b4d77fa7cd6887de3dcbe7-Abstract-Datasets_and_Benchmarks_Track.html | 未知（**休假中，能否招生需当面确认**） | **中**：方向非常对口，但他人在 DeepMind，带学生的情况不确定 |
| Chi Jin | Princeton University / ECE（PLI） | Assistant Professor（2025 年普林斯顿新闻稿） | 开源 Lean 证明器、数据合成、verifier 反馈的自我纠错 | Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction（ICLR 2026，通讯/资深作者） | https://ai.princeton.edu/news/2025/princeton-researchers-unveil-improved-mathematical-theorem-prover-powered-ai ；https://iclr.cc/virtual/2026/poster/10007912 | 未知 | **高**：纯 ML/LLM 训练路线，不需要 PL 背景；另有 Goedel-Code-Prover（arXiv 2603.19329，作者归属待核实） |
| Sanjeev Arora | Princeton University / Computer Science（PLI） | Professor | LLM 定理证明、合成数据、推理 | Goedel-Prover-V2（ICLR 2026，合作者） | https://iclr.cc/virtual/2026/poster/10007912 ；https://dais.princeton.edu/news/2025/princeton-researchers-unveil-improved-mathematical-theorem-prover-powered-ai | 未知 | **高**：属于 ML 理论 + LLM 组，NLP/ML 背景直接适配；竞争极其激烈 |
| Danqi Chen | Princeton University / Computer Science（PLI） | 教授（职级待核实） | NLP、LLM 训练；参与形式化定理证明 | Goedel-Prover-V2（ICLR 2026，合作者） | https://iclr.cc/virtual/2026/poster/10007912 | 未知 | **高**：NLP 大组，形式化证明只是她的支线之一，套磁时要说明自己为什么想做定理证明 |
| Anima Anandkumar | Caltech / Computing + Mathematical Sciences | Professor | LeanDojo 系列、终身学习定理证明、AI for math | LeanAgent: Lifelong Learning for Formal Theorem Proving（ICLR 2025） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/b67c77f8db8b991d73d6f2e16f491840-Abstract-Conference.html | 未知 | **中**：ML 组，Lean 只是方向之一；组的规模和导师投入时间请自行了解 |
| Tengyu Ma | Stanford University / CS & Statistics | Assistant Professor（**单位待核实**：同时担任 MongoDB Chief AI Scientist，是否休假不明） | 自博弈定理证明、conjecturing、RL for LLM | STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving（ICML 2025） | https://proceedings.mlr.press/v267/dong25h.html ；https://ai.stanford.edu/~tengyuma | 未知 | **中**：方向高度匹配（同时属于主题二），但工业界任职使带学生情况不明 |
| Nada Amin | Harvard University / SEAS | 职称来源不一致（Assistant / Associate，待核实） | Dafny、LLM + 验证器的树搜索、可验证程序合成 | VerMCTS: Synthesizing Multi-Step Programs using a Verifier, a Large Language Model, and Tree Search（POPL 2025 Dafny Workshop）；dafny-annotator: AI-Assisted Verification of Dafny Programs（POPL 2025 Dafny Workshop）；DafnyBench（合作） | https://popl25.sigplan.org/details/dafny-2025-papers/12/VerMCTS-Synthesizing-Multi-Step-Programs-using-a-Verifier-a-Large-Language-Model-a ；https://www.alphaxiv.org/@nada-amin | 未知（有 PL+AI 博后招聘广告，目标是"最强的可验证程序合成系统"，不代表 PhD 招生） | **中**：PL+AI 交叉，组的目标正好是 vericoding；需要补 Dafny/PL 基础 |
| Max Tegmark | MIT / Physics（IAIFI） | Professor | Vericoding 概念与基准（Dafny / Verus / Lean） | A benchmark for vericoding: formally verified program synthesis（arXiv 2509.22908；POPL 2026 Dafny Workshop） | https://arxiv.org/abs/2509.22908v1 ；https://popl26.sigplan.org/details/dafny-2026-papers/13/A-benchmark-for-vericoding-formally-verified-program-synthesis | 未知 | **低–中**：Vericoding 这个词就出自他和 Beneficial AI Foundation 的工作，但他在物理系，CS PhD 走常规渠道难以直接投到他门下 |
| Clark Barrett | Stanford University / CS（Centaur 中心） | Professor（Research 序列，待核实） | SMT、Lean-SMT、AI 辅助验证平台、LLM + 自动推理 | Lean-SMT（CAV 2025，合作者）；CSLib: Building a Platform for AI-assisted Formal Verification in Lean（2026）；早期有 Clover（SAIV 2024）、Lemur（ICLR 2024） | https://centaur.stanford.edu/news.html ；https://sos-vo.org/node/109653 ；https://theory.stanford.edu/~barrett/pubs/WCB24-abstract.html | 未知 | **低–中**：主线是 SMT/形式化方法，适合愿意转向 FM 的同学 |
| Alex Aiken | Stanford University / CS | Professor | LLM 不变式合成、程序验证加速 | Quokka: Accelerating Program Verification with LLMs via Invariant Synthesis（arXiv 2509.21629，v3 2026-04） | https://arxiv.org/html/2509.21629v3 | 未知 | **低–中**：以 PL/编译为主，LLM 工作似乎主要由学生 Anjiang Wei 推动 |
| Dawn Song | UC Berkeley / EECS | Professor | 可验证代码生成基准（Lean）、AI for math、AI 安全 | VERINA: Benchmarking Verifiable Code Generation（ICLR 2026；ICML 2025 workshop 版） | https://iclr.cc/virtual/2026/poster/10011965 （代码托管在 sunblaze-ucb 命名空间下；"由 Berkeley Sunblaze 组完成"是根据托管位置推断的） | 未知 | **中–高**：大组、资源多，偏 ML/安全；组很大，每个学生分到的导师时间可能有限 |
| Alvin Cheung | UC Berkeley / EECS | 教授（职级待核实） | 可验证提升（verified lifting）、LLM 生成等价性证明、DSL 转译 | Verified Code Transpilation with LLMs（LLMLift，NeurIPS 2024，与 Sanjit Seshia 合作） | https://slice.eecs.berkeley.edu/?p=1141 ；https://people.eecs.berkeley.edu/~sseshia/pubs/b2hd-bhatia-neurips24.html | 未知 | **中**：PL/DB 组；本轮没有检索到 2025 年后的后续工作，请自行核实 |
| Nadia Polikarpova | UC San Diego / CSE | 教授（职级待核实） | LLM + Dafny 断言生成、程序合成 | Laurel: Unblocking Automated Verification with Large Language Models（POPL 2025 Dafny Workshop 报告） | https://popl25.sigplan.org/details/dafny-2025-papers/7/dafny-annotator-AI-Assisted-Verification-of-Dafny-Programs （同一 workshop 的论文列表）；Laurel 作者信息来自 POPL 2025 Dafny Workshop 页面 | 未知 | **中**：属于 PL + HCI + LLM 方向，对动手能力强的 NLP 学生也友好 |
| Ranjit Jhala | UC San Diego / CSE | Professor | 精化类型、LLM 辅助验证 | Laurel（同上，合作者） | 同上 | 未知 | **低–中**：偏纯 PL |
| Vijay Ganesh | Georgia Tech / School of Computer Science | Professor | 自动形式化（autoformalization）、LLM + SAT/SMT/CAS、AI for math | 2026-01 佐治亚理工数学系报告"Auto-formalization via Joint Embeddings"（对应论文标题待核实）；2025-05 报告"Bridging Learning and Reasoning: From Solvers to LLMs" | https://www.cc.gatech.edu/people/vijay-ganesh ；https://math.gatech.edu/seminars-colloquia/series/school-mathematics-colloquium/vijay-ganesh-20260129 | 未知 | **中**：属于非 top-4，autoformalization 部分 NLP 友好，求解器部分需要补课 |

**说明**
- **Haoze Wu（Amherst College）**：Lemur（ICLR 2024）的一作，在 Quokka v3（2026-04）中署名 Amherst College。Amherst College 是**文理学院，不授予 PhD**，所以不放进正表；可作为本科/硕士阶段的科研合作者，或作为推荐人来源。
- **Sanjit Seshia（Berkeley）**是 LLMLift 的合作者，本轮没有单独核实他的 LLM + 验证工作，未收录。
- **Armando Solar-Lezama（MIT）、Loris D'Antoni（UCSD）、Kexin Pei（UChicago）、Saikat Dutta（Cornell）、Lin Tan（Purdue）**：本轮检索**没有找到** 2024–2026 年他们在本方向的直接证据，所以不收录。这不代表他们没在做，请自行在 DBLP 上查。

---

## 二、自我改进 & LLM 引导的进化搜索（FunSearch/AlphaEvolve 式程序搜索、开放式学习、自博弈/自奖励/自进化、自动化科研）

| 姓名（英文） | 学校 / 院系 | 职称 | 相关方向关键词 | 1–2 项 2024–2026 代表工作 | 主页 / 来源 URL | 招生信号 | 适配度 |
|---|---|---|---|---|---|---|---|
| Omar Khattab | MIT / EECS（CSAIL） | Assistant Professor，**青年教师**（2025 年秋入职） | 反思式 prompt 进化、DSPy、LLM 程序优化 | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning（arXiv 2507.19457，2025；其个人简介列出 GEPA，完整作者顺序待核实） | https://www.eecs.mit.edu/people/omar-khattab/ ；https://www.csail.mit.edu/person/omar-khattab | 未知（新组，没有找到明确来源） | **高**：NLP 出身（ColBERT/DSPy），GEPA 正是"LLM 引导的进化搜索"，对 NLP 背景最友好 |
| Ion Stoica | UC Berkeley / EECS（Sky Lab） | Professor | AI 驱动的系统研究（ADRS）、OpenEvolve/AlphaEvolve 式算法发现 | Barbarians at the Gate: How AI is Upending Systems Research（arXiv 2510.06189，2025）；后续博文 "Let the Barbarians In"（2025-12，比较 OpenEvolve / GEPA / ShinkaEvolve） | https://arxiv.org/pdf/2510.06189 ；https://www.sigops.org/2026/let-the-barbarians-in-how-ai-can-accelerate-systems-performance-research/ | 未知 | **中**：系统组，申请时要能讲系统问题；"进化搜索 + 自动评估器"这条线很新 |
| Jiaxin Huang | Washington University in St. Louis / CSE | 教员（职称和入职年份待核实；据既有了解为 2024 年入职的 Assistant Professor，可能属于**青年教师**） | 自进化推理 LLM、Challenger–Solver 自博弈、无数据自我改进 | R-Zero: Self-Evolving Reasoning LLM from Zero Data（ICLR 2026，与腾讯 AI Lab Seattle 合作） | https://proceedings.iclr.cc/paper_files/paper/2026/hash/d49b9aacebda61051166335af6fd3061-Abstract-Conference.html ；https://arxiv.org/html/2508.05004v4 | 未知 | **高**：纯 NLP/LLM 路线；学校不在 top-4，录取门槛相对低一些 |
| Quanquan Gu | UCLA / Computer Science | 教授（职级待核实） | 自博弈微调（SPIN）、自博弈偏好优化（SPPO）、正则化自博弈 | Self-Play Preference Optimization for Language Model Alignment（SPPO，ICLR 2025）；Game-Theoretic Regularized Self-Play Alignment of LLMs（arXiv 2503.00030，2025） | https://arxiv.org/html/2503.00030v1 ；https://export.arxiv.org/pdf/2405.00675 （代码在 uclaml GitHub） | 未知 | **中–高**：ML 理论 + LLM 对齐，需要一定的数学功底 |
| Yiming Yang | Carnegie Mellon University / LTI | Professor | 自博弈偏好优化、LLM 对齐 | SPPO（ICLR 2025，合作者） | https://export.arxiv.org/pdf/2405.00675 | 未知 | **高**：NLP 院系（LTI），但自博弈只是她的方向之一，本轮没有核实 2025 年后的后续工作 |
| Natasha Jaques | University of Washington / Paul G. Allen School | 教员（职称和入职年份待核实；据既有了解为 Assistant Professor，同时在 Google DeepMind 任职） | 多智能体自博弈 RL、零和语言博弈激发推理 | SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning（arXiv 2506.24119，末位作者，v3 2026-03） | https://arxiv.org/html/2506.24119v3 | 未知 | **中–高**：多智能体 RL + LLM；有 RL 经验更佳 |
| Pulkit Agrawal | MIT / EECS（CSAIL） | 教员（职级待核实） | 自适应/自编辑语言模型、RL 学习自我更新 | Self-Adapting Language Models（SEAL，NeurIPS 2025） | https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b41e04c41726e2a60e456d0a2b961ab-Abstract-Conference.html | 未知 | **中**：组的主线是机器人/RL，SEAL 是 LLM 支线 |
| Yoon Kim | MIT / EECS（CSAIL） | 教员（职级待核实） | 自我改进 LLM、高效 LLM、NLP | SEAL（NeurIPS 2025，合作者） | https://neurips.cc/virtual/2025/poster/118690 | 未知 | **高**：NLP 背景的教员，和 NLP 申请者天然对口 |
| Aviral Kumar | Carnegie Mellon University / CSD & MLD（AIRe Lab） | Assistant Professor，**青年教师**（2025 年 AI2050 Early Career Fellow；入职年份待核实） | 用 RL 训练自我纠错、测试时计算、LLM 的自我改进 | Training Language Models to Self-Correct via Reinforcement Learning（SCoRe，ICLR 2025） | https://csd.cmu.edu/people/faculty/aviral-kumar ；https://cs.cmu.edu//news/2025/ai2050-fellows | 未知 | **中–高**：偏 RL，NLP 学生需要补 RL 基础；同时与 Google DeepMind 有合作关系 |
| Jiaxuan You | UIUC / Siebel School of Computing and Data Science | Assistant Professor，**青年教师**（2024 年至今） | 自动化科研 / AI scientist、研究社区多智能体模拟 | ResearchTown: Simulator of Human Research Community（ICML 2025）；TinyScientist（arXiv 2510.06579，2025） | https://siebelschool.illinois.edu/about/people/adjunct-faculty/jiaxuan ；https://dblp.org/pid/192/4727 | 未知 | **高**：LLM agent 方向，对 NLP 友好；注意他到 2025-12 为止仍在 NVIDIA 兼职（第三方资料） |
| Kevin Ellis | Cornell University / Computer Science | 教员（职级待核实） | LLM 程序合成与搜索、ARC、代码形式的世界模型 | PoE-World（NeurIPS 2025 Spotlight，arXiv 2505.10819）；Combining Induction and Transduction for Abstract Reasoning（ARC；发表时间和会议待核实） | https://www.alphaxiv.org/@kevin-ellis ；https://www.cs.cornell.edu/~wp237 | 未知 | **中**：神经-符号程序搜索 + 认知科学，适合对"LLM + 搜索"感兴趣的人 |
| Chandan K. Reddy | Virginia Tech / Computer Science | Professor | LLM + 进化搜索做科学方程发现（FunSearch 式） | LLM-SR: Scientific Equation Discovery via Programming with Large Language Models（ICLR 2025 Oral）；LLM-SRBench（ICML 2025，会议信息待核实） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/28df8e730c054c5331855fd4d5403ba9-Abstract-Conference.html | 未知 | **中–高**：属于非 top-4，方向就是 LLM 引导的程序/方程进化搜索 |
| Amir Barati Farimani | Carnegie Mellon University / Mechanical Engineering | 教授（职级待核实） | LLM 驱动的科学发现、方程发现 | LLM-SR（ICLR 2025 Oral，合作者） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/28df8e730c054c5331855fd4d5403ba9-Abstract-Conference.html | 未知 | **低–中**：机械系，需要走机械系的 PhD 项目申请 |
| Sean Welleck（跨主题） | CMU / LTI | Assistant Professor，**青年教师** | 自我改进的形式化代码生成（翻译 + Treefinement 自举） | AlphaVerus（ICML 2025） | 同主题一 | 未知 | **高**：两个主题的交叉点 |
| Tengyu Ma（跨主题） | Stanford / CS & Stats | Assistant Professor（**单位待核实**） | 自博弈 conjecturer–prover | STP（ICML 2025） | 同主题一 | 未知 | **中**：在 MongoDB 任职，带学生情况不明 |

**主题二覆盖说明**：Jeff Clune（UBC，加拿大）、Tim Rocktäschel（UCL）、Jakob Foerster（Oxford）这些开放式学习的代表人物都不在美国，按要求不收录。美国学术界纯"open-endedness / quality-diversity"方向（如 NYU 的 Julian Togelius、USC 的 Stefanos Nikolaidis、UT Austin 的 Risto Miikkulainen）**本轮因搜索配额耗尽未能核实**，见文末"未核实候选"。

---

## 业界实验室（不作为 PI 推荐，仅供参考）

- **Google DeepMind**：AlphaEvolve、AlphaProof。Swarat Chaudhuri 目前在这里休假。
- **Microsoft Research**：Verus / AutoVerus（OOPSLA 2025；Shuvendu Lahiri、Chris Hawblitzel、Jacob Lorch、Shan Lu 等）。
- **Meta FAIR**：Kaiyu Yang（LeanDojo、VERINA 合作者）。
- **Beneficial AI Foundation**：vericoding benchmark。
- **Sakana AI**：AI Scientist、ShinkaEvolve。
- **其他**：Lean FRO、Harmonic、Numina、DeepSeek-Prover 等。

---

## 申请策略建议

1. **NLP 友好的切入点**：首选 Welleck（CMU LTI）、Khattab（MIT）、Jiaxin Huang（WashU）、Chi Jin / Arora / Danqi Chen（Princeton）、Yoon Kim（MIT）、Jiaxuan You（UIUC）。这些组把形式化证明或自我改进当作 **LLM 训练/推理问题**来做，不要求 PL 背景。其中 Welleck 和 Princeton Goedel 团队同时覆盖两个主题（verifier 反馈下的自我改进）。
2. **需要 PL/FM 背景的组**：Parno、Barrett、Aiken、Jhala、Brun、Ringer、Amin、Polikarpova。申请这些组之前，最好先完成一个小项目，例如在 DafnyBench、VERINA、CLEVER 或 vericoding benchmark 上跑通一个 agent / 搜索 baseline，或者学完 Lean 4 的 "Functional Programming in Lean" 并做一个 Verus 小练习，这样能证明你愿意补 PL。
3. **讲好"可验证奖励"这条主线**：两个主题的共同点是"有可靠 verifier 或评估器的搜索/RL"，包括 Lean 编译器、Dafny 验证器、系统模拟器、方程拟合误差。SOP 可以写成：NLP 背景 → 对 RLVR / 推理感兴趣 → 想把 verifier 从"单元测试"升级为"形式化证明"或"自动评估器驱动的进化搜索"。
4. **优先联系青年教师 / 非 top-4 学校**：Emily First（Rutgers）、Jiaxin Huang（WashU）、Jiaxuan You（UIUC）、Khattab（MIT，新组）、Aviral Kumar（CMU）、Chandan Reddy（VT）、Vijay Ganesh（GT）。新组更需要学生，导师投入时间多。邮件里要点名对方 1 篇具体论文（例如 Cobblestone、R-Zero、ResearchTown），并给出一个可执行的后续想法。
5. **利用联合指导的结构**：CMU 的 Welleck + Parno / Avigad、Berkeley 的 Song + Cheung / Seshia、Princeton PLI 的几位老师都有跨 PL 和 ML 合作的先例。申请时可以同时列出 ML 和 PL 方向的教员，提高被"捞"的概率。
6. **注意导师在工业界的任职**：Chaudhuri（在 DeepMind 休假）、Tengyu Ma（MongoDB）、Jaques 与 Aviral Kumar（和 DeepMind 有关联）、Jiaxuan You（曾在 NVIDIA 兼职）。联系前先问清楚 2027 年是否在校、能否招新生。
7. **时间线**：Fall 2027 申请季的截止日期大多在 2026 年 12 月。建议 10–11 月发套磁邮件，同时关注各 PI 在 X/Bluesky 上的招生帖。本清单**没有找到任何官方招生声明**。

---

## 需要你自己核实的事项

- **职称和入职年份**：Talia Ringer、Nada Amin（来源不一致）、Jiaxin Huang、Natasha Jaques、Aviral Kumar、Quanquan Gu、Pulkit Agrawal、Yoon Kim、Kevin Ellis、Bryan Parno、Clark Barrett、Danqi Chen、Alvin Cheung、Polikarpova。请以学校官方 directory 为准。
- **当前是否在校**：Swarat Chaudhuri（在 DeepMind 休假）和 Tengyu Ma（MongoDB）需要确认是否招生，以及学生在校期间能否得到指导。
- **论文署名**：GEPA 的完整作者列表（确认 Khattab 的位置）；"Combining Induction and Transduction for Abstract Reasoning"的会议和年份；LeanHammer 的正式标题；Goedel-Code-Prover（arXiv 2603.19329）的作者是否包括 Chi Jin；LLM-SRBench 是否发表在 ICML 2025。
- **Laurel 的 PI 归属**：Laurel 的作者是 Mugnier、Anaya Gonzalez、Polikarpova、Jhala、Yuanyuan Zhou（均为 UCSD），请确认哪位是主导 PI。
- **VERINA 是否出自 Berkeley Dawn Song 组**：目前是根据 GitHub/HF 托管在 sunblaze-ucb 下推断的；Jingxuan He 等作者的现任单位未核实。
- **Alvin Cheung 在 2025 年后是否还有 LLM + 验证的工作**：本轮只找到 NeurIPS 2024 的论文。
- **招生信号**：所有 PI 都写的是"未知"。请查看各人主页的 "Prospective students" 段落和他们最近的社交媒体动态。
- **未核实候选**（因搜索配额耗尽未检索，**不要直接套用**）：James Zou（Stanford，Virtual Lab / AI scientist）、Julian Togelius（NYU，开放式学习）、Risto Miikkulainen（UT Austin，LLM + 进化计算）、Stefanos Nikolaidis（USC，quality diversity）、Huaxiu Yao（UNC，自奖励 VLM）、Huan Sun（OSU，ScienceAgentBench）、Diyi Yang / Tatsunori Hashimoto（Stanford，LLM 生成研究想法）、Noah Goodman（Stanford，STaR 系列）、Tong Zhang（UIUC，self-rewarding correction）、Mengdi Wang（Princeton，AI for science agent）、Matei Zaharia / Koushik Sen / Dan Klein（Berkeley，疑似 GEPA 合作者）、Meng Jiang（Notre Dame，疑似 GEPA 合作者）、Sanjit Seshia（Berkeley）、Gagandeep Singh / Lingming Zhang（UIUC）、Ziyang Li（JHU）、Qingyun Wu（Penn State）。

---

## Sources

**主题一**
- [A benchmark for vericoding (arXiv 2509.22908)](https://arxiv.org/abs/2509.22908v1)｜[POPL 2026 Dafny Workshop 条目](https://popl26.sigplan.org/details/dafny-2026-papers/13/A-benchmark-for-vericoding-formally-verified-program-synthesis)｜[Kavli 预印本页 (Tegmark)](https://preprints.kavlimeetings.org/2025/09/26/a-benchmark-for-vericoding-formally-verified-program-synthesis)
- [AlphaVerus (PMLR v267, ICML 2025)](https://proceedings.mlr.press/v267/aggarwal25a.html)｜[arXiv 2412.06176](https://arxiv.org/html/2412.06176v1)｜[Bryan Parno (alphaXiv)](https://www.alphaxiv.org/@bryan-parno)
- [Sean Welleck – CMU LTI](https://lti.cmu.edu/people/faculty/welleck-sean.html)｜[CMU Hoskinson – Welleck](https://www.cmu.edu/hoskinson/people/sean-welleck.html)｜[CMU Dietrich: AI & Mathematics](https://www.cmu.edu/dietrich/ai/news/ai-mathematics-carnegie-mellon.html)｜[Thomas Zhu (Siebel Scholar) 简介](https://www.siebelscholars.com/scholar-profile/3886/)｜[第三方招生聚合页（非官方）](https://researchersjob.com/cmu-lti-phd-program/)
- [Talia Ringer – researchr profile](https://conf.researchr.org/profile/talialilyringer)｜[Kevin Fisher (UIUC)](https://siebelschool.illinois.edu/academics/graduate/phd-program/amazon-ai-phd-fellows/Kevin-Fisher)｜[UIUC Rising Stars 简介](https://publish.illinois.edu/rising-stars/?p=828)
- [Emily First – ICSE 2027 profile](https://conf.researchr.org/profile/icse-2027/emilyfirst1)｜[Rutgers 报告 2025-03-11](https://www.cs.rutgers.edu/events/icalrepeat.detail/2025/03/11/4818/-/machine-learning-for-formal-software-verification)｜[Emily First 主页](https://people.cs.umass.edu/~efirst)｜[Cobblestone (arXiv 2410.19940)](https://arxiv.org/pdf/2410.19940)
- [Yuriy Brun 主页](https://people.cs.umass.edu/~brun)｜[Rango – ICSE 2025](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/88/Rango-Adaptive-Retrieval-Augmented-Proving-for-Automated-Software-Verification)｜[Rango (arXiv 2412.14063)](https://arxiv.org/html/2412.14063v2)
- [Swarat Chaudhuri 主页](https://www.cs.utexas.edu/~swarat)｜[UT AI news](https://ai.utexas.edu/news/0006/how-ai-redefining-research)｜[CLEVER – NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a7f67788f7b4d77fa7cd6887de3dcbe7-Abstract-Datasets_and_Benchmarks_Track.html)｜[PutnamBench – NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1582eaf9e0cf349e1e5a6ee453100aa1-Abstract.html)
- [Princeton 新闻：Goedel-Prover-V2](https://ai.princeton.edu/news/2025/princeton-researchers-unveil-improved-mathematical-theorem-prover-powered-ai)｜[DAIS 新闻](https://dais.princeton.edu/news/2025/princeton-researchers-unveil-improved-mathematical-theorem-prover-powered-ai)｜[Goedel-Prover-V2 – ICLR 2026](https://iclr.cc/virtual/2026/poster/10007912)
- [LeanAgent – ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b67c77f8db8b991d73d6f2e16f491840-Abstract-Conference.html)
- [STP – PMLR (ICML 2025)](https://proceedings.mlr.press/v267/dong25h.html)｜[Tengyu Ma 主页](https://ai.stanford.edu/~tengyuma)｜[Tengyu Ma (alphaXiv)](https://www.alphaxiv.org/@tengyu-ma)
- [VerMCTS – POPL 2025 Dafny](https://popl25.sigplan.org/details/dafny-2025-papers/12/VerMCTS-Synthesizing-Multi-Step-Programs-using-a-Verifier-a-Large-Language-Model-a)｜[dafny-annotator – POPL 2025 Dafny](https://popl25.sigplan.org/details/dafny-2025-papers/7/dafny-annotator-AI-Assisted-Verification-of-Dafny-Programs)｜[Nada Amin (alphaXiv)](https://www.alphaxiv.org/@nada-amin)｜[Harvard 博后招聘](https://jobs.protocol.ai/companies/harvard-university/jobs/62907288-postdoctoral-fellowship-in-computer-science-programming-languages-and-artificial-intelligence)
- [Centaur news (Stanford)](https://centaur.stanford.edu/news.html)｜[CSLib](https://sos-vo.org/node/109653)｜[Lemur (Barrett 页)](https://theory.stanford.edu/~barrett/pubs/WCB24-abstract.html)｜[Clover](https://arxiv.org/html/2310.17807v4)
- [Quokka (arXiv 2509.21629 v3)](https://arxiv.org/html/2509.21629v3)
- [VERINA – ICLR 2026](https://iclr.cc/virtual/2026/poster/10011965)｜[VERINA – ICML 2025](https://icml.cc/virtual/2025/52464)
- [Verified Code Transpilation with LLMs (SLICE Berkeley)](https://slice.eecs.berkeley.edu/?p=1141)｜[Seshia 出版物页](https://people.eecs.berkeley.edu/~sseshia/pubs/b2hd-bhatia-neurips24.html)
- [Vijay Ganesh – GT](https://www.cc.gatech.edu/people/vijay-ganesh)｜[GT 数学系报告 2026-01-29](https://math.gatech.edu/seminars-colloquia/series/school-mathematics-colloquium/vijay-ganesh-20260129)｜[Tech AI 报告](https://tech.ai.gatech.edu/event/vijay-ganesh-seminar)
- [AutoVerus (arXiv 2409.13082)](https://arxiv.org/pdf/2409.13082)
- [Saikat Dutta – Cornell](https://www.cs.cornell.edu/people/saikat-dutta)（用于排除）

**主题二**
- [Barbarians at the Gate (arXiv 2510.06189)](https://arxiv.org/pdf/2510.06189)｜[Let the Barbarians In (SIGOPS)](https://www.sigops.org/2026/let-the-barbarians-in-how-ai-can-accelerate-systems-performance-research/)｜[The Register 报道](https://theregister.com/2025/10/25/openevolve_ai_better_algorithms)
- [GEPA (arXiv 2507.19457)](https://arxiv.org/pdf/2507.19457)｜[Omar Khattab – MIT EECS](https://www.eecs.mit.edu/people/omar-khattab/)｜[Omar Khattab – CSAIL](https://www.csail.mit.edu/person/omar-khattab)｜[CMU 校友简介](https://www.cmu.edu/engage/alumni/get-involved/tartansontherise/2025/khattab.html)
- [R-Zero – ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d49b9aacebda61051166335af6fd3061-Abstract-Conference.html)｜[R-Zero arXiv](https://arxiv.org/html/2508.05004v4)
- [SPPO (arXiv 2405.00675)](https://export.arxiv.org/pdf/2405.00675)｜[RSPO (arXiv 2503.00030)](https://arxiv.org/html/2503.00030v1)｜[SPIN (arXiv 2401.01335)](https://arxiv.org/html/2401.01335v1)
- [SPIRAL (arXiv 2506.24119 v3)](https://arxiv.org/html/2506.24119v3)
- [SEAL – NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b41e04c41726e2a60e456d0a2b961ab-Abstract-Conference.html)｜[SEAL poster](https://neurips.cc/virtual/2025/poster/118690)
- [Aviral Kumar – CMU CSD](https://csd.cmu.edu/people/faculty/aviral-kumar)｜[AI2050 Fellows (CMU news 2025)](https://cs.cmu.edu//news/2025/ai2050-fellows)｜[SCoRe – ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/871ac99fdc5282d0301934d23945ebaa-Abstract-Conference.html)
- [Jiaxuan You – UIUC Siebel](https://siebelschool.illinois.edu/about/people/adjunct-faculty/jiaxuan)｜[DBLP](https://dblp.org/pid/192/4727)｜[TinyScientist (arXiv 2510.06579)](https://arxiv.org/pdf/2510.06579)
- [Kevin Ellis (alphaXiv)](https://www.alphaxiv.org/@kevin-ellis)｜[PoE-World (arXiv 2505.10819)](https://arxiv.org/abs/2505.10819v3)｜[Wasu Top Piriyakulkij 主页](https://www.cs.cornell.edu/~wp237)
- [LLM-SR – ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/28df8e730c054c5331855fd4d5403ba9-Abstract-Conference.html)｜[LLM-SR oral](https://iclr.cc/virtual/2025/oral/31782)
