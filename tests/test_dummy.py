import os
import sys

from fastapi.testclient import TestClient

from app.main import app

# Добавляем корень проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Recipe API is running"}


def test_get_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_recipe_validation():
    response = client.post("/recipes", json={})
    assert response.status_code == 422
