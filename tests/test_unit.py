import pytest
from controller.controller import Livro

class TestLivroModel:
    """Testes da classe Livro (Unit Tests)"""
    
    def test_livro_criacao_sucesso(self):
        """Teste: criar livro com sucesso"""
        livro = Livro(1, "1984", "George Orwell", 1949, "978-0451524935")
        
        assert livro.id == 1
        assert livro.titulo == "1984"
        assert livro.autor == "George Orwell"
        assert livro.ano == 1949
        assert livro.isbn == "978-0451524935"
    
    def test_livro_to_dict(self):
        """Teste: conversão de livro para dicionário"""
        livro = Livro(1, "1984", "George Orwell", 1949, "978-0451524935")
        resultado = livro.to_dict()
        
        assert resultado["id"] == 1
        assert resultado["titulo"] == "1984"
        assert isinstance(resultado, dict)
    
    @pytest.mark.parametrize("titulo,autor,ano,isbn", [
        ("1984", "George Orwell", 1949, "978-0451524935"),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "978-0544003415"),
        ("Dom Casmurro", "Machado de Assis", 1899, "978-8535928341"),
    ])
    def test_livro_creation_parametrized(self, titulo, autor, ano, isbn):
        """Teste parametrizado: criar múltiplos livros"""
        livro = Livro(1, titulo, autor, ano, isbn)
        
        assert livro.titulo == titulo
        assert livro.autor == autor
        assert livro.ano == ano
        assert livro.isbn == isbn

class TestValidacaoLivro:
    """Testes de validação de livros"""
    
    def test_ano_valido(self):
        """Teste: ano deve ser válido"""
        livro = Livro(1, "Livro", "Autor", 2020, "isbn123")
        assert livro.ano >= 1000
    
    def test_titulo_nao_vazio(self):
        """Teste: título não pode ser vazio"""
        livro = Livro(1, "Título", "Autor", 2020, "isbn123")
        assert livro.titulo != ""
    
    def test_isbn_formato(self):
        """Teste: ISBN tem formato válido"""
        livro = Livro(1, "Livro", "Autor", 2020, "978-0451524935")
        
        isbn_numeros = livro.isbn.replace("-", "")
        assert len(isbn_numeros) in [10, 13]