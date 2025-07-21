import asyncio
from db import db

async def test_connection():
    try:
        result = await db.command("ping")  # Ping the MongoDB server
        print("✅ MongoDB connected successfully:", result)
    except Exception as e:
        print("❌ MongoDB connection failed:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())
