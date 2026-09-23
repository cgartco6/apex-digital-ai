#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir -p marketing_studio/brand_assets marketing_studio/landing_pages marketing_studio/uploads web_dev_studio/generated/xtreme_web/app web_dev_studio/generated/xtreme_web/components
echo "Setup complete."
