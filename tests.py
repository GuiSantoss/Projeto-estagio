from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_listar_empresas():
    response = client.get("/empresas")
    assert response.status_code == 200

def test_listar_obrigacoes():
    response = client.get("/obrigacoes")
    assert response.status_code == 200
