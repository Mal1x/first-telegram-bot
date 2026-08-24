import aiosqlite

DB_NAME = "bot_database.db"

async def init_db():
    """Creates tabel if not exists"""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                service_type TEXT,
                user_phone TEXT
            )
        """)
        await db.commit()

async def add_order(user_id: int, service_type: str, user_phone: str):
    """Saves data to database"""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO orders (user_id, service_type, user_phone) VALUES (?, ?, ?)",
            (user_id, service_type, user_phone)
        )
        await db.commit()