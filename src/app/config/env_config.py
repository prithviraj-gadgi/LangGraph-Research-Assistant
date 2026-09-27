from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: Literal["local", "dev", "test", "uat", "prod"] = Field(
        default="local",
        description="Application environment",
        alias="APP_ENV",
    )

    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Log level",
        alias="LOG_LEVEL",
    )

    structlog_json: bool = Field(
        default=False,
        description="Whether to use structlog for logging",
        alias="STRUCTLOG_JSON",
    )

    langsmith_tracing: bool = Field(
        default=True,
        description="Whether the tracing is enabled or not",
        alias="LANGSMITH_TRACING",
    )

    langsmith_endpoint: AnyHttpUrl = Field(
        default=AnyHttpUrl("https://aws.api.smith.langchain.com"),
        description="The endpoint to access the LangSmith API",
        alias="LANGSMITH_ENDPOINT",
    )

    langsmith_api_key: str = Field(
        default="",
        description="The API key to access the LangSmith API",
        alias="LANGSMITH_API_KEY",
    )

    langsmith_project: str = Field(
        default="",
        description="LangSmith project name",
        alias="LANGSMITH_PROJECT",
    )

    tavily_api_key: str = Field(
        default="",
        description="The API key to access the Tavily API",
        alias="TAVILY_API_KEY",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
