# 评分结果（由 score.py 自动生成，勿手改）

权重：增长动量 G=0.25, 能力拐点 C=0.25, 使能条件 E=0.10, 资源注入 R=0.10, 学术空间 H=0.10, 外溢平台性 X=0.20；总分 = 20 × Σ(w·s) × (0.5 + 0.1·S) − P。
敏感性：Dirichlet(浓度 40) 随机扰动权重 5000 次，报告排名中位数、10–90% 分位区间与进入前 10 的概率。

## 候选领域排名

| # | 领域 | 方向 | 总分 | 势(G,C) | 时机系数(S) | 质(E,R,H,X) | 分项 | 排名区间 | P(前10) | 档位 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LLM驱动的形式化验证 / 可验证代码生成<br><sub>LLM-driven Formal Verification & Verified Code Generation ("vericoding": Verus/Dafny/Lean code with proofs)</sub> | AI-可信与推理 | **80.5** | 85.0 | ×1.00 | 82.0 | `G4.5 S5 C4 E4 R3.5 H5 X4 P3` | 1–2 | 100% | A 强烈关注 |
| 2 | 自我改进与自博弈（LLM引导的进化搜索/开放式学习）<br><sub>Self-Improvement & Self-Play (LLM-guided Evolutionary Search, Open-Endedness)</sub> | AI-模型与方法 | **79.0** | 85.0 | ×0.95 | 94.0 | `G4.5 S4.5 C4 E4 R4.5 H5 X5 P6` | 1–4 | 100% | A 强烈关注 |
| 3 | AI数学与形式化定理证明<br><sub>AI for Mathematics & Formal Theorem Proving (Lean, AlphaProof, autoformalization, Seed-Prover, IMO gold, Erdős problems)</sub> | AI-可信与推理 | **78.9** | 100.0 | ×0.90 | 82.0 | `G5 S4 C5 E4 R5 H3.5 X4 P3` | 1–5 | 100% | A 强烈关注 |
| 4 | 机器人基础模型 / 视觉-语言-动作模型(VLA)<br><sub>Robot Foundation Models / Vision-Language-Action Models</sub> | 具身/空间/生命科学交叉 | **77.7** | 90.0 | ×0.95 | 82.0 | `G5 S4.5 C4 E3.5 R5 H4 X4 P4` | 3–4 | 100% | A 强烈关注 |
| 5 | 世界模型 / 可交互视频生成<br><sub>World Models & Interactive Video Generation</sub> | AI-模型与方法 | **75.8** | 90.0 | ×0.95 | 80.0 | `G5 S4.5 C4 E3 R5 H4 X4 P5` | 5–7 | 100% | A 强烈关注 |
| 6 | 持续学习与测试时训练 / 测试时记忆<br><sub>Continual Learning & Test-Time Training / Test-Time Memory</sub> | AI-模型与方法 | **75.5** | 75.0 | ×1.00 | 86.0 | `G4.5 S5 C3 E3.5 R4 H5 X4.5 P5` | 3–8 | 100% | A 强烈关注 |
| 7 | 智能体系统基础设施<br><sub>Agent Systems Infrastructure</sub> | 系统与硬件 | **75.1** | 90.0 | ×0.90 | 88.0 | `G5 S4 C4 E4 R5 H4 X4.5 P5` | 6–7 | 100% | A 强烈关注 |
| 8 | 空间智能 / 3D基础模型（前馈式三维重建）<br><sub>Spatial Intelligence / 3D Foundation Models (Feed-forward 3D Reconstruction)</sub> | 具身/空间/生命科学交叉 | **73.0** | 85.0 | ×0.90 | 84.0 | `G4.5 S4 C4 E4.5 R4 H4.5 X4 P3` | 7–10 | 94% | B 值得投入 |
| 9 | 自动化科研 / AI科学家<br><sub>Automated Research / AI Scientist (AI Scientist, AlphaEvolve-style discovery, Co-Scientist, autonomous labs)</sub> | AI-可信与推理 | **71.9** | 85.0 | ×0.90 | 88.0 | `G5 S4 C3.5 E3 R5 H4 X5 P6` | 8–12 | 65% | B 值得投入 |
| 10 | 量子纠错与容错量子计算软件栈<br><sub>Quantum Error Correction & Fault-Tolerant Quantum Computing Stack</sub> | 量子/密码/网络/理论 | **71.8** | 90.0 | ×0.95 | 76.0 | `G4.5 S4.5 C4.5 E3 R5 H4 X3.5 P7` | 8–12 | 70% | B 值得投入 |
| 11 | 扩散语言模型 / 非自回归LLM<br><sub>Diffusion Language Models (non-autoregressive LLMs)</sub> | AI-模型与方法 | **70.5** | 75.0 | ×1.00 | 74.0 | `G4.5 S5 C3 E4 R3.5 H5 X3 P4` | 9–13 | 34% | B 值得投入 |
| 12 | 大模型驱动的芯片设计/EDA<br><sub>LLM-Driven Chip Design / EDA</sub> | 系统与硬件 | **70.5** | 85.0 | ×1.00 | 64.0 | `G5 S5 C3.5 E3 R4 H4 X2.5 P4` | 9–13 | 34% | B 值得投入 |
| 13 | GUI/计算机使用智能体<br><sub>GUI / Computer-Use Agents</sub> | AI-模型与方法 | **68.1** | 90.0 | ×0.85 | 82.0 | `G4.5 S3.5 C4.5 E4 R5 H3.5 X4 P5` | 11–14 | 1% | B 值得投入 |
| 14 | 智能体安全<br><sub>AI Agent Security (prompt-injection defenses, tool-use security, agent sandboxing, AgentDojo-style benchmarks)</sub> | AI-可信与推理 | **67.0** | 80.0 | ×0.90 | 80.0 | `G5 S4 C3 E5 R5 H4 X3 P5` | 13–14 | 2% | C 观察 |
| 15 | AI控制与可扩展监督<br><sub>AI Control & Scalable Oversight (control protocols, CoT monitoring, model organisms of misalignment, alignment auditing)</sub> | AI-可信与推理 | **65.0** | 70.0 | ×1.00 | 68.0 | `G4 S5 C3 E4 R4 H4 X2.5 P4` | 15–16 | 0% | C 观察 |
| 16 | 学习增强算法 / 带预测的算法（含LLM驱动的算法发现）<br><sub>Learning-Augmented Algorithms & LLM-Driven Algorithm Discovery</sub> | 量子/密码/网络/理论 | **63.3** | 70.0 | ×0.95 | 76.0 | `G4 S4.5 C3 E4 R3.5 H4.5 X3.5 P6` | 15–17 | 0% | C 观察 |
| 17 | 神经数据基础模型与脑机接口解码<br><sub>Neural Data Foundation Models and BCI Decoding</sub> | 具身/空间/生命科学交叉 | **62.9** | 75.0 | ×0.95 | 68.0 | `G4 S4.5 C3.5 E2.5 R4 H4.5 X3 P5` | 16–18 | 0% | C 观察 |
| 18 | 机制可解释性<br><sub>Mechanistic Interpretability (SAEs, transcoders, attribution graphs / circuit tracing, model diffing)</sub> | AI-可信与推理 | **61.7** | 70.0 | ×0.90 | 76.0 | `G4 S4 C3 E4 R4 H5 X3 P4` | 17–19 | 0% | C 观察 |
| 19 | 人形机器人全身控制与sim2real<br><sub>Humanoid Whole-Body Control and Sim-to-Real</sub> | 具身/空间/生命科学交叉 | **59.6** | 80.0 | ×0.85 | 72.0 | `G4 S3.5 C4 E4.5 R4.5 H4 X2.5 P5` | 18–22 | 0% | D 暂缓 |
| 20 | 虚拟细胞 / 单细胞基础模型<br><sub>Virtual Cell / Single-Cell Foundation Models</sub> | 具身/空间/生命科学交叉 | **59.6** | 60.0 | ×0.95 | 76.0 | `G4 S4.5 C2 E3 R4 H5 X3.5 P5` | 18–22 | 0% | D 暂缓 |
| 21 | AI数据中心能效与电力感知计算<br><sub>AI Datacenter Energy and Power-Aware Computing</sub> | 系统与硬件 | **59.5** | 65.0 | ×0.90 | 76.0 | `G4 S4 C2.5 E3 R5 H4 X3.5 P4` | 19–22 | 0% | D 暂缓 |
| 22 | 光计算与光互连<br><sub>Optical Interconnect and Photonic Computing</sub> | 系统与硬件 | **57.6** | 75.0 | ×0.90 | 64.0 | `G4 S4 C3.5 E2 R5 H3 X3 P5` | 20–25 | 0% | D 暂缓 |
| 23 | Transformer/大模型理论<br><sub>Theory of Transformers & Large Language Models</sub> | 量子/密码/网络/理论 | **56.6** | 65.0 | ×0.85 | 80.0 | `G4 S3.5 C2.5 E5 R3 H5 X3.5 P5` | 21–26 | 0% | D 暂缓 |
| 24 | 零知识证明系统与zkVM<br><sub>Zero-Knowledge Proof Systems & zkVMs</sub> | 量子/密码/网络/理论 | **55.4** | 75.0 | ×0.80 | 76.0 | `G3.5 S3 C4 E4.5 R3.5 H4 X3.5 P5` | 23–26 | 0% | D 暂缓 |
| 25 | 后Transformer架构：SSM/线性注意力/混合架构<br><sub>Post-Transformer Architectures: SSMs, Linear Attention & Hybrids</sub> | AI-模型与方法 | **55.0** | 65.0 | ×0.80 | 80.0 | `G3 S3 C3.5 E5 R4 H4 X3.5 P3` | 23–26 | 0% | D 暂缓 |
| 26 | 全同态加密及其硬件加速<br><sub>Fully Homomorphic Encryption & Hardware Acceleration</sub> | 量子/密码/网络/理论 | **53.9** | 65.0 | ×0.90 | 68.0 | `G3 S4 C3.5 E3 R3.5 H4.5 X3 P6` | 24–28 | 0% | D 暂缓 |
| 27 | 端侧/边缘大模型<br><sub>On-Device / Edge LLMs</sub> | 系统与硬件 | **53.4** | 70.0 | ×0.80 | 76.0 | `G4 S3 C3 E4 R5 H4 X3 P5` | 24–28 | 0% | D 暂缓 |
| 28 | 推理时计算与可验证奖励强化学习<br><sub>Test-Time Compute & RL with Verifiable Rewards (RLVR)</sub> | AI-模型与方法 | **52.5** | 85.0 | ×0.65 | 92.0 | `G3.5 S1.5 C5 E5 R5 H3 X5 P5` | 25–29 | 0% | D 暂缓 |
| 29 | 大模型推理/服务系统<br><sub>LLM Serving Systems</sub> | 系统与硬件 | **50.6** | 80.0 | ×0.70 | 76.0 | `G4 S2 C4 E5 R5 H3 X3 P4` | 28–29 | 0% | D 暂缓 |
| 30 | 低轨卫星互联网与空天地一体化网络<br><sub>LEO Satellite Networking & Space-Air-Ground Integrated Networks</sub> | 量子/密码/网络/理论 | **48.0** | 65.0 | ×0.85 | 62.0 | `G3 S3.5 C3.5 E2.5 R5 H3 X2.5 P6` | 30–30 | 0% | D 暂缓 |
| 31 | 存内/近存计算<br><sub>Processing-in-Memory / Compute-in-Memory</sub> | 系统与硬件 | **44.6** | 60.0 | ×0.80 | 64.0 | `G3 S3 C3 E2.5 R3.5 H4 X3 P5` | 31–32 | 0% | D 暂缓 |
| 32 | 后量子密码迁移工程<br><sub>Post-Quantum Cryptography Migration Engineering</sub> | 量子/密码/网络/理论 | **42.9** | 55.0 | ×0.75 | 70.0 | `G3.5 S2.5 C2 E5 R5 H2.5 X2.5 P4` | 31–32 | 0% | D 暂缓 |
| 33 | 3D/4D高斯泼溅与神经渲染<br><sub>3D/4D Gaussian Splatting and Neural Rendering</sub> | 具身/空间/生命科学交叉 | **33.4** | 50.0 | ×0.65 | 68.0 | `G2 S1.5 C3 E5 R3.5 H2.5 X3 P5` | 33–33 | 0% | D 暂缓 |

## 历史回测（事前视角打分 vs 实际走向）

| 案例 | 时点 | 总分 | 分项 | 实际走向 |
|---|---|---|---|---|
| 大语言模型 LLM | 2020-21 | **92.0** | `G5 S5 C5 E4 R4 H4 X5 P2` | 爆发并成为整个 CS 的通用底座（基准案例） |
| 扩散模型 Diffusion | 2021 | **84.0** | `G5 S5 C4 E4 R3 H5 X4 P1` | 爆发，成为图像/视频/分子生成的主流范式 |
| 3D 高斯泼溅 3DGS | 2023 | **80.0** | `G5 S5 C4 E5 R3 H5 X3 P3` | 约 1 年内取代 NeRF，2026 年已进入 glTF/OpenUSD 标准化 |
| 生成对抗网络 GAN | 2016 | **78.0** | `G5 S5 C4 E4 R3 H5 X3 P3` | 繁荣约 5 年，2021 后被扩散模型取代 |
| 神经辐射场 NeRF | 2021 | **72.0** | `G5 S5 C4 E4 R2 H5 X2 P3` | 爆发约 2.5 年，2023 后被 3D 高斯泼溅大面积取代 |
| 深度强化学习（游戏） | 2016 | **66.1** | `G5 S4 C4 E3 R4 H4 X3 P5` | 游戏外落地慢，沉寂后以 RLHF/RLVR 形式回归 |
| 大语言模型 LLM（对照：今天） | 2026 | **51.6** | `G4 S1 C5 E5 R5 H3 X5 P3` | 对照组：重要但已是主流，不再是新兴方向，应被时机系数压低 |
| 神经架构搜索 NAS | 2018 | **51.4** | `G5 S4 C3 E3 R3 H3 X2 P8` | 收益被随机搜索基线质疑，2021 后明显降温 |
| 区块链（CS 研究） | 2018 | **43.8** | `G4 S4 C2 E3 R4 H3 X3 P12` | 收缩为密码学/共识等细分方向，泛化应用未兑现 |
| 胶囊网络 CapsNet | 2018 | **41.7** | `G3 S4 C2 E4 R2 H4 X2 P6` | 未能规模化，基本消失 |
| 元宇宙 Metaverse | 2021 | **37.5** | `G4 S4 C1 E2 R5 H2 X3 P12` | 资本退潮，研究热度回落 |
