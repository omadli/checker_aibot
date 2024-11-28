from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
OPENAI_API_KEY = env.str("OPENAI_API_KEY")
DEBUG = env.bool("DEBUG")
ADMINS = list(map(int, env.list("ADMINS")))
DB_URL = env.str("DB_URL")
USE_REDIS = env.bool("USE_REDIS", False)
REDIS_DB = env.int("REDIS_DB", 0)
REDIS_PASSWORD = env.str("REDIS_PASSWORD", None)


TORTOISE_ORM = {
    "connections": {
        "default": DB_URL
    },
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
