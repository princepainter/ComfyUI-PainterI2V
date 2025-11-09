🎨 ComfyUI-PainterI2V
An enhanced Wan2.2 Image-to-Video node specifically designed to fix the slow-motion issue in 4-step LoRAs (like lightx2v).
🎯 Problems Solved
✅ Reduces Slow-Motion Drag: Increases motion amplitude by 15-30%
✅ Maintains Brightness Stability: Enhancement algorithm preserves brightness distribution
✅ Optimized for Single Frame: Designed specifically for single-frame image-to-video workflows
✅ Plug & Play: Fully compatible with original Wan2.2 workflows
📦 Installation
Method 1: ComfyUI Manager (Recommended)
Open ComfyUI Manager
Search for PainterI2V
Click Install
Method 2: Manual Installation
bash
复制
# Navigate to ComfyUI's custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/yourusername/ComfyUI-PainterI2V.git

# Restart ComfyUI
🚀 Usage
Replace Node: In your workflow, replace WanImageToVideo with PainterI2V
Parameter Settings:
motion_amplitude: 1.15 (Recommended starting value)
Keep other parameters identical to the original
Recommended Scenarios:
Running, jumping (fast motion): motion_amplitude = 1.3
Walking, waving (normal motion): motion_amplitude = 1.15
Slow-motion effects: motion_amplitude = 0.9
Prompt Optimization:
Clearly describe motion rhythm, e.g., "quickly running", "smoothly walking"
Avoid vague descriptions like "moving" or "walking"
📊 Effects Comparison
表格
复制
Parameter	Motion Amplitude	Brightness Change	Use Case
1.0 (Original)	100%	None	Slow motion
1.15 (Recommended)	115%	None	General purpose
1.3	130%	None	Fast motion
1.5	150%	None	Extreme speed
🔧 Technical Principles
Brightness-Preserving Algorithm: Separates motion information from brightness mean, amplifying only motion amplitude
Zero Latent Initialization: Strictly maintains 4-step LoRA's temporal dependency chain
Reference Frame Enhancement: Maintains subject consistency through reference_latents
🤝 Contributing
Issues and PRs are welcome!
📄 License
MIT License


\# 🎨 ComfyUI-PainterI2V



Wan2.2 图生视频增强节点，专门针对4步LoRA（如 lightx2v）的慢动作问题进行优化。



\## 🎯 解决的问题



\- ✅ \*\*减少慢动作拖影\*\*：提升运动幅度15-30%

\- ✅ \*\*保持画面亮度\*\*：增强算法不破坏亮度分布

\- ✅ \*\*单帧输入优化\*\*：专为单帧图生视频设计

\- ✅ \*\*即插即用\*\*：完全兼容原版Wan2.2工作流



\## 📦 安装



\### 方法1：ComfyUI Manager（推荐）

1\. 打开ComfyUI Manager

2\. 搜索 `PainterI2V`

3\. 点击安装



\### 方法2：手动安装

```bash

\# 进入ComfyUI的custom\_nodes目录

cd ComfyUI/custom\_nodes



\# 克隆仓库

git clone https://github.com/yourusername/ComfyUI-PainterI2V.git



\# 重启ComfyUI


