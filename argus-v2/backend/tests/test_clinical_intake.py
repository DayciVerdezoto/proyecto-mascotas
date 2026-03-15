from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200


def test_clinical_intake_txt_file():
    payload = (
        b"Diagnostico principal: apendicitis aguda\n"
        b"Hallazgos operatorios: inflamacion severa del apendice\n"
        b"Procedimiento: apendicectomia laparoscopico"
    )
    response = client.post(
        '/clinical/intake',
        files={'file': ('informe.txt', payload, 'text/plain')},
    )
    assert response.status_code == 200
    body = response.json()
    assert 'diagnosticos' in body
    assert 'hallazgos' in body
