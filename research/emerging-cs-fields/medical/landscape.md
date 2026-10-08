# 医疗 CS 新兴方向全景（面向 ML/NLP 背景研究者）

> 调研日期：2026-10-08。证据来自约36次网络检索（WebFetch 不可用，多数数字来自检索摘要或二手报道）。
> 标注约定：**（待核实）** 指来源之间有冲突或只有二手来源；**（背景知识）** 指本次没有检索、依据既有知识写入的内容。
> 评分细节、逐维理由与证据链接见 `evidence/medical.json`。评分框架与主项目相同：
> Score = 20 ×（0.25G + 0.25C + 0.10E + 0.10R + 0.10H + 0.20X）×（0.5 + 0.1S）− P。
> 校准参照：2021 年的 LLM 约92分，2021 年的 NeRF 约72分，今天已成主流的 LLM 约52分。

---

## 1. 医疗 CS 全景：哪些方向对 ML/NLP 背景最友好

| 排名 | 方向 | G | S | C | E | R | H | X | P | **得分** | ML/NLP 友好度 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 临床大模型智能体（诊断对话 + EHR 智能体） | 5 | 4.5 | 4 | 3.5 | 5 | 4 | 4 | 7 | **74.7** | 很高 |
| 2 | 医疗 LLM 评测、安全与幻觉 | 4.5 | 4 | 3.5 | 4.5 | 4 | 5 | 4 | 4 | **70.7** | 很高 |
| 3 | 医学推理模型（RLVR） | 5 | 4 | 4 | 4.5 | 4 | 4.5 | 3 | 7 | **67.7** | 很高 |
| 4 | 患者模拟器与医疗数字孪生 | 4 | 5 | 3 | 4 | 3 | 5 | 3.5 | 7 | **66.0** | 很高 |
| 5 | EHR / 结构化病历基础模型 | 4 | 4.5 | 4 | 2.5 | 4 | 3 | 4 | 6 | **65.3** | 高（受数据限制） |
| 6 | 基因组语言模型 | 4 | 4 | 3.5 | 4.5 | 4 | 3.5 | 4 | 6 | **63.8** | 中（需生物学知识） |
| 7 | 可穿戴与生理信号基础模型 | 4 | 4.5 | 3.5 | 2.5 | 4 | 3.5 | 3.5 | 5 | **62.9** | 中 |
| 8 | 多模态/通用医学基础模型 | 4 | 3.5 | 3.5 | 4 | 4.5 | 3.5 | 4 | 6 | **59.9** | 中高 |
| 9 | 医疗 AI 监管科学与部署后监测 | 3.5 | 4.5 | 2.5 | 2.5 | 3 | 4 | 3 | 5 | **53.0** | 中 |
| 10 | 病理基础模型 | 3.5 | 3 | 3.5 | 3 | 3.5 | 3.5 | 2.5 | 6 | **46.0** | 中低（偏视觉） |
| 11 | 医学知识编辑与持续更新 | 3 | 4 | 2 | 4 | 1.5 | 4.5 | 3 | 7 | **44.3** | 高（但空间小） |
| 12 | 环境式临床文档（AI Scribe） | 4.5 | 2.5 | 3.5 | 2 | 5 | 2 | 2.5 | 8 | **43.0** | 中（已被产业吸收） |
| 13 | 医学影像分割基础模型 | 2.5 | 2 | 3 | 4.5 | 2.5 | 3 | 2.5 | 5 | **35.3** | 低 |
| 14 | 隐私保护/联邦医疗学习 | 1.5 | 2 | 2 | 3 | 2.5 | 3 | 3 | 6 | **26.6** | 低 |

**总体判断**

- **没有一个医疗方向能达到 2021 年 LLM 的约92分。** 最高分（临床智能体 74.7）和 2021 年的 NeRF（72）大致相当。医疗方向普遍要额外扣 5-8 分，原因包括临床验证缺口、监管、数据获取，以及被前沿大厂吸收的风险。
- **最像 2020-21 年 LLM 的方向是 EHR 基础模型。** 2025 年它出现了「缩放律时刻」：CoMET 在1.18亿患者、1150亿医疗事件上得到幂律，并在78个任务上零样本匹敌专用模型；同年 Delphi-2M 发表于 Nature。社区仍小，也没有共识范式。但数据被 Epic 等少数机构掌握，学术界能拿到的 MIMIC-IV 规模不足以支撑缩放，所以 E/H 偏低。这和 2020 年「只有 OpenAI 能训 GPT-3」的局面非常相似。
- **按 ML/NLP 迁移成本排序**，最友好的四个方向是：临床智能体、评测与安全、医学推理、患者模拟器。四者都以文本或对话为核心，数据门槛低，可以用开源 7B-32B 模型和合成环境在学术算力上完成。它们彼此高度耦合：患者模拟器是智能体的训练环境，rubric 评测是推理模型的奖励来源。
- **已成熟或降温的方向**：分割基础模型（nnU-Net 仍是强基线）、联邦学习（真实部署率仅3-5%）。AI Scribe 的产业热度很高，但技术已被 Abridge、Microsoft 等公司吸收，学术空间小。

---

## 2. 各方向通俗解释（是什么、为什么是现在、代表工作）

**2.1 临床大模型智能体（74.7）**
- **是什么**：让 LLM 不止回答医学问题，还能在电子病历系统里查数据、下医嘱，或与患者多轮问诊后给出鉴别诊断。
- **为什么是现在**：静态考试题已经饱和，MedQA 上几乎所有新模型都超过95%。
  - 2025 年 AMIE 发表于 Nature：159个模拟病例中，32个评估维度有30个优于全科医生。
  - 随后 AMIE 在 BIDMC 对100名真实患者做了前瞻研究，鉴别诊断包含最终诊断的比例为90%，没有触发安全叫停。
  - Microsoft MAI-DxO 在304个 NEJM 病例上报告「最高85%」的正确率，为厂商自报。
- **差距仍大**：
  - MedAgentBench 上最好的模型成功率约70%，涉及写操作的动作类任务只有54%。
  - PhysicianBench 上 GPT-5.5 的 pass^3 仅28%。
- **代表工作**：AMIE、MedAgentBench（Stanford，FHIR 环境）、AgentClinic、MAI-DxO、PhysicianBench、EHR-Complex。

**2.2 医疗 LLM 评测、安全与幻觉（70.7）**
- **是什么**：衡量医疗 LLM「在真实场景下是否靠谱」，而不只看考试分数。
- **为什么是现在**：选择题已经饱和。JMIR 一篇覆盖39个基准的综述显示，知识考试类得分为84-90%，实践类只有约45-69%。
- **代表工作**：
  - 2025 年 OpenAI 发布 HealthBench：262名医生、5000段对话、48,562条 rubric 评分标准。
  - Stanford 发布 MedHELM：121个真实临床任务。
  - 2026-04 OpenAI 发布 HealthBench Professional：525个医生编写的任务，并以医生作为基线。
  - 幻觉方向有 MedHallu：最好的模型检测「困难」幻觉的 F1 仅0.625。
- **学术切入**：这是学术界最有比较优势的方向，算力需求低，核心是方法论，例如 LLM 评委的校准、rubric 的效度。

**2.3 医学推理模型（67.7）**
- **是什么**：用 o1/R1 式的强化学习（GRPO 加可验证奖励）训练会「想清楚再答」的医学模型。
- **为什么是现在**：
  - 2024-12 HuatuoGPT-o1 只用4万个可验证问题就跑通了「验证器 + RL」。
  - 2025 年 Med-R1、MedReason、Fleming-R1、Baichuan-M2/M3 相继出现。
  - Baichuan-M3 自报 HealthBench Hard 得分44.4，高于 GPT-5.2-High 的42.0。
- **最大风险**：被通用前沿模型吸收。医学专用推理模型的独立价值主要在本地部署、隐私和成本，必须论证清楚。

**2.4 患者模拟器与医疗数字孪生（66.0）**
- **是什么**：用 LLM 扮演「病人」，用于医学教育、评测医生智能体，或作为医生智能体的 RL 训练环境。数字孪生则是用生成模型模拟个体的未来健康轨迹。
- **为什么是现在**：
  - AgentClinic 显示，把 MedQA 改成多轮问诊后，诊断准确率可降到原来的十分之一以下。也就是说，必须有模拟器才能测出静态基准看不到的缺陷。
  - 2025 年 DoctorAgent-RL 和 Baichuan-M2 都把患者模拟器做成了奖励来源。
- **核心问题**：模拟器的真实性没有共识度量。PatientHub（2026）正是为统一评估而提出的。
- **学术切入**：门槛最低、空间最大。用户模拟器的评估本来就是对话系统研究中的老问题。

**2.5 EHR / 结构化病历基础模型（65.3）**
- **是什么**：把一个人的就诊、诊断、化验、用药序列当作「句子」，训练 GPT 式模型来预测下一个医疗事件。
- **为什么是现在**：2025 年有三件事：
  - Microsoft 在 MIMIC-IV 上发现缩放律。
  - Epic 与 Microsoft 的 CoMET 在1.18亿患者上验证了幂律缩放。
  - Delphi-2M（Nature）可预测1000多种疾病，并能生成20年的合成轨迹。
- **瓶颈**：数据。公开的 EHRSHOT 只有6,739名患者；CLMBR 的权重需要签协议才能使用。

**2.6 基因组语言模型（63.8）**
- **是什么**：在 DNA 序列上训练的语言模型。
- **为什么是现在**：
  - Evo 2 有40B 参数，在约9万亿碱基对上训练，上下文达100万 token，权重和数据全部开放，2026 年发表于 Nature。
  - DeepMind AlphaGenome 于2026-01发表于 Nature 并开源。
- **争议**：DART-Eval 发现 DNA LM 在多数任务上相对简单基线没有显著收益。NVIDIA 复现 Evo 2 的 BRCA1 示例时注明，多数配置下结果「近乎随机」。
- **学术切入**：适合做可解释性和严格评测，但需要补生物学知识。

**2.7 可穿戴与生理信号基础模型（62.9）**
- **是什么**：在心电、PPG、加速度计等信号上做自监督预训练。
- **为什么是现在**：
  - Google LSM 在4000万小时数据上证明了缩放律；SensorLM 做了传感器与语言的对齐。
  - Apple 的行为基础模型使用了25亿小时数据。
  - 2025-09 Apple Watch 高血压提醒获 FDA 许可，但敏感度只有41.2%。
- **瓶颈**：大规模数据被 Apple、Google 私有。开放的有 ECG-FM（150万份心电，开放权重）。

**2.8 多模态/通用医学基础模型（59.9）**
- **是什么**：可以同时看影像、读文本、写报告的医学视觉语言模型。
- **代表工作**：
  - 2025-05 Google 开放 MedGemma：4B 模型在 MIMIC-CXR 报告生成上的 RadGraph F1 为29.5-30.3，达到 SOTA。
  - 2026-01 MedGemma 1.5 扩展到 3D CT/MRI 和全切片病理。
  - 3D 方向有 Merlin、Pillar-0（Pillar-0 的数字为开发方自报，待核实）。
- **评价**：属于已建立的赛道。学术界拿到开放权重后，可以做报告事实性和 3D 理解。

**2.9 医疗 AI 监管科学与部署后监测（53.0）**
- **是什么**：研究 AI 医疗器械上线后如何检测性能漂移、如何管理模型更新。
- **为什么是现在**：
  - FDA 的 AI 设备清单 2025-05 为1,016个，2025 年末约1,450个（口径不一）。
  - 2025-11 FDA 咨询委员会讨论了生成式 AI 设备的全生命周期监测。
  - 2026-08 FDA 发布生成式 AI 设备讨论稿，提出定期再基准化和漂移监测，意见征集截至2026-10-19。
- **适合人群**：做统计 ML 和监测方法的人。

**2.10 病理基础模型（46.0）**
- **是什么**：在数十万张全切片病理图像上训练的视觉基础模型，代表有 UNI、Virchow、Prov-GigaPath、CONCH、TITAN。
- **为什么分数不高**：已进入「基准测试与审视期」。
  - 2026 年一项包含12个模型的基准显示，规模收益趋平。
  - 多数模型的嵌入按医院聚类，而不是按癌种聚类。
  - 商业侧，Tempus 以8125万美元收购了曾融资2.2亿美元的 Paige。

**2.11 医学知识编辑与持续更新（44.3）**
- **是什么**：在不重训模型的情况下，更新过时的医学知识，例如指南变更。
- **现状**：有 MedLaSA、MedEditBench、MedVersa（批量编辑）等基准。但参数编辑对无关知识有副作用，而且面临被 RAG 和工具调用替代的结构性风险。本次检索没有找到以「指南版本更替」为核心的基准，这本身就是一个空白。

**2.12 环境式临床文档 / AI Scribe（43.0）**
- **是什么**：AI 在诊室旁听医患对话，自动生成病历。
- **现状**：
  - 产业爆发：Abridge 的估值4个月内从27.5亿美元涨到53亿美元。
  - UCLA 的随机对照试验显示，书写时间相对对照组多降约9.5%，效果温和。
  - 2026 年一项审计发现31.3%的笔记有经核实的错误。
- **学术空间**：只剩错误审计和评测。

**2.13 医学影像分割基础模型（35.3）**
- **代表工作**：MedSAM2 用45.5万对 3D 数据训练，可降低85%以上的标注成本。
- **评价**：nnU-Net Revisited 表明，严格验证后许多架构增益并不成立。属于成熟赛道。

**2.14 隐私保护/联邦医疗学习（26.6）**
- 2026 年的范围综述中，772篇论文里只有3.2%是真实部署，瓶颈是基础设施和组织问题，而不是算法。
- 隐私问题正在转向「本地部署 LLM」：PhysioNet 已禁止把 MIMIC 数据经 API 发往第三方 LLM。

---

## 3. 关键数据集与基准（含获取要求）

| 名称 | 类型 | 获取要求 / 备注 |
|---|---|---|
| **MIMIC-IV** / MIMIC-IV-Note / MIMIC-CXR / MIMIC-IV-ECG | ICU/急诊 EHR、临床笔记、胸片、心电 | PhysioNet **认证访问**：注册账号，完成 **CITI「Data or Specimens Only Research」** 人类受试者课程（需提交完成报告），提供机构隶属与推荐人信息，再按数据集签署 **DUA**。另有100名患者的 demo 版无需认证。**2025-09 PhysioNet 明确：不得将 MIMIC 数据通过 API 发送给第三方 LLM 服务**，推荐本地部署模型。**2025-07 起依美国 DOJ 数据安全计划，对来自中国大陆、香港、澳门等「关注国家」IP 或机构的用户屏蔽部分受控数据集**，具体受影响的数据集列表需向 PhysioNet 确认（待核实）。 |
| eICU-CRD | 多中心 ICU | 同为 PhysioNet 认证访问（背景知识） |
| **MedQA**（USMLE）、MedMCQA、PubMedQA | 选择题问答 | 公开。MedQA 已饱和（新模型 >95%），Vals.ai 已将其归档；只适合作为合理性检查。MedMCQA 为背景知识。 |
| **HealthBench**（含 Consensus/Hard） | 多轮对话 + 医生 rubric | 开源（OpenAI simple-evals，背景知识）；5000段对话，评分需 LLM 评委（原文用 GPT-4.1） |
| **HealthBench Professional** | 医生真实工作任务 | 开放基准，525个任务（2026-04） |
| **MedHELM** | 121个真实临床任务、35-37个基准 | 框架开源；部分子基准依赖受限数据（背景知识） |
| **MedAgentBench**（v1/v2）、FHIR-AgentBench | FHIR EHR 智能体环境 | 开源，使用合成患者，无需认证，是最友好的智能体入口 |
| **AgentClinic**（MedQA/NEJM 版） | 患者模拟 + 诊断对话 | 开源 |
| EHR-Complex、PhysicianBench | EHR 智能体 | EHR-Complex 基于 MIMIC-IV，需认证；PhysicianBench 访问方式待核实 |
| **EHRSHOT** + CLMBR-T-base / MOTOR | 纵向结构化 EHR 少样本基准 | Stanford 研究数据使用协议；模型权重在 HF 上需签协议 |
| **MEDS** / MEDS-DEV | EHR 机器学习数据标准与基准 | 开源工具链 |
| MedHallu | 医学幻觉检测 | 公开（1万对） |
| CheXpert / CheXpert Plus | 胸片 | Stanford 研究使用协议（背景知识） |
| TCGA | 病理切片 + 基因组 | 公开（背景知识）；注意与私有预训练数据可能重叠 |
| PTB-XL | 12导联心电 | PhysioNet 开放访问（背景知识） |
| UK Biobank | 队列数据（Delphi-2M 训练数据） | 需申请并付费（背景知识）；同样可能受 DOJ 规则影响（待核实） |
| OpenGenome2 / Evo 2 权重 | 基因组 | 完全开放 |
| MedGemma / MedSigLIP | 医学多模态权重 | Hugging Face 上需同意 HAI-DEF 使用条款 |
| CMB、CMExam、Huatuo-26M 等中文医学数据 | 中文医学问答 | 公开（背景知识）；对中国研究者是 MIMIC 受限后的重要替代 |

---

## 4. 医疗方向特有的坑

1. **数据获取**
   - PhysioNet 认证需要完成 CITI 培训并签 DUA，一般要花数天到数周（背景知识）。
   - MIMIC 数据**不能**直接发给 GPT/Claude 等云端 API，只能用本地开源模型。这会实质影响实验设计，例如不能用闭源模型做 MIMIC 上的零样本基线。
   - **对位于中国的研究者尤其关键**：2025-07 起 PhysioNet 依美国 DOJ 数据安全计划屏蔽了部分受控数据集。动手前应先确认能否访问，并准备替代方案：中文公开数据、合成 FHIR 环境、与国内医院合作。
   - 真实院内 EHR、诊室对话音频、可穿戴原始波形几乎都在企业或医院手里。
2. **IRB / 伦理审查**
   - 只要涉及真实患者数据，即使是回顾性数据，通常也需要 IRB 批准或豁免（背景知识）。
   - 前瞻研究要预注册，例如 AMIE 的 BIDMC 研究注册号为 NCT06911398，从启动到完成跨度近一年。
   - 纯合成环境（MedAgentBench、AgentClinic、HealthBench）可以绕开这一步，是 ML/NLP 研究者最快的起点。
3. **临床验证缺口**
   - 基准分数不等于临床获益。AMIE 的 Nature 研究用的是演员扮演的患者；实践类基准得分只有45-69%；AI Scribe 的随机对照试验效果仅约9.5%。
   - 审稿人（尤其医学期刊）会追问前瞻性证据、子群体公平性和失败模式。
   - 报告规范可参考 TRIPOD-LLM、CONSORT-AI、DECIDE-AI（背景知识）。
4. **监管**
   - 截至2025年末，FDA 尚未授权任何生成式 AI 临床设备（律所总结，待核实）。
   - 已获许可的 AI 设备约1,450个，以影像类为主。
   - 中国 NMPA 对 AI 医疗器械也有三类证要求（背景知识）。
   - 学术论文不受监管约束，但如果目标是落地，越早了解 PCCP（预定变更控制计划）和上市后监测越好。
5. **发表周期与评价体系**
   - ML 会议（NeurIPS/ICLR/ACL）的周期是3-6个月；医学期刊（Nature Medicine、NEJM AI、JAMA 系列、Lancet Digital Health）往往要6-18个月，看重临床意义（背景知识）。
   - 专门的交叉会议有 ML4H、CHIL、MLHC（背景知识）。
   - 建议两条线并行：方法在 ML 会议快速发表，临床验证与 MD 合作者投医学期刊。
6. **MD 合作**
   - 高质量的 rubric 和评测离不开医生：HealthBench 动用了262名医生，MedHELM 有29名临床医生参与，HealthBench Professional 使用了医生基线。
   - 没有临床合作者的论文，选题容易「技术上漂亮、临床上无关」。应尽早找一位愿意每周花1小时的临床合作者。
7. **被大厂吸收与利益冲突**
   - 推理模型、AI Scribe、通用多模态模型都面临前沿实验室直接覆盖的风险。
   - 很多「SOTA」数字由厂商自报，例如 MAI-DxO 的85%、Baichuan-M3 的成绩，以及 HealthBench Professional 中 GPT-5.4 超过医生的结果。
   - 学术工作应尽量选「大厂不愿做或不便做」的题目：独立评测、失败模式、低资源语言、本地部署、可复现基准。
8. **可复现性**
   - 病理基础模型的预训练数据可能与评测数据重叠；Evo 2 的零样本结果依赖硬件和精度配置；分割领域存在弱基线问题。
   - 一定要与强基线（nnU-Net、保守性分数、CADD 等）比较。

---

## 5. 给 ML/NLP 研究者的 Top 3 建议

1. **临床智能体，以患者模拟器为环境（74.7 + 66.0）**
   - 这是增长最快、能力拐点最明确的方向。
   - 切入点：在 MedAgentBench、AgentClinic 等合成环境里，用开源模型做多轮工具调用和问诊策略的 RL，重点报告 pass^k 可靠性。
   - 患者模拟器的保真度研究可以作为配套的低门槛子课题。
2. **医疗 LLM 评测、安全与幻觉（70.7）**
   - 学术比较优势最大：算力和数据门槛最低，NLP 的评测方法论可以直接迁移。
   - 可做的题目：LLM-judge 校准、rubric 盲区、中文或低资源语言的 HealthBench 式基准、对抗性幻觉。
3. **EHR 基础模型（65.3），作为「下一个 GPT-3 时刻」的押注**
   - 2025 年刚出现缩放律，社区小，与 LM 的方法同构（tokenization、缩放、生成）。
   - 代价是数据门槛，需要尽早解决数据访问并找到医院合作者。
   - 如果数据确实无法获得，可以换成第3名的医学推理模型（67.7），但要接受较高的被吸收风险。

---

## 6. Sources

**临床智能体 / 诊断对话**
- AMIE（Nature 2025）：https://ideas.repec.org/a/nat/nature/v642y2025i8067d10.1038_s41586-025-08866-7.html ； https://research.google/pubs/towards-conversational-diagnostic-ai/
- AMIE BIDMC 前瞻研究：https://arxiv.org/abs/2603.08448 ； https://research.google/blog/exploring-the-feasibility-of-conversational-diagnostic-ai-in-a-real-world-clinical-study/ ； https://clinicaltrials.gov/study/NCT06911398
- MedAgentBench：https://arxiv.org/abs/2501.14654 ； https://hai.stanford.edu/news/stanford-develops-real-world-benchmarks-for-healthcare-ai-agents
- MedAgentBench v2：https://psb.stanford.edu/psb-online/proceedings/psb26/chen_eric.pdf
- MAI-DxO：https://microsoft.ai/news/the-path-to-medical-superintelligence/
- PhysicianBench：https://arxiv.org/html/2605.02240v1
- EHR-Complex：https://arxiv.org/html/2606.23301
- CliniCARE-Bench：https://arxiv.org/pdf/2608.07796
- FHIR-AgentBench：https://arxiv.org/pdf/2509.19319
- 医疗 AI 智能体综述：https://www.sciencedirect.com/science/article/pii/S1532046426000699
- OpenAI × Penda Health：https://openai.com/index/ai-clinical-copilot-penda-health

**评测 / 安全 / 幻觉**
- HealthBench：https://arxiv.org/abs/2505.08775 ； https://openai.com/index/healthbench/
- HealthBench Professional：https://arxiv.org/pdf/2604.27470 ； https://openai.com/index/making-chatgpt-better-for-clinicians/
- MedHELM：https://arxiv.org/pdf/2505.23802v2 ； https://hai.stanford.edu/news/holistic-evaluation-of-large-language-models-for-medical-applications
- MedQA 归档（Vals.ai）：https://www.vals.ai/benchmarks/medqa-08-12-2025
- 39个临床基准综述（JMIR 2025）：https://www.jmir.org/2025/1/e84120
- MedHallu：https://arxiv.org/abs/2502.14302
- 临床笔记幻觉率（npj Digit Med）：https://doi.org/10.1038/s41746-025-01670-7
- When Rubrics Fail：https://arxiv.org/pdf/2609.12718
- Medmarks：https://icml.cc/virtual/2026/72057
- ChatGPT Health：https://www.unite.ai/openai-launches-chatgpt-health-for-230-million-weekly-users ； https://techcrunch.com/2026/07/23/openai-makes-chatgpt-health-available-to-all-u-s-users/

**医学推理**
- HuatuoGPT-o1：https://arxiv.org/abs/2412.18925v1
- Med-R1：https://arxiv.org/html/2503.13939v4
- MedReason：https://arxiv.org/html/2504.00993v1
- Fleming-R1：https://arxiv.org/pdf/2509.15279v1
- Baichuan-M2：https://arxiv.org/pdf/2509.02208
- Baichuan-M3：https://arxiv.org/pdf/2602.06570
- 医学推理综述：https://arxiv.org/pdf/2508.00669 ； https://arxiv.org/pdf/2508.19097

**多模态 / 影像**
- MedGemma 技术报告：https://arxiv.org/pdf/2507.05201
- MedGemma 1.5：https://papers.cool/arxiv/2604.05081
- Merlin：https://www.huggingface.co/stanfordmimi/Merlin/tree/main
- MedSAM2：https://arxiv.org/abs/2504.03600v1
- nnU-Net Revisited：https://arxiv.org/abs/2404.09556v2

**病理**
- 鲁棒性基准（12个模型）：https://arxiv.org/abs/2607.04401
- 病理基础模型失败分析综述：https://arxiv.org/html/2510.23807v1
- CellPath-Bench：https://arxiv.org/pdf/2608.21060
- 肾脏病理基准：https://arxiv.org/pdf/2603.15967
- Tempus 收购 Paige：https://www.fiercehealthcare.com/medtech/tempus-claims-ai-pathology-developer-paige-81m-deal
- Bioptimus 融资：https://www.bioptimus.com/news/bioptimus-hits-76m-funding

**EHR 基础模型**
- CoMET：https://arxiv.org/html/2508.12104v3
- EHR 缩放律：https://arxiv.org/pdf/2505.22964
- Delphi-2M：https://www.ukbiobank.ac.uk/publications/learning-the-natural-history-of-human-disease-with-generative-transformers/
- Epic 宣布：https://www.healthcareitnews.com/news/epic-unveils-ai-agents-showcases-new-foundational-models
- EHRSHOT：https://arxiv.org/pdf/2307.02028
- MEDS：https://www.ohdsi.org/wp-content/uploads/2026/05/Meds-Slidedeck.pdf

**可穿戴 / 生理信号**
- LSM：https://arxiv.org/pdf/2410.13638
- LSM-2：https://research.google/blog/lsm-2-learning-from-incomplete-wearable-sensor-data/
- SensorLM：https://alphaxiv.org/abs/2506.09108
- Apple 行为基础模型：https://arxiv.org/html/2507.00191v1
- ECG-FM：https://pubmed.ncbi.nlm.nih.gov/41113504/
- ECGFounder：https://arxiv.org/pdf/2410.04133
- Apple 高血压提醒：https://www.apple.com/sg/health/pdf/Hypertension_Notifications_Validation_Paper_September_2025.pdf ； https://www.aafp.org/pubs/afp/afp-community-blog/entry/smartwatch-screening-for-hypertension.html

**AI Scribe**
- Abridge 融资：https://oodaloop.com/briefs/technology/abridge-whose-ai-app-takes-notes-for-doctors-valued-at-5-3-billion-at-funding
- UCLA RCT：https://www.uclahealth.org/news/release/ucla-study-finds-ai-scribes-may-reduce-documentation-time
- 倦怠研究：https://pmc.ncbi.nlm.nih.gov/articles/PMC12492056/
- 笔记错误研究：https://medinform.jmir.org/2026/1/e86474 ； https://huggingface.co/papers/2608.31017
- 数字健康投资：https://www.fiercehealthcare.com/digital-health/jpm26-digital-health-funding-hit-142b-2025-ai-companies-taking-lions-share-dollars

**患者模拟器**
- AgentClinic：https://arxiv.org/abs/2405.07960v4
- DoctorAgent-RL：https://arxiv.org/abs/2505.19630v3
- PatientHub：https://arxiv.org/pdf/2602.11684
- 虚拟患者综述（JMIR 2026）：https://medinform.jmir.org/2026/1/e79039/PDF
- 虚拟患者鲁棒性研究（Cureus 2026）：https://assets.cureus.com/uploads/original_article/pdf/485892/20260618-261691-ziqwms.pdf

**基因组**
- Evo 2（Nature 2026）：https://astrobiology.com/2026/03/with-evo-2-ai-can-model-and-design-the-genetic-code-for-all-domains-of-life.html
- AlphaGenome：https://gigazine.net/gsc_news/en/20260129-google-deepmind-alphagenome-open-source/ ； https://www.genomeweb.com/informatics/google-alphagenome-users-scrutinize-ai-models-ability-predict-variant-effects
- DART-Eval：https://arxiv.org/abs/2412.05430v1
- GPN-MSA：https://www.biorxiv.org/content/10.1101/2023.10.10.561776.full.pdf
- NVIDIA Evo 2 复现说明：https://docs.nvidia.com/bionemo-framework/latest/main/examples/bionemo-evo2/zeroshot_brca1/

**监管**
- FDA 设备数量：https://jmai.amegroups.org/article/view/10846/html ； https://intuitionlabs.ai/articles/fda-ai-medical-device-tracker
- DHAC 2025-11：https://hlc.com/en/publications/fdas-digital-health-advisory-committee-weighs-guardrails-for-generative-ai-in-mental-health-devices
- 真实世界性能征求意见：https://healthcarefinancenews.com/news/fda-requests-comment-performance-ai-enabled-medical-devices
- 2026-08 生成式 AI 讨论稿：https://www.arnoldporter.com/en/perspectives/advisories/2026/09/fda-seeks-public-feedback-on-regulatory-approach-for-generative-ai-enabled-medical-devices

**联邦学习 / 知识编辑**
- 联邦学习系统综述（2024）：https://pmc.ncbi.nlm.nih.gov/articles/PMC10897620
- 联邦学习范围综述（2026）：https://epjst.epj.org/articles/epjst/abs/first/11734_2026_Article_2475/11734_2026_Article_2475.html
- 医学影像联邦学习差距分析：https://orbilu.uni.lu/bitstream/10993/65947/1/Paper-0007.pdf
- MedLaSA：https://www.arxiv.org/abs/2402.18099
- MedEditBench：https://arxiv.org/abs/2506.03490v2
- MedREK / MedVersa：https://arxiv.org/html/2510.13500v2
- MultiMedEdit：https://arxiv.org/html/2508.07022v1

**数据访问**
- MIMIC 访问 FAQ：https://mimic.mit.edu/docs/faq/how-to-get-access.html
- PhysioNet LLM 使用规定：https://physionet.org/news/post/llm-responsible-use/
- PhysioNet DOJ 数据安全计划限制：https://physionet.org/news/post/data-security-program-1/
- MIMIC-IV DUA：https://www.physionet.org/content/mimiciv/view-dua/2.2/
