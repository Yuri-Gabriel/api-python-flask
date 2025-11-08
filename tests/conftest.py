import pytest
from flask import Flask
from app import app as flask_app
from controller.controller import Livro, livros_db
from faker import Faker

fake = Faker('pt_BR')

@pytest.fixture
def client():
    """Cliente de teste do Flask"""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

@pytest.fixture
def cleanup_db():
    """Limpa o banco antes e depois de cada teste"""
    livros_db.clear()
    yield
    livros_db.clear()

@pytest.fixture
def livro_exemplo():
    """Livro de exemplo para testes"""
    return {
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949,
        "isbn": "978-0451524935"
    }

@pytest.fixture
def livros_multiplos():
    """Múltiplos livros para testes"""
    return [
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "ano": 1949,
            "isbn": "978-0451524935"
        },
        {
            "titulo": "O Senhor dos Anéis",
            "autor": "J.R.R. Tolkien",
            "ano": 1954,
            "isbn": "978-0544003415"
        },
        {
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "ano": 1899,
            "isbn": "978-8535928341"
        }
    ]

@pytest.fixture
def livro_fake():
    """Livro aleatório gerado pela Faker"""
    return {
        "titulo": fake.sentence(),
        "autor": fake.name(),
        "ano": fake.year_int(),
        "isbn": fake.isbn10()
    }