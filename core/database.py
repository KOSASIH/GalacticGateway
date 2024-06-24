import asyncio
import aiomysql

class Database:
    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.pool = None

    async def connect(self):
        self.pool = await aiomysql.create_pool(
            host=self.config['host'],
            port=self.config['port'],
            user=self.config['user'],
            password=self.config['password'],
            db=self.config['database']
        )

    async def disconnect(self):
        self.pool.close()
        await self.pool.wait_closed()

    async def execute(self, query: str, params: List[str] = None):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(query, params)
                return await cur.fetchall()

# Example usage:
# db = Database({'host': 'localhost', 'port': 3306, 'user': 'root', 'password': 'password', 'database': 'galactic_gateway'})
# asyncio.run(db.connect())
