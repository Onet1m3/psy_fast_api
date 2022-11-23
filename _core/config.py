from starlette.config import Config

config = Config(".env")
# For Postgesql
# DATABASE_URL=f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@{config('POSTGRES_HOST')}:{config('POSTGRES_PORT')}/{config('POSTGRES_DB')}"
# For sqllite
DATABASE_URL = config("DATABASE_URL")
