cat > src/core/config.py <<'EOF'
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Enterprise Knowledge Intelligence Platform"

    database_url: str = (
        "postgresql+asyncpg://enterprise:enterprise@localhost:5432/enterprise_rag"
    )

    redis_url: str = "redis://localhost:6379/0"

    embedding_model: str = "all-MiniLM-L6-v2"

    llm_provider: str = "openai"

    llm_model: str = ""

    openai_api_key: str = ""

    jwt_secret: str = "change-this-secret"


settings = Settings()
EOF