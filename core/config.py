import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    BASE_UI_URL = os.getenv("BASE_URL", "http://localhost:8000")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", 30000))