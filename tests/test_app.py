def test_index():
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_footer():
    response = client.get('/')
    assert response.status_code == 200
    assert b'Vitalii Mahdych' in response.data
