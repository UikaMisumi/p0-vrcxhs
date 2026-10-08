# 医疗 / 健康 AI（ML/NLP 方向）研究组清单：美国 · 香港 · 新加坡

> 面向：有 ML/NLP 背景、准备申请 PhD 的同学
> 整理日期：2026-10-08
> 检索方式：WebSearch（standard 模式），共成功检索 42 次。WebFetch 对大学官网（如 duke-nus.edu.sg、comp.nus.edu.sg）被网络代理拦截，没法直接打开主页核对。
> **重要限制**：本轮检索额度在开始查新加坡时就用完了（多个 agent 共享上限），所以**新加坡部分没有一条经过本轮检索核实**。新加坡只给出一份"待检索候选名单"，没有放进正式表格。

## 标注说明

- **子方向标签**
  - [A] 临床 NLP / 医疗 LLM（评测、安全、幻觉、临床 agent、医学推理）
  - [B] 多模态医疗基础模型（报告生成、病理 FM、通用医疗 AI）
  - [C] EHR / 时序 / 可穿戴基础模型与临床预测
  - [D] 可信 / 公平 / 监管 ML（部署监测、公平性、因果）
  - [E] 基因组 / 生物 + 语言模型方法（只收 CS 系或 CS 主导的组）
- **证据**
  - ✅：找到 2025–2026 年带日期的来源，能同时说明当前单位和医疗 AI 工作。
  - ⚠️：来源未注明日期、早于 2025 年，或不同来源说法冲突。这类条目标"(单位待核实)"或"(职称待核实)"。
- **系别**：「CS 系」指学生通常读 CS/EECS PhD；「医学院/BMI」指学生通常读生物医学信息学、生物医学数据科学或流行病等 PhD。
- **青年教师**：2022–2026 年起任 Assistant Professor，且来源能证实起始年份。起始年份查不到的不标。
- **招生信号**：只有来源明确写了 2026 或 2027 招生，才标"招生中"，其余一律标"未知"。
- **代表工作**：没有确认到的论文题目、期刊或年份都标"(待核实)"。正文不编造论文题目。

---

## 一、美国（33 人）

| 姓名（英文） | 学校 / 院系（CS 系 or 医学院/BMI） | 职称（青年教师标注） | 子方向标签 + 关键词 | 1–2 项 2024–2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Nigam Shah | Stanford 医学院（Medicine / BMIR），Stanford Health Care 首席数据科学家 — **医学院/BMI** | Professor | [A][C] LLM 真实临床任务评测、医疗系统部署 | ① MedHELM：医疗 LLM 整体评测框架（2025 年 2 月由 HAI 发布；检索结果称发表于 Nature Medicine 2025，期刊待核实）② 医疗 LLM red-teaming 研究，npj Digital Medicine 8:149（2025，合作者） ✅ | https://profiles.stanford.edu/nigam-shah ; https://hai.stanford.edu/news/holistic-evaluation-of-large-language-models-for-medical-applications ; https://dbds.stanford.edu/nigam-shah-which-llm-is-best-for-real-health-care-needs | 未知 | **高**：LLM 评测和部署正是 NLP 背景的强项；可以接触 Stanford 真实临床数据 |
| James Zou | Stanford Biomedical Data Science（courtesy：CS、EE）— **医学院/BMI 为主，可经 courtesy 接触 CS** | Associate Professor（据 2025 年讲座简介，职称待核实） | [A][E][B] 生物医学 AI agent、科学发现 agent、医学影像推理 | ① Virtual Lab：AI 科学家 agent 团队设计新冠 nanobody，并经实验验证 ② CellVoyager（基因组数据分析 agent）、Paper2Agent ✅ | https://ml4mi.wisc.edu/8757-2/ ; https://ysph.yale.edu/event/ai-agents-for-biomedical-discoveries/ | 未知 | **高**：以 LLM/agent 为核心方法，非常适合 NLP 背景 |
| Serena Yeung-Levy | Stanford Biomedical Data Science（MARVL 实验室）— **医学院/BMI** | Assistant Professor（Bio-X 页面可能过时，职称待核实） | [B] 生物医学多模态大模型、手术视频、细胞形态 | ① 关于图像分辨率对生物医学多模态 LLM 影响的论文（MLHC 2025）② CellFlux（ICML 2025）；手术 AI 大视觉语言模型系统评测（arXiv）✅ | https://marvl.stanford.edu/publications.html | 未知 | 中高：偏视觉-语言，有 NLP 背景可以做 VLM 一侧 |
| Roxana Daneshjou | Stanford Dermatology + Biomedical Data Science — **医学院/BMI**（医生科学家） | Assistant Professor（起始年份待核实） | [A][D] LLM red-teaming、安全/偏见、皮肤科 AI | ① 医疗 LLM red-teaming（npj Digital Medicine 8:149, 2025）② 评估聊天式 AI 给出的皮肤癌预防建议是否恰当（JAAD International 2025） ✅ | https://profiles.stanford.edu/roxana-daneshjou ; https://aimi.stanford.edu/grand-rounds/2025-aimi-grand-rounds/july | 未知 | 中高：LLM 安全评测与 NLP 直接相关，但 PhD 学生需要走 BMDS 等项目 |
| Curtis Langlotz | Stanford Radiology / Medicine / BMDS，AIMI 中心主任 — **医学院/BMI** | Professor | [B][A] 放射报告生成、报告生成评测指标 | ① 自动结构化放射报告生成（ACL 2025，Delbrouck 等，合作者）② GREEN 生成报告评测指标（EMNLP 2024） ✅ | https://profiles.stanford.edu/curtis-langlotz ; https://langlotzlab.stanford.edu/ ; https://news.stanford.edu/stories/2025/11/research-matters-curtis-langlotz | 未知 | **高**：报告生成和评测本质上是 NLG 问题 |
| Marzyeh Ghassemi | MIT EECS + IMES（CSAIL、Jameel Clinic）— **CS 系** | Associate Professor | [D][A] 健康 ML 公平性、临床人机交互、可解释性对公平的影响 | 2025-04 讲座 "The Pulse of Ethical ML in Health"（2026-02 在 MIT 再次开讲）；本轮未核实具体 2024–2026 论文题目，请查 Healthy ML 主页 ✅ | https://ilp.mit.edu/node/23481 ; https://wgs.mit.edu/events-all/2026/2/26/the-pulse-of-ethical-machine-learning-in-health | 未知 | **高**：CS PhD，做 LLM 偏见和公平性，与 NLP 背景契合 |
| Regina Barzilay | MIT EECS / CSAIL，Jameel Clinic AI 负责人 — **CS 系** | Professor | [B][E] 癌症风险影像模型、分子/表位预测 | ① MUNIS：CD8+ T 细胞表位预测（Nature Machine Intelligence, 2025-01）② Boltz（开源 AlphaFold3 复现）；2025 IEEE Frances E. Allen Medal ✅ | https://www.csail.mit.edu/news/mit-eecs-professor-regina-barzilay-receives-2025-frances-e-allen-medal ; https://communityjameel.org/news/regina-barzilay-looks-ahead-at-ai-in-cancer-research-and-treatment-in-2025 | 未知 | 中高：NLP 出身，但当前重心在影像和分子 |
| Pranav Rajpurkar | Harvard Medical School DBMI — **医学院/BMI**（Harvard BMI PhD） | Associate Professor | [B][A] 通用医疗 AI、放射学、多模态 + 自然语言、AI agent | ① "Coordinated AI agents for advancing healthcare"（Nature Biomedical Engineering，年份待核实）② AI 辅助对放射科医生影响的异质性研究（Nature Medicine，年份待核实）⚠️ 本轮未查到明确的 2025 年论文 | https://dbmi.hms.harvard.edu/people/pranav-rajpurkar ; https://www.rajpurkarlab.hms.harvard.edu/home | 未知 | **高**：明确融合 CV、NLP 和结构化数据 |
| Marinka Zitnik | Harvard Medical School DBMI — **医学院/BMI** | 职称待核实（检索结果未给出） | [E][A] AI for therapeutics、临床治疗推理 agent、知识图谱 | ① TxAgent：调用 211 个工具做治疗推理的 agent（arXiv 2503.10970, 2025-03）② 后续 "An AI agent for treatment reasoning over a biomedical tool universe"（arXiv 2606.28692，内容待核实）✅ | https://arxiv.org/abs/2503.10970v1 ; https://zitniklab.hms.harvard.edu/jobs | 未知（Jobs 页称"每年招收新 PhD"，未写 2026/2027） | **高**：LLM agent + 工具调用，NLP 背景可以直接上手 |
| Arjun (Raj) Manrai | Harvard Medical School DBMI；NEJM AI 创刊副主编 — **医学院/BMI** | Assistant Professor（DBMI 页面，职称待核实） | [A] LLM 临床推理、医学决策 | 据转载称 2026-04-30 发表于 Science：LLM 在多项临床推理任务上超过医生（与 Adam Rodman 共同通讯）——**仅见论坛转载，待核实** ⚠️ | https://dbmi.hms.harvard.edu/people/arjun-raj-manrai | 未知 | **高**（方向契合），但需要核实最新工作 |
| Faisal Mahmood | Harvard Medical School / Mass General Brigham 病理科 — **医学院** | 职称待核实 | [B] 病理基础模型、病理视觉-语言、报告生成 | ① TITAN：多模态全切片病理基础模型（Nature Medicine 31:3749–3761, 2025）② UNI / CONCH（Nature Medicine 2024） ✅ | https://hms.harvard.edu/news/researchers-design-foundation-ai-models-use-pathology ; https://ai.meta.com/blog/mahmood-lab-human-pathology-dinov2/ | 未知 | 中：以视觉为主，NLP 背景可以切入报告对齐和 copilot 一侧；PhD 招生途径待核实 |
| Danielle Bitterman | Mass General Brigham AIM Program / Brigham 放射肿瘤科（HMS）— **医院/医学院**（医生科学家） | 职称待核实 | [A][D] 临床 NLP、LLM 风险测量（偏见、推理错误）、自动化偏差 | 2025 World Medical Innovation Forum 讲者；2024-11 Harvard CRCS 讲座（LLM 风险测量）；本轮未核实具体 2025 论文 ✅（单位） | https://2025.worldmedicalinnovation.org/speaker/danielle-bitterman-md/ ; https://aim.mgh.harvard.edu/team/danielle-bitterman | 未知 | 方向**高**、结构上中：医院实验室没有自己的 PhD 项目，需要经 Harvard/MIT 项目联合指导（待核实） |
| Monica Agrawal | Duke Biostatistics & Bioinformatics + Computer Science（2024 起）+ BME（2025 起）— **CS 系 / 生统双挂** | Assistant Professor（**青年教师**，2024 起） | [A] 医疗 LLM 真实场景评测、环境式临床记录（ambient scribe）评测、患者用 LLM 查询健康信息 | ① 用对话式 AI 大规模数据集分析用户如何寻求健康信息（Findings of EMNLP 2025）② 用 LLM 促进健康公平（NEJM AI, 2025-01）；"evaluation illusion"（2025，载体待核实） ✅ | https://scholars.duke.edu/person/monica.agrawal ; https://aihealth.duke.edu/2025/09/10/seminar-monica-agrawal/ | 未知 | **高**：纯 NLP 路线，可以走 Duke CS PhD。注意她是 Layer Health 联合创始人 |
| Irene Y. Chen | UC Berkeley EECS + UCSF Computational Precision Health（CPH）— **CS 系**（也可读 CPH PhD） | Assistant Professor（2023-07 入职；**青年教师**以 2022–2026 计） | [D][C][A] 公平临床 ML、EHR、LLM 健康公平审计、分布偏移 | LLM 健康公平审计；"evaluation illusion"（医疗 LLM 评测局限）；本轮未核实具体发表载体 ⚠️（单位待核实：最新带日期来源为 2024-01） | https://www2.eecs.berkeley.edu/Faculty/Homepages/iychen.html ; https://news.berkeley.edu/2024/01/16/meet-our-new-faculty-irene-chen-computer-science | 未知（CDSS 有 "invites PhD applicants" 新闻，日期待核实） | **高**：CS PhD + 公平性 + LLM |
| Ahmed Alaa | UC Berkeley / UCSF CPH（附属 EECS、Statistics）— **CS/统计 + CPH** | Assistant Professor（CPH 首批教师；入职年份待核实） | [C][D] 多模态患者表征、统计推断、心血管风险 | 本轮未核实具体 2024–2026 论文 ⚠️（单位待核实：来源未注明日期） | https://ctml.berkeley.edu/people/ahmed-alaa-phd ; https://bakarinstitute.ucsf.edu/people-at-bakar/ahmed | 未知 | 中：偏统计和表征学习 |
| Emma Pierson | UC Berkeley（附属 BAIR、CPH、CHAI）— **CS 系**（具体所属系待核实） | Zhang Family Endowed Professor（2026-01 新闻；职级待核实） | [D] 医学与社会科学中的 AI、算法偏见、健康不平等 | 疾病风险评估算法中的种族/性别偏见研究（2026-01 Berkeley 新闻描述；具体论文待核实）✅ | https://vcresearch.berkeley.edu/node/29573 | 未知 | 中高：方法偏统计，有 LLM 相关工作（待核实） |
| Jimeng Sun | UIUC Siebel School of Computing and Data Science + Carle Illinois College of Medicine — **CS 系** | Health Innovation Professor | [C][A] 临床 LLM、临床试验 AI、EHR 预测 | ① "Improving Medical Machine Learning Models with Generative Balancing for Equity and Excellence"（npj Digital Medicine 2025）② Sunlab "Large Language Models for Medicine" 方向（学生做临床 LLM、多模态、RL）✅ | https://sunlab.org ; https://cs.illinois.edu/directory/profile/jimeng ; https://medicine.illinois.edu/research/hips/sun | 未知 | **高**：CS PhD、组大、LLM 方向明确（注意他联合创办了 Keiji AI） |
| Yifan Peng | Weill Cornell Medicine, Population Health Sciences；AIDH 副主任 — **医学院/BMI** | Associate Professor | [A][B] 生物医学文本挖掘、放射报告生成、医学证据摘要、医学 VQA | ① NSF 资助项目"知识增强、可解释的放射报告生成"② 2025-02 讲座：证据检索中的 lost-in-the-middle 问题与医学证据摘要 LLM 微调；CXR-LT 2024 挑战报告 ✅ | https://penglab.weill.cornell.edu/team/yifan-peng ; https://phs.weill.cornell.edu/news/dr-yifan-peng-receives-prestigious-national-science-foundation-award ; https://penglab.weill.cornell.edu/node/259 | **招生中**（实验室有 "PhD opportunities for Fall 2027" 页面，请打开核实具体项目） | **高**：BioNLP 正统，并明确招 Fall 2027 PhD |
| Fei Wang | Weill Cornell Medicine PHS，Health Informatics & AI 分部主任，AIDH 创始主任（同时在 Cornell Tech 授课）— **医学院/BMI** | Professor（另一处来源写 Associate Professor，职称待核实） | [C] 计算健康、EHR 机器学习 | 本轮未核实具体 2024–2026 论文 ⚠️（职称/单位页未注明日期） | https://phs.weill.cornell.edu/research-collaboration/our-divisions/institute-artificial-intelligence-digital-health ; https://tech.cornell.edu/news/fei-wang-cornell-tech | 未知 | 中高：需要自己查近期论文 |
| Matthew McDermott | Columbia DBMI — **医学院/BMI**（本人为 MIT CS PhD，导师 Szolovits） | Assistant Professor（2025 起，**青年教师**） | [C] EHR 基础模型、MEDS 医疗事件数据标准、可复现性 | ① MEDS（Medical Event Data Standard）开源生态 ② 2025 秋 Weill Cornell 讲座 "Foundation Models for Electronic Health Record Data"；早期工作 Clinical BERT ✅ | https://www.dbmi.columbia.edu/profile/matthew-mcdermott/ ; https://www.dbmi.columbia.edu/matthew-mcdermott-xuhai-orson-xu-excited-to-join-dbmi-faculty-in-2025/ | 未知（2025-09 招博后，不是 PhD） | **高**：EHR 序列建模与语言模型同构，方法高度可迁移 |
| Xuhai "Orson" Xu | Columbia DBMI — **医学院/BMI** | Assistant Professor（2025 起，**青年教师**） | [C][A] 移动/可穿戴健康 + LLM（方向据既有了解，待核实） | 本轮仅核实 2025 入职新闻，代表作待核实 ⚠️ | https://www.dbmi.columbia.edu/matthew-mcdermott-xuhai-orson-xu-excited-to-join-dbmi-faculty-in-2025/ | 未知 | 中高（待核实具体方向） |
| Noémie Elhadad | Columbia DBMI 系主任；VP&S AI 副院长 — **医学院/BMI** | Associate Professor & Chair | [A] 临床 NLP、以人为本的 AI、女性健康 | 本轮未核实具体 2024–2026 论文 ⚠️ | https://www.dbmi.columbia.edu/profile/noemie-elhadad ; https://www.cuimc.columbia.edu/news/noemie-elhadad-phd-appointed-vice-dean-ai-initiatives | 未知 | 中：方向契合，但行政负担很重 |
| Qingyu Chen | Yale Biomedical Informatics & Data Science（BIDS），兼 Ophthalmology — **医学院/BMI** | Assistant Professor（tenure-track，2024 起，**青年教师**） | [A][B] 医疗 LLM 事实性与推理、生物医学 NLP、多模态诊断 | ① "Benchmarking large language models for biomedical natural language processing applications and recommendations"（Nature Communications 16:3280, 2025，一作）② NIH R01：提升医疗 LLM 的事实性与推理 ✅ | https://medicine.yale.edu/profile/qingyu-chen/ | 未知 | **高**：医疗 LLM 幻觉与推理，NLP 背景的理想匹配 |
| Hua Xu | Yale BIDS，McCluskey Professor，系副主任 — **医学院/BMI** | Professor | [A] 临床 NLP（CLAMP 工具包）、生物医学 RAG | ① BiomedRAG（Journal of Biomedical Informatics 162, 2025）② LLM 生物医学 NLP 基准（Nat Commun 2025，通讯作者）✅ | https://medicine.yale.edu/profile/hua-xu | 未知 | **高**：临床 NLP 老牌组 |
| Mark Dredze | JHU Computer Science；兼 Dept. of Medicine BIDS；JHU Data Science & AI Institute 首任主任（2025-10）— **CS 系** | Professor | [A] 医疗 LLM、患者信息、公共卫生 NLP | 医疗 LLM 机遇与挑战系列讲座（评测、偏见、安全、监管）；2025-10 任 DSAI 主任；具体 2025 论文待核实 ✅（单位） | https://hub.jhu.edu/2025/10/13/mark-dredze-johns-hopkins-dsai-director/ ; https://talks.cam.ac.uk/talk/index/212968/ | 未知 | **高**：CS PhD + NLP 老牌（新行政职务可能压缩指导时间） |
| Suchi Saria | JHU CS + Bloomberg 公卫（统计、卫生政策）— **CS 系** | Professor（各来源说法不一，待核实） | [C][D] 临床预测（败血症）、部署与安全 | 2025 秋 JHU 杂志专访（AI in medicine）；具体 2024–2026 论文待核实 ✅（单位） | https://hub.jhu.edu/magazine/2025/fall/suchi-saria-qa-ai-medicine ; https://suchisaria.jhu.edu/ | 未知 | 中：偏时序和部署（注意她是 Bayesian Health 创始人） |
| Narges Razavian | NYU Langone（Center for Healthcare Innovation & Delivery Science）— **医学院** | Associate Professor（2026-03 讲座介绍） | [C][A] 健康系统规模的 EHR 基础模型、下次就诊生成式预训练 | ① "Foundation Models for Clinical Records at Health System Scale"（arXiv 2507.00574, 2025）② RAVEN：下次就诊预测的 EHR 基础模型（arXiv 2603.24562）✅ | https://med.nyu.edu/faculty/narges-razavian ; https://arxiv.org/abs/2507.00574v1 | 未知 | **高**：EHR 上的 LM 式预训练 |
| Rajesh Ranganath | NYU Courant CS + Center for Data Science；兼 Population Health — **CS 系** | Assistant Professor（页面可能过时，职称待核实） | [D][C] 因果推断、OOD、可解释性、临床 ML | 2025 年 JAMIA（3 月）与 Neurocritical Care（2 月，与 Razavian 合作）论文，题目待核实 ⚠️ | https://cims.nyu.edu/~rajeshr/ ; https://med.nyu.edu/faculty/rajesh-ranganath | 未知 | 中高：方法论强，适合想做 robust/causal 的同学 |
| Su-In Lee | UW Paul G. Allen School（AIMS Lab），Boeing Endowed Professor — **CS 系** | Professor | [D][E] 可解释 AI（SHAP）、基础模型可解释性、AI 审计、阿尔茨海默/癌症 | 2025-10 Princeton QCB 讲座 "Explainable AI for health"；2026-02 Schmidt Center 讲座（癌症精准医学 XAI）✅ | https://aims.cs.washington.edu/testing ; https://lists.cs.princeton.edu/hyperkitty/list/talks@lists.cs.princeton.edu/thread/DZBE766ICQKVI5FOEJ4WPL5NT5X4MCT3 | 未知 | 中：偏可解释和生物，LLM 可解释性方向契合 |
| Sheng Wang | UW Paul G. Allen School — **CS 系** | Assistant Professor | [B][E] 多模态生物医学基础模型、病理 FM | ① BiomedParse（Nature Methods, 2024-11，把 9 种影像模态投影到文本空间）② GigaPath 全切片病理 FM（与 Microsoft 合作，2024）⚠️（单位待核实：最新带日期来源为 2024-11） | https://www.washington.edu/news/2024/11/18/biomedparse-ai-medical-image/ ; https://hai.stanford.edu/events/sheng-wang-generative-ai-multimodal-biomedicine | 未知 | **高**：CS PhD，"以文本为中心"的多模态方法 |
| Meliha Yetişgen | UW Biomedical Informatics & Medical Education（BIME），UW-BioNLP 负责人 — **医学院/BMI** | Professor | [A] 临床笔记错误检测、幻觉、SDOH 抽取、医学 VQA | ① MEDEC：临床笔记医疗错误检测与纠正基准（ACL Findings 2025）② LLM 抽取 SDOH 的捷径学习（ACL 2025）✅ | https://bime.uw.edu/faculty/meliha-yetisgen ; https://faculty.washington.edu/melihay | 未知 | **高**：ACL 系发表，纯 NLP |
| Trevor Cohen | UW BIME — **医学院/BMI** | Professor | [A][D] 语言计算模型、LLM 部署治理（UW Medicine LLM 工作组）、精神健康语言 | ① LLM 能否预测大众对健康内容的理解（JBI 2025）② 多机构数据偏差的 task arithmetic 方法（JBI 168, 2025，与 Yetişgen 合作）✅ | https://bime.uw.edu/faculty/trevor-cohen | 未知 | **高** |
| Hong Yu | UMass Lowell Miner School of CIS，CHORDS 主任；UMass BioNLP — **CS 系** | Professor | [A] 临床 LLM、检索增强推理、多 agent ICD 编码、医学可读性 | ① RARE：检索增强推理（ACL 2025）② CARE-AD：多 agent LLM 从纵向笔记预测阿尔茨海默病（npj Digital Medicine 2025）✅（同名作者多，请逐篇核对） | https://fenway.cs.uml.edu ; https://dblp.org/pid/55/6749.html | 未知 | **高**：CS PhD + ACL/NAACL 发表 |
| Jenna Wiens | Michigan CSE，Precision Health 联合主任（MLD3 组）— **CS 系** | Associate Professor（来源未注明日期，职称待核实） | [C][D] 临床时序、迁移学习、规避捷径学习、临床 RL | 规避有害捷径的迁移学习、患者-治疗匹配 RL（讲座摘要，年份待核实）⚠️ | https://midas.umich.edu/faculty-member/jenna-wiens ; https://wiens-group.engin.umich.edu/team | 未知 | 中高 |
| Carl Yang | Emory Computer Science（兼公卫学院、护理学院）— **CS 系** | Assistant Professor | [A][C] KG 与 LLM 协同学习、多机构联邦多 agent、多模态健康数据 | 2025 ACM SIGKDD Rising Star、NSF CAREER（2025）、MedInfo 2025 Best Paper；2025–2026 系列讲座 "Expediting Next-Generation AI for Health via KG and LLM Co-Learning" ✅ | https://cse.hkust.edu.hk/pg/seminars/S25/yang.html ; https://diabetes.emory.edu/researchers/faculty/yang-carl.html ; https://www.cc.gatech.edu/events/2026/02/13/school-cse-seminar-series-carl-yang | 未知 | **高**：CS PhD + LLM/KG |
| Qi Long | UPenn Biostatistics, Epidemiology & Informatics（DBEI）— **医学院/生统** | Professor（职称待核实） | [C][D] LLM 统计基础（与 Weijie Su 合作）、EHR/多组学基础模型、agentic AI | 2025-09 博后招聘：方向为 LLM 统计基础和生物医学 agentic AI（只能说明方向，不是论文）⚠️ | https://careers.insidehighered.com/job/3531364/postdoctoral-researcher-in-bio-statistics-and-machine-learning/ | 未知 | 中：偏统计 |
| Lin Xu | UT Southwestern（所属系待核实）— **医学院** | Assistant Professor（tenure-track，实验室 2022 年成立，**青年教师**） | [E] 生物医学发现中的基础模型与 LLM | 本轮未核实具体论文 ⚠️（单位待核实：主页未注明日期） | https://profiles.utsouthwestern.edu/profile/140757/lin-xu.html | 未知 | 中 |

**美国说明**
- **CMU**：本轮没有找到 2024–2026 年能核实的医疗 AI 教职，所以没收录。Zachary Lipton 同时任 Abridge CTO/首席科学家，属于产业身份，按规则排除。建议你自己查 CMU MLD/LTI 的教师目录。
- **David Sontag（MIT EECS）**：本人主页称 2025 年部分休假、任 Layer Health CEO；2026 年更新的 CSAIL 页面写的是 "visiting professor"。**单位待核实，暂不推荐作为 PhD 导师首选**（来源：https://people.csail.mit.edu/dsontag ）。
- **UPenn CIS、UCSF 本部、Emory BMI 等**：检索额度有限，未单独核实。

---

## 二、香港（12 人）

| 姓名（英文） | 学校 / 院系（CS 系 or 医学院/BMI） | 职称（青年教师标注） | 子方向标签 + 关键词 | 1–2 项 2024–2026 代表工作 | 主页/来源 URL | 招生信号 | 与 ML/NLP 背景的适配度 |
|---|---|---|---|---|---|---|---|
| Hao Chen（陈浩） | HKUST CSE & CBE（兼 Life Science），Smart Lab — **CS 系** | Assistant Professor（据 HKUST 简介，职称待核实） | [B][A] 病理基础模型、多模态医疗大模型、医疗聊天 LLM | ① GPFM：通用病理基础模型（Nature Biomedical Engineering，2025-04 实验室发布）② SmartPath 病理全流程平台（2025-10 新闻稿，含自动报告生成）；HKUST 项目 "Large Multimodal Medical Foundation Model"（2025） ✅ | https://smartlab.cse.ust.hk/2025/10/22/smartpath ; https://smartlab.cse.ust.hk/2025/04/15/gpfm ; https://researchportal.hkust.edu.hk/en/projects/large-multimodal-medical-foundation-model/ | 未知（旧招聘帖截至 2023-12，已过期） | **高**：香港 CS 系里医疗大模型最活跃的组之一，有 MedMR 等 LLM 工作 |
| Xiaomeng Li（李小萌） | HKUST ECE（CSE 有 profile），医学影像分析中心副主任 — **EE/CS 系** | Assistant Professor | [B] 医学影像、大视觉语言基础模型 | 2025 年讲座：大视觉语言基础模型及其临床意义；具体论文待核实 ✅（讲座）/ ⚠️（主页未注明日期） | https://ece.hkust.edu.hk/eexmli ; https://cse.hkust.edu.hk/admin/people/faculty/profile/eexmli | 未知 | 中高：偏视觉，VLM 方向可以发挥 NLP 背景 |
| Qi Dou（窦琪） | CUHK CSE，T Stone Robotics Institute — **CS 系** | Associate Professor（2025 年由 Assistant 升任） | [B] 手术机器人 AI、视觉基础模型、手术 VLM | ① 纯视觉手术机器人自动化框架（Science Robotics, 2025-08，活体动物多任务测试）② SurgΣ / SurgVLM 手术基础模型合作（NUS、CUHK、SJTU、NVIDIA；仅见 LinkedIn，待核实）✅ | https://www.cse.cuhk.edu.hk/~qdou/ ; https://www.cpr.cuhk.edu.hk/en/?p=227659 | 未知 | 中：偏机器人和视觉 |
| Pheng-Ann Heng（王平安） | CUHK CSE，Choh-Ming Li Professor，Institute of Medical Intelligence and XR 主任 — **CS 系** | Professor | [B] 医学影像 AI、手术模拟、XR | 2025-03 获 Choh-Ming Li 讲座教授；2025 年 Highly Cited Researcher；具体 2024–2026 论文待核实 ✅（单位） | https://www.cse.cuhk.edu.hk/news/achievements/prof-heng-pheng-ann-has-been-recognised-as-highly-cited-researchers-2025/ ; https://www.cse.cuhk.edu.hk/~pheng/Home.html | 未知 | 中：组大，偏影像和 XR |
| Yixuan Yuan（袁奕萱） | CUHK Electronic Engineering — **EE 系** | Associate Professor | [B][D] 医疗 AI、模型可解释性/鲁棒性/安全 | AAAI 2025 "Top 1 most influential papers"（主页所列，主题待核实）⚠️ | https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-yixuan-yuan | 未知 | 中 |
| Yu Li（李煜） | CUHK CSE — **CS 系** | Assistant Professor | [E] 用 LLM 做复杂疾病建模与药物发现 | 2025-02 HKUST 讲座 "Complex Disease Modeling and Efficient Drug Discovery with Large Language Models" ✅（讲座）；具体论文待核实 | https://life-sci.hkust.edu.hk/events/2025-02-21 | 未知 | **高**（对想做 bio+LM 的同学） |
| Helen Meng（蒙美玲） | CUHK 系统工程与工程管理系（SEEM），CPII 主任 — **工程/CS 类** | Professor | [A] 口语语言生物标志物筛查认知障碍（痴呆）、语音/语言健康 AI | RGC 主题研究计划 "AI in Extraction and Identification of Spoken Language Biomarkers for Screening and Monitoring of Neurocognitive Disorders"（2024 年研讨会仍在报告）；CPII 2025 年仍在运营 ⚠️（2025–2026 医疗产出待核实） | https://www.se.cuhk.edu.hk/research/information-systems/ai-for-digital-health/ ; https://cuhk.edu.hk/english/research/innohk-centres/perceptual-and-interactive-intelligence.html | 未知 | **高**：语音/NLP 直接用于健康 |
| Lequan Yu（俞乐全） | HKU School of Computing and Data Science（统计与精算），Medical AI Lab — **数据科学/统计（CS 学院）** | Assistant Professor | [B][A] 多模态生物医学学习、医学影像、临床 NLP | 研究兴趣明确列出 clinical NLP 与多模态整合；具体 2024–2026 论文本轮未核实 ⚠️（目录页未注明日期，但学院名称说明页面是 2024 年改组后更新的） | https://saasweb.hku.hk/staff/lqyu ; https://ai.hku.hk/people/academic-staff/yulequan | 未知 | **高**：香港少数明确写"临床 NLP"的 CS 学院教师 |
| Ruibang Luo（罗锐邦） | HKU Computer Science — **CS 系** | Associate Professor | [E] 生物信息算法、基因组、临床信息学 | GIW/ISCB-Asia 2025 大会主席；HKU 杰出青年研究员奖 2023–24；具体 LM 方法论文待核实 ✅（单位） | https://cs.hku.hk/people/academic-staff/rbluo ; https://www.bio8.cs.hku.hk | 未知 | 中：偏基因组算法，未必以 LM 为主 |
| Jing (Harry) Qin（秦璟） | PolyU 护理学院，Centre for Smart Health 主任 — **医学/护理类学院** | Professor | [B] 神经退行性疾病 AI 诊断、XR、康复 | RGC 策略研究项目 Co-PI：基层医疗 AI 辅助泌尿评估（2026-01 起）✅ | https://www.polyu.edu.hk/sn/about-sn/our-school/academic-staff/professorial-staff/prof-harry-qin/ | 未知 | 中低：护理学院背景，PhD 学位类型需要核实 |
| William K. W. Cheung（张国威） | HKBU Computer Science，Centre for Health Informatics 主任 — **CS 系** | Professor | [C] 健康信息学、数据挖掘 | 本轮未核实具体 2024–2026 论文 ⚠️（单位待核实） | https://interdisciplinary-research.hkbu.edu.hk/people/william-cheung ; https://scholars.hkbu.edu.hk/en/organisations/centre-for-health-informatics/ | 未知 | 中 |
| Jiming Liu（刘际明） | HKBU Computer Science，Chair Professor，副校长（研究发展）— **CS 系** | Chair Professor | [C][D] 健康信息学、计算流行病学、AI 疾病防控 | 本轮未核实具体 2024–2026 论文 ⚠️（单位待核实） | https://www.comp.hkbu.edu.hk/~jiming | 未知 | 中低：偏流行病学建模 |

**香港说明**
- **CityU**：本轮检索没有找到能核实的医疗 LLM / 医疗 AI 教职，所以没有收录，不代表 CityU 没有。Yixuan Yuan 曾在 CityU（2018–2022），现已转到 CUHK。
- **HKBU Yang Liu**（CS 助理教授、健康信息中心副主任）：名字太常见，来源也未注明日期，暂不收录。
- **CUHK-Shenzhen / HKUST-GZ**（如 HuatuoGPT 相关团队）不在香港本地，按地域要求没有收录。
- **医院合作**：HKUST 团队称"正与香港多家医院讨论试验与落地"（Healthcare IT News）。医管局（HA）设有 **Data Collaboration Lab** 自助数据平台，支持使用 HA 临床数据做研究（https://www3.ha.org.hk/data/DCL/SummaryandPublication/?year=2020 ）。

---

## 三、新加坡（0 人核实 · 待检索候选名单）

**说明**：本轮检索额度在开始查新加坡时就用完了，duke-nus.edu.sg 和 comp.nus.edu.sg 也被网络代理拦截，所以**下面名单没有一条经过 2024–2026 年来源核实**。名单只来自既有知识，**不能当作已核实信息使用**，套磁前必须逐一到官网确认。

| 候选姓名 | 可能单位（待核实） | 可能方向（待核实） | 需要核实的点 |
|---|---|---|---|
| Mengling Feng | NUS Saw Swee Hock 公卫学院 / Institute of Data Science | [C] EHR、临床 AI | 职称、是否仍在 NUS、2025 年后的论文 |
| Nan Liu | Duke-NUS（Centre for Quantitative Medicine） | [C][D] 临床预测、可解释评分、医疗 AI 评估 | 同上；Duke-NUS 的 PhD 项目类型 |
| Yueming Jin | NUS（BME / ECE） | [B] 手术 AI、多模态 | 是否参与 SurgΣ（Qi Dou 条目中的 LinkedIn 帖子提到"NUS"，但没写人名） |
| Wynne Hsu / Mong Li Lee | NUS School of Computing | [B][C] 医学影像、健康数据挖掘 | 2025 年后是否仍在招生 |
| Yih-Chung Tham | NUS Yong Loo Lin 医学院 | [B] 眼科 AI | 医学院 PhD 途径 |
| Daniel S. W. Ting | Duke-NUS / 新加坡国家眼科中心（医生科学家） | [A][B] 眼科 AI、医疗 LLM | 是否能作为 PhD 主导师 |
| NTU（CCDS、LKC Medicine）、SMU | — | — | 本轮只确认 NTU Computing（2025-03、2025-06）和 SMU Computing 请 Carl Yang 讲过"KG + LLM for Health"，说明有相关兴趣，但**没有核实到本校 PI** |
| A*STAR（I2R / IHPC / BII 等） | 研究院，不是大学 | — | 研究员不是大学教职；学生通常经 A*STAR 奖学金（如 SINGA，待核实）挂靠 NUS/NTU 读博 |

---

## 四、医疗 AI 方向申请建议

1. **CS PhD 与 BMI PhD 的取舍**
   - CS/EECS PhD（MIT Ghassemi、Duke Agrawal、UIUC Sun、Berkeley Chen、UW Allen School、Emory Yang、HKUST Hao Chen 等）：课程和资格考以 ML/NLP 为主，毕业后去业界研究岗或 CS 教职都更顺，但要自己去争取临床合作。
   - 医学院/BMI PhD（Harvard DBMI、Stanford BMDS、Columbia DBMI、Yale BIDS、UW BIME、Weill Cornell）：离临床数据和医生更近，课题更容易落地，但课程会包含生物统计、临床信息学，毕业去向偏医疗系统、药企和 BMI 教职。
   - 有 NLP 背景的同学，两条路都可以走。选导师时要看清**学位由哪个项目授予**，以及能否跨项目联合指导。
2. **数据访问资质本身就是简历信号**：主动完成 PhysioNet 的数据使用培训，并拿到 MIMIC 等受控数据集的访问资格，在简历上写清已有 credentialed access，能说明你具备处理真实临床数据的能力和合规意识。具体培训要求以 PhysioNet 官网为准。
3. **用"评测"切入医疗 LLM**：多位 PI（Shah 的 MedHELM、Daneshjou 的 red-teaming、Agrawal 的 evaluation illusion、Yetişgen 的 MEDEC、Qingyu Chen 的 LLM 基准）都把**真实临床任务评测**当作核心问题。NLP 背景的人在评测设计、LLM-as-judge、幻觉检测上有天然优势，研究陈述（SOP）里可以以此为卖点。
4. **展示临床动机，不要只写"医疗是好的应用场景"**：可以写具体痛点，比如临床笔记里的错误、报告生成的事实一致性、患者用 LLM 查询健康信息带来的风险。最好附上一个小项目，例如在公开数据上复现 MedHELM 或 MEDEC 类评测，或给 MEDS 这类开源生态贡献代码（McDermott 组）。
5. **留意导师的产业身份**：Agrawal（Layer Health 联合创始人）、Sun（Keiji AI）、Saria（Bayesian Health）、Langlotz（Sirona 董事）、Sontag（Layer Health CEO，部分休假）都有产业角色。面谈时要问清指导时间、数据与知识产权安排。
6. **新行政职务可能压缩指导时间**：Dredze（2025-10 任 JHU DSAI 主任）、Elhadad（DBMI 系主任 + VP&S AI 副院长）等资深 PI，可以优先和他们组里的高年级学生或博后沟通，确认实际带人方式。
7. **医院实验室要走合作路径**：Bitterman、Mahmood 等的实验室在医院或病理科，通常没有自己的 PhD 学位项目，需要通过 Harvard BMI、MIT 等项目联合指导。申请前请直接写邮件确认。
8. **香港特点**：CS 系里医疗 AI 以**影像和多模态基础模型**为主（HKUST Hao Chen / Xiaomeng Li，CUHK Dou / Heng / Yuan），纯临床 NLP 的组相对少，可以重点看 HKU Lequan Yu（列出临床 NLP）、CUHK Helen Meng（语音/语言健康）、CUHK Yu Li（LLM + 药物）。HA 设有 Data Collaboration Lab 支持使用 HA 数据做研究，HKUST 团队称正和多家香港医院讨论试验；具体某个导师是否能接触 HA 数据，需要直接问。
9. **新加坡**：本轮没有核实。SingHealth、NUHS 与 NUS / Duke-NUS 的合作关系是常识性判断，但**本轮没有找到来源**，请自行核实。
10. **关注明确的招生页**：目前唯一找到明确写 2027 招生的是 Yifan Peng 组（"PhD opportunities for Fall 2027"）。Zitnik 组称每年招新 PhD。其他人建议直接查主页的 "Prospective students" 栏，或直接发邮件询问。

---

## 五、需要你自己核实的事项

1. **新加坡全部候选人**（第三节）：单位、职称、2025–2026 年论文、招生情况。
2. 标 ⚠️ 的条目：Sheng Wang（最新带日期来源为 2024-11）、Irene Chen（2024-01）、Ahmed Alaa、Jenna Wiens、Fei Wang、Xuhai Xu、Noémie Elhadad、Rajesh Ranganath（职称）、Lin Xu（所属系）、Qi Long、Lequan Yu（近作）、Yixuan Yuan、Helen Meng（2025 年后医疗产出）、HKBU 两位。
3. 职称冲突或可能过时：James Zou、Serena Yeung-Levy、Arjun Manrai、Marinka Zitnik、Hao Chen、Suchi Saria、Emma Pierson（所属系）、Fei Wang。
4. 论文细节：MedHELM 的正式发表期刊；Manrai 2026 年 Science 论文（目前只见论坛转载）；Rajpurkar 两篇论文的年份；Agrawal "evaluation illusion" 的发表载体；Hong Yu 论文的作者归属（同名学者很多）；Qi Dou 的 SurgΣ 合作。
5. David Sontag 是否仍在 MIT 全职、是否招生。
6. **招生**：除 Yifan Peng（Fall 2027 页面）外，其他人全部标"未知"，需要逐一查看主页或发邮件。
7. **学位授予项目**：医学院/BMI 的 PI 能否指导 CS PhD 学生（或反过来），以及 courtesy appointment 能否独立招生。
8. **本轮没有覆盖**：CMU、UPenn CIS、UCSF 本部、Emory BMI、Michigan DCMB、CityU、NTU、SMU 等，可以下一轮补查。

---

## 六、Sources

**美国**
- https://hai.stanford.edu/news/holistic-evaluation-of-large-language-models-for-medical-applications
- https://profiles.stanford.edu/nigam-shah
- https://dbds.stanford.edu/nigam-shah-which-llm-is-best-for-real-health-care-needs
- https://www.medrxiv.org/content/10.1101/2025.05.02.25326781v2.article-info
- https://ml4mi.wisc.edu/8757-2/
- https://ysph.yale.edu/event/ai-agents-for-biomedical-discoveries/
- https://marvl.stanford.edu/publications.html
- https://profiles.stanford.edu/roxana-daneshjou
- https://aimi.stanford.edu/grand-rounds/2025-aimi-grand-rounds/july
- https://doaj.org/article/565b78e78ecb473295de919c2dcf0533
- https://profiles.stanford.edu/curtis-langlotz
- https://langlotzlab.stanford.edu/
- https://news.stanford.edu/stories/2025/11/research-matters-curtis-langlotz
- https://sironamedical.com/company/press/dr-curtis-langlotz-joins-sirona-board
- https://ilp.mit.edu/node/23481
- https://wgs.mit.edu/events-all/2026/2/26/the-pulse-of-ethical-machine-learning-in-health
- https://imes.mit.edu/node/686
- https://www.csail.mit.edu/news/mit-eecs-professor-regina-barzilay-receives-2025-frances-e-allen-medal
- https://communityjameel.org/news/regina-barzilay-looks-ahead-at-ai-in-cancer-research-and-treatment-in-2025
- https://people.csail.mit.edu/dsontag
- https://dbmi.hms.harvard.edu/people/pranav-rajpurkar
- https://www.rajpurkarlab.hms.harvard.edu/home
- https://arxiv.org/abs/2503.10970v1
- https://arxiv.org/pdf/2606.28692
- https://zitniklab.hms.harvard.edu/jobs
- https://dbmi.hms.harvard.edu/people/arjun-raj-manrai
- https://piefed.nullspace.lol/post/215026 （Manrai 2026 论文的论坛转载，可信度低）
- https://hms.harvard.edu/news/researchers-design-foundation-ai-models-use-pathology
- https://ai.meta.com/blog/mahmood-lab-human-pathology-dinov2/
- https://huggingface.co/MahmoodLab/TITAN/resolve/main/README.md
- https://2025.worldmedicalinnovation.org/speaker/danielle-bitterman-md/
- https://aim.mgh.harvard.edu/team/danielle-bitterman
- https://crcs.seas.harvard.edu/event/danielle-bitterman-mass-general-brigham
- https://scholars.duke.edu/person/monica.agrawal
- https://aihealth.duke.edu/2025/09/10/seminar-monica-agrawal/
- https://aihealth.duke.edu/2025/06/16/agrawal-whitehead-scholar/
- https://www2.eecs.berkeley.edu/Faculty/Homepages/iychen.html
- https://news.berkeley.edu/2024/01/16/meet-our-new-faculty-irene-chen-computer-science
- https://cdss.berkeley.edu/news/computational-precision-health-program-welcomes-new-faculty-invites-phd-applicants
- https://ctml.berkeley.edu/people/ahmed-alaa-phd
- https://bakarinstitute.ucsf.edu/people-at-bakar/ahmed
- https://vcresearch.berkeley.edu/node/29573
- https://sunlab.org
- https://cs.illinois.edu/directory/profile/jimeng
- https://medicine.illinois.edu/research/hips/sun
- https://penglab.weill.cornell.edu/team/yifan-peng
- https://penglab.weill.cornell.edu/node/259
- https://phs.weill.cornell.edu/news/dr-yifan-peng-receives-prestigious-national-science-foundation-award
- https://phs.weill.cornell.edu/research-collaboration/our-divisions/institute-artificial-intelligence-digital-health
- https://tech.cornell.edu/news/fei-wang-cornell-tech
- https://www.dbmi.columbia.edu/profile/matthew-mcdermott/
- https://www.dbmi.columbia.edu/matthew-mcdermott-xuhai-orson-xu-excited-to-join-dbmi-faculty-in-2025/
- https://phs.weill.cornell.edu/news/hiai-seminar-foundation-models-electronic-health-record-data
- https://www.dbmi.columbia.edu/profile/noemie-elhadad
- https://www.cuimc.columbia.edu/news/noemie-elhadad-phd-appointed-vice-dean-ai-initiatives
- https://medicine.yale.edu/profile/qingyu-chen/
- https://medicine.yale.edu/profile/hua-xu
- https://hub.jhu.edu/2025/10/13/mark-dredze-johns-hopkins-dsai-director/
- https://talks.cam.ac.uk/talk/index/212968/
- https://hub.jhu.edu/magazine/2025/fall/suchi-saria-qa-ai-medicine
- https://suchisaria.jhu.edu/
- https://med.nyu.edu/faculty/narges-razavian
- https://arxiv.org/abs/2507.00574v1
- https://arxiv.org/pdf/2603.24562
- https://cims.nyu.edu/~rajeshr/
- https://med.nyu.edu/faculty/rajesh-ranganath
- https://aims.cs.washington.edu/testing
- https://lists.cs.princeton.edu/hyperkitty/list/talks@lists.cs.princeton.edu/thread/DZBE766ICQKVI5FOEJ4WPL5NT5X4MCT3
- https://www.washington.edu/news/2024/11/18/biomedparse-ai-medical-image/
- https://hai.stanford.edu/events/sheng-wang-generative-ai-multimodal-biomedicine
- https://bime.uw.edu/faculty/meliha-yetisgen
- https://faculty.washington.edu/melihay
- https://bime.uw.edu/faculty/trevor-cohen
- https://fenway.cs.uml.edu
- https://dblp.org/pid/55/6749.html
- https://midas.umich.edu/faculty-member/jenna-wiens
- https://wiens-group.engin.umich.edu/team
- https://cse.hkust.edu.hk/pg/seminars/S25/yang.html
- https://diabetes.emory.edu/researchers/faculty/yang-carl.html
- https://www.cc.gatech.edu/events/2026/02/13/school-cse-seminar-series-carl-yang
- https://careers.insidehighered.com/job/3531364/postdoctoral-researcher-in-bio-statistics-and-machine-learning/
- https://profiles.utsouthwestern.edu/profile/140757/lin-xu.html
- https://www.cmu.edu/news/experts/zachary.lipton

**香港**
- https://smartlab.cse.ust.hk/2025/10/22/smartpath
- https://smartlab.cse.ust.hk/2025/04/15/gpfm
- https://researchportal.hkust.edu.hk/en/projects/large-multimodal-medical-foundation-model/
- https://www.healthcareitnews.com/news/asia/hong-kong-university-test-four-genai-models-hospitals
- https://ece.hkust.edu.hk/eexmli
- https://cse.hkust.edu.hk/admin/people/faculty/profile/eexmli
- https://www.cse.cuhk.edu.hk/~qdou/
- https://www.cpr.cuhk.edu.hk/en/?p=227659
- https://www2.yicaiglobal.com/news/ai-progress-to-make-surgical-robots-a-bigger-presence-in-hospitals-cuhk-professor-says
- https://www.cse.cuhk.edu.hk/news/achievements/prof-heng-pheng-ann-has-been-recognised-as-highly-cited-researchers-2025/
- https://www.cse.cuhk.edu.hk/~pheng/Home.html
- https://www.ee.cuhk.edu.hk/en-gb/people/academic-staff/professors/prof-yixuan-yuan
- https://life-sci.hkust.edu.hk/events/2025-02-21
- https://www.se.cuhk.edu.hk/research/information-systems/ai-for-digital-health/
- https://cuhk.edu.hk/english/research/innohk-centres/perceptual-and-interactive-intelligence.html
- https://saasweb.hku.hk/staff/lqyu
- https://ai.hku.hk/people/academic-staff/yulequan
- https://cs.hku.hk/people/academic-staff/rbluo
- https://www.bio8.cs.hku.hk
- https://www.polyu.edu.hk/sn/about-sn/our-school/academic-staff/professorial-staff/prof-harry-qin/
- https://interdisciplinary-research.hkbu.edu.hk/people/william-cheung
- https://scholars.hkbu.edu.hk/en/organisations/centre-for-health-informatics/
- https://www.comp.hkbu.edu.hk/~jiming
- https://www3.ha.org.hk/data/DCL/SummaryandPublication/?year=2020

**新加坡（只有间接信号，不是 PI 核实来源）**
- https://www.ntu.edu.sg/computing/news-events/events/detail/2025/06/11/default-calendar/seminar--expediting-next-generation-ai-for-health-via-kg-and-llm-co-learning
- https://computing.smu.edu.sg/newsletter/research-seminar-carl-yang-expediting-next-generation-ai-health-kg-and-llm-co-learning
- https://hk.linkedin.com/in/dmeng94 （SurgΣ 合作帖，未经一手来源核实）
