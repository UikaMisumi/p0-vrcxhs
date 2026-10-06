# 深度调研：智能体系统基础设施（Agent Systems Infrastructure）

> 撰写日期：2026-10-06 ｜ 读者：偏系统方向、正在评估是否进入该领域的 CS 研究者
> 说明：事实与数字来自检索摘要（见文末 Sources）；标注"(背景知识)"者来自作者既有知识，标注"(待核实)"者为未经本次检索确认的信息。2026 年的大量 arXiv 预印本仅读过摘要，数字以论文自报为准。

---

## 1. 定义、与聊天式 LLM 服务的区别、为什么是现在

**一句话定义**：智能体系统基础设施研究的是"以 LLM 智能体程序（而非单次请求）为调度、隔离、状态与容错单位"的系统软件栈——从推理引擎、运行时/OS 抽象、沙箱、工具协议、记忆存储，到训练智能体的 RL rollout 系统与可观测性。

**与 chat/单请求 LLM serving 的本质差异**：

| 维度 | Chat / 单请求 serving | Agent 工作负载 |
|---|---|---|
| 执行单元 | 独立请求（prefill+decode） | 多步程序：LLM 调用 ⇄ 工具执行循环，可能分叉/并行（子智能体、树搜索） |
| 时延构成 | TTFT/TPOT | 端到端任务完成时间（JCT）；工具执行、沙箱冷启动成为关键路径 |
| 状态 | 会话短、KV 用完即弃 | 长生命周期 KV、文件系统/进程状态、外部世界副作用 |
| 输入/输出形态 | 中等长度 | 长上下文+短输出；UIUC 等测得跨轮缓存命中率 84.6–99.5%，decode 占 LLM 时间 91.0–98.6% [S4] |
| 失败语义 | 重试即可 | 有副作用（写文件、调 API），需幂等、检查点、回滚 |
| 成本 | 按 token 线性 | 多智能体约为聊天的 ~15× token [S27] |

生产规模证据：微软对 GitHub Copilot 2026 年 6 月采样轨迹的刻画涵盖 320 万用户、1300 万会话、7.61 亿次 LLM 调用、95T token，发现"稀疏的人类回合 + 每回合展开为自主的 LLM-工具循环"[S6]。

**为什么是现在**：(1) 编码/终端/研究型智能体（Claude Code、Codex、Copilot agent 等）在 2025-2026 成为主流 token 消耗者，工作负载形态已变；(2) 协议收敛——MCP（2024-11）与 A2A 均进入 Linux 基金会旗下 Agentic AI Foundation（AAIF，2025-12 成立）[S15][S16]；(3) 智能体 RL（SWE 类任务）让"rollout = 推理 + 沙箱 + 工具"成为训练瓶颈，DeepSeek DSec 支持 38 万并发沙箱 [S21]；(4) 专门会场出现：ACM CAIS 2026（首届，2026-05，61 篇论文）[S28]，OSDI/SOSP/EuroSys 持续接收此类论文。

---

## 2. 技术版图（9 个细分方向）

### 2.1 智能体工作负载刻画（Workload Characterization）
- **是什么**：用真实/基准轨迹量化 LLM 调用、工具时延分布、上下文增长、缓存复用、分支结构，为系统设计提供依据。
- **代表工作**：
  - *Agentic AI Workload Characteristics*（UIUC/Gimlet Labs/Intel，arXiv 2026-05）：缓存命中 84.6–99.5%，decode 主导；工具使用呈"先读/探索、后执行/写"的时序结构。https://arxiv.org/abs/2605.26297
  - *TraceLab: Characterizing Coding Agent Workloads*（arXiv 2026-06）：长自主循环、长上下文短输出、工具调用强长尾、前缀命中高但不完美。https://arxiv.org/abs/2606.30560
  - *Agentic Coding in the Wild*（Microsoft，2026-08）：Copilot 生产轨迹 761M 调用 / 95T token。https://www.alphaxiv.org/abs/2608.00101
  - *XPerf*（arXiv 2026-08，面向 agentic 负载的 serving 基准，未深读）。https://arxiv.org/abs/2608.20370
- **现状**：2026 年刚出现第一批公开刻画，且多基于单一场景（编码）。
- **核心开放问题**：缺乏开放、多场景（浏览器/GUI/数据分析/多智能体）、含工具时延与沙箱资源的标准 trace 集；对"工作负载随模型能力变化而漂移"的建模。

### 2.2 面向智能体的推理服务与调度（程序级调度、KV 复用、工具重叠）
- **是什么**：把"程序/会话"而非"请求"作为调度单位；跨步骤保留和预取 KV；让工具执行与解码重叠。
- **代表工作**：
  - **Parrot**（MSR，OSDI'24，2024-07）：Semantic Variable 抽象暴露应用级数据流，端到端最高一个数量级加速。https://www.usenix.org/conference/osdi24/presentation/lin-chaofan
  - **SGLang**（Berkeley/Stanford 等，NeurIPS'24）：RadixAttention 前缀复用，吞吐最高 6.4×。https://github.com/sgl-project/sglang
  - **Autellix**（Berkeley/GDM/SJTU，arXiv 2025-02）：程序级 attained-service 调度（PLAS/ATLAS），相同延迟下程序吞吐 4–15×（对比 vLLM）。https://arxiv.org/abs/2502.13965
  - **KVFlow**（UCSD/AWS，NeurIPS'25）：Agent Step Graph + steps-to-execution 驱逐 + 预取，较 SGLang HiCache 最高 1.83×/2.19×。https://arxiv.org/abs/2507.07400
  - **Continuum**（ICLR'26，arXiv 2025-11）：工具调用期间按 TTL 钉住 KV，延迟最高降 8.18×。https://arxiv.org/abs/2511.02230
  - **Conveyor**（Duke，arXiv 2024-06）：工具"部分执行"与解码重叠，完成时延最多降 38.8%。https://arxiv.org/abs/2406.00059
  - **Pie**（Yale，SOSP'25）：把生成循环拆成可编程 handler，用 WASM "inferlet" 承载应用逻辑，agentic 工作流 1.3–3.4× 提升。https://arxiv.org/abs/2510.24051
- **现状**：最"拥挤"的方向，思想正被 vLLM/SGLang 吸收；2026 年延伸到推测执行（AOSpec，动作+观测协同推测，arXiv 2608.00881）与异构感知调度（HexAGenT，arXiv 2605.16637）。
- **核心开放问题**：工具时延不可预测下的鲁棒调度；跨节点/分离式（PD 分离）架构中的会话亲和与 KV 迁移；对闭源 API 模型（只能通过 prompt caching 接口）的"黑盒"优化。

### 2.3 智能体运行时 / "Agent OS" 抽象
- **是什么**：为智能体提供类 OS 的调度、上下文切换、权限与资源抽象。
- **代表工作**：**AIOS**（Rutgers，arXiv 2024-03；COLM 2025 (待核实)）：LLM 调度器、上下文管理、访问控制，报告最高 2× 执行加速。https://arxiv.org/abs/2403.16971 ；**Pie**（上节）可视作"可编程推理内核"；**LogAct**（Meta，arXiv 2026-04）把智能体解构为回放共享日志的状态机。
- **现状**：概念多、共识少；工业界实际 runtime 是框架（LangGraph、OpenAI Agents SDK、Claude Agent SDK）+ 持久化执行引擎（Temporal 等）。
- **核心开放问题**：正确的抽象边界在哪里（进程？事务？日志？）；智能体级别的配额、优先级与公平性；与宿主 OS 语义鸿沟（见 Crab）。

### 2.4 沙箱与隔离（microVM、gVisor、快照/分叉）
- **是什么**：为执行不可信代码/工具的智能体提供强隔离、低冷启动、可检查点/分叉的执行环境，同时服务于线上推理与 RL 训练。
- **代表工作**：
  - **E2B**（初创，Firecracker microVM，启动 <200ms；2025-07 A 轮 2100 万美元）[S12]
  - **Kubernetes Agent Sandbox**（SIG Apps，2025-11 立项，gVisor/Kata 后端，WarmPool 亚秒启动）https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox
  - **Crab**（HKUST，arXiv 2026-04）：eBPF 判定每回合 OS 副作用，>75% 回合无需检查点；恢复正确率 8%→100%，检查点流量降 87%，开销 ≤1.9%。https://arxiv.org/abs/2604.28138
  - **DeltaBox**（arXiv 2026-05）：毫秒级沙箱 C/R，服务 SWE-bench MCTS 与 RL 扇出。https://arxiv.org/abs/2605.22781
  - **SpecBox**（arXiv 2026-07）：在 token 生成中途识别工具意图并预热沙箱，P99 降 2.9×，峰值内存降 45.9%。https://arxiv.org/abs/2607.23933
  - **DSec**（DeepSeek，arXiv 2026-09）：四类后端（FnCall/容器/microVM/VM），5000+ 沙箱/秒创建、38 万并发，基于 3FS+EROFS。https://arxiv.org/abs/2609.22978
- **现状**：2026 年学术论文井喷，属"OS/虚拟化老技术 + 新负载"，系统组切入门槛最低之一。
- **核心开放问题**：带外部副作用的状态（网络、数据库）的一致回滚；高密度下内存去重与镜像分层；隔离强度 vs 启动/IO 开销的自适应选择；沙箱与 GPU 推理的协同调度。

### 2.5 协议与工具生态（MCP / A2A / 大规模工具发现）
- **是什么**：智能体-工具（MCP）与智能体-智能体（A2A）的互操作协议，及数千工具规模下的检索、路由、鉴权网关。
- **代表工作**：MCP（Anthropic，2024-11-25）；A2A（Google，2025-04 发布 (背景知识)，2025-06 捐给 LF，2026-08 并入 AAIF [S16][S17]）；**RAG-MCP**（arXiv 2025-05）：工具检索使 prompt token 降 >50%、选择准确率提升 >3×；**云规模 MCP 网关**（南大/阿里云等，arXiv 2026-07）：3000+ 工具，Top-15 召回 98%，选择时间降 8.9×、token 降 23.8×。https://arxiv.org/abs/2607.15593
- **现状**：标准已收敛，系统问题转向网关、会话路由、权限、工具注册表。
- **核心开放问题**：工具调用的安全/权限模型（prompt 注入、混淆代理）；有状态 MCP 会话的横向扩展；协议层的流式/取消/超时语义；跨组织 A2A 的信任与计费。

### 2.6 记忆与状态管理
- **是什么**：跨会话长期记忆（事实、偏好、技能）、上下文窗口的分页/压缩，以及与 KV cache 的分层关系。
- **代表工作**：**MemGPT**（Berkeley，arXiv 2023-10 (背景知识)）→ Letta（2024-09 种子轮 1000 万美元，Felicis 领投）；**Mem0**（arXiv 2025-04，向量+图混合存储）https://arxiv.org/abs/2504.19413 ；Letta 报告"仅用文件存历史"在 LoCoMo 上达 74.0%，提示基准本身有缺陷 [S19]。**AgileLog**（arXiv 2026-04，可分叉共享日志）。
- **现状**：偏 NLP/产品，系统贡献（存储格式、一致性、成本）稀缺；基准争议大。
- **核心开放问题**：记忆的一致性与版本（多智能体并发写）；"文本记忆—KV 缓存—权重"三级层次的放置与淘汰；记忆污染/投毒防护。

### 2.7 智能体 RL 训练系统（异步 rollout）
- **是什么**：在多轮、有状态环境里生成 rollout 并训练策略的系统；瓶颈在长尾生成、环境/沙箱、训练-推理权重同步。
- **代表工作**：
  - **verl / HybridFlow**（ByteDance Seed+HKU，EuroSys'25）：混合控制器编程模型，吞吐 1.5–20×。https://github.com/volcengine/verl
  - **AReaL**（NeurIPS'25，arXiv 2025-05）：完全异步，生成与训练解耦，最高 2.77× 训练加速，用 staleness-aware PPO 保稳定。https://arxiv.org/abs/2505.24298
  - **SkyRL / SkyRL-Agent**（Berkeley Sky Lab，arXiv 2025-11）：异步分发器 1.55×；Qwen3-32B 纯 RL 在 SWE-bench Verified 由 24.4%→39.4%。https://github.com/NovaSky-AI/SkyRL
  - **slime**（THUDM，Megatron+SGLang，GLM-4.5 至 GLM-5.x 背后的 RL 框架）https://github.com/THUDM/slime ；**RollPacker**（arXiv 2025-09，tail batching 最高 2.21×）
- **现状**：工业主导但开源活跃，是"算力最贵"的子方向；沙箱基础设施（DSec、DeltaBox、Crab）正与之合流。
- **核心开放问题**：异步度与策略陈旧（off-policy）对收敛的定量权衡；长尾工具调用下的 rollout 负载均衡；树形/分叉 rollout 的环境状态复用；奖励计算（单测、判官模型）的调度。

### 2.8 可观测性、调试与回放
- **是什么**：对智能体轨迹的 tracing、失败归因、确定性回放、在线干预。
- **代表工作**：**MAST**（Berkeley，arXiv 2025-03）：7 个 MAS 框架 1600+ 标注轨迹，14 种失败模式，κ=0.88，失败主要来自系统设计与智能体间失配。https://arxiv.org/abs/2503.13657 ；**OpenTelemetry GenAI 语义约定**（仍为 Development 状态）；**LogAct**（Meta，2026-04）：动作执行前写入共享日志、可被投票者拦截，对目标模型拦截所有不良动作仅损失 3% 良性效用。https://arxiv.org/abs/2604.07988
- **现状**：工业产品（LangSmith、Langfuse）以日志+UI 为主，缺乏系统层"可回放性"保证。
- **核心开放问题**：非确定性 LLM + 外部世界下的确定性回放；跨智能体因果追踪；自动根因定位。

### 2.9 多智能体编排与成本/时延优化
- **是什么**：编排并行子智能体、路由/级联不同模型、编译式并行函数调用、预算控制。
- **代表工作**：**LLMCompiler**（Berkeley，ICML'24 (背景知识)）：并行函数调用，较 ReAct 时延 3.7×、成本 6.7×。https://arxiv.org/abs/2312.04511 ；**Teola**（arXiv 2024-07，原语级数据流图优化）https://arxiv.org/abs/2407.00326 ；**KVFlow**（多智能体 KV）；Anthropic 多智能体研究系统：较单智能体提升 90.2%，token ~15×，token 用量解释 80% 性能方差 [S27]；SwarmX（arXiv 2026-06，未深读）。
- **现状**：大量是提示工程层面的"框架"，系统层（编译、全局成本模型）尚薄。
- **核心开放问题**：任务级"质量-成本-时延"联合优化器；子智能体扇出的动态调整；跨供应商 API 的端到端 SLO。

---

## 3. 关键基准、开源系统与工具

| 名称 | 类别 | 说明 | 链接 |
|---|---|---|---|
| SWE-bench (Verified) | 基准 | 真实 GitHub issue 修复，RL/agent 训练事实标准 (背景知识) | https://www.swebench.com |
| Terminal-Bench 2.0 + Harbor | 基准/框架 | 89 个终端任务；Harbor 支持云容器与 RL/SFT rollout 接口（2025-11-07） | https://www.tbench.ai/news/announcement-2-0 |
| τ-bench / OSWorld | 基准 | 工具-用户交互 / GUI 操作 (背景知识) | https://github.com/sierra-research/tau-bench |
| MAST-Data | 数据集 | 1600+ 多智能体失败轨迹 | https://sky.cs.berkeley.edu/project/mast/ |
| vLLM / SGLang | 推理引擎 | 前缀缓存、分层 KV；大多数 agent serving 论文的基线与落点 | https://github.com/sgl-project/sglang |
| AIOS | 运行时 | Agent OS 原型 | https://github.com/agiresearch/AIOS (背景知识) |
| verl / AReaL / SkyRL / slime | RL 训练 | 同步/异步 rollout 训练框架 | https://github.com/volcengine/verl ；https://github.com/NovaSky-AI/SkyRL ；https://github.com/THUDM/slime |
| E2B / Agent Sandbox (k8s) | 沙箱 | Firecracker microVM / gVisor-Kata CRD | https://e2b.dev ；https://agent-sandbox.sigs.k8s.io |
| MCP / A2A | 协议 | 工具协议 / 智能体间协议（AAIF 托管） | https://modelcontextprotocol.io |
| Letta / Mem0 | 记忆 | 分层记忆 / 抽取式记忆 | https://github.com/letta-ai/letta |
| Temporal / Restate | 持久化执行 | 事件历史回放，LLM 调用即 activity | https://temporal.io |
| Langfuse / OTel GenAI | 可观测性 | 基于 OpenTelemetry 的 trace | https://langfuse.com/docs/opentelemetry |

---

## 4. 主要玩家与会场

**学术**：
- **UC Berkeley Sky Computing Lab**（Stoica、Gonzalez 等）：SGLang/vLLM 渊源、Autellix、LLMCompiler、SkyRL、MAST、MemGPT——该领域最核心的学术重镇。
- **Stanford**（SGLang 合作者；DSPy 系 compound AI (背景知识)）；**CMU**（Catalyst/Zhihao Jia 组等 LLM serving (背景知识)）；**Yale**（Pie）；**UCSD**（KVFlow）；**Duke**（Conveyor）；**UIUC**（工作负载刻画）；**HKUST**（Crab）；**Rutgers**（AIOS）；**SJTU IPADS**（LLM 调度，OSDI'26 论文）；**清华 THUDM/IIIS**（slime；AReaL 与蚂蚁合作 (背景知识)）；**南京大学**+阿里云（MCP 网关）。

**工业**：Anthropic（MCP、Claude Code、多智能体研究系统）、OpenAI（Agents SDK、Codex）、Google（A2A、GKE Agent Sandbox、gVisor）、Microsoft（Parrot、Copilot 轨迹）、Meta（LogAct）、ByteDance Seed（verl）、DeepSeek（DSec、3FS）、Moonshot（Kimi 系列沙箱 (待核实)）、阿里（MCP 网关、ROLL (背景知识)）、AWS（Firecracker、KVFlow 合作）。

**初创**：E2B（累计 3200 万美元，A 轮 2100 万，Insight Partners 领投，2025-07）；Letta（种子 1000 万美元，2024-09）；Mem0（融资额待核实）；Daytona、Modal、Browserbase（沙箱/浏览器基础设施，融资待核实）；Temporal（持久化执行）；LangChain（LangGraph/LangSmith）。

**会场**：ACM CAIS（首届 2026-05-26~29，San Jose，61 篇论文+45 个 demo，主旨演讲含 Anthropic Claude Code 团队）；OSDI/SOSP/EuroSys/ATC/NSDI（serving 与沙箱论文）；MLSys；NeurIPS/ICLR/ICML（KVFlow、AReaL、Continuum 均在 ML 会议发表——说明该领域论文常"系统内容、ML 会场"）。

---

## 5. 2024–2026 时间线

| 时间 | 事件 |
|---|---|
| 2024-03 | AIOS 预印本发布（Agent OS 概念） |
| 2024-06 | Conveyor：工具部分执行与解码重叠 |
| 2024-07 | Parrot（OSDI'24）：Semantic Variable，应用级 LLM 服务 |
| 2024-09 | Letta（MemGPT 团队）种子轮 1000 万美元；HybridFlow/verl 预印本 |
| 2024-11-25 | Anthropic 发布 MCP |
| 2024-12 | SGLang 于 NeurIPS'24 发表（RadixAttention） |
| 2025-02 | Autellix：程序级调度，4–15× |
| 2025-03 | MAST 多智能体失败分类；HybridFlow 于 EuroSys'25 发表；OpenAI 宣布支持 MCP (时间为背景知识) |
| 2025-05 | AReaL 完全异步 RL；RAG-MCP |
| 2025-06 | A2A 捐赠给 Linux 基金会；Anthropic 公开多智能体研究系统工程细节 |
| 2025-07 | E2B A 轮 2100 万美元 |
| 2025-10 | Pie 于 SOSP'25 发表 |
| 2025-11 | Terminal-Bench 2.0 + Harbor；Kubernetes Agent Sandbox 立项；SkyRL-Agent；Continuum |
| 2025-12-09 | Linux 基金会成立 Agentic AI Foundation，MCP 捐入 |
| 2026-04 | Crab（语义感知沙箱 C/R）、LogAct（共享日志智能体）、AgileLog |
| 2026-05 | ACM CAIS 首届召开；UIUC 工作负载刻画；DeltaBox |
| 2026-07 | SpecBox；云规模 MCP 网关论文；OSDI'26 |
| 2026-08 | A2A 正式并入 AAIF；Microsoft Copilot 生产轨迹刻画 |
| 2026-09 | DeepSeek DSec（38 万并发沙箱）论文 |

---

## 6. 研究机会（按适合学术系统组的程度排序）

| # | 问题 | 算力 | 难度 | 说明 |
|---|---|---|---|---|
| 1 | **开放多场景 agent trace 集 + 回放模拟器** | 低 | 中 | 现有刻画集中于编码；建一个含工具时延、沙箱资源、分支结构的 trace 格式与 trace-driven 模拟器，可成为社区基础设施（类似 Azure LLM trace 的地位）。 |
| 2 | **带外部副作用的智能体事务/回滚语义** | 低 | 高 | Crab/LogAct 只覆盖本地 OS 状态或日志；对网络/DB/SaaS 副作用做补偿事务（saga）、意图日志、可撤销工具接口——经典 OS/DB 技术的新战场。 |
| 3 | **沙箱—推理协同调度** | 低-中 | 中 | SpecBox 证明预热有效；进一步将 CPU 沙箱与 GPU 推理放在同一调度器内（工具期间释放 KV vs 保留、沙箱放置与 KV 亲和），单机多卡即可做。 |
| 4 | **RL rollout 的分叉/快照复用** | 中 | 中 | 树形 GRPO/MCTS 需要从同一状态分叉成百上千沙箱；结合 microVM 快照 + 前缀 KV 共享做"联合分叉"，可用小模型（≤8B）评估。 |
| 5 | **鲁棒的不确定工具时延调度** | 低-中 | 中 | Continuum 的 TTL 是启发式；可做在线学习/排队论最优策略，给出理论界与 trace 驱动评估。 |
| 6 | **智能体安全执行的系统化机制** | 低 | 中-高 | 能力（capability）式工具权限、信息流控制（对抗 prompt 注入导致的数据外泄）、可验证的拦截点；与 MCP 网关结合。 |
| 7 | **大规模工具/MCP 服务的有状态扩展** | 低-中 | 中 | 有状态 MCP 会话的负载均衡、迁移、缓存（工具结果缓存与失效）、工具检索与路由。 |
| 8 | **记忆—KV—权重三级层次** | 中 | 高 | 何时把长期记忆保持为 KV（可复用但贵）、文本（便宜但需 prefill）或 LoRA；统一成本模型与淘汰策略。 |
| 9 | **异步 agent RL 的陈旧度-吞吐联合控制** | 高 | 高 | 需要大规模 GPU；可与工业合作，学术侧做理论分析与小规模验证。 |
| 10 | **全局"质量-成本-时延"编排编译器** | 中 | 高 | 将多智能体工作流视为可优化程序（模型选择、扇出度、提前终止），需要可靠的质量评估信号，风险在于评估噪声。 |

---

## 7. 入门路径

**10 篇必读（按阅读顺序）**：
1. **SGLang**（NeurIPS'24）——理解前缀复用与"LLM 程序"视角，所有后续工作的基线。
2. **Parrot**（OSDI'24）——首次把应用级数据流暴露给服务端的系统论文范式。
3. **Autellix**（2025-02）——程序级调度的标准表述与 PLAS/ATLAS 算法。
4. **Conveyor**（2024-06）——工具执行与解码重叠的最小可行思路。
5. **Agentic AI Workload Characteristics**（2026-05）+ **Copilot 生产轨迹**（2026-08）——用数据校准直觉：decode 主导、缓存命中高、工具长尾。
6. **Continuum**（ICLR'26）与 **KVFlow**（NeurIPS'25）——工具间隙与多智能体下的 KV 保留/预取。
7. **Pie**（SOSP'25）——"可编程推理内核"，Agent OS 的一种系统化答案。
8. **Crab**（2026-04）——智能体-OS 语义鸿沟，沙箱 C/R 的范本论文。
9. **HybridFlow/verl**（EuroSys'25）+ **AReaL**（NeurIPS'25）——RL 训练系统的同步与异步两种范式。
10. **MAST**（2025-03）+ **LogAct**（2026-04）——失败模式与"日志即智能体"的可靠性抽象。

补充：AIOS（概念全景）、DSec（工业规模沙箱的真实约束）、SkyRL-Agent（长时程 SWE RL）。

**开源代码库**：sgl-project/sglang、vllm-project/vllm、volcengine/verl、NovaSky-AI/SkyRL、THUDM/slime、inclusionAI/AReaL (背景知识)、agiresearch/AIOS、e2b-dev/E2B、kubernetes-sigs/agent-sandbox、harbor-framework（Terminal-Bench）、letta-ai/letta。

**第一个 3 个月项目（建议）**："Agent-aware KV + 沙箱协同调度的 trace 驱动研究"
- **第 1 月**：在单机（2–8 张 GPU）上部署 SGLang + Qwen3-8B/32B，用 Harbor 跑 Terminal-Bench 2.0 与 SWE-bench Verified 子集，搭建 OpenTelemetry tracing，采集每步 LLM 时延、工具时延、沙箱冷启动、KV 命中、上下文长度；产出开放 trace（对应机会 #1）。
- **第 2 月**：复现 Continuum 式 TTL 与 SpecBox 式沙箱预热两条基线，在 trace 驱动模拟器 + 真实系统中量化 JCT、GPU 显存、P99。
- **第 3 月**：提出联合策略——基于工具类型/历史时延预测决定"保留 KV / 卸载到 CPU / 丢弃重算"，同时决定沙箱预热与放置；目标是在相同显存下 JCT 降 20–40%（目标值，非已知结果）。可投 CAIS / EuroSys / MLSys workshop，再扩为完整论文。

---

## 8. 风险与争议

1. **框架迭代过快使研究过时**：Agent 框架与产品（SDK、harness）以月为单位更新，基于某框架行为的优化可能半年即失效；对策是把贡献落在稳定抽象（KV、沙箱、日志、事务）而非框架 API 上。
2. **工业主导与数据壁垒**：最有价值的生产 trace、超大规模 RL 与沙箱（DSec 38 万并发、Copilot 95T token）在工业界；学术组需靠开放 trace、模拟器、小模型可验证的机制取胜，或与工业合作。
3. **与通用 LLM serving 高度重叠**：多数"agent serving"创新本质是前缀缓存/调度的变体，审稿人常质疑新颖性；需要证明依赖于 agent 特有结构（工具间隙、分支、副作用）。
4. **基准不可靠**：LoCoMo 上"仅存文件"即达 74% 的结果说明记忆基准有漏洞；Terminal-Bench 等需大量人工验证。系统论文若以任务成功率为指标，需谨慎。
5. **闭源 API 的不可见性**：主流智能体跑在闭源模型 API 上，服务端优化无法部署；仅能在客户端（缓存命中、并发、路由）做文章，学术影响力受限。
6. **"Agent OS"的概念泡沫**：大量论文以 OS 类比包装而缺乏严格系统评估；进入时应避免停留在比喻层。
7. **安全与责任**：可执行代码智能体的沙箱逃逸、提示注入导致的副作用，任何系统设计都需显式威胁模型。

---

## 9. Sources

- [S1] Autellix: https://arxiv.org/abs/2502.13965
- [S2] Parrot (OSDI'24): https://www.usenix.org/conference/osdi24/presentation/lin-chaofan
- [S3] AIOS: https://arxiv.org/html/2403.16971v2
- [S4] Agentic AI Workload Characteristics: https://arxiv.org/pdf/2605.26297 ; https://www.alphaxiv.org/abs/2605.26297
- [S5] TraceLab: https://arxiv.org/pdf/2606.30560
- [S6] Agentic Coding in the Wild (Copilot traces): https://www.alphaxiv.org/abs/2608.00101 ; https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/ghcp_traces-6.pdf
- [S7] KVFlow: https://arxiv.org/html/2507.07400v1 ; https://neurips.cc/virtual/2025/poster/119883
- [S8] Continuum: https://arxiv.org/pdf/2511.02230 ; https://iclr.cc/virtual/2026/10012473
- [S9] SGLang: https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract.html
- [S10] Conveyor: https://arxiv.org/abs/2406.00059 ; LLMCompiler: https://www.arxiv.org/pdf/2312.04511v3 ; Teola: https://export.arxiv.org/pdf/2407.00326
- [S11] Pie (SOSP'25): https://arxiv.org/abs/2510.24051v1 ; https://www.yecl.org/publications/gim2025sosp.pdf
- [S12] E2B 融资: https://venturebeat.com/ai/how-e2b-became-essential-to-88-of-fortune-100-companies-and-raised-21-million ; https://vestbee.com/blog/articles/e2-b-secures-21-m
- [S13] 沙箱技术对比（博客）: https://dev.to/aiagentengineering/how-to-sandbox-ai-agents-in-2026-firecracker-gvisor-runtimes-isolation-strategies-14pk
- [S14] Kubernetes Agent Sandbox: https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox ; https://agent-sandbox.sigs.k8s.io/docs/getting_started/overview/
- [S15] MCP 发布: https://en.wikipedia.org/wiki/Model_Context_Protocol ; https://simonwillison.net/2024/Nov/25/model-context-protocol/
- [S16] AAIF / MCP 捐赠: https://agentic-ai.readthedocs.io/en/latest/Standards/agentic-ai-foundation/ ; https://www.flowhunt.io/blog/agentic-ai-foundation-a2a-mcp-standards/
- [S17] A2A 捐赠: https://sdtimes.com/ai/googles-agent2agent-protocol-finds-new-home-at-the-linux-foundation/ ; https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards
- [S18] RAG-MCP: https://arxiv.org/html/2505.03275v1 ; 云规模 MCP 网关: https://arxiv.org/pdf/2607.15593
- [S19] Mem0: https://arxiv.org/pdf/2504.19413 ; Letta 记忆基准: https://www.letta.com/blog/benchmarking-ai-agent-memory ; Letta 融资: https://pulse2.com/letta-uc-berkeley-genai-spin-out-raises-10-million-seed/
- [S20] Crab: https://arxiv.org/html/2604.28138v1 ; DeltaBox: https://arxiv.org/html/2605.22781
- [S21] DSec: https://arxiv.org/pdf/2609.22978 ; https://mer.vin/news/inside-dsec-how-deepseek-runs-3-million-ai-agent-sandboxes-a-day/
- [S22] SpecBox: https://arxiv.org/pdf/2607.23933 ; AOSpec: https://arxiv.org/pdf/2608.00881 ; HexAGenT: https://arxiv.org/pdf/2605.16637 ; XPerf: https://arxiv.org/pdf/2608.20370 ; SwarmX: https://arxiv.org/pdf/2606.21401
- [S23] AReaL: https://arxiv.org/abs/2505.24298v4 ; https://neurips.cc/virtual/2025/poster/117538
- [S24] SkyRL: https://sky.cs.berkeley.edu/project/skyrl/ ; https://arxiv.org/html/2511.16108v1 ; https://github.com/NovaSky-AI/SkyRL
- [S25] HybridFlow/verl: https://arxiv.org/pdf/2409.19256 ; slime: https://github.com/THUDM/slime ; RollPacker: https://arxiv.org/pdf/2509.21009
- [S26] MAST: https://arxiv.org/abs/2503.13657 ; LogAct: https://arxiv.org/pdf/2604.07988 ; AgileLog: https://arxiv.org/pdf/2604.14590
- [S27] Anthropic 多智能体研究系统: https://www.anthropic.com/engineering/multi-agent-research-system
- [S28] ACM CAIS 2026: https://www.caisconf.org/ ; https://www.caisconf.org/program/2026/
- [S29] Durable execution / Temporal: https://temporal.io/blog/manetu-the-thread-is-the-workflow ; https://ai.pydantic.dev/temporal
- [S30] OTel GenAI / Langfuse: https://langfuse.com/docs/opentelemetry ; https://portkey.ai/blog/opentelemetry-semantic-conventions-for-genai-traces/
- [S31] Terminal-Bench 2.0 / Harbor: https://www.tbench.ai/news/announcement-2-0 ; https://venturebeat.com/ai/terminal-bench-2-0-launches-alongside-harbor-a-new-framework-for-testing
- [S32] EuroSys'26 / OSDI'26 serving 论文汇总: https://github.com/JiusiServe/InferMatrixCopilot/issues/57 ; https://ipads.se.sjtu.edu.cn/pub/publication
