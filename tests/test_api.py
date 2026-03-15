from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_cases_flow():
    payload = {
        'edad': 9,
        'raza': 'Labrador',
        'peso': 30,
        'velocidad_crecimiento': 'moderado',
        'diagnostico_citologico': 'sospechoso',
        'indice_mitotico': 6,
    }
    create_resp = client.post('/cases', json=payload)
    assert create_resp.status_code == 200
    case_id = create_resp.json()['id']

    get_resp = client.get(f'/cases/{case_id}')
    assert get_resp.status_code == 200
    assert get_resp.json()['raza'] == 'Labrador'

    list_resp = client.get('/cases')
    assert list_resp.status_code == 200
    assert isinstance(list_resp.json(), list)
