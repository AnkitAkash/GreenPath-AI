from dotenv import load_dotenv
import os

load_dotenv()

required_keys = [
    "GROQ_API_KEY",
    "ORS_API_KEY",
    "NEWS_API_KEY"
]

for key in required_keys:
    value = os.getenv(key)
    print(f"{key}: {'✅ SET' if value else '❌ MISSING'}")
