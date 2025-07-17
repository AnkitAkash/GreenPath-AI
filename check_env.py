from dotenv import load_dotenv
import os

load_dotenv()

# Required keys for core functionality
required_keys = [
    "NEWS_API_KEY",
    "ORS_API_KEY", 
    "GROQ_API_KEY"
]

# Optional keys (currently not used but checked)
optional_keys = [
    "OPENSTREETMAP_API_KEY",
    "OPENAI_API_KEY",
    "SECRET_SALT"
]

print("🔧 Required Environment Variables:")
print("=" * 40)
for key in required_keys:
    value = os.getenv(key)
    status = '✅ SET' if value and value != 'your_news_api_key_here' else '❌ MISSING'
    print(f"{key}: {status}")

print("\n📋 Optional Environment Variables:")
print("=" * 40)
for key in optional_keys:
    value = os.getenv(key)
    status = '✅ SET' if value and value != 'your_openstreetmap_api_key_here' else '❌ MISSING'
    print(f"{key}: {status}")

print("\n💡 To set up your environment variables:")
print("1. Copy .env.example to .env")
print("2. Replace the placeholder values with your actual API keys")
print("3. Run this script again to verify")
