# 深度调研：持续学习与测试时训练 / 测试时记忆（Continual Learning & Test-Time Training / Memory）

> 调研日期：2026-10-06。信息来源以网页搜索摘要为主（arXiv 等原文未能直接抓取）。标注“(背景知识)”的内容来自作者既有知识，“(待核实)”表示细节或链接未经本次检索确认。

---

## 1. 一句话定义、它解决什么问题、为什么是现在

**一句话定义**：让基础模型在**部署之后**仍能把新信息、新技能、新经验持续写入自身（权重、快权重或可训练的记忆模块），同时不遗忘旧能力——其中“测试时训练（TTT）”是把“在推理时对当前输入做梯度更新”变成模型的标准组成部分。

**解决的问题**：
- **权重在部署后冻结**：今天的 LLM 训练完就停止学习；知识有截止日期，用户纠正、任务反馈、一次次失败的经验都不会沉淀成能力。Dwarkesh Patel 在 2025-06 的文章中把持续学习列为 AGI 的首要瓶颈：模型无法像人一样“在岗位上学习”[S21]。
- **上下文窗口不是记忆**：上下文是易失的工作记忆，对话结束即清空；它的代价是二次（注意力）或线性增长的 KV cache，而且“放进上下文”≠“学会”。参数化知识与上下文之间“没有通路相连”[S21]。把 Markdown 笔记在会话间传递只是权宜之计（Dwarkesh 2026-08）[S22]。
- **经典深度学习的两大顽疾**：灾难性遗忘（EWC, 2017）[S16] 与可塑性丧失（Dohare et al., Nature 2024）[S17]。

**为什么是现在**：
1. **架构侧趋同**：线性注意力 / SSM / DeltaNet 被证明都是“测试时在线回归”的特例（test-time regression, 2025-01）[S9]，TTT 层、Titans、ATLAS 把“记忆=在线优化”做成可扩展的序列层；TTT-E2E（2025-12）在 3B 规模上展示了与全注意力同样的上下文扩展曲线，且 128K 时推理快 2.7×[S5]。
2. **推理/泛化侧证据**：ARC 上的 TTT 让 8B 模型达到 53%，集成后 61.9%（与人类平均持平）[S6]；ARC Prize 2025 冠军 NVARC 仍以 TTT 模型为核心[S24]。
3. **后训练范式转向 RL**：RL 被发现比 SFT 遗忘更少（RL's Razor）[S12]，使“从部署经验在线 RL”变得可行；Cursor 已在生产中用在线 RL 每天多次更新 Tab 模型[S19]。
4. **叙事与资本**：Silver & Sutton《Era of Experience》（2025-04）[S20]；Google 把 Nested Learning 定位为“持续学习的新范式”[S4]；2026 年出现专门的持续学习创业公司（Trajectory $15M 种子轮，kausable €12M）[S23]。

---

## 2. 技术版图：8 个细分方向

### 2.1 测试时训练作为序列建模层（TTT layers / Titans / 线性注意力统一视角）
- **是什么**：把 RNN 的隐状态换成一个“小模型”（线性层/MLP），每读入一个 token 就用自监督损失做一步梯度更新——隐状态即快权重，更新规则即优化器。
- **代表作**：
  - *TTT layers*（Sun et al., Stanford/UCSD/Berkeley/Meta, 2024-07；ICML 2025）：TTT-Linear / TTT-MLP，125M–1.3B 规模，与 Transformer 一样随上下文增长持续降低困惑度，而 Mamba 在 16K 后停滞。https://arxiv.org/abs/2407.04620 [S1]
  - *Titans*（Behrouz, Zhong, Mirrokni, Google Research, 2025-01）：神经长期记忆模块 + 注意力的混合架构，用“惊奇度”（梯度）驱动写入。https://arxiv.org/abs/2501.00663 [S2]；后续 *MIRAS*（2025-04）把架构拆为记忆结构/注意偏置目标/保留门/记忆学习算法四个设计轴[S10]；*ATLAS*（2025-05，ICML 2026）优化整个上下文窗口而非单 token，在 BABILong 1000 万长度上比 Titans 提升 +80% 准确率 https://arxiv.org/abs/2505.23735 [S3]。
  - *TTT-E2E*（Tandon et al., Stanford/NVIDIA/Berkeley/UCSD/Astera, 2025-12）：不改架构，直接用标准 Transformer + 滑窗注意力，在测试时对上下文做下一词预测训练，训练时用元学习优化初始化；3B/164B tokens 下与全注意力同样扩展，Mamba 2 / Gated DeltaNet 不能。https://arxiv.org/abs/2512.23675 [S5]
  - *Test-time regression*（Wang, Shi, Fox, Stanford, 2025-01）：线性注意力、门控变体、SSM、softmax 注意力都是测试时回归的特例；Gated DeltaNet ≡ 带 L2 正则的 SGD 回归。https://arxiv.org/abs/2501.12352 [S9]
  - 应用扩展：*One-Minute Video Generation with TTT*（CVPR 2025），人评比 Mamba2/Gated DeltaNet/滑窗注意力高 34 Elo [S11]；2026 年的 In-Place TTT（2604.06169）、TTT-NTP（2606.21803）把快权重写入预训练 LLM 的 MLP [S25]。
- **现状**：最成熟、最“工程化”的子方向，已有 kernel 生态（flash-linear-attention，背景知识）；但仍以 ≤3B 规模为主，前沿闭源模型是否采用不可知。
- **核心开放问题**：内循环优化器/目标的设计（为何 NTP 最好？）、硬件效率（大 chunk 并行 vs 表达力）、记忆容量与“遗忘门”的理论刻画，以及在 >10B 规模和 agent 长轨迹上是否仍然成立。

### 2.2 测试时训练用于推理与泛化（ARC TTT）
- **是什么**：对每个测试实例，用其少量示例（加数据增强、留一构造）临时微调 LoRA，再推理。
- **代表作**：
  - *The Surprising Effectiveness of TTT for Few-Shot Learning*（Akyürek et al., MIT, 2024-11；ICML 2025）：8B 模型在 ARC 公开验证集 53%，与程序合成集成达 61.9%；三要素：相似任务预微调、辅助任务格式与增强、逐实例训练。https://arxiv.org/abs/2411.07279 [S6]
  - ARC Prize 2024/2025：2025 冠军 NVARC 在 ARC-AGI-2 上约 24%，方案是“改进的 Architects 式 TTT 模型 + TRM 组件”的集成；论文奖包括 *Test-time Adaptation of Tiny Recursive Models* [S24]。
- **现状**：在 ARC 类任务上几乎是标配；对通用推理（数学、代码）中 TTT 与“长链思维 + 采样”的性价比比较尚无定论。
- **开放问题**：TTT 增益有多少来自“额外算力”而非“学习”（需要等算力对照）；如何为没有示例对的任务自动构造测试时目标。

### 2.3 自我编辑 / 自适应 LLM（SEAL）
- **是什么**：模型自己生成“训练数据 + 更新指令”（self-edit），用 SFT 更新自身权重；外环用 RL 以“更新后下游表现”为奖励来训练生成 self-edit 的能力。
- **代表作**：
  - *SEAL*（Zweiger, Pari, Guo, Akyürek, Kim, Agrawal, MIT, 2025-06；NeurIPS 2025）：SQuAD 知识注入从基线提升到 47.0%，超过用 GPT-4.1 生成合成数据的 46.3%；ARC 子集上 Llama-3.2-1B 达 72.5%（ICL 0%，未优化 self-edit 20%）。https://arxiv.org/abs/2506.10943 [S7]
  - *Cartridges / self-study*（Eyuboglu et al., Stanford Hazy Research, 2025-06）：为语料离线训练一个小 KV cache，合成对话 + 上下文蒸馏；匹配 ICL 质量，内存省 38.6×、吞吐 26.4×，MTOB 有效上下文从 128K 扩到 484K，可组合。https://arxiv.org/abs/2506.06266 [S13]
  - *On-Policy Distillation*（Thinking Machines, 2025-10）：Qwen3-8B 在内部文档上中训练后 IF-eval 从 85% 掉到 79%，用 on-policy distillation 恢复到 83%，QA 同时升到 41%——给出“学新知识 + 恢复行为”的实用配方 [S14]。
- **现状**：概念吸引力最高，但 SEAL 自承在连续多次 self-edit 下仍有遗忘，且每次 RL 外环评估很昂贵（背景知识，待核实）。
- **开放问题**：多轮/长期的自我编辑如何不崩溃；奖励来自哪里（无标注部署场景）；self-edit 的安全审计。

### 2.4 参数化记忆与长期记忆架构（memory layers、Nested Learning / Hope）
- **是什么**：在模型中加入可稀疏读写、可按不同频率更新的记忆参数，使“写入新知识”局部化，从结构上降低干扰。
- **代表作**：
  - *Nested Learning: The Illusion of Deep Learning Architectures*（Behrouz, Mirrokni 等, Google Research, NeurIPS 2025；博客 2025-11）：把模型视为多层嵌套优化问题，架构与优化器是不同“层级”；提出 Continuum Memory System（多频率更新的记忆谱）与 Hope（Titans 变体、自修改的递归架构），在语言建模/常识推理上困惑度更低、准确率更高 [S4]。
  - *Continual Learning via Sparse Memory Finetuning*（Meta FAIR + Berkeley, 2025-10）：只更新被新知识高度激活（相对预训练使用频率）的记忆槽；学同样多新事实时，NaturalQuestions F1 全量微调下降 89%、LoRA 下降 71%，稀疏记忆微调仅下降 11%。https://arxiv.org/abs/2510.15103 [S8]
  - *Memory Layers at Scale*（Meta, 2024-12）(背景知识，待核实)。
- **现状**：Meta 的稀疏记忆微调是目前“参数化持续学习”最干净的正面证据；Nested Learning 理论框架宏大，独立复现与大规模验证仍少。
- **开放问题**：记忆槽的容量/寻址/整合（类似海马-皮层的 consolidation）；多频率更新的调度原理；与 MoE 的关系。

### 2.5 LLM 持续预训练与持续后训练中的遗忘
- **是什么**：在新语料（新领域、新语言、新时间段）上继续预训练，或在一系列新任务上持续 SFT/RL，同时保留通用能力。
- **代表作**：
  - *Simple and Scalable Strategies to Continually Pre-train LLMs*（Ibrahim et al., 2024-03, TMLR）：LR 重新 warmup + 重新衰减 + 回放旧数据即可匹配从头重训，在 405M 与 10B 上验证。https://arxiv.org/abs/2403.08763 [S15]
  - *LoRA Learns Less and Forgets Less*（Biderman et al., 2024-05, TMLR）：LoRA 在代码/数学上明显弱于全量微调，但更好保留域外能力；全量微调学到的扰动秩高出常见 LoRA 10–100 倍 [S18]。
  - *RL's Razor*（2025-09, NeurIPS 2025）：同等新任务准确率下 RL 遗忘更少；遗忘量由新任务分布上微调策略与基座的 KL 决定，on-policy 更新偏向 KL 最小解。https://arxiv.org/abs/2509.04259 [S12]；同期 *RFT Naturally Mitigates Forgetting in Continual Post-Training*（2507.05386）。
  - 反方证据：*RL Forgets! Towards Continual Policy Optimization*（2026-07, 2607.04364）、多模态持续 RL 基准显示 RL 仍会灾难性遗忘 [S12]。
  - 背景：TRACE 基准上 Llama2-chat-13B 的 GSM8K 从 28.8% 掉到 2% [S26]；*Loss of plasticity*（Nature 2024）[S17]。
- **现状**：工业界最刚需（每次版本迭代都在做），但多为内部经验，公开的规模化研究偏少。
- **开放问题**：持续 RL 的遗忘与可塑性；“表面遗忘”（格式/对齐丢失）与“真遗忘”（知识丢失）的区分；回放数据不可得时的替代。

### 2.6 知识编辑（Model / Knowledge Editing）
- **是什么**：对特定事实做外科式修改（“定位-编辑”），不重训。
- **代表作**：ROME（2022, 背景知识）→ *MEMIT*（Meng et al., Northeastern/MIT, ICLR 2023）：一次编辑上万条事实，GPT-J/NeoX 上验证 https://memit.baulab.info/ [S27]；*AlphaEdit*（USTC/NUS, ICLR 2025）：把扰动投影到“保留知识”的零空间，一行代码让多数定位-编辑方法平均提升 36.7% https://arxiv.org/abs/2410.02355 [S28]。
- **现状**：单跳事实编辑基本解决；多跳推理传导（MQuAKE 类，背景知识）、顺序大批量编辑下的模型崩溃仍是难题。社区热度已部分转向 2.3/2.4 的“通过训练写入知识”。
- **开放问题**：编辑的涟漪效应与一致性；与持续微调的统一（编辑≈约束极强的持续学习）。

### 2.7 从部署经验中在线学习 / 经验时代
- **是什么**：把用户交互、环境反馈、任务成败作为持续训练信号——在线 RL、经验库、技能沉淀。
- **代表作**：
  - *Welcome to the Era of Experience*（Silver & Sutton, DeepMind, 2025-04）：智能体应从“经验流”中长期学习，而非依赖静态人类数据 [S20]。
  - *Cursor Tab online RL*（2025，月份待核实）：每天多次向用户推送新模型，用接受/拒绝信号做策略梯度 https://cursor.com/en/blog/tab-rl [S19]。
  - 冻结权重路线：*Learning on the Job*（2026-07, 2607.22157），用外部记忆把结果裁决与事后纠正转化为能力，单次成功率达静态 RAG 的 2.6× [S29]；Evo-Memory（2025-11）的 ExpRAG / ReMem 基线 [S29]。
  - 产业：Trajectory（用产品使用信号持续训练 agentic 模型）[S23]。
- **现状**：工业落地最快（推荐系统式的“在线学习”回归 LLM），但学术界缺少可共享的真实部署流；“权重更新”与“外部记忆/技能文件”两条路线竞争激烈。
- **开放问题**：噪声/对抗性用户反馈下的稳健性；个性化与全局模型的分离；隐私与数据投毒。

### 2.8 持续学习的评测
- **是什么**：衡量“学得进 + 不遗忘 + 能迁移 + 随时间累积”的基准。现有长上下文基准测的是检索，不是学习。
- **代表作**：TRACE（2023-10）[S26]、LifelongAgentBench（2025-05）、Evo-Memory（2025-11）、SkillLearnBench（2026-04）、PATH-Bench（2026-08，路径依赖评测）[S29]。
- **开放问题**：缺少“等算力”对照与“与长上下文/RAG 基线公平比较”的协议；缺少真实时间流（真实新知识而非合成事实）的大规模基准。

---

## 3. 关键基准与评测

| 基准 | 测什么 | 链接 |
|---|---|---|
| ARC-AGI-1 / ARC-AGI-2 | 少样本抽象推理，TTT 的主战场 | https://arcprize.org/competitions/2025/archive |
| BABILong | 超长上下文（至 10M）事实推理，Titans/ATLAS 报告 | 背景知识，arXiv 2406.10149（待核实） |
| RULER / Needle-in-a-Haystack | 长上下文检索与多跳 | 背景知识（待核实） |
| SQuAD 知识注入（SEAL 设定） | 读段落→更新权重→闭卷问答 | https://arxiv.org/abs/2506.10943 |
| MTOB | 从一本语法书学新语言（Cartridges 使用） | https://arxiv.org/abs/2506.06266 |
| CounterFact / zsRE | 单事实编辑的有效性/泛化/特异性 | https://memit.baulab.info/ |
| MQuAKE | 编辑后多跳推理是否传导 | 背景知识（待核实） |
| TRACE | LLM 持续指令微调后的遗忘（通用能力/指令遵循） | https://arxiv.org/abs/2310.06762 |
| NaturalQuestions 保留率（SMF 设定） | 注入新事实后的旧知识保留 | https://arxiv.org/abs/2510.15103 |
| LifelongAgentBench | Agent 跨任务终身学习 | https://arxiv.org/abs/2505.11942 |
| Evo-Memory | 流式任务下 agent 自演化记忆的测试时学习 | https://arxiv.org/abs/2511.20857 |
| SkillLearnBench | 从工作经验生成新技能的持续学习 | https://arxiv.org/abs/2604.20087 |
| PATH-Bench | 终身 agent 的路径依赖评测 | https://arxiv.org/abs/2608.01149 |

---

## 4. 主要玩家

**学术界**
- Stanford / UCSD / Berkeley 的 TTT 团队：Yu Sun（TTT 系列一作，现与 NVIDIA 合作）、Xiaolong Wang（UCSD）、Karan Dalal 等 [S1][S11]；Stanford Hazy Research（Chris Ré 组，Cartridges）[S13]；Emily Fox 组（test-time regression）[S9]。
- MIT：Pulkit Agrawal（Improbable AI）、Yoon Kim、Jacob Andreas 相关（Akyürek、Zweiger；ARC TTT 与 SEAL）[S6][S7]；Songlin Yang 等（Gated DeltaNet / flash-linear-attention，背景知识）。
- Alberta / Amii：Rich Sutton、Rupam Mahmood（可塑性丧失、经验时代）[S17][S20]。
- Northeastern Bau Lab（ROME/MEMIT）[S27]；USTC + NUS（AlphaEdit）[S28]；Mila / EleutherAI（持续预训练）[S15]。

**工业实验室**
- Google Research（Behrouz、Mirrokni、Zhong：Titans → MIRAS → ATLAS → Nested Learning/Hope）[S2–S4]；Google DeepMind（Silver：经验时代）。
- Meta FAIR（Sparse Memory Finetuning、Memory Layers）[S8]。
- NVIDIA（TTT-E2E 合作、NVARC ARC Prize 2025 冠军）[S5][S24]。
- Thinking Machines（On-policy distillation 用于持续学习/个性化）[S14]；Cursor（生产级在线 RL）[S19]。
- 各前沿实验室普遍把持续学习视为核心议题，但公开的具体方法很少（Dwarkesh 2026-08 的预测即以此为背景）[S22]。

**创业公司**
- Trajectory（SF，2026-05 $15M 种子，Conviction 领投，Jeff Dean、李飞飞为天使）：基于产品使用信号的持续训练平台 [S23]。
- kausable（欧洲，2026-07 €12M）：反方向——不更新权重，靠少样本推理适应 [S23]。
- 记忆基础设施：Letta（MemGPT 团队）、Mem0、Zep 等（背景知识，走外部记忆路线）。
- Astera Institute（非营利，参与 TTT-E2E）[S5]。

---

## 5. 时间线（2023–2026）

| 时间 | 里程碑 |
|---|---|
| 2023-05 | MEMIT 发表于 ICLR 2023（arXiv 2022-10）：万级事实批量编辑 [S27] |
| 2023-10 | TRACE 基准揭示对齐 LLM 持续微调的严重遗忘 [S26] |
| 2024-03 | 持续预训练“LR 重热 + 重衰减 + 回放”配方匹配重训 [S15] |
| 2024-05 | LoRA Learns Less and Forgets Less [S18] |
| 2024-07 | TTT layers（TTT-Linear/MLP）[S1] |
| 2024-08 | Loss of plasticity 发表于 Nature [S17] |
| 2024-11 | ARC 上 TTT：8B 53%，集成 61.9% [S6] |
| 2025-01 | Titans；test-time regression 统一框架 [S2][S9] |
| 2025-04 | Era of Experience；MIRAS；One-Minute Video TTT [S20][S10][S11] |
| 2025-05/06 | ATLAS；SEAL；Cartridges；Dwarkesh 称持续学习为首要瓶颈 [S3][S7][S13][S21] |
| 2025-09/10 | RL's Razor；Sparse Memory Finetuning；On-policy distillation [S12][S8][S14] |
| 2025-11 | Google 发布 Nested Learning / Hope（NeurIPS 2025）[S4] |
| 2025-12 | TTT-E2E；ARC Prize 2025 NVARC 以 TTT 方案夺冠（ARC-AGI-2 ~24%）[S5][S24] |
| 2026-04~07 | In-Place TTT、TTT-NTP；ATLAS 入选 ICML 2026；“RL Forgets!” 反驳 RL 天然抗遗忘；Trajectory / kausable 融资 [S25][S3][S12][S23] |
| 2026-08 | Dwarkesh《8 Predictions for the Era of Continual Learning》；PATH-Bench [S22][S29] |

---

## 6. 研究机会（按学术实验室适配度排序）

| # | 问题 | 算力 | 难度 | 说明 |
|---|---|---|---|---|
| 1 | **公平评测协议：TTT/持续学习 vs 长上下文 vs RAG vs 等算力采样** | 低 | 中 | 很多增益可能来自额外 FLOPs。建立“等 FLOPs、等延迟、等存储”对照，并用真实时间流新知识（非合成事实）构造基准。高引用潜力，0.5–8B 模型即可。 |
| 2 | **遗忘的机制性刻画：持续 SFT vs RL vs on-policy 蒸馏** | 低–中 | 中 | 在 RL's Razor 与 “RL Forgets!” 的冲突证据之间做受控实验；区分格式/对齐层面的“表面遗忘”与知识遗忘；KL 预测器能否推广到多轮持续 RL。 |
| 3 | **稀疏/局部化写入的参数化记忆** | 中 | 中 | 复现并扩展 Sparse Memory Finetuning：把“选择性写入”迁移到 LoRA/MoE 专家/MLP 行；研究记忆整合（快记忆→慢权重）的调度。 |
| 4 | **测试时训练的内循环设计理论** | 低 | 高 | 在 test-time regression / MIRAS 框架下分析：内循环目标、步长、保留门与容量/遗忘的关系；小规模合成任务（关联回忆）即可出理论+实验论文。 |
| 5 | **多轮自我编辑的稳定性（SEAL 的长期版本）** | 中 | 高 | SEAL 单次有效，连续 N 次如何避免漂移/崩溃？结合回放、KL 约束或 on-policy 蒸馏；奖励来源从“标注 QA”换成自监督信号。 |
| 6 | **无示例任务的测试时目标自动构造** | 中 | 中 | ARC TTT 依赖示例对；对数学/代码/agent 任务，用自生成测试、验证器或环境反馈构造测试时损失，并与等算力 best-of-N 对比。 |
| 7 | **Agent 经验的“权重 vs 外部记忆”选择** | 中 | 中 | 何种经验应写入权重（程序性技能）、何种留在外部记忆（情景事实）？在 Evo-Memory/SkillLearnBench 上做系统对比与混合路由。 |
| 8 | **可塑性维持在 LLM 规模的表现** | 中 | 中 | Continual backprop 等方法在 Transformer 持续预训练/持续 RL 中是否必要；可塑性指标（有效秩、死单元）能否预测持续训练崩溃。 |
| 9 | **自修改模型的安全与可审计性** | 低–中 | 中 | 部署中被投毒的用户反馈、self-edit 植入后门、对齐属性随在线更新退化的检测与回滚；红队基准。 |
| 10 | **大规模 TTT 层/快权重的系统实现** | 高 | 高 | >10B 规模、长 agent 轨迹上的 TTT-E2E / Titans 类架构，kernel、并行与推理服务（每用户状态）设计。更适合与工业合作。 |

---

## 7. 入门路径

### 7.1 十篇必读（按阅读顺序）
1. **Kirkpatrick et al., EWC（PNAS 2017）**——灾难性遗忘与“重要权重少动”这一基本思想 [S16]。
2. **Dohare et al., Loss of Plasticity（Nature 2024）**——持续学习的另一半问题：不是忘，而是学不动 [S17]。
3. **Ibrahim et al., Continual Pre-training Strategies（2024）**——LLM 时代持续预训练的强基线 [S15]。
4. **Sun et al., TTT layers（2024）**——“隐状态即模型、更新即训练”的核心范式 [S1]。
5. **Wang, Shi, Fox, Test-time regression（2025）**——用统一视角理解线性注意力/SSM/TTT [S9]。
6. **Behrouz et al., Titans（2025）**（再读 ATLAS、Nested Learning）——Google 的长期记忆路线 [S2][S3][S4]。
7. **Tandon et al., TTT-E2E（2025）**——不改架构、用元学习 + NTP 实现长上下文的最新结果 [S5]。
8. **Akyürek et al., TTT for Few-Shot Learning / ARC（2024）**——TTT 用于推理泛化的标杆 [S6]。
9. **Zweiger et al., SEAL（2025）**——自我生成训练数据并更新权重 [S7]。
10. **Sparse Memory Finetuning（Meta, 2025）+ RL's Razor（2025）**——后训练遗忘的两条最清晰实证线索 [S8][S12]。

补充：MEMIT / AlphaEdit（知识编辑）、Cartridges（离线上下文蒸馏）、On-policy distillation 博客、Era of Experience。

### 7.2 开源代码库
- TTT 官方：test-time-training 组织下的 ttt-lm-pytorch / ttt-lm-jax（背景知识，链接待核实）；视频版 https://test-time-training.github.io/video-dit [S11]
- flash-linear-attention（fla-org，含 DeltaNet/Gated DeltaNet 等 kernel，背景知识，待核实）
- Titans 非官方实现：lucidrains/titans-pytorch（背景知识，待核实）
- ARC TTT：marc（镜像 https://github.com/standardgalactic/marc [S6]）
- SEAL：https://jyopari.github.io/posts/seal [S7]
- Cartridges：https://github.com/HazyResearch/cartridges [S13]
- AlphaEdit：jianghoucheng/AlphaEdit [S28]；EasyEdit（zjunlp，背景知识，待核实）
- 通用持续学习库：Avalanche（ContinualAI，背景知识）

### 7.3 一个具体的前三个月项目
**题目**：《同等算力下，测试时写入权重真的比长上下文/检索更好吗？——一个时间流知识注入基准与系统对比》
- **第 1 月**：构建数据流——选取模型知识截止后的真实新闻/维基修订（按周切片），自动生成闭卷 QA、多跳 QA 与“旧知识保留”测试集；选 Qwen/Llama 系 1–8B 模型。
- **第 2 月**：实现 5 条基线并统一记账 FLOPs/延迟/存储：(a) 长上下文全塞；(b) RAG；(c) 每周持续 SFT（全量 vs LoRA）+ 回放；(d) SEAL 式自生成数据微调（不训 RL 外环，先用固定 prompt）；(e) Cartridges 式离线上下文蒸馏；可加 (f) on-policy distillation 恢复步骤。
- **第 3 月**：分析“学得进/保得住/能推理”三维曲线随周数的变化，测量 KL 与遗忘的相关性（检验 RL's Razor 的推广），撰写 workshop/主会论文并开源基准。
- **算力**：约 8×A100/H100 量级数周即可；产出既是基准也是机制性结论，对应第 6 节机会 #1、#2。

---

## 8. 风险与争议

1. **增益可能来自算力而非“学习”**：TTT 在测试时额外做了梯度步与增强推理，若不与等 FLOPs 的采样/投票/长思维链比较，结论可能被高估（ARC 冠军方案本身就是大规模集成）[S24]。
2. **可能被“长上下文 + 检索 + 记忆文件”吸收**：Nathan Lambert 的《Contra Dwarkesh》对“持续学习是瓶颈”提出异议，倾向于认为上下文、工具与记忆可获得大部分收益（论点概括为背景知识，待核实，见 [S30]）；kausable 走“不更新权重”路线[S23]；Learning on the Job 显示冻结权重 + 外部记忆即可达 RAG 的 2.6× [S29]。反方（Dwarkesh 2026-08）认为“写 Markdown 文件”不足以胜任整份工作[S22]。
3. **证据仍以小规模为主**：TTT 层、Titans、Hope 的主实验多在 ≤3B；Nested Learning 的“范式”主张缺少独立大规模复现；RL 是否天然抗遗忘已出现相互矛盾的论文[S12]。
4. **自修改模型的安全性**：在线更新让对齐属性可能随时间漂移；用户反馈可被投毒；SEAL 式 self-edit 可能写入后门，审计和回滚比静态模型难得多。
5. **隐私与合规**：把用户数据写进权重后，“被遗忘权”与数据删除更难实现（与机器遗忘研究交叉）。
6. **服务成本**：每用户/每会话独立的快权重或 LoRA 状态对推理基础设施是巨大挑战，可能限制学术成果的落地。
7. **竞争格局**：Dwarkesh 指出持续学习可能成为前沿实验室的护城河（越早部署越多经验）[S22]，意味着最有价值的“部署经验数据”学术界难以获得——学术界更适合做评测、机制与小规模算法。

---

## 9. 来源（Sources）

- [S1] TTT layers: https://arxiv.org/abs/2407.04620 ; https://proceedings.mlr.press/v267/sun25h.html
- [S2] Titans: https://arxiv.org/abs/2501.00663 ; https://research.google/pubs/titans-learning-to-memorize-at-test-time/
- [S3] ATLAS: https://arxiv.org/abs/2505.23735v1 ; https://proceedings.mlr.press/v306/behrouz26b.html
- [S4] Nested Learning / Hope: https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/
- [S5] TTT-E2E: https://arxiv.org/pdf/2512.23675 ; https://x.com/stanfordnlp/status/2010807762893349067 ; https://bdtechtalks.com/2026/01/12/nvidia-end-to-end-test-time-training/
- [S6] ARC TTT: https://arxiv.org/abs/2411.07279 ; https://proceedings.mlr.press/v267/akyurek25a.html ; https://github.com/standardgalactic/marc
- [S7] SEAL: https://arxiv.org/abs/2506.10943 ; https://neurips.cc/virtual/2025/poster/118690 ; https://jyopari.github.io/posts/seal
- [S8] Sparse Memory Finetuning: https://arxiv.org/abs/2510.15103
- [S9] Test-time regression: https://arxiv.org/abs/2501.12352 ; Gated DeltaNet: https://arxiv.org/pdf/2412.06464 ; MesaNet: https://arxiv.org/pdf/2506.05233
- [S10] MIRAS: https://arxiv.org/pdf/2504.13173
- [S11] One-Minute Video TTT: https://arxiv.org/abs/2504.05298 ; https://test-time-training.github.io/video-dit
- [S12] RL's Razor: https://arxiv.org/pdf/2509.04259v1 ; https://neurips.cc/virtual/2025/123874 ; RFT mitigates forgetting: https://arxiv.org/pdf/2507.05386 ; RL Forgets!: https://arxiv.org/pdf/2607.04364
- [S13] Cartridges: https://arxiv.org/abs/2506.06266 ; https://hazyresearch.stanford.edu/blog/2025-06-08-cartridges ; https://github.com/HazyResearch/cartridges
- [S14] On-Policy Distillation（Thinking Machines）: https://thinkingmachines.ai/blog/on-policy-distillation （经二手页面确认）; https://www.maginative.com/article/thinking-machines-claims-30x-cost-cut-for-training-ai-models/
- [S15] Continual pre-training: https://arxiv.org/abs/2403.08763v2 ; https://www.eleuther.ai/papers-blog/simple-and-scalable-strategies-to-continually-pre-train-large-language-models
- [S16] EWC: https://arxiv.org/abs/1612.00796 ; https://deepmind.google/discover/blog/enabling-continual-learning-in-neural-networks/
- [S17] Loss of plasticity: https://arxiv.org/abs/2306.13812v2 ; https://www.amii.ca/updates-insights/loss-of-plasticity
- [S18] LoRA Learns Less and Forgets Less: https://arxiv.org/abs/2405.09673v2
- [S19] Cursor Tab online RL: https://cursor.com/en/blog/tab-rl
- [S20] Era of Experience: https://bdtechtalks.com/2025/04/21/are-we-at-the-cusp-of-a-new-era-for-artificial-intelligence/ ; https://the-decoder.com/the-next-leap-in-ai-depends-on-agents-that-learn-by-doing-not-just-by-reading-what-humans-wrote/
- [S21] Dwarkesh 2025-06: https://www.dwarkesh.com/p/timelines-june-2025 ; https://www.lesswrong.com/posts/YEwzhjFzt3zKctg2F/dwarkesh-patel-on-continual-learning
- [S22] Dwarkesh 2026-08: https://www.dwarkesh.com/p/era-of-continual-learning
- [S23] 创业公司: https://pulse2.com/trajectory-raises-15-million-to-build-a-platform-for-continual-learning/ ; https://tech.eu/2026/07/23/kausable-raises-eur12m-to-rethink-how-ai-learns/
- [S24] ARC Prize 2025: https://arcprize.org/competitions/2025/archive ; ARC Prize 2024 报告: https://arxiv.org/html/2412.04604v2
- [S25] 2026 TTT 进展: https://arxiv.org/html/2604.06169v1 （In-Place TTT）; https://arxiv.org/abs/2606.21803 （TTT-NTP）; https://arxiv.org/pdf/2607.09415 （Self-Guided TTT）; https://arxiv.org/pdf/2606.06906 （EASE-TTT）; 综述 https://arxiv.org/pdf/2609.01679
- [S26] TRACE: https://arxiv.org/abs/2310.06762 ; LLM 持续学习综述: https://arxiv.org/html/2404.16789v3
- [S27] MEMIT: https://memit.baulab.info/ ; https://mlanthology.org/iclr/2023/meng2023iclr-massediting
- [S28] AlphaEdit: https://arxiv.org/abs/2410.02355 ; https://iclr.cc/virtual/2025/poster/30202
- [S29] Agent 持续学习评测: https://arxiv.org/abs/2511.20857 （Evo-Memory）; https://arxiv.org/pdf/2505.11942 （LifelongAgentBench）; https://arxiv.org/html/2604.20087v1 （SkillLearnBench）; https://arxiv.org/pdf/2608.01149 （PATH-Bench）; https://arxiv.org/pdf/2607.22157 （Learning on the Job）; https://iclr.cc/virtual/2026/10012519
- [S30] 争论: https://www.interconnects.ai/p/contra-dwarkesh-on-continual-learning ; https://www.lesswrong.com/posts/Lby4gMvKcLPoozHfg/are-we-in-a-continual-learning-overhang-1
