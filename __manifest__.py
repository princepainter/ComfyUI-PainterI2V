MANIFEST = {
    "name": "ComfyUI-PainterI2V",
    "version": "1.0.0",
    "author": "Painter (社区贡献)",
    "description": "Wan2.2图生视频增强节点，修复4步LoRA慢动作问题，保持亮度稳定",
    "tags": ["wan", "video", "i2v", "lora", "slow-motion"],
    "requirements": [],
    "custom_nodes": {
        "PainterI2V": {
            "category": "conditioning/video_models",
            "display_name": "🎨 PainterI2V (Wan2.2)",
            "description": "增强版图生视频，解决慢动作问题"
        }
    }
}
