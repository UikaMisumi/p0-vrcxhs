# 美国学术界课题组清单：LLM 持续学习 / 测试时训练 & LLM 智能体 / 智能体系统

> 面向：ML/NLP 背景的博士申请者
> 检索日期：2026-10-08（约 40 次 WebSearch；WebFetch 未使用，以下信息全部来自检索结果摘要中的页面）
> 使用前必读：
> - 每位 PI 至少有一个 2024–2026 的来源能同时说明 (a) 当前在美国高校任职、(b) 确实在做相关方向。凡是来源冲突、单位证据早于 2025 年或只有间接证据的，都标了"(单位待核实)"或"(待核实)"。
> - "招生信号"一栏：只有找到写明 Fall 2026/2027 招生的来源时才会写"招生中"。本轮**没有**找到任何此类来源，所以全部为"未知"。
> - "青年教师"指 2022–2026 年间入职的助理教授。凡是入职年份或当前职称没有在来源里直接看到的，都标了"待核实"。
> - 论文标题都在检索结果里出现过。会议或年份没能确认的已单独注明。

---

## 一、持续学习 / 测试时训练（TTT）/ 测试时记忆 / 知识编辑

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 相关方向关键词 | 1-2 项 2024-2026 代表工作（标题 + 会议/年份） | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Yoon Kim | MIT EECS / CSAIL | 职称待核实（助理或副教授） | 自适应 LLM（self-editing）、测试时训练、高效序列模型 | 《Self-Adapting Language Models》(SEAL)，NeurIPS 2025；《The Surprising Effectiveness of Test-Time Training for Few-Shot Learning》，ICML 2025 | https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b41e04c41726e2a60e456d0a2b961ab-Abstract-Conference.html ; https://proceedings.mlr.press/v267/akyurek25a.html | 未知 | 高：纯 NLP/LLM 方法组，SEAL 就是"模型自己生成微调数据并更新权重"的典型代表 |
| Pulkit Agrawal | MIT EECS / CSAIL（Improbable AI Lab） | 职称待核实 | 自适应 LLM、RL、持续学习 | SEAL（同上，NeurIPS 2025，通讯作者之一） | https://alphaxiv.org/abs/2506.10943 | 未知 | 中：组里主线偏机器人与 RL，LLM 自适应是新方向；有 RL 经验更合适 |
| Jacob Andreas | MIT EECS / CSAIL | 职称待核实 | 测试时训练、语言模型的学习与推理 | 《The Surprising Effectiveness of Test-Time Training for Few-Shot Learning》，ICML 2025（ARC / BBH 上的 TTT） | https://proceedings.mlr.press/v267/akyurek25a.html | 未知 | 高：NLP 核心组，TTT 和 in-context learning 方向都对口 |
| Tatsunori Hashimoto | Stanford CS | 职称待核实 | TTT 层、长上下文、LM 训练 | 《Learning to (Learn at Test Time): RNNs with Expressive Hidden States》，ICML 2025 Spotlight（联合指导） | https://icml.cc/virtual/2025/poster/43617 ; https://profiles.stanford.edu/314034?tab=bio（Yu Sun 的 Stanford 页面写明由 Guestrin / Hashimoto / Koyejo 联合 host） | 未知 | 高：Stanford NLP 核心组，TTT 层系列论文的联合指导者之一 |
| Sanmi Koyejo | Stanford CS | 职称待核实 | TTT 层、可信 ML、评测 | 同上（TTT 层，ICML 2025，联合指导） | https://arxiv.org/html/2407.04620v4 ; https://profiles.stanford.edu/314034?tab=bio | 未知 | 中：组里方向较广（评测、可信 ML），TTT 是合作项目之一 |
| Carlos Guestrin | Stanford CS | 教授（职称待核实） | TTT 层、ML 系统 | 同上（TTT 层，ICML 2025，联合指导） | https://arxiv.org/html/2407.04620v4 ; https://profiles.stanford.edu/314034?tab=bio | 未知 | 中：偏 ML 与系统，适合想做 TTT 架构和训练效率的人 |
| Xiaolong Wang | UC San Diego ECE/CSE | 职称待核实 | TTT 层、测试时训练（视觉 + 序列建模） | TTT 层论文，ICML 2025 Spotlight（论文中署名 UCSD，联合指导） | https://icml.cc/virtual/2025/poster/43617 ; https://arxiv.org/html/2407.04620v4 | 未知 | 中：组里主线是视觉和机器人，TTT 是重要分支；纯 NLP 背景需要补 CV |
| Thomas (Tom) Hartvigsen | University of Virginia, School of Data Science | 助理教授，**青年教师**（2023 年加入 UVA） | 终身/持续模型编辑（lifelong model editing）、知识更新、变化环境下的可靠 AI | 《WikiBigEdit》终身知识编辑基准（arXiv 2503.05683, 2025，合作者）；《Efficient knowledge editing via minimal precomputation》（arXiv 2506.04226, 2025，合作者）。早期代表作 GRACE 是 NeurIPS 2023 之前的工作 | https://api.dsi.virginia.edu/sites/default/files/2025-09/Hartvigsen%20CV_2025.pdf ; https://languagescience.umd.edu/events/clip-talk-tom-hartvigsen | 未知 | 高：知识编辑和持续编辑是本组主线，学校不在 top-4，竞争相对小 |
| Mengye Ren | NYU Courant CS & Center for Data Science（Agentic Learning AI Lab） | 助理教授，**青年教师**（入职年份待核实，约 2022–23） | 持续学习、LLM 的记忆与遗忘、部署后持续学习、测试时学习 | 《Are LLMs Prescient? A Continuous Evaluation using Daily News…》，ICML 2025；《SkillFactory: Self-Distillation for Learning Cognitive Behaviors》，ICLR 2026（以上取自 mlanthology 索引，标题需核对完整版） | https://cds.nyu.edu/team/mengye-ren ; https://mlanthology.org/authors/r/ren-mengye/ ; https://www.bu.edu/cise/cise-seminar-mengye-ren-new-york-university/ | 未知 | 高：实验室就以"持续学习的智能体"命名，与本方向高度一致 |
| Bing Liu | University of Illinois Chicago (UIC) CS | Distinguished Professor | 持续/终身学习、LLM 持续学习、灾难性遗忘 | 《Continual Learning Using Only Large Language Model Prompting》，COLING 2025；《In-context Continual Learning Assisted by an External Continual Learner》，COLING 2025 | https://computing.smu.edu.sg/newsletter/research-seminar-liu-bing-achieving-upper-bound-accuracy-continual-learning（2025-01，写明 UIC） ; https://preview.aclanthology.org/setup/2025.coling-main.487 ; https://icml.cc/virtual/2026/75703 | 未知 | 中-高：持续学习领域的资深 PI，NLP 出身；非 top-4，组风格偏理论加方法 |
| Xiang Ren | USC CS（INK Lab） | 职称待核实 | LM 微调遗忘的预测与缓解、知识更新 | 《Demystifying Language Model Forgetting with Low-rank Example Associations》（arXiv 2406.14026；NeurIPS 2025 poster 页面可查，另有 ICML 2025 列表，**会议待核实**） | https://inklab.usc.edu/lm-forgetting-prediction/ ; https://neurips.cc/virtual/2025/poster/115530 | 未知 | 高：NLP 组，直接研究 LLM 持续微调中的遗忘 |
| Jundong Li | University of Virginia ECE / CS / School of Data Science | 职称待核实 | LLM 知识编辑、图学习 | 《Knowledge Editing for Large Language Models: A Survey》，ACM Computing Surveys 57(3), 2025 | https://dblp.org/pid/144/7997 ; https://arxiv.org/pdf/2310.16218 | 未知 | 中：知识编辑是本组 LLM 方向之一，但组的主线偏图学习/数据挖掘 |
| Yu Su | Ohio State University CSE（OSU NLP Group） | 职称待核实 | LLM 长期记忆、非参数持续学习、智能体记忆（也见第二部分） | 《From RAG to Memory: Non-Parametric Continual Learning for Large Language Models》(HippoRAG 2)，ICML 2025 | https://proceedings.mlr.press/v267/gutierrez25a.html ; https://icml.cc/virtual/2025/poster/45585 | 未知 | 高：NLP 组，"LM 长期记忆"与"智能体"两个方向都有，非 top-4 但实力强 |
| Yoav Artzi | Cornell University CS / Cornell Tech | 职称待核实（2022 年资料为副教授） | 从部署交互中学习、利用用户隐式反馈持续学习 | 《Retrospective Learning from Interactions》(ReSpect)，arXiv 2410.13852（v2 为 2025-05，**会议待核实**） | https://yoavartzi.com/ ; https://arxiv.org/html/2410.13852v2 | 未知 | 高：NLP 组，"learning from deployment experience"最直接的学术代表之一 |
| Sewon Min | UC Berkeley EECS | 助理教授，**青年教师**（2025 年秋入职） | 非参数/模块化 LM、可插拔数据与参数、知识存储 | 《FlexOlmo: Open Language Models for Flexible Data Use》，arXiv 2507.07024（2025，合作者） | https://www2.eecs.berkeley.edu/Faculty/Homepages/sewonmin.html ; https://engineering.berkeley.edu/?p=50560 | 未知 | 中-高：NLP 背景完全匹配；与"持续学习"的关系是可增删的模块化知识，不是传统 CL |
| Akari Asai | Carnegie Mellon University LTI | 助理教授，**青年教师**（Fall 2026 起，**入职状态待核实**） | 检索增强 LM、参数化与非参数化知识、LM 知识更新 | 2024–2026 具体代表作本轮未逐篇核实（主线是 RAG / 自反思检索 / 科研文献 LM，**待核实**） | https://lti.cs.cmu.edu/people/faculty/index.html ; https://www.lti.cs.cmu.edu/news-and-events/news/2025-09-12-asai-35-under-35.html | 未知 | 中：NLP 完全匹配，但更偏 RAG / 外部记忆，不是权重层面的持续学习 |

> 交叉相关：Huaxiu Yao（UNC）的 SkillRL / MetaClaw（部署期从交互中学习、空闲时微调）也属于"从部署经验中学习"，列在第二部分。

---

## 二、LLM 智能体（ML/NLP 视角）+ 智能体系统基础设施

| 姓名（英文） | 学校 / 院系 | 职称（青年教师标注） | 相关方向关键词 | 1-2 项 2024-2026 代表工作（标题 + 会议/年份） | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Graham Neubig | CMU LTI | 职称待核实 | 代码/软件智能体、Web 智能体、智能体记忆、开源智能体平台 | 《Agent Workflow Memory》，ICML 2025；《OpenHands: An Open Platform for AI Software Developers as Generalist Agents》，ICLR 2025 | https://proceedings.mlr.press/v267/wang25bx.html ; https://proceedings.iclr.cc/paper_files/paper/2025/hash/a4b6ad6b48850c0c331d1259fc66a69c-Abstract-Conference.html | 未知 | 高：NLP 核心组，智能体方向最活跃的学术组之一（注意他同时在 All Hands AI 任职） |
| Daniel Fried | CMU LTI | 助理教授（入职年份待核实） | Web 智能体、代码生成、智能体记忆 | 《Agent Workflow Memory》，ICML 2025（合作者） | https://proceedings.mlr.press/v267/wang25bx.html | 未知 | 高：NLP 组，Web 和代码智能体 |
| Karthik Narasimhan | Princeton CS | 职称待核实 | 软件工程智能体、智能体基准与可靠性 | 《τ-bench》（ICLR 2025，**会议信息来自 wiki，待核实**）；SWE-agent（NeurIPS 2024，**待核实**）；2025 年 Schmidt Sciences 资助的 SWE 智能体可靠性项目 | https://www.schmidtsciences.org/grantee/karthik-narasimhan/ ; https://aiwiki.ai/wiki/tau-bench/raw | 未知 | 高：NLP 和 RL 出身，SWE-bench / SWE-agent 系列（2023–25 曾任 Sierra 研究负责人） |
| Huan Sun | Ohio State University CSE | 职称待核实 | Web / 计算机使用智能体（CUA）、科研智能体、智能体安全与评测 | 《ScienceAgentBench》，ICLR 2025；《EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage》，ICLR 2025 | https://engineering.osu.edu/news/2025/05/huan-sun-joins-10m-ai-safety-science-initiative ; https://nlp.stanford.edu/seminar/details/huan_sun_2026.shtml ; https://dblp1.uni-trier.de/pid/33/2952-1.html | 未知 | 高：NLP 组，评测、安全和 CUA 都做，非 top-4 |
| Yu Su | Ohio State University CSE | 职称待核实 | 智能体记忆、Web 智能体（Mind2Web 系列） | HippoRAG 2（ICML 2025，见第一部分）；2024–26 的 Web 智能体具体论文本轮未核实（**待核实**） | https://proceedings.mlr.press/v267/gutierrez25a.html | 未知 | 高：同时覆盖本清单的两个主题 |
| Aviral Kumar | CMU CSD & MLD | 助理教授，**青年教师**（入职年份待核实，约 2024） | 面向 LLM 智能体的多轮 RL、自我纠错、设备控制智能体 | 《Training Language Models to Self-Correct via Reinforcement Learning》，ICLR 2025；Digi-Q（设备控制智能体的 Q 函数训练），ICLR 2025 | https://ai2050.schmidtsciences.org/?p=916 ; https://mlanthology.org/authors/k/kumar-aviral/ | 未知 | 中-高：RL 色彩很重，NLP 背景需要补 RL 理论 |
| Sergey Levine | UC Berkeley EECS | 职称待核实 | 智能体的 RL 训练、设备控制 / GUI 智能体 | 《DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning》，NeurIPS 2024 | https://neurips.cc/virtual/2024/poster/96658 ; https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-43.html | 未知 | 中：组很大，主线是机器人 RL，LLM 智能体只是一部分，竞争极激烈 |
| Manling Li | Northwestern University CS | 助理教授，**青年教师**（AAAI 2025 New Faculty Highlights） | 智能体的多轮 RL（RAGEN / VAGEN）、具身智能体评测、世界模型 | 《EmbodiedBench》，ICML 2025 Oral；《RAGEN-2: Reasoning Collapse in Agentic RL》，ICML 2026 Oral（据实验室主页）；VAGEN，NeurIPS 2025 | https://www.mll.lab.northwestern.edu/ ; https://hg.gatech.edu/node/688451 | 未知 | 高：NLP 出身（UIUC Heng Ji 组），智能体 RL 正是热点；非 top-4 |
| Xin (Eric) Wang | UC Santa Barbara CS（此前在 UCSC） | 助理教授（2026 年来源；不在 2022–26 入职区间，原因是从 UCSC 转来） | 计算机使用智能体（Agent S）、多模态智能体 | 《Agent S: An Open Agentic Framework that Uses Computers Like a Human》，ICLR 2025 | https://www.ece.ucsb.edu/events/all/2026/ece-seminar-series-feb-20-fri-200pm-building-ai-agents-reason-act-and-evolve-xin | 未知 | 中-高：NLP 加多模态；注意他同时任 Simular 研究负责人 |
| Jiaxuan You | UIUC CS | **青年教师**（2024-09 起，职称待核实） | 多智能体协作与评测、自我进化的多智能体、科研模拟 | 《MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents》，ACL 2025 | https://preview.aclanthology.org/setup/2025.acl-long.421 ; https://courses.grainger.illinois.edu/CS598JY2 ; https://www.alphaxiv.org/@jiaxuan-you | 未知 | 高：开设 LLM Agents 专题课，组新、扩张中；非 top-4 |
| Prithviraj (Raj) Ammanabrolu | UC San Diego CSE（PEARLS Lab） | 助理教授，**青年教师**（入职年份待核实） | RL + NLP 的交互式语言智能体、世界模型、人类反馈 | 2024–26 的具体论文标题本轮未确认（**待核实**）；2024-11 Stanford NLP 讲座的主题是从人类反馈中学习世界模型的 RL 智能体 | https://jacobs.ucsd.edu/people/profile/raj-ammanabrolu ; https://nlp.stanford.edu/seminar/details/rajammanabrolu_2024.shtml | 未知 | 高：NLP 与 RL 交叉，正好匹配"RL for agents"（行业兼职的来源有冲突） |
| Alane Suhr | UC Berkeley EECS | 助理教授，**青年教师**（入职年份待核实） | 交互式语言智能体、从人类交互中训练智能体、智能体评测 | ICML 2025 Computer Use Agents Workshop 受邀报告《Training Language-Conditioned Agents with Reinforcement Learning》；2025 年具体论文**待核实** | https://www2.eecs.berkeley.edu/Faculty/Homepages/suhr.html ; https://icml.cc/virtual/2025/50097 | 未知 | 高：NLP 组（Artzi 学生），同时契合"从部署交互中学习" |
| Omar Khattab | MIT EECS / CSAIL | 助理教授，**青年教师**（2025 年秋入职） | 复合 AI 系统 / LM 程序优化（DSPy）、提示与流程优化（GEPA）、检索 | DSPy 系列；GEPA（**具体会议待核实**） | https://www.eecs.mit.edu/people/omar-khattab/ ; https://www.csail.mit.edu/person/omar-khattab | 未知 | 高：NLP 和 IR 出身，"智能体程序"抽象层面的代表人物（同时任 Databricks 研究科学家） |
| Azalia Mirhoseini | Stanford CS（Scaling Intelligence Lab） | 助理教授，**青年教师**（入职年份待核实） | 自我改进 AI 系统、代码/内核智能体、推理时扩展 | 《KernelBench: Can LLMs Write Efficient GPU Kernels?》，ICML 2025；《Astra: A Multi-Agent System for GPU Kernel Performance Optimization》，arXiv 2509.07506（2025） | https://profiles.stanford.edu/azalia-mirhoseini ; https://proceedings.mlr.press/v267/ouyang25a.html | 未知 | 中：偏系统和代码；**注意**她的 Stanford 主页写着共同创办 Ricursive Intelligence，可能影响带学生的精力 |
| Huaxiu Yao | UNC Chapel Hill CS（兼 School of Data Science and Society） | 助理教授，**青年教师** | 自我进化智能体、Web 智能体、从部署交互中持续学习（SkillRL / MetaClaw） | 《Adapting Web Agents with Synthetic Supervision》（arXiv 2025-11，**会议待核实**）；SkillRL / MetaClaw（2026 RIKEN 讲座摘要提及，**年份与会议待核实**） | https://aip.riken.jp/?p=22473 ; https://dblp.org/pid/197/1635 | 未知 | 高：同时覆盖两个主题，非 top-4，组规模大、产出多 |
| Ion Stoica【偏系统】 | UC Berkeley EECS（Sky Computing Lab） | 教授（职称待核实） | 智能体服务引擎、程序级调度、LLM serving（vLLM 生态） | 《Autellix: An Efficient Serving Engine for LLM Agents as General Programs》，arXiv 2502.13965（2025） | https://arxiv.org/abs/2502.13965 | 未知 | 中：需要较强的系统背景；纯 ML/NLP 背景的人建议走与 Gonzalez 联合指导的路线 |
| Joseph E. Gonzalez【偏系统】 | UC Berkeley EECS | 职称待核实 | 智能体服务、工具调用（Gorilla / BFCL）、LLM 系统 | Autellix（同上，2025）；BFCL 函数调用评测（**具体会议待核实**） | https://arxiv.org/abs/2502.13965 | 未知 | 中-高：工具使用评测对 NLP 背景友好，serving 部分偏系统 |
| Junchen Jiang【偏系统】 | University of Chicago CS（LMCache Lab） | 副教授（来源：Heavybit 播客简介；同时任 Tensormesh CEO） | KV cache 层、跨请求上下文复用、支撑复杂智能体的推理基础设施 | 《CacheBlend》，EuroSys 2025 Best Paper；具体面向智能体的论文**待核实** | https://computerscience.uchicago.edu/news/cacheblend-university-of-chicagos-game-changer-in-ai-speed-and-precision ; https://www.heavybit.com/library/podcasts/lab-notes/ep-4-the-new-big-data-of-inference-with-junchen-jiang | 未知 | 低-中：典型的网络/系统组，与智能体的关系在基础设施层 |

### 单位存疑或证据不足、未列入主表的人选（**不要直接据此联系**）

- **Shuyan Zhou**（WebArena 作者）：Duke Scholars 页面显示她是 Duke CS 助理教授（2025 至今），另一个 Duke 页面写的是 Adjunct；但 2026-09 的 36kr / 量子位报道称她已离开学术界、加入 Meta Superintelligence Labs。**(单位待核实)**，来源：https://scholars.duke.edu/person/shuyan.zhou ; https://eu.36kr.com/zh/p/3992329241656324
- **Yu Sun**（TTT 方法的提出者）：检索到的最新资料仍是 Stanford 博士后兼 NVIDIA 研究员，没有找到他担任教职的来源，因此**不是 PI**。要做 TTT，可以联系他的 host（Hashimoto / Koyejo / Guestrin）以及 Xiaolong Wang。来源：https://profiles.stanford.edu/314034?tab=bio
- **Hao Zhang（UCSD HDSI/CSE）、Zhihao Jia（CMU CSD）、Ravi Netravali（Princeton）**：都是 LLM serving 领域的强组，但本轮没有检索到他们 2024–26 年**明确针对智能体 serving 或 RL rollout** 的论文，所以未入表。如果你对系统方向有兴趣，可以自己查他们的主页。来源：https://www.cs.cmu.edu/~zhihaoj2/ ; https://www.cs.princeton.edu/~ravian/netravali_cv.pdf
- **David Bau（Northeastern）**：ROME / MEMIT 是知识编辑的奠基工作，但都在 2022–23 年；2025 年的工作转向可解释性，所以未入表（如果对"编辑 + 可解释性"感兴趣，可以自行核实）。来源：https://www.khoury.northeastern.edu/people/david-bau/
- **Tianyi Zhou（UMD）**：没有检索到能确认其单位和相关工作的来源，未入表。

### 工业界相关实验室（不作为 PI，仅供参考）

- **Google Research / DeepMind**：Titans 式神经长期记忆（Ali Behrouz 等）。
- **NVIDIA Research**：Gated DeltaNet（ICLR 2025，与 MIT 学生合作）、ProRL Agent（智能体 RL rollout 服务，2026 arXiv）、TTT 方向（Yu Sun）。
- **Sierra**（τ-bench）、**All Hands AI**（OpenHands）、**Simular**（Agent S）、**Databricks**（DSPy 相关）、**Microsoft Research**（Web 智能体合成监督，与 UNC 合作）。
- **Meta Superintelligence Labs**、**OpenAI**、**Anthropic**：智能体与持续学习都有大量工作，但不招博士生。

---

## (a) 申请策略建议

- **按"NLP 友好程度"分层投递。** 第一层是纯 NLP 组：Yoon Kim、Jacob Andreas、Graham Neubig、Huan Sun / Yu Su、Yoav Artzi、Xiang Ren、Manling Li、Jiaxuan You。第二层是 NLP 加 RL：Aviral Kumar、Raj Ammanabrolu、Alane Suhr、Karthik Narasimhan。第三层是需要补系统能力的组：Stoica、Gonzalez、Junchen Jiang。
- **重点投"非 top-4 + 青年教师"。** 例如 UVA Hartvigsen、NYU Mengye Ren、Northwestern Manling Li、UIUC Jiaxuan You、UNC Huaxiu Yao、UCSD Ammanabrolu、OSU 双组。青年教师更可能亲自带学生，录取概率也比 MIT/Stanford/Berkeley/CMU 资深组高。
- **把两个主题连起来讲。** "智能体的持续学习 / 从部署经验中学习"（agent memory、self-evolving、learning from interaction）是两个主题的交集，也是 2025–26 年的热点。Artzi、Suhr、Mengye Ren、Huaxiu Yao、Yu Su、Neubig/Fried（AWM）都可以从这个角度写研究陈述。
- **套磁信写具体论文。** 选 1 篇上表中已核实标题的论文（如 SEAL、AWM、HippoRAG 2、ReSpect、RAGEN），写清楚你会怎么扩展它（例如"把 SEAL 的 self-edit 用在智能体轨迹记忆上"）。不要泛泛地说"对持续学习感兴趣"。
- **复现项目最有说服力。** 在 TTT 层、SEAL、HippoRAG 2、AWM 中选 1 个开源仓库，复现并做一个小改进，放进 CV 或 GitHub。
- **注意 PI 的工业界身份。** 好几位 PI 同时在公司任职（Neubig / All Hands、Mirhoseini / Ricursive、Khattab / Databricks、Xin Wang / Simular、Junchen Jiang / Tensormesh、Sewon Min / Ai2），套磁前先看他们的主页或推特，确认还在正常招生。
- **系统方向要单独准备材料。** 如果想走"偏系统"路线（智能体 serving / RL rollout），需要展示 CUDA、分布式或 vLLM / SGLang 源码贡献等经验，纯 NLP 论文对这类组说服力有限。
- **时间线。** Fall 2027 入学的申请多在 2026 年 12 月截止，建议在 10–11 月完成套磁。很多教授会在个人主页或推特发 "I'm recruiting" 帖子，本清单中这一栏全部为"未知"，需要你逐一确认。

## (b) 需要你自己核实的事项

1. **所有"职称待核实"的条目**：对照学校官方 faculty directory 确认当前职称（助理/副/正教授）。晋升不影响能否招生，但会影响你对组规模的预期。
2. **招生信号**：逐一查看个人主页的 "Prospective students" 一节和近期推特/Bluesky，确认 Fall 2027 是否招生。本清单**没有任何一位**被确认为"招生中"。
3. **Akari Asai** 是否已在 2026 年秋正式到 CMU 入职（LTI 页面写的是 "Beginning Fall 2026"）。
4. **Shuyan Zhou** 是否仍在 Duke（与 Meta 的报道冲突）。
5. **标注"会议待核实"的论文**：τ-bench、SWE-agent、ReSpect、Xiang Ren 遗忘论文（ICML 2025 还是 NeurIPS 2025）、GEPA、BFCL、Huaxiu Yao 的 SkillRL / MetaClaw。到 arXiv、OpenReview 或会议官网核对。
6. **Mengye Ren 的论文标题**：取自 mlanthology 自动索引，"Are LLMs Prescient?" 的完整标题需要到 ICML 2025 官网核对。
7. **Raj Ammanabrolu、Alane Suhr、Akari Asai** 的 2024–26 代表作标题本轮没有确认，套磁前请到 Google Scholar 查最新论文。
8. **青年教师入职年份**（Daniel Fried、Aviral Kumar、Alane Suhr、Mirhoseini、Ammanabrolu、Mengye Ren）：以个人主页 CV 为准。
9. 检索工具返回的是摘要（不是原网页全文），个别细节可能有误。联系前请**亲自打开每个 URL** 确认。

## (c) Sources

- SEAL (NeurIPS 2025): https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b41e04c41726e2a60e456d0a2b961ab-Abstract-Conference.html ; https://alphaxiv.org/abs/2506.10943
- TTT for Few-Shot Learning (ICML 2025): https://proceedings.mlr.press/v267/akyurek25a.html ; https://icml.cc/virtual/2025/poster/44773
- TTT layers (ICML 2025): https://icml.cc/virtual/2025/poster/43617 ; https://arxiv.org/html/2407.04620v4
- Yu Sun Stanford profile: https://profiles.stanford.edu/314034?tab=bio
- Hartvigsen CV 2025: https://api.dsi.virginia.edu/sites/default/files/2025-09/Hartvigsen%20CV_2025.pdf ; UMD talk: https://languagescience.umd.edu/events/clip-talk-tom-hartvigsen ; UVA SDS news: https://datascience.virginia.edu/news/departments/166?page=6
- Mengye Ren: https://cds.nyu.edu/team/mengye-ren ; https://mlanthology.org/authors/r/ren-mengye/ ; https://www.bu.edu/cise/cise-seminar-mengye-ren-new-york-university/ ; https://www.alphaxiv.org/@mengye-ren
- Bing Liu: https://computing.smu.edu.sg/newsletter/research-seminar-liu-bing-achieving-upper-bound-accuracy-continual-learning ; https://preview.aclanthology.org/setup/2025.coling-main.487 ; https://arxiv.org/abs/2412.15479v1 ; https://icml.cc/virtual/2026/75703
- Xiang Ren / Xisen Jin: https://inklab.usc.edu/lm-forgetting-prediction/ ; https://neurips.cc/virtual/2025/poster/115530 ; https://icml.cc/virtual/2025/51873
- Jundong Li: https://dblp.org/pid/144/7997 ; https://arxiv.org/pdf/2310.16218
- HippoRAG 2 (ICML 2025): https://proceedings.mlr.press/v267/gutierrez25a.html ; https://icml.cc/virtual/2025/poster/45585
- Yoav Artzi / ReSpect: https://yoavartzi.com/ ; https://arxiv.org/html/2410.13852v2
- Sewon Min: https://www2.eecs.berkeley.edu/Faculty/Homepages/sewonmin.html ; https://engineering.berkeley.edu/?p=50560 ; FlexOlmo: https://arxiv.org/abs/2507.07024
- Akari Asai: https://lti.cs.cmu.edu/people/faculty/index.html ; https://www.lti.cs.cmu.edu/news-and-events/news/2025-09-12-asai-35-under-35.html
- Agent Workflow Memory (ICML 2025): https://proceedings.mlr.press/v267/wang25bx.html
- OpenHands (ICLR 2025): https://proceedings.iclr.cc/paper_files/paper/2025/hash/a4b6ad6b48850c0c331d1259fc66a69c-Abstract-Conference.html
- Karthik Narasimhan: https://www.schmidtsciences.org/grantee/karthik-narasimhan/ ; https://aiwiki.ai/wiki/tau-bench/raw ; https://snorkel.ai/author/karthik-narasimhan/
- Huan Sun: https://engineering.osu.edu/news/2025/05/huan-sun-joins-10m-ai-safety-science-initiative ; https://engineering.osu.edu/news/2025/09/ai-safety-research-attracts-funding-open-philanthropy ; https://nlp.stanford.edu/seminar/details/huan_sun_2026.shtml ; https://dblp1.uni-trier.de/pid/33/2952-1.html
- Aviral Kumar: https://ai2050.schmidtsciences.org/?p=916 ; https://mlanthology.org/authors/k/kumar-aviral/
- DigiRL (NeurIPS 2024): https://neurips.cc/virtual/2024/poster/96658 ; https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-43.html
- Manling Li: https://www.mll.lab.northwestern.edu/ ; https://hg.gatech.edu/node/688451 ; https://www.mccormick.northwestern.edu/computer-science/news-events/news/articles/2024/strong-northwestern-presence-at-the-2024-neurips-conference.html
- Xin Eric Wang: https://www.ece.ucsb.edu/events/all/2026/ece-seminar-series-feb-20-fri-200pm-building-ai-agents-reason-act-and-evolve-xin
- Jiaxuan You: https://preview.aclanthology.org/setup/2025.acl-long.421 ; https://courses.grainger.illinois.edu/CS598JY2 ; https://www.alphaxiv.org/@jiaxuan-you
- Raj Ammanabrolu: https://jacobs.ucsd.edu/people/profile/raj-ammanabrolu ; https://cse.ucsd.edu/node/3026 ; https://nlp.stanford.edu/seminar/details/rajammanabrolu_2024.shtml
- Alane Suhr: https://www2.eecs.berkeley.edu/Faculty/Homepages/suhr.html ; https://icml.cc/virtual/2025/50097 ; https://ee.sonoma.edu/lecture-series/interactive-language-agents-training-evaluation-and-interface
- Omar Khattab: https://www.eecs.mit.edu/people/omar-khattab/ ; https://www.csail.mit.edu/person/omar-khattab ; https://www.cmu.edu/engage/alumni/get-involved/tartansontherise/2025/khattab.html
- Azalia Mirhoseini: https://profiles.stanford.edu/azalia-mirhoseini ; KernelBench: https://proceedings.mlr.press/v267/ouyang25a.html
- Huaxiu Yao: https://aip.riken.jp/?p=22473 ; https://dblp.org/pid/197/1635 ; https://www.microsoft.com/en-us/research/people/baolinpeng/publications
- Autellix: https://arxiv.org/abs/2502.13965 ; https://huggingface.co/papers/2502.13965
- Junchen Jiang: https://computerscience.uchicago.edu/news/cacheblend-university-of-chicagos-game-changer-in-ai-speed-and-precision ; https://www.heavybit.com/library/podcasts/lab-notes/ep-4-the-new-big-data-of-inference-with-junchen-jiang
- Shuyan Zhou（存疑）: https://scholars.duke.edu/person/shuyan.zhou ; https://eu.36kr.com/zh/p/3992329241656324
- Zhihao Jia: https://www.cs.cmu.edu/~zhihaoj2/ ; Ravi Netravali CV: https://www.cs.princeton.edu/~ravian/netravali_cv.pdf ; David Bau: https://www.khoury.northeastern.edu/people/david-bau/
- Gated DeltaNet (NVIDIA, ICLR 2025): https://proceedings.iclr.cc/paper_files/paper/2025/hash/4904fad153f6434a7bcf04465d4be2cc-Abstract-Conference.html
