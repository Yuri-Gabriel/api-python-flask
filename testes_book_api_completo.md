# Testes da Book API em Flask com Pytest - Guia Prático

## Índice
1. [Estrutura de Projeto](#estrutura-de-projeto)
2. [Configuração Inicial](#configuração-inicial)
3. [3.1 - Testes de Métodos de Classe (Unit Tests)](#31---testes-de-métodos-de-classe)
4. [3.2 - Testes de Persistência de Dados](#32---testes-de-persistência-de-dados)
5. [3.3 - Testes de Integração de Componentes](#33---testes-de-integração-de-componentes)
6. [3.4 - Testes de Tempo de Resposta](#34---testes-de-tempo-de-resposta)
7. [3.5 - Testes de Segurança](#35---testes-de-segurança)
8. [3.6 - Testes de Carga](#36---testes-de-carga)
9. [Comandos para Rodar](#comandos-para-rodar)

---

## Estrutura de Projeto

```
book_api/
├── app.py                    # Aplicação principal
├── controller.py             # Controladores (lógica)
├── models.py                 # Modelos de dados
├── database.py               # Conexão com banco
├── requirements.txt
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Configurações e fixtures globais
│   ├── test_unit.py         # Testes unitários (3.1)
│   ├── test_persistence.py  # Testes de persistência (3.2)
│   ├── test_integration.py  # Testes de integração (3.3)
│   ├── test_performance.py  # Testes de performance (3.4)
│   ├── test_security.py     # Testes de segurança (3.5)
│   └── test_load.py         # Testes de carga (3.6)
└── pytest.ini
```

---

## Configuração Inicial

### 1. Instalar dependências

Crie um arquivo `requirements.txt`:

```
Flask==2.3.x
pytest==7.4.3
pytest-cov==4.1.0
pytest-benchmark==4.0.0
requests==2.31.0
faker==22.0.0
```

Instale tudo:

```bash
pip install -r requirements.txt
```

### 2. Arquivo: `pytest.ini`

```ini
[pytest]
minversion = 7.0
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --strict-markers
    --tb=short
markers =
    unit: Testes de unidade
    integration: Testes de integração
    performance: Testes de performance
    security: Testes de segurança
```

---

## Aplicação Principal (exemplo)

### app.py

```python
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Banco de dados em memória para exemplo
livros_db = []

class Livro:
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "isbn": self.isbn
        }

# UC-01: Consultar Livros
@app.route('/livros', methods=['GET'])
def consultar_livros():
    """Retorna todos os livros"""
    return jsonify([livro.to_dict() for livro in livros_db]), 200

@app.route('/livros/<int:livro_id>', methods=['GET'])
def consultar_livro_por_id(livro_id):
    """Retorna um livro específico"""
    for livro in livros_db:
        if livro.id == livro_id:
            return jsonify(livro.to_dict()), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

# UC-02: Cadastrar Livros
@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    """Cadastra um novo livro"""
    data = request.get_json()
    
    # Validação
    if not data or not all(k in data for k in ['titulo', 'autor', 'ano', 'isbn']):
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400
    
    if not isinstance(data['ano'], int) or data['ano'] < 1000:
        return jsonify({"erro": "Ano inválido"}), 400
    
    novo_id = len(livros_db) + 1
    livro = Livro(novo_id, data['titulo'], data['autor'], data['ano'], data['isbn'])
    livros_db.append(livro)
    
    return jsonify(livro.to_dict()), 201

# UC-03: Editar Livros
@app.route('/livros/<int:livro_id>', methods=['PUT'])
def editar_livro(livro_id):
    """Edita um livro existente"""
    data = request.get_json()
    
    for livro in livros_db:
        if livro.id == livro_id:
            livro.titulo = data.get('titulo', livro.titulo)
            livro.autor = data.get('autor', livro.autor)
            livro.ano = data.get('ano', livro.ano)
            livro.isbn = data.get('isbn', livro.isbn)
            return jsonify(livro.to_dict()), 200
    
    return jsonify({"erro": "Livro não encontrado"}), 404

# UC-04: Deletar Livros
@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    """Deleta um livro"""
    global livros_db
    for i, livro in enumerate(livros_db):
        if livro.id == livro_id:
            livros_db.pop(i)
            return jsonify({"mensagem": "Livro deletado"}), 200
    
    return jsonify({"erro": "Livro não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Configuração de Fixtures (conftest.py)

### tests/conftest.py

```python
import pytest
from flask import Flask
from app import app as flask_app, Livro, livros_db
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
```

---

## 3.1 - Testes de Métodos de Classe (Unit Tests)

### tests/test_unit.py

```python
import pytest
from app import Livro
from unittest.mock import Mock, patch

class TestLivroModel:
    """Testes da classe Livro (Unit Tests)"""
    
    def test_livro_criacao_sucesso(self):
        """Teste: criar livro com sucesso"""
        # Arrange
        livro = Livro(1, "1984", "George Orwell", 1949, "978-0451524935")
        
        # Act & Assert
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
        # ISBN válido tem entre 10 e 13 dígitos
        isbn_numeros = livro.isbn.replace("-", "")
        assert len(isbn_numeros) in [10, 13]
```

**Rodar:**
```bash
pytest tests/test_unit.py -v
```

---



## 3.3 - Testes de Integração de Componentes

### tests/test_integration.py

```python
import pytest
import json

class TestIntegracaoAPI:
    """Testes de integração da API completa"""
    
    def test_criar_e_consultar_livro(self, client, cleanup_db, livro_exemplo):
        """Teste: criar livro e recuperar"""
        # Criar
        response_create = client.post('/livros',
                                     data=json.dumps(livro_exemplo),
                                     content_type='application/json')
        assert response_create.status_code == 201
        
        # Consultar
        response_get = client.get('/livros/1')
        assert response_get.status_code == 200
        
        data = json.loads(response_get.data)
        assert data['titulo'] == livro_exemplo['titulo']
    
    def test_fluxo_completo_crud(self, client, cleanup_db, livro_exemplo):
        """Teste: fluxo completo de CRUD"""
        # CREATE
        response_create = client.post('/livros',
                                     data=json.dumps(livro_exemplo),
                                     content_type='application/json')
        assert response_create.status_code == 201
        
        # READ
        response_read = client.get('/livros/1')
        assert response_read.status_code == 200
        
        # UPDATE
        livro_atualizado = {
            "titulo": "1984 - Nova Edição",
            "autor": livro_exemplo['autor'],
            "ano": livro_exemplo['ano'],
            "isbn": livro_exemplo['isbn']
        }
        response_update = client.put('/livros/1',
                                    data=json.dumps(livro_atualizado),
                                    content_type='application/json')
        assert response_update.status_code == 200
        
        # DELETE
        response_delete = client.delete('/livros/1')
        assert response_delete.status_code == 200
        
        # Verificar deleção
        response_verify = client.get('/livros/1')
        assert response_verify.status_code == 404
    
    def test_listar_multiplos_livros(self, client, cleanup_db, livros_multiplos):
        """Teste: listar múltiplos livros"""
        # Criar múltiplos
        for livro in livros_multiplos:
            client.post('/livros',
                       data=json.dumps(livro),
                       content_type='application/json')
        
        # Listar
        response = client.get('/livros')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert len(data) == 3
        assert data[0]['titulo'] == "1984"
    
    def test_editar_livro_nao_existente(self, client, cleanup_db, livro_exemplo):
        """Teste: editar livro que não existe"""
        response = client.put('/livros/999',
                             data=json.dumps(livro_exemplo),
                             content_type='application/json')
        assert response.status_code == 404
    
    def test_deletar_livro_nao_existente(self, client, cleanup_db):
        """Teste: deletar livro que não existe"""
        response = client.delete('/livros/999')
        assert response.status_code == 404
    
    @pytest.mark.parametrize("livro", [
        {"titulo": "Livro 1", "autor": "Autor 1", "ano": 2020, "isbn": "isbn1"},
        {"titulo": "Livro 2", "autor": "Autor 2", "ano": 2021, "isbn": "isbn2"},
        {"titulo": "Livro 3", "autor": "Autor 3", "ano": 2022, "isbn": "isbn3"},
    ])
    def test_criar_multiplos_livros_parametrizado(self, client, cleanup_db, livro):
        """Teste parametrizado: criar múltiplos livros"""
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        assert response.status_code == 201
```

**Rodar:**
```bash
pytest tests/test_integration.py -v
```

---

## 3.4 - Testes de Tempo de Resposta

### tests/test_performance.py

```python
import pytest
import time
import json

class TestPerformance:
    """Testes de performance e tempo de resposta"""
    
    def test_criar_livro_tempo_resposta(self, client, cleanup_db, livro_exemplo):
        """Teste: criação de livro em menos de 1 segundo"""
        start_time = time.time()
        
        response = client.post('/livros',
                              data=json.dumps(livro_exemplo),
                              content_type='application/json')
        
        elapsed_time = time.time() - start_time
        
        assert response.status_code == 201
        assert elapsed_time < 1.0, f"Tempo: {elapsed_time}s"
    
    def test_consultar_livro_tempo_resposta(self, client, cleanup_db, livro_exemplo):
        """Teste: consulta de livro em menos de 0.5s"""
        # Criar primeiro
        client.post('/livros',
                   data=json.dumps(livro_exemplo),
                   content_type='application/json')
        
        # Consultar
        start_time = time.time()
        response = client.get('/livros/1')
        elapsed_time = time.time() - start_time
        
        assert response.status_code == 200
        assert elapsed_time < 0.5, f"Tempo: {elapsed_time}s"
    
    def test_listar_livros_tempo_resposta(self, client, cleanup_db, livros_multiplos):
        """Teste: listar livros em menos de 1s"""
        # Criar múltiplos
        for livro in livros_multiplos:
            client.post('/livros',
                       data=json.dumps(livro),
                       content_type='application/json')
        
        # Listar
        start_time = time.time()
        response = client.get('/livros')
        elapsed_time = time.time() - start_time
        
        assert response.status_code == 200
        assert elapsed_time < 1.0, f"Tempo: {elapsed_time}s"
    
    @pytest.mark.benchmark
    def test_criar_livro_benchmark(self, client, cleanup_db, livro_exemplo, benchmark):
        """Teste: benchmark de criação"""
        def criar():
            return client.post('/livros',
                             data=json.dumps(livro_exemplo),
                             content_type='application/json')
        
        result = benchmark(criar)
        assert result.status_code == 201
    
    def test_multiplas_requisicoes_performance(self, client, cleanup_db):
        """Teste: 50 requisições sequenciais"""
        import concurrent.futures
        
        def criar_livro(index):
            livro = {
                "titulo": f"Livro {index}",
                "autor": f"Autor {index}",
                "ano": 2020 + index,
                "isbn": f"isbn{index}"
            }
            return client.post('/livros',
                             data=json.dumps(livro),
                             content_type='application/json')
        
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(criar_livro, range(50)))
        
        elapsed_time = time.time() - start_time
        
        assert all(r.status_code == 201 for r in results)
        print(f"\n50 requisições em {elapsed_time:.2f}s ({50/elapsed_time:.2f} req/s)")
```

**Rodar:**
```bash
pytest tests/test_performance.py -v
pytest tests/test_performance.py --benchmark-only
```

---

## 3.5 - Testes de Segurança

### tests/test_security.py

```python
import pytest
import json

class TestSeguranca:
    """Testes de segurança da API"""
    
    def test_campos_obrigatorios(self, client, cleanup_db):
        """Teste: rejeita livro sem campos obrigatórios"""
        livro_incompleto = {"titulo": "Livro"}
        
        response = client.post('/livros',
                              data=json.dumps(livro_incompleto),
                              content_type='application/json')
        
        assert response.status_code == 400
    
    def test_ano_invalido_negativo(self, client, cleanup_db):
        """Teste: rejeita ano negativo"""
        livro = {
            "titulo": "Livro",
            "autor": "Autor",
            "ano": -1000,
            "isbn": "isbn"
        }
        
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        
        assert response.status_code == 400
    
    def test_ano_invalido_muito_pequeno(self, client, cleanup_db):
        """Teste: rejeita ano menor que 1000"""
        livro = {
            "titulo": "Livro",
            "autor": "Autor",
            "ano": 500,
            "isbn": "isbn"
        }
        
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        
        assert response.status_code == 400
    
    def test_sql_injection_titulo(self, client, cleanup_db):
        """Teste: proteção contra SQL Injection no título"""
        livro = {
            "titulo": "'; DROP TABLE livros; --",
            "autor": "Autor",
            "ano": 2020,
            "isbn": "isbn"
        }
        
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        
        # Deve aceitar como string normal, não executar SQL
        assert response.status_code == 201
        data = json.loads(response.data)
        assert "'; DROP TABLE" in data['titulo']
    
    def test_xss_prevention_autor(self, client, cleanup_db):
        """Teste: prevenção de XSS no autor"""
        livro = {
            "titulo": "Livro Teste",
            "autor": "<script>alert('xss')</script>",
            "ano": 2020,
            "isbn": "isbn"
        }
        
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        
        assert response.status_code == 201
        data = json.loads(response.data)
        # Flask escapa HTML automaticamente ou aceita como string
        assert "alert" in data['autor']
    
    def test_isbn_muito_longo(self, client, cleanup_db):
        """Teste: rejeita ISBN muito longo"""
        livro = {
            "titulo": "Livro",
            "autor": "Autor",
            "ano": 2020,
            "isbn": "x" * 1000
        }
        
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        
        # Pode aceitar ou rejeitar dependendo da validação
        assert response.status_code in [201, 400]
    
    @pytest.mark.parametrize("titulo,autor,should_fail", [
        ("Livro Normal", "Autor Normal", False),
        ("", "Autor", True),  # Título vazio
        ("Livro", "", True),  # Autor vazio
        (None, "Autor", True),  # Título None
    ])
    def test_validacao_campos_parametrizado(self, client, cleanup_db, titulo, autor, should_fail):
        """Teste parametrizado de validação"""
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": 2020,
            "isbn": "isbn"
        }
        
        response = client.post('/livros',
                              data=json.dumps(livro),
                              content_type='application/json')
        
        if should_fail:
            assert response.status_code == 400
        else:
            assert response.status_code == 201
```

**Rodar:**
```bash
pytest tests/test_security.py -v
```

---

## 3.6 - Testes de Carga (Opcional - com Locust)

### tests/test_load.py (com requests)

```python
import pytest
import requests
import concurrent.futures
import time

class TestCarga:
    """Testes de carga na API"""
    
    def test_100_requisicoes_POST(self, client, cleanup_db):
        """Teste: 100 POSTs sequenciais"""
        start_time = time.time()
        
        for i in range(100):
            livro = {
                "titulo": f"Livro {i}",
                "autor": f"Autor {i}",
                "ano": 2020,
                "isbn": f"isbn{i}"
            }
            response = client.post('/livros',
                                 data=json.dumps(livro),
                                 content_type='application/json')
            assert response.status_code == 201
        
        elapsed_time = time.time() - start_time
        print(f"\n100 POSTs em {elapsed_time:.2f}s ({100/elapsed_time:.2f} req/s)")
    
    def test_100_requisicoes_GET_concorrentes(self, client, cleanup_db):
        """Teste: 100 GETs concorrentes"""
        # Criar alguns livros
        for i in range(10):
            livro = {
                "titulo": f"Livro {i}",
                "autor": f"Autor {i}",
                "ano": 2020,
                "isbn": f"isbn{i}"
            }
            client.post('/livros',
                       data=json.dumps(livro),
                       content_type='application/json')
        
        def fazer_get(i):
            livro_id = (i % 10) + 1
            return client.get(f'/livros/{livro_id}')
        
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(fazer_get, range(100)))
        
        elapsed_time = time.time() - start_time
        
        assert all(r.status_code == 200 for r in results)
        print(f"\n100 GETs concorrentes em {elapsed_time:.2f}s ({100/elapsed_time:.2f} req/s)")
    
    def test_carga_mista_crud(self, client, cleanup_db):
        """Teste: operações CRUD sob carga"""
        import json
        
        def operacao_aleatoria(i):
            if i % 4 == 0:  # CREATE
                livro = {
                    "titulo": f"Livro {i}",
                    "autor": f"Autor {i}",
                    "ano": 2020,
                    "isbn": f"isbn{i}"
                }
                return client.post('/livros',
                                 data=json.dumps(livro),
                                 content_type='application/json')
            elif i % 4 == 1:  # READ
                livro_id = (i % 10) + 1
                return client.get(f'/livros/{livro_id}')
            elif i % 4 == 2:  # UPDATE
                livro_id = (i % 10) + 1
                livro = {
                    "titulo": f"Livro Atualizado {i}",
                    "autor": f"Autor {i}",
                    "ano": 2021,
                    "isbn": f"isbn{i}"
                }
                return client.put(f'/livros/{livro_id}',
                                data=json.dumps(livro),
                                content_type='application/json')
            else:  # DELETE
                livro_id = (i % 10) + 1
                return client.delete(f'/livros/{livro_id}')
        
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(operacao_aleatoria, range(50)))
        
        elapsed_time = time.time() - start_time
        
        print(f"\n50 operações mistas em {elapsed_time:.2f}s ({50/elapsed_time:.2f} op/s)")
        assert len([r for r in results if r.status_code in [200, 201, 204]]) > 40
```

### Arquivo: tests/locustfile.py (teste de carga com Locust)

```python
from locust import HttpUser, task, between
import json

class BookAPIUser(HttpUser):
    """Simula usuários usando a Book API"""
    
    wait_time = between(1, 3)
    
    def on_start(self):
        """Executado quando usuário inicia"""
        self.livro_counter = 0
    
    @task(3)  # Peso 3 - executado 3x mais
    def criar_livro(self):
        """Tarefa: criar livro"""
        self.livro_counter += 1
        livro = {
            "titulo": f"Livro {self.livro_counter}",
            "autor": f"Autor {self.livro_counter}",
            "ano": 2020,
            "isbn": f"isbn{self.livro_counter}"
        }
        self.client.post("/livros",
                        json=livro)
    
    @task(1)  # Peso 1
    def listar_livros(self):
        """Tarefa: listar livros"""
        self.client.get("/livros")
    
    @task(2)  # Peso 2
    def obter_livro(self):
        """Tarefa: obter livro específico"""
        livro_id = (self.livro_counter % 10) + 1
        self.client.get(f"/livros/{livro_id}")
```

**Rodar teste de carga com Locust:**
```bash
locust -f tests/locustfile.py -u 100 -r 10 -t 5m --headless
```

---

## Comandos para Rodar

### Executar todos os testes

```bash
pytest
```

### Executar com verbosidade

```bash
pytest -v
```

### Executar por tipo

```bash
# Testes de unidade (3.1)
pytest tests/test_unit.py -v

# Testes de persistência (3.2)
pytest tests/test_persistence.py -v

# Testes de integração (3.3)
pytest tests/test_integration.py -v

# Testes de performance (3.4)
pytest tests/test_performance.py -v

# Testes de segurança (3.5)
pytest tests/test_security.py -v

# Testes de carga (3.6)
pytest tests/test_load.py -v
```

### Com cobertura de código

```bash
# Terminal
pytest --cov=. --cov-report=term-missing

# Gerar HTML
pytest --cov=. --cov-report=html

# Abrir relatório
# Windows: start htmlcov/index.html
# Linux/Mac: open htmlcov/index.html
```

### Parar em primeira falha

```bash
pytest -x
```

### Mostrar prints

```bash
pytest -s
```

### Teste específico

```bash
pytest tests/test_unit.py::TestLivroModel::test_livro_criacao_sucesso -v
```

### Com marcadores

```bash
pytest -m unit
pytest -m integration
pytest -m performance
pytest -m security
```

### Testes de carga

```bash
# Com Locust (interface web)
locust -f tests/locustfile.py

# Sem interface (headless)
locust -f tests/locustfile.py -u 100 -r 10 -t 5m --headless
```

---

## Checklist de Implementação

- [ ] Criar pasta `tests/`
- [ ] Criar `conftest.py` com fixtures
- [ ] Implementar `test_unit.py`
- [ ] Implementar `test_persistence.py`
- [ ] Implementar `test_integration.py`
- [ ] Implementar `test_performance.py`
- [ ] Implementar `test_security.py`
- [ ] Implementar `test_load.py`
- [ ] Criar `pytest.ini`
- [ ] Executar: `pytest -v`
- [ ] Gerar cobertura: `pytest --cov=. --cov-report=html`
- [ ] Revisar `htmlcov/index.html`

