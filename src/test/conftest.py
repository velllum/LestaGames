import pytest
from flask import Flask

from src.core.app import create_app


@pytest.fixture
def client() -> Flask:
    """- получить объект приложения"""
    yield create_app()

