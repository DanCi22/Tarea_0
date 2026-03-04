from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_tarea_0():
    response = client.get("/tarea-0")
    assert response.status_code == 200
    assert response.json() == {"respuesta": "Primer tarea realizada"}