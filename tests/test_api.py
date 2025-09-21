import pytest
import json

from app import app as flask_app

@pytest.fixture(scope="session")
def app():
    """Fixture obrigatória para pytest-flask"""
    flask_app.config.update({"TESTING": True})
    return flask_app



def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Books API" in res.data


def test_show_books(client):
    res = client.get("/book")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert any(book["title"] == "Código Limpo" for book in data)


def test_store_book(client):
    new_book = {"id": 3, "title": "Clean Architecture", "author": "Robert Martin"}
    res = client.post("/book", data=json.dumps(new_book), content_type="application/json")

    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "Clean Architecture"


def test_find_book(client):
    res = client.get("/book/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "Código Limpo"


def test_update_book(client):
    update = {"title": "Código Limpo (2ª edição)"}
    res = client.put("/book/1", data=json.dumps(update), content_type="application/json")

    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "Código Limpo (2ª edição)"

def test_update_non_existent_book(client):
    update = {"title": "Código Limpo (2ª edição)"}
    res = client.put("/book/9", data=json.dumps(update), content_type="application/json")

    assert res.status_code == 200
    data = res.get_json()
    assert data == {}


def test_delete_book(client):
    tmp_book = {"id": 99, "title": "Livro Temp", "author": "Autor X"}
    client.post("/book", data=json.dumps(tmp_book), content_type="application/json")


    res = client.delete("/book/99")
    assert res.status_code == 200
    data = res.get_json()
    assert not any(book["id"] == 99 for book in data)

