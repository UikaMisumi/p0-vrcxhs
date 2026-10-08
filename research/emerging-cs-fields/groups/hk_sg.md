# 香港 / 新加坡 学术课题组清单（ML/NLP 背景博士申请向）

> 编制日期：2026-10-08（第二轮补充核实于同日完成）｜ 方法：WebSearch，两轮合计约 75 次。WebFetch 对 arxiv.org、cse.hkust.edu.hk、cse.cuhk.edu.hk 等域名均被拦截，因此只能依据检索结果摘要中能看到的信息。
> 方向标签：**(1)** LLM 驱动的形式化验证 / 可验证代码生成 / AI4Math·定理证明；**(2)** 自我改进 & LLM 引导的进化搜索；**(3)** LLM 持续学习 / 知识编辑 / 记忆 / 测试时适应；**(4)** LLM 智能体 + 智能体系统基础设施（系统组标注“偏系统”）。
> 收录标准：至少有一条 2024–2026 年来源，同时显示 (a) 当前在所列学校任职、(b) 在对应方向确有工作。凡单位证据冲突或早于 2025 年，标“(单位待核实)”；论文作者归属在检索摘要中看不到的，标“(待核实)”。
> 招生信号：只有找到明确写着 2026/2027 入学招生的来源才标“招生中”。**两轮检索都没有找到任何一条这样的来源，因此全部标为“未知”。**
> “青年教师”：2022–2026 年入职的助理教授。入职年份无法确认的，写作“助理教授（入职年份待核实）”。

## 概览：主表 PI 数量（共 32 人）

| 学校 | 人数 | PI |
|---|---|---|
| HKU | 4 | Tao Yu、Chao Huang、Chuan Wu（偏系统）、Ping Luo |
| HKUST（清水湾） | 3 | Junxian He、May Fung、Binhang Yuan（偏系统） |
| HKUST(GZ)（**内地校区**） | 3 | Zhijiang Guo、Xuming Hu、Yuyu Luo |
| CUHK | 3 | Weiyang Liu、Yu Cheng、Michael R. Lyu |
| PolyU | 2 | Xiao-Ming Wu、Wenjie Li |
| CityU | 2 | Qingfu Zhang、Xiangyu Zhao |
| HKBU | 1 | Bo Han |
| NUS | 9 | Tat-Seng Chua、Bryan Low、Wee Sun Lee、Min-Yen Kan、Michael Shieh、Abhik Roychoudhury、Ilya Sergey、Mike Shou、Yang You（偏系统） |
| NTU | 2 | Bo An、Yang Liu |
| SMU | 3 | Yang Deng、Jun Sun、David Lo |
| SUTD | 0 | 没有确认符合条件的 PI（Poria、Wei Lu 单位有冲突，见第三节） |

另有约 25 位候选人放在第三节的“证据不足 / 单位待核实”表中，请勿直接据此套磁。

---

## 一、香港

### HKU（香港大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Tao Yu（余涛） | HKU 计算机科学系，XLANG Lab | 助理教授（入职年份待核实，可能属青年教师） | **(4)** computer-use agent、GUI agent、agent 评测基准 | OpenCUA: Open Foundations for Computer-Use Agents（2025-08，arXiv 2508.09123）；OSWorld 基准（agent 评测，NeurIPS 2024） | https://www.xlang.ai/ ；https://eu.36kr.com/en/p/3422013601860997 ；https://nlp.stanford.edu/seminar/details/taoyu_2024.shtml | 未知 | **高**：NLP 出身（Text-to-SQL/Spider），agent 数据、训练、评测一条龙，NLP 学生上手快 |
| Chao Huang（黄超） | HKU 计算与数据科学学院（Data Intelligence Lab / HKUDS） | 助理教授（入职年份待核实） | **(4)(2)** 深度研究 agent、AI scientist、自动科研 | Auto-Deep-Research 开源个人研究助手（HKU 新闻稿 2025-03）；AI-Researcher: Autonomous Scientific Innovation（arXiv 2505.18705，代码在 HKUDS GitHub 组织下；**作者名单是否含 Chao Huang 待核实**） | https://hku.hk/press/news_detail_28160.html ；https://arxiv.org/pdf/2505.18705 | 未知 | **高**：偏 LLM 应用与 agent 系统，开源产出多；偏工程，理论较少 |
| Chuan Wu（吴川） | HKU 计算机科学系 | 教授（具体职称待核实） | **(4) 偏系统**：RLHF / agent RL 训练框架 | HybridFlow: A Flexible and Efficient RLHF Framework（EuroSys 2025，即开源框架 verl 背后的论文，与字节跳动 Seed 合作） | https://arxiv.org/html/2409.19256v1 ；https://seed.bytedance.com/en/public_papers/hybridflow-a-flexible-and-efficient-rlhf-framework | 未知 | **中**：适合想转向 RL 后训练基础设施的人；纯 NLP 背景需要补分布式系统 |
| Ping Luo（罗平） | HKU 计算机科学系 | 副教授（据 HKU 个人页，页面未标日期） | **(4)（偏多模态 / 具身）** GUI agent、移动操作 agent、LLM 世界模型 | GUI Odyssey: 跨 App 移动端 GUI 导航数据集（ICCV 2025）；Text2World（ACL Findings 2025）；OWMM-Agent（arXiv 2506.04217，2025） | https://www.ai.hku.hk/people/academic-staff/pluo ；https://dblp1.uni-trier.de/pid/54/4989-2.html | 未知 | **中**：组大、方向偏视觉和具身；同名作者很多，引用前请核对单位 |

### HKUST（香港科技大学，清水湾）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Junxian He（何俊贤） | HKUST 计算机科学与工程系（CSE） | 助理教授（入职年份待核实，可能属青年教师） | **(2)** 自我改进 / self-taught reasoner、推理 RL | B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners（ICLR 2025） | https://cse.hkust.edu.hk/admin/people/faculty/?a=AI ；https://arxiv.org/pdf/2412.17256 | 未知 | **高**：纯 NLP/LLM 组，自我改进和推理 RL 是核心方向 |
| Yi R. (May) Fung | HKUST CSE | 助理教授，**青年教师**（入选 AAAI 2026 New Faculty Highlights） | **(4)** agentic AI、工具学习、可信基础模型 | Tool Learning with Foundation Models（ACM Computing Surveys 2025，合著）；The Law of Knowledge Overshadowing（ACL 2025，关于幻觉） | https://seng.hkust.edu.hk/news/20251210/prof-may-fung-and-alumna-dr-wang-yaqing-selected-aaai-new-faculty-highlights-program ；https://www.alphaxiv.org/@yi-r-fung | 未知 | **高**：UIUC NLP 博士出身，方向是推理 + agent，新组招人需求通常较大 |
| Binhang Yuan | HKUST CSE | 助理教授（入职年份待核实，可能属青年教师） | **(4) 偏系统**：去中心化 LLM 训练、异步 RL 系统 | AReaL: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning（arXiv 2505.24298，**本人为合著者，依据是其他论文的参考文献，待核实**） | https://calendar.hkust.edu.hk/node/39051 ；https://arxiv.org/pdf/2510.12633 | 未知 | **中**：偏系统，适合对 RL rollout / 训练基础设施有兴趣、又懂 LLM 的人 |

### HKUST(GZ)（香港科技大学（广州）——**内地校区，注意：学位、签证、生活均在广州**）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Zhijiang Guo | HKUST(GZ)（内地校区） | 职称待核实 | **(1)** 自动形式化（Lean）、事实性 | FormalAlign: Automated Alignment Evaluation for Autoformalization（ICLR 2025，论文署 HKUST(GZ)）；CtrlA 自适应 RAG（ACL Findings 2025） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/fceedf8c9c0ff51f41b9fe0294ef0070-Abstract-Conference.html ；https://dblp1.uni-trier.de/pid/43/6147.html | 未知 | **高**：NLP 出身，做 autoformalization，是 NLP 学生进入 AI4Math 最顺的入口之一 |
| Xuming Hu（胡旭明） | HKUST(GZ) AI Thrust（内地校区） | 职称待核实 | **(3)（证据偏弱）** 可信 LLM、遗忘 / unlearning、幻觉 | SafeEraser（多模态 unlearning，年份待核实）；StructFact（ACL Findings 2025） | https://ait.hkust-gz.edu.cn/?p=3690 ；https://dblp.org/pid/262/3664 | 未知 | **中-高**：NLP 背景完全对口；“知识编辑”方向两轮都没有检索到直接证据 |
| Yuyu Luo | HKUST(GZ) 数据科学与分析（DSA）Thrust（内地校区），兼任 HKUST 职务 | 助理教授，**青年教师**（2023 年清华博士毕业） | **(4)(2)** 数据 agent、agentic workflow 自动搜索、NL2SQL | Data Agents: Levels, State of the Art, and Open Problems（arXiv 2602.04261，2026，文中作者简介写明其职位）；AFlow（自动搜索 agentic workflow，据个人资料页，**会议与年份待核实**）；Alpha-SQL（MCTS 零样本 Text-to-SQL） | https://arxiv.org/pdf/2602.04261 ；https://www.alphaxiv.org/@yuyu-luo ；https://dsa.hkust-gz.edu.cn/zh/blog/2026/07/20/llm-agents-for-data-science-workflows-a-survey-on-data-processing-analysis-andreliable-execution/ | 未知 | **高**：LLM agent 加数据，“用 LLM 搜索 workflow”同时贴合方向 (2) 和 (4) |

### CUHK（香港中文大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Weiyang Liu | CUHK 计算机科学与工程系（CSE），SphereLab | 助理教授，**青年教师**（新入职；HKUST 2025 论坛讲者页写的是 CUHK CSE 助理教授） | **(1)** LLM 形式化推理、Lean 基准 | FormalMATH: Benchmarking Formal Mathematical Reasoning of LLMs（arXiv 2505.02735，2025；一作为 CUHK SphereLab 博士生；该论文中刘本人署名为 MPI-IS） | https://cse.hkust.edu.hk/ai-formal/2025fm/weiyang.html ；https://arxiv.org/abs/2505.02735v1 ；https://www.alphaxiv.org/@zhouliang-yu | 未知 | **高**：ML 理论加 LLM 推理，非常欢迎 ML 背景的学生 |
| Yu Cheng | CUHK CSE | 职称待核实（个人页写 2024 年加入，此前为 MSR Redmond Principal Researcher） | **(4)** LLM 决策 agent、MoE、高效大模型 | ICML 2025 用离线分层 RL 把 LLM grounding 为决策 agent（**题目与作者归属待核实**，同名作者较多）；Linear-MoE（ICLR Workshop 2025，待核实） | https://www.cse.cuhk.edu.hk/people/faculty/yu-cheng/ ；https://mlanthology.org/authors/c/cheng-yu/ | 未知 | **中**：LLM/多模态方向对口；agent 方向的证据偏弱 |
| Michael R. Lyu（吕荣聪） | CUHK CSE | 教授 | **(1)（弱，代码 LLM，并非验证）** LLM 自动编程、代码生成的实证研究 | Automatic Programming: Large Language Models and Beyond（ACM TOSEM 2025，与 Roychoudhury 等合著）；Divide-and-Conquer: Generating UI Code from Screenshots（FSE 2025） | https://dblp1.uni-trier.de/pid/l/MichaelRLyu.html ；https://www.cse.cuhk.edu.hk/lyu/students/fyp | 未知 | **中**：软件工程大组，偏代码 LLM 的实证与应用；没有检索到“LLM + 形式化验证”的工作 |

### PolyU（香港理工大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Xiao-Ming Wu | PolyU 计算机系 / 数据科学与人工智能系（两种署名都出现过，待核实） | 职称待核实 | **(3)** LLM 持续学习、知识编辑、模型合并 | GeoEdit: Geometric Knowledge Editing for LLMs（EMNLP 2025）；AIMMerging（EMNLP 2025，持续学习）；Recurrent Knowledge Identification and Fusion（ACL 2025） | https://www4.comp.polyu.edu.hk/~csxmwu/ ；https://theses.lib.polyu.edu.hk/handle/200/14657 | 未知 | **高**：(3) 方向在香港证据最扎实的组之一，NLP 背景完全对口 |
| Wenjie Li (Maggie) | PolyU 计算机系 | 教授 | **(3)** LLM 长期记忆、个性化助手 | Personalized Large Language Model Assistant with Evolving Conditional Memory（COLING 2025，署 PolyU） | https://www.polyu.edu.hk/comp/people/academic-staff/prof-li-wenjie-maggie/ ；https://preview.aclanthology.org/setup/2025.coling-main.254 | 未知 | **高**：老牌 NLP 组，记忆方向有现成积累；同名作者多，引用前核对 DBLP（Wenjie Li 0002） |

### CityU（香港城市大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Qingfu Zhang（张青富） | CityU 计算机科学系 | 讲座教授（Chair Professor） | **(2)** LLM 驱动的算法发现、LLM + 进化计算 | Evolution of Heuristics (EoH)（ICML 2024）；LLM4AD 开源平台（2025 年 IEEE CIS 讲座介绍） | https://proceedings.mlr.press/v235/liu24bs.html ；https://cis.taskforce.ieee.org/esco/webinar-series/esco-webinar-26/ | 未知 | **中**：FunSearch/AlphaEvolve 类方向在亚洲最强的组之一；但组的底色是进化计算 / 优化，NLP 技能主要用在 LLM 端 |
| Xiangyu Zhao（赵翔宇） | CityU 数据科学系 | 副教授（终身，2025-07 提前晋升） | **(4)** 工具使用 agent、LLM + 推荐 | 为工具使用 agent 生成困难样本（arXiv 2026，**题目待核实**）；GARLIC（AAAI 2025） | https://scholars.cityu.edu.hk/en/persons/xianzhao/ ；https://dblp.uni-trier.de/pid/08/890-1.html | 未知 | **中**：组大、产出多，偏推荐 / 数据挖掘 |

### HKBU（香港浸会大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Bo Han（韩波） | HKBU 计算机科学系，TMLR Group | 副教授 | **(2)（证据偏弱）** 自监督 RL 推理；可信 ML / unlearning | Co-reward: Self-supervised RL for LLM reasoning via contrastive agreement（ICLR 2026，**依据是其他论文的参考文献，作者归属待核实**） | https://datascience.hku.hk/2025/11/hku-ids-scholar-seminar-series-21/ | 未知 | **中**：可信 ML 底色，LLM 推理和自我奖励是新方向 |

---

## 二、新加坡

### NUS（新加坡国立大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Tat-Seng Chua（蔡达成） | NUS 计算学院（SoC） | KITHCT 讲座教授 | **(3)** 知识编辑 | AlphaEdit: Null-Space Constrained Knowledge Editing for LMs（ICLR 2025 Outstanding Paper，与中科大合作） | https://comp.nus.edu.sg/bytes/prof-chua-tat-seng-iclr-2025 ；https://www.comp.nus.edu.sg/features/ai-without-side-effects-alphaedit/ | 未知 | **高**：大组（NExT++），NLP/多模态全覆盖；资深 PI，学生多，指导可能偏间接 |
| Bryan Kian Hsiang Low | NUS 计算机系 | 副教授 | **(3)(4)** agent 记忆、长程 agent RL、数据中心 AI | MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents（ICLR 2026；NeurIPS 2025 workshop 最佳论文；**该文中他的署名为 SMART/MIT**） | https://www.scai.gov.sg/2025/participants-of-scai-2025/bryan-low/ ；https://www.nus.edu.sg/about/management/bryan-low ；https://arxiv.org/html/2506.15841v1 ；https://www.comp.nus.edu.sg/bytes/phd-student-wins-2025-best-paper-award-at-neurips-2025 | 未知 | **高**：记忆加 RL agent，ML 背景的人很好切入 |
| Wee Sun Lee | NUS 计算机系 | 教授（具体职称待核实） | **(2)(4)** self-play 自我提升推理、多智能体多轮 RL、LLM agent 训练环境 | SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL（ICLR 2026，arXiv 2506.24119，作者单位块写明 NUS）；GEM: A Gym for Generalist LLMs（ICLR 2026，**作者列表据第三方索引**） | https://arxiv.org/html/2506.24119v3 ；https://iclr.cc/virtual/2026/poster/10011289 ；https://mlanthology.org/authors/l/lee-wee-sun/ | 未知 | **高**：self-play 和 agent RL 都是最前沿方向；与 Sea AI Lab（Min Lin 等）合作紧密 |
| Min-Yen Kan | NUS 计算机系，WING（Web IR / NLP Group） | 职称待核实 | **(2)（经由学生工作）** LLM/VLM 推理的自主改进；agent 记忆检索（硕士生项目） | 其博士生 Yuxi Xie 的学位论文 Closed Loop Scaling: Autonomous Improvement of LLM and VLM Reasoning（2026-05 答辩）；组内 2025 年起有多名学生做 AI agents | https://wing.comp.nus.edu.sg/author/yuxi-xie/ ；https://wing.comp.nus.edu.sg/people ；https://www.comp.nus.edu.sg/~kanmy/research.html | 未知 | **高**：纯 NLP 老牌组，氛围开放；他本人 2025 年署名论文偏话语分析 / 长文本生成，前沿方向主要由学生推动 |
| Michael Qizhe Shieh | NUS 计算机系 | 助理教授（入职年份待核实；有 Google Brain/DeepMind 背景） | **(4)（证据偏弱）** LLM agent 训练环境、LLM 推理 | GEM: A Gym for Generalist LLMs（ICLR 2026，**合著，作者列表据第三方索引，待核实**） | https://www.comp.nus.edu.sg/cs/people/mshieh ；https://wing.comp.nus.edu.sg/author/michael-qizhe-shieh/ ；https://mlanthology.org/authors/l/lee-wee-sun/ | 未知 | **中-高**：兴趣包括 LLM 推理与训练目标，NLP 背景对口；本人一作 / 通讯的 2025 年 agent 论文没有检索到 |
| Abhik Roychoudhury | NUS 计算学院 | 教授（具体讲座职称待核实） | **(1)(4)** 规约推断、LLM 程序修复 agent、可信 AI 编程 | SpecRover（ICSE 2025）；AutoCodeRover（ISSTA 2024，衍生公司 2025 年被 Sonar 收购） | https://www.comp.nus.edu.sg/news/how-nus-computing-research-became-the-technology-behind-sonars-globally-launched-ai-remediation-agent/ ；https://arxiv.org/abs/2408.02232v4 | 未知 | **中-高**：软件工程组，NLP 学生需要补程序分析；“代码 agent + 验证”方向非常前沿 |
| Ilya Sergey | NUS 计算学院，VERSE Lab | 副教授 | **(1)** Lean 中的程序验证（可验证代码的目标框架） | Velvet: A Foundational Multi-Modal Verifier for Imperative Programs in Lean（CAV 2026 杰出论文）；Veil（SAS/SPLASH 2025） | https://www.comp.nus.edu.sg/bytes/associate-professor-ilya-sergey-and-team-win-distinguished-paper-award-at-cav-2026/ ；https://ilyasergey.net/ | 未知 | **低-中**：纯形式化方法组，检索到的来源**没有**提到 LLM；只有当你愿意深入 PL/Lean 时才适合（也适合做“LLM 生成 + Lean 验证”的合作导师） |
| Mike Zheng Shou（寿政） | NUS Show Lab | 职称待核实 | **(4)** GUI 视觉 agent、视觉-语言-动作模型 | ShowUI: One Vision-Language-Action Model for GUI Visual Agent（CVPR 2025） | https://arxiv.org/html/2411.17465v1 | 未知 | **中**：偏视觉 / 多模态，NLP 背景需要补 VLM |
| Yang You（尤洋） | NUS 计算机系，HPC-AI Lab | Presidential Young Professor（2021 年起，不属于 2022–2026 入职） | **(4) 偏系统（与 agent 关联弱）** 大模型训练 / 推理系统 | Expert-as-a-Service（MoE 推理服务，2025，见实验室页面）；Colossal-AI | https://ai.comp.nus.edu.sg/index.html ；https://www.comp.nus.edu.sg/~youy/index_files/CV.pdf | 未知 | **低-中**：HPC 方向，对 NLP 学生的门槛较高 |

### NTU（南洋理工大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Bo An（安波） | NTU 计算与数据科学学院（CCDS） | President's Chair Professor；AI 学部主任 | **(4)** LLM 智能体、agent RL、多智能体协作 | IAS 讲座 “From Algorithmic and RL-based to LLM-powered Agents”（2025-10）；Agent Orchestra 基准（讲座中提到，**论文信息待核实**） | https://www.ntu.edu.sg/ias/news-events/news/detail/from-algorithmic-and-reinforcement-learning-based-to-llm-powered-agents-by-prof-bo-an ；https://personal.ntu.edu.sg/boan/ | 未知 | **高**：RL 加 LLM agent，大组，资源充足 |
| Yang Liu（刘杨） | NTU CCDS；NTU 网络安全研究中心执行主任 | 教授（据 2025-08 哈工大讲座简介） | **(1)(4)** 需求形式化与可靠代码生成、多智能体代码生成 / 调试、LLM 安全 | Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision（ASE 2025）；TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code（ICSE 2026）（**题目据 researchr 个人页**） | https://conf.researchr.org/profile/ase-2025/yangliu ；https://encs.hit.edu.cn/2025/0831/c21303a381565/page.htm ；https://conf.researchr.org/profile/fse-2026/yangliu | 未知 | **中-高**：形式化方法加安全的大组，近年大量 LLM 代码 / agent 工作；NLP 学生需要补 SE / PL |

### SMU（新加坡管理大学）

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 方向标签(1-4) + 关键词 | 1-2 项 2024-2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Yang Deng（邓扬） | SMU 计算与信息系统学院（SCIS） | 助理教授（2024-07 入职），**青年教师**；Lee Kong Chian Fellow | **(4)** LLM 驱动的 agent、主动式对话 agent、LLM 可信性 | 主动式对话 AI 综述（ACM TOIS 2025）；Towards Human-centered Proactive Conversational AI（AAAI 2026 New Faculty Highlights） | https://faculty.smu.edu.sg/profile/deng-yang-7801 ；https://computing.smu.edu.sg/sites/scis.smu.edu.sg/files/2026-02/ydeng-CV.pdf | 未知（CV 中有邮箱 ydeng@smu.edu.sg，可直接询问） | **高**：纯 NLP 出身（CUHK 博士），对话 agent 方向，新组 |
| Jun Sun（孙军） | SMU SCIS | 教授 | **(1)** LLM 加形式化方法 / 测试 | ConTested: Consistency-Aided Tested Code Generation with LLM（ISSTA 2025，**题目据 researchr 页面，待核实**）；LLM-aided Automatic Modeling for Security Protocol Verification（ICSE，**年份待核实**）；担任 HKUST AI+FM 论坛 2025 会场主席 | https://conf.researchr.org/profile/issta-2025/junsun ；https://cse.hkust.edu.hk/ai-formal/ | 未知 | **中**：形式化方法底色（PAT 模型检测器），LLM + 验证是新方向 |
| David Lo | SMU SCIS；智能软件工程研究中心（RISE）创始主任 | OUB 讲座教授 | **(1)（弱，代码 LLM，并非验证）(4)** 高效代码 LLM、代码生成基准、多智能体 SE | Token Sugar（ASE 2025，面向 LLM 的 token 高效代码表示）；BigCodeBench（代码生成基准，合著）；2025 年主题演讲 “Efficient and Green Code LLMs” | https://conf.researchr.org/profile/ase-2025/davidlo ；https://events.csiro.au/Events/2025/August/7/Efficient-and-Green-Code-LLMs ；https://conf.researchr.org/profile/davidlo | 未知 | **中**：SE 顶级大组，代码 LLM 产出极多；agent 论文主要发表在 2026 年会议（如 PatchGPT 补丁回移植多智能体系统） |

### SUTD（新加坡科技设计大学）

两轮检索都**没有**确认同时满足“2025 年后在 SUTD 任职”和“四个方向之一”的 PI：
- Soujanya Poria、Wei Lu 的单位都有冲突，可能已转到 NTU，见第三节。
- Roy Ka-Wei Lee 确认在 SUTD，但没有检索到四个方向的工作。

### A*STAR（只作备注，不计入 PI）

A*STAR（CFAR、I2R 等）可以通过 **A*STAR Graduate Scholarship (AGS)** 与 NUS/NTU 联合培养博士。SPIRAL 论文的署名中就有 A*STAR CFAR。本次没有检索 A*STAR 的具体 PI。

---

## 三、证据不足 / 单位待核实的候选（**不要直接据此套磁**）

| 姓名 | 可能单位 | 为什么没放进主表 |
|---|---|---|
| Lingpeng Kong（孔令鹏） | HKU 计算机系（HKU 页面写助理教授，可能已晋升，待核实） | 主攻扩散语言模型（Dream 7B，2025）和推理；两轮都没找到四个方向的 2025 年署名论文。作为 NLP 导师适配度很高 |
| Qi Liu | HKU 计算机系助理教授（2022 年入职，属青年教师） | 单位已确认；HKU 页面列出的代表作多为 2019–2022 年（如 Relational Memory Augmented LMs，TACL 2022），没有找到 2024–2026 年的方向证据 |
| Soujanya Poria | **(单位待核实)**：NUS WING 作者页写 NTU EEE 副教授；SUTD 2024-07 新闻写 SUTD 讲座教授职位，另一资料页写 “Associate Professor @ SUTD” | 单位证据冲突；方向是 LLM 推理 / 安全，和 agent 的关联未核实 |
| Wei Lu | **(单位待核实)**：alphaXiv 资料写 NTU 教授（曾任 SUTD），SUTD 页面最新信息停在 2024 年中 | 单位冲突；没找到四个方向的 2025 年论文 |
| Roy Ka-Wei Lee | SUTD 助理教授 | 方向是 AI 信任与安全、计算社会科学，没找到 agent 方向的工作 |
| Chengwei Qin | **(单位待核实)**：可能是 HKUST(GZ)，检索只找到 NTU 时期的资料 | 持续学习（终身学习）方向高度对口，但 2025 年后的任职没能证实 |
| Xiaowen Chu（褚晓文） | **(单位待核实)**：HKBU 旧页面显示其处于无薪假，HKUST(GZ) 任职没有检索到直接来源 | 偏系统：Reasoning Language Model Inference Serving Unveiled（ICLR 2026）、ChunkKV（NeurIPS 2025），均据第三方索引。单位核实后可进主表（4 偏系统） |
| Yangqiu Song（宋阳秋） | HKUST CSE 副教授 | 只找到 2025 年关于“合规 LLM agent / 上下文完整性”的报告，没找到对应论文；ACL 2025 的 KG-Agent 作者是另一位同名学者 |
| Linqi Song（宋林琦） | CityU 计算机系副教授，兼 InnoHK AIFT（页面未标日期） | 是定理证明数据合成工作 MUSTARD（ICLR 2024）的合著者，但没找到 2025 年后带单位的 AI4Math 论文。单位核实后可进主表（1） |
| Kenji Kawaguchi | NUS | WING “Self-Improving and Self-Adapting Agents” 项目页列他为博士生联合导师（方向 2/3），但没找到他署名的 2025 年具体论文；VDS-TTT 经核实**不是**他的论文（作者来自 Concordia/华为） |
| Hongsheng Li（李鸿升） | CUHK 电子工程系 / MMLab（本次检索未确认单位） | 有非形式化数学推理工作：MathCoder2（ICLR 2025）、MathCoder-VL（ACL Findings 2025）。不属于 Lean/形式化方向，同名作者也多 |
| Michael Lyu 之外的 CUHK 候选：Bei Yu、Kam-Fai Wong、Irwin King、Sinno Pan | CUHK | Bei Yu：没找到 LLM 硬件验证的 2025 年署名论文。Kam-Fai Wong：没有检索结果。Irwin King：2025 年任 CUHK 副校长（教育），工作为水印 / 图学习等，与四个方向不符。Sinno Pan：没找到 LLM 持续学习的直接论文 |
| Hwee Tou Ng、Reza Shokri、Xinchao Wang、Bryan Hooi | NUS | Ng：2025 年工作为摘要和偏好数据，与四个方向不符。Shokri：有记忆化 / 隐私方向，但没找到 2025 年论文。Xinchao Wang：高效推理综述（TMLR 2025），单位未在结果中确认。Hooi：没找到方向证据 |
| Jing Ma（马晶） | HKBU 计算机系助理教授（页面未标日期，HKBU-NLP 组负责人） | 方向为事实核查、多模态 / LLM，但没找到四个方向的具体工作 |
| Luu Anh Tuan | **(单位待核实)** | 检索没能确认当前单位 |
| Jing Jiang | **已离开 SMU**：现为澳大利亚国立大学（ANU）教授（ANU 2026-06 新闻） | 不在港新范围，排除 |
| Yew-Soon Ong | NTU（传闻兼任 A*STAR 首席 AI 科学家，未核实） | LLM 驱动进化优化的代表作 LMEA 是 2023 年的；2025 年后的单位和论文均未核实 |
| Shing-Chi Cheung（张成志） | HKUST CSE | 在 HKUST AI+形式化方法论坛 2025 开幕致辞，但没找到 LLM 验证的具体论文 |
| **本次未检索**：Yi Ma、Difan Zou（HKU），Wai Lam、Helen Meng（CUHK），Chen Ma（CityU），Aixin Sun、Ziwei Liu（NTU），Ye Wang（NUS） | — | 检索配额有限，没有覆盖；其中多数人的方向可能偏离四个主题 |

## 四、产业界 / 校企联合实验室（不作为 PI）

- **HKU × 字节跳动 Seed**：HybridFlow/verl 由 HKU 吴川组与字节 Seed 合作完成（EuroSys 2025）。
- **NUS → SonarSource**：AutoCodeRover 由 NUS 衍生，2025 年 2 月被 Sonar 收购，现为 SonarQube Remediation Agent；Roychoudhury 任 Sonar 高级顾问。
- **NUS × Sea AI Lab**：SPIRAL 和 GEM 都由 NUS（Wee Sun Lee、Michael Shieh）与 Sea AI Lab（Min Lin、Zichen Liu 等）合作完成；Sea AI Lab 研究员属于产业界，不是 PI。
- **SMART（新加坡-MIT 联盟）**：MEM1 的署名机构之一，适合做 NUS + MIT 联合项目。
- **InnoHK AIFT 实验室（香港）**：CityU 宋林琦兼任研究科学家。
- **HKUST–微众银行联合实验室**：Yangqiu Song 任联合主任 / 副主任（不同页面版本说法不一）。
- 华为诺亚方舟实验室 Zhenguo Li（LEGO-Prover、ProofAug）属于产业界，**不是**高校 PI（他在 HKUST 的职位是兼职教授）。

---

## 五、港新申请须知

1. **HKPFS（香港博士研究生奖学金计划，2027/28 学年）**
   - **初始申请期**：2026-09-01 至 **2026-12-01 中午 12:00（香港时间）**，逾期不收。
   - **待遇**：月津贴 **HK$28,700**（每年 HK$344,400），另有每年 **HK$14,400** 会议 / 研究旅费津贴，最长 3 年。
   - **学校加码**：HKU 对 4 年制博士把资助延到第 4 年，并另发奖励金（第一年 HK$40,000，其后每年 HK$20,000）。
   - **双重申请**：仍需同时向目标大学提交申请，部分学校的截止日与 HKPFS 相同或非常接近。
   - **来源**：PolyU 2026-09-04 新闻；津贴细节来自第三方汇总，请以 RGC 官网 rgc.edu.hk/hkphd 为准。
   - **离截止只有不到 8 周**，现在就要套磁并准备材料。
2. **香港各校自己的轮次**：不走 HKPFS 的常规轮次截止较晚（各校、各系不同，待核实）。很多组的名额会在 HKPFS 轮次前通过套磁锁定，建议 **10–11 月** 联系导师。
3. **HKUST(GZ) 是内地校区**：学位由 HKUST 授予，但读书、生活、签证都在广州，津贴标准与香港本部不同（待核实）。不要把它当作“香港 PhD”申请。
4. **AISG PhD Fellowship（AI Singapore）**
   - **待遇**：月津贴最高 **S$6,700**，另有津贴，全额学费，最长 4 年，可在 NUS/NTU/SMU/SUTD 就读。
   - **申请方式**：采用**提名制**，不能直接向 AISG 申请，须由所读大学推荐（在读博士 2 年以内也可被提名）。
   - **服务义务**：据 NUS 页面，非新加坡公民 / 永久居民的获奖者需在新加坡本地公司服务 **2 年**。
   - **时间窗口**：最近一期指南（2026-02-05 版）对应 **2026 年 8 月入学**，已关闭；**2027 年入学的窗口尚未公布**。
5. **NUS Research Scholarship（2026-01-01 起）**
   - **月津贴**：公民 S$3,800 / 永久居民 S$3,400 / **国际生 S$3,000**。
   - **QE 加薪**：通过资格考试（QE）后每月最多加 S$500。加薪期限说法不一：官方条款写到第 48 个月，计算学院页面写“两年”，请向院系确认。
   - **期限**：奖学金一年一续，博士最长 4 年。
   - **另有更高档的奖学金**：President's Graduate Fellowship、A*STAR ACIS / AGS 等，金额以官方页面为准。
6. **NTU Research Scholarship**
   - **津贴**：津贴表于 2026 年 1 月修订，但官方具体数字本次没有取到。第三方给出 S$2,900–3,800/月（按国籍不同），QE 后另加 S$500，**待核实**。
   - **期限与条件**：博士最长 4 年，**无服务约束**。申请博士时在表中勾选即可申请奖学金。
   - **NPGS**：更高档的 Nanyang President's Graduate Scholarship，AY2026-27 窗口为 2026-06-01 至 07-31，已关闭。
7. **学制差异**
   - **香港**：HKPFS 按 3 年设计（有硕士入学）。本科直博一般 4 年，例如 HKU 为 4 年制学生延长资助。
   - **新加坡**：NUS/NTU 奖学金按最长 4 年设计，第一年有课程和 QE；入学后再确定导师的情况更常见，因院系而异（待核实）。
   - **津贴**：港方 HKPFS 的津贴明显高于新加坡普通研究奖学金；AISG Fellowship 与之相当，但有服务义务。
8. **套磁节奏**：青年教师（May Fung、Yuyu Luo、Yang Deng、Weiyang Liu）通常回复更积极。资深大组（Chua、Bo An、Wee Sun Lee、David Lo）可能要先经组内博后或高年级学生筛选。

---

## 六、需要你自己核实的事项

- [ ] **每位 PI 2026/27 是否招生**：本表全部标“未知”，请看各人主页的 “Prospective students” 或直接发邮件询问。
- [ ] **职称和入职年份**：
  - 以下几位是否属于 2022–2026 年入职（决定是否算“青年教师”）：Tao Yu、Junxian He、Binhang Yuan、Chao Huang、Michael Shieh。
  - Lingpeng Kong 是否已晋升。
  - 具体职称待核实：Chuan Wu、Abhik Roychoudhury、Wee Sun Lee、Min-Yen Kan、Zhijiang Guo、Xuming Hu、Xiao-Ming Wu、Yu Cheng、Mike Shou。
- [ ] **论文作者归属**：
  - AI-Researcher（arXiv 2505.18705）是否包含 Chao Huang。
  - AReaL 是否包含 Binhang Yuan。
  - Co-reward 是否包含 Bo Han。
  - GEM 是否包含 Michael Shieh、Wee Sun Lee（目前依据是第三方索引）。
  - Yu Cheng 名下 ICML 2025 agent 论文的题目；Xiangyu Zhao 2026 年 tool-use agent 论文的题目。
  - Jun Sun 的 ConTested 题目和 ICSE 论文年份；Yang Liu 的 ASE 2025 / ICSE 2026 论文题目（来自 researchr 页面）。
  - AFlow 的会议与年份，以及 Yuyu Luo 在其中的角色。
- [ ] **Weiyang Liu**：FormalMATH 中他的署名是 MPI-IS，需要确认他在 CUHK 的入职时间和实验室网址。
- [ ] **单位冲突**：Soujanya Poria 和 Wei Lu（NTU 还是 SUTD）、Chengwei Qin（是否在 HKUST(GZ)）、Xiaowen Chu（是否已正式在 HKUST(GZ)）、Luu Anh Tuan（当前单位）。
- [ ] **Ilya Sergey 组是否接收 LLM 方向的学生**：检索到的工作全是纯形式化方法。
- [ ] **Min-Yen Kan**：方向 (2) 的证据来自学生的学位论文，请确认他本人是否继续带这个方向。
- [ ] **奖学金**：
  - HKPFS 金额请以 RGC 官网为准（目前部分来自第三方汇总）。
  - AISG 2027 窗口何时开放。
  - NTU 2026 年官方津贴表。
  - NUS QE 加薪的期限。
- [ ] **SUTD**：两轮都没有确认符合条件的 PI。

---

## 七、来源列表

**HKU**
- https://www.xlang.ai/
- https://eu.36kr.com/en/p/3422013601860997
- https://nlp.stanford.edu/seminar/details/taoyu_2024.shtml
- https://hku.hk/press/news_detail_28160.html
- https://arxiv.org/pdf/2505.18705
- https://arxiv.org/html/2409.19256v1
- https://seed.bytedance.com/en/public_papers/hybridflow-a-flexible-and-efficient-rlhf-framework
- https://www.ai.hku.hk/people/academic-staff/pluo ；https://dblp1.uni-trier.de/pid/54/4989-2.html （Ping Luo）
- https://hub.hku.hk/cris/rp/rp02775 ；https://cs.hku.hk/people/academic-staff/lpk （Lingpeng Kong）
- https://talks.cam.ac.uk/talk/index/226255
- https://cs.hku.hk/people/academic-staff/liuqi （Qi Liu）

**HKUST / HKUST(GZ)**
- https://cse.hkust.edu.hk/admin/people/faculty/?a=AI
- https://arxiv.org/pdf/2412.17256 ；https://proceedings.iclr.cc/paper_files/paper/2025/hash/c8db30c6f024a3f667232ed7ba5b6d47-Abstract-Conference.html
- https://seng.hkust.edu.hk/news/20251210/prof-may-fung-and-alumna-dr-wang-yaqing-selected-aaai-new-faculty-highlights-program
- https://www.alphaxiv.org/@yi-r-fung
- https://calendar.hkust.edu.hk/node/39051
- https://arxiv.org/pdf/2510.12633
- https://cse.hkust.edu.hk/ai-formal/
- https://cse.hkust.edu.hk/ai-formal/2025fm/weiyang.html
- https://proceedings.iclr.cc/paper_files/paper/2025/hash/fceedf8c9c0ff51f41b9fe0294ef0070-Abstract-Conference.html
- https://dblp1.uni-trier.de/pid/43/6147.html
- https://ait.hkust-gz.edu.cn/?p=3690
- https://dblp.org/pid/262/3664
- https://arxiv.org/pdf/2602.04261 ；https://www.alphaxiv.org/@yuyu-luo ；https://dsa.hkust-gz.edu.cn/zh/blog/2026/07/20/llm-agents-for-data-science-workflows-a-survey-on-data-processing-analysis-andreliable-execution/ （Yuyu Luo）
- https://cse.hkust.edu.hk/~yqsong/ （Yangqiu Song）
- https://www.comp.hkbu.edu.hk/~chxw/home.htm ；https://mlanthology.org/authors/c/chu-xiaowen/ （Xiaowen Chu）

**CUHK**
- https://arxiv.org/abs/2505.02735v1
- https://www.alphaxiv.org/@zhouliang-yu
- https://www.cse.cuhk.edu.hk/people/faculty/yu-cheng/
- https://mlanthology.org/authors/c/cheng-yu/
- https://dblp1.uni-trier.de/pid/l/MichaelRLyu.html ；https://www.cse.cuhk.edu.hk/lyu/students/fyp （Michael Lyu）
- https://www.cse.cuhk.edu.hk/~byu/bio.html （Bei Yu）
- https://www.inns.org/assets/Irwin%20King%20CV%20202509%202%20pages.pdf （Irwin King）
- https://researchr.org/publication/0036PWZSL0YRZ025 （MathCoder-VL）
- https://www.cse.cuhk.edu.hk/~sinnopan/
- https://saasweb.hku.hk/seminar/2025/20250530.php

**PolyU / CityU / HKBU**
- https://www4.comp.polyu.edu.hk/~csxmwu/
- https://theses.lib.polyu.edu.hk/handle/200/14657
- https://www.polyu.edu.hk/comp/people/academic-staff/prof-li-wenjie-maggie/ ；https://preview.aclanthology.org/setup/2025.coling-main.254 ；https://www4.comp.polyu.edu.hk/~cswjli （Wenjie Li）
- https://proceedings.mlr.press/v235/liu24bs.html
- https://cis.taskforce.ieee.org/esco/webinar-series/esco-webinar-26/
- https://scholars.cityu.edu.hk/en/persons/xianzhao/
- https://dblp.uni-trier.de/pid/08/890-1.html
- https://www.cityu.edu.hk/stfprofile/songlinqi.htm
- https://datascience.hku.hk/2025/11/hku-ids-scholar-seminar-series-21/
- https://interdisciplinary-research.hkbu.edu.hk/people/jing-ma ；https://huggingface.co/HKBU-NLP （Jing Ma）

**NUS**
- https://comp.nus.edu.sg/bytes/prof-chua-tat-seng-iclr-2025
- https://www.comp.nus.edu.sg/features/ai-without-side-effects-alphaedit/
- https://media.iclr.cc/Conferences/ICLR2025/ICLR2025_Outstanding_Paper_Awards.pdf
- https://www.scai.gov.sg/2025/participants-of-scai-2025/bryan-low/
- https://www.nus.edu.sg/about/management/bryan-low
- https://arxiv.org/html/2506.15841v1
- https://www.comp.nus.edu.sg/bytes/phd-student-wins-2025-best-paper-award-at-neurips-2025
- https://arxiv.org/html/2506.24119v3 ；https://iclr.cc/virtual/2026/poster/10011289 ；https://mlanthology.org/authors/l/lee-wee-sun/ （Wee Sun Lee、GEM）
- https://wing.comp.nus.edu.sg/author/yuxi-xie/ ；https://wing.comp.nus.edu.sg/people ；https://www.comp.nus.edu.sg/~kanmy/research.html （Min-Yen Kan）
- https://wing.comp.nus.edu.sg/project/selfadaptation （Kawaguchi 相关项目）
- https://arxiv.org/pdf/2505.19475 （VDS-TTT，经核实非 NUS 论文）
- https://www.comp.nus.edu.sg/news/how-nus-computing-research-became-the-technology-behind-sonars-globally-launched-ai-remediation-agent/
- https://arxiv.org/abs/2408.02232v4
- https://www.comp.nus.edu.sg/bytes/associate-professor-ilya-sergey-and-team-win-distinguished-paper-award-at-cav-2026/
- https://ilyasergey.net/
- https://arxiv.org/html/2411.17465v1
- https://ai.comp.nus.edu.sg/index.html
- https://www.comp.nus.edu.sg/~youy/index_files/CV.pdf
- https://www.comp.nus.edu.sg/cs/people/mshieh ；https://wing.comp.nus.edu.sg/author/michael-qizhe-shieh/
- https://ids.nus.edu.sg/people-faculty.html
- https://nusgs.nus.edu.sg/thesis-advisors/dcsnght （Hwee Tou Ng）
- https://comp.nus.edu.sg/cs/bio/reza （Reza Shokri）
- https://jmlr.org/tmlr/papers/bib/sySqlxj8EB.bib （Xinchao Wang）
- https://wing.comp.nus.edu.sg/author/soujanya-poria/

**NTU / SMU / SUTD**
- https://www.ntu.edu.sg/ias/news-events/news/detail/from-algorithmic-and-reinforcement-learning-based-to-llm-powered-agents-by-prof-bo-an
- https://personal.ntu.edu.sg/boan/
- https://conf.researchr.org/profile/ase-2025/yangliu ；https://conf.researchr.org/profile/fse-2026/yangliu ；https://encs.hit.edu.cn/2025/0831/c21303a381565/page.htm （Yang Liu）
- https://arxiv.org/abs/2310.19046v1 （Ong，2023）
- https://faculty.smu.edu.sg/profile/deng-yang-7801
- https://computing.smu.edu.sg/sites/scis.smu.edu.sg/files/2026-02/ydeng-CV.pdf
- https://conf.researchr.org/profile/issta-2025/junsun
- https://conf.researchr.org/profile/ase-2025/davidlo ；https://conf.researchr.org/profile/davidlo ；https://events.csiro.au/Events/2025/August/7/Efficient-and-Green-Code-LLMs （David Lo）
- https://comp.anu.edu.au/people/jing-jiang/ ；https://comp.anu.edu.au/news/2026/06/09/acl-vp-elect-jing-jiang-will-help-steer-the-future-of-natural-language-processing/ （Jing Jiang 已去 ANU）
- https://www.sutd.edu.sg/profile/soujanya-poria ；https://sutd.edu.sg/achievements-listing/congratulations-to-assistant-professor-soujanya-poria-for-receiving-the-2024-ieee-cis-outstanding-early-career-award
- https://sutd.edu.sg/profile/lu-wei ；https://www.alphaxiv.org/@wei-lu （Wei Lu）
- https://ipie.info/scientists/roy-ka-weilee （Roy Ka-Wei Lee）

**奖学金 / 申请**
- https://www.polyu.edu.hk/ls/news-and-events/news/2026/20260904_hkpfs-202728/ （HKPFS 2027/28 截止日期与年度津贴）
- https://opportunitiesforyouth.org/2026/09/08/hong-kong-phd-fellowship-scheme-2027-28-hk344400-annual-stipend-for-international-phd-students-in-hong-kong/ （第三方汇总，津贴细节）
- https://aisingapore.org/research/phd-fellowship/
- https://aisingapore.org/wp-content/uploads/2026/02/2-AISG-Research-PhD-Fellowship-Application-Guideline_Aug-2026-Intake_IHL_v2.pdf
- https://nusgs.nus.edu.sg/scholarships/ai-singapore-scholarship
- https://nusgs.nus.edu.sg/nus-research-scholarship-terms-conditions
- https://comp.nus.edu.sg/financial-support/graduate-scholarships
- https://ntu.edu.sg/admissions/graduate/financialmatters/scholarships/rss
- https://www.ntu.edu.sg/admissions/graduate/scholarships/npgs
