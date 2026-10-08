# 评分结果（由 score.py 自动生成，勿手改）

权重：增长动量 G=0.25, 能力拐点 C=0.25, 使能条件 E=0.10, 资源注入 R=0.10, 学术空间 H=0.10, 外溢平台性 X=0.20；总分 = 20 × Σ(w·s) × (0.5 + 0.1·S) − P。
敏感性：Dirichlet(浓度 40) 随机扰动权重 5000 次，报告排名中位数、10–90% 分位区间与进入前 10 的概率。

## 候选领域排名

| # | 领域 | 方向 | 总分 | 势(G,C) | 时机系数(S) | 质(E,R,H,X) | 分项 | 排名区间 | P(前10) | 档位 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 临床大模型智能体（诊断对话 + EHR 交互智能体）<br><sub>Clinical LLM Agents (Diagnostic Dialogue & EHR-Interacting Agents)</sub> | 医疗CS | **74.7** | 90.0 | ×0.95 | 82.0 | `G5 S4.5 C4 E3.5 R5 H4 X4 P7` | 1–1 | 100% | B 值得投入 |
| 2 | 医疗 LLM 评测、安全与幻觉<br><sub>Medical LLM Evaluation, Safety & Hallucination</sub> | 医疗CS | **70.7** | 80.0 | ×0.90 | 86.0 | `G4.5 S4 C3.5 E4.5 R4 H5 X4 P4` | 2–2 | 100% | B 值得投入 |
| 3 | 医学推理模型（RLVR / 可验证奖励）<br><sub>Medical Reasoning Models (RL with Verifiable Rewards)</sub> | 医疗CS | **67.7** | 90.0 | ×0.90 | 76.0 | `G5 S4 C4 E4.5 R4 H4.5 X3 P7` | 3–4 | 100% | C 观察 |
| 4 | 患者模拟器与医疗数字孪生（LLM 驱动）<br><sub>LLM Patient Simulators & Medical Digital Twins</sub> | 医疗CS | **66.0** | 70.0 | ×1.00 | 76.0 | `G4 S5 C3 E4 R3 H5 X3.5 P7` | 3–6 | 100% | C 观察 |
| 5 | EHR / 结构化病历基础模型（医疗事件生成模型）<br><sub>EHR Foundation Models / Generative Medical Event Models</sub> | 医疗CS | **65.2** | 80.0 | ×0.95 | 70.0 | `G4 S4.5 C4 E2.5 R4 H3 X4 P6` | 3–6 | 100% | C 观察 |
| 6 | 基因组语言模型（DNA/RNA 语言模型）<br><sub>Genomic Language Models (DNA/RNA LMs)</sub> | 医疗CS | **63.8** | 75.0 | ×0.90 | 80.0 | `G4 S4 C3.5 E4.5 R4 H3.5 X4 P6` | 5–7 | 100% | C 观察 |
| 7 | 可穿戴与生理信号基础模型（ECG/PPG/传感器-语言）<br><sub>Wearable & Physiological Signal Foundation Models</sub> | 医疗CS | **62.9** | 75.0 | ×0.95 | 68.0 | `G4 S4.5 C3.5 E2.5 R4 H3.5 X3.5 P5` | 6–7 | 100% | C 观察 |
| 8 | 多模态/通用医学基础模型（含放射报告生成、3D 影像）<br><sub>Multimodal Generalist Medical Foundation Models</sub> | 医疗CS | **59.9** | 75.0 | ×0.85 | 80.0 | `G4 S3.5 C3.5 E4 R4.5 H3.5 X4 P6` | 8–8 | 100% | D 暂缓 |
| 9 | 医疗 AI 监管科学与部署后监测<br><sub>Medical AI Regulatory Science & Post-Deployment Monitoring</sub> | 医疗CS | **53.0** | 60.0 | ×0.95 | 62.0 | `G3.5 S4.5 C2.5 E2.5 R3 H4 X3 P5` | 9–9 | 100% | D 暂缓 |
| 10 | 病理基础模型<br><sub>Computational Pathology Foundation Models</sub> | 医疗CS | **46.0** | 70.0 | ×0.80 | 60.0 | `G3.5 S3 C3.5 E3 R3.5 H3.5 X2.5 P6` | 10–11 | 65% | D 暂缓 |
| 11 | 医学知识编辑与持续更新<br><sub>Medical Knowledge Editing & Continual Updating</sub> | 医疗CS | **44.3** | 50.0 | ×0.90 | 64.0 | `G3 S4 C2 E4 R1.5 H4.5 X3 P7` | 10–12 | 28% | D 暂缓 |
| 12 | 环境式临床文档（AI 听写/Ambient Scribe）<br><sub>Ambient AI Clinical Documentation (AI Scribes)</sub> | 医疗CS | **43.0** | 80.0 | ×0.75 | 56.0 | `G4.5 S2.5 C3.5 E2 R5 H2 X2.5 P8` | 11–12 | 7% | D 暂缓 |
| 13 | 医学影像分割基础模型（MedSAM 等）<br><sub>Medical Image Segmentation Foundation Models</sub> | 医疗CS | **35.2** | 55.0 | ×0.70 | 60.0 | `G2.5 S2 C3 E4.5 R2.5 H3 X2.5 P5` | 13–13 | 0% | D 暂缓 |
| 14 | 隐私保护/联邦医疗学习<br><sub>Privacy-Preserving & Federated Medical Learning</sub> | 医疗CS | **26.5** | 35.0 | ×0.70 | 58.0 | `G1.5 S2 C2 E3 R2.5 H3 X3 P6` | 14–14 | 0% | D 暂缓 |

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
