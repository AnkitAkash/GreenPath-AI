from dotenv import load_dotenv
import os

load_dotenv()

required_keys = [
    "OPENSTREETMAP_API_KEY",
    "OPENAI_API_KEY",
    "SECRET_SALT"
]

for key in required_keys:
    value = os.getenv(key)
    print(f"{key}: {'✅ SET' if value else '❌ MISSING'}")
