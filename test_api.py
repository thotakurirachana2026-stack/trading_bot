from bot.client import get_client

client = get_client()

# Try to fetch account info
try:
    account_info = client.get_account()
    print("✅ API connection successful!")
    print(account_info)
except Exception as e:
    print("❌ API connection failed:", e)
