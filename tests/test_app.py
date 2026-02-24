from http import HTTPStatus


def test_read_root(client):
    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def test_read_jota(client):
    response = client.get('/jota')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'johndoe',
            'email': 'john@email.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'johndoe',
        'email': 'john@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'johndoe',
                'email': 'john@email.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'john_doe',
            'email': 'john_doe@email.com',
            'password': 'new_secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'john_doe',
        'email': 'john_doe@email.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'john_doe',
        'email': 'john_doe@email.com',
        'id': 1,
    }
