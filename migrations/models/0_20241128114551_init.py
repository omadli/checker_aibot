from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "dbuser" (
    "uuid" UUID NOT NULL  PRIMARY KEY,
    "id" BIGINT NOT NULL UNIQUE,
    "full_name" VARCHAR(255) NOT NULL,
    "username" VARCHAR(255),
    "join_date" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS "idx_dbuser_id_c6dd93" ON "dbuser" ("id");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
