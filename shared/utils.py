import os
import json

def save_output(studio: str, content: str):
    os.makedirs(f"deliverables/{studio}", exist_ok=True)
    with open(f"deliverables/{studio}/output.md", "w", encoding="utf-8") as f:
        f.write(content)

def system_health():
    return {
        "status": "healthy",
        "openai_key": bool(os.getenv("OPENAI_API_KEY")),
        "brand_assets": len(os.listdir("marketing_studio/brand_assets")) if os.path.exists("marketing_studio/brand_assets") else 0,
        "landing_pages": len(os.listdir("marketing_studio/landing_pages")) if os.path.exists("marketing_studio/landing_pages") else 0
    }
