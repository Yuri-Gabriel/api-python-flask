# Guia Completo: Testes de API em Python com Pytest

## Índice
1. [Instalação e Setup](#instalação-e-setup)
2. [Estrutura de Projeto](#estrutura-de-projeto)
3. [Tipos de Testes Implementados](#tipos-de-testes-implementados)
4. [Exemplos Práticos](#exemplos-práticos)
5. [Executando os Testes](#executando-os-testes)
6. [Cobertura de Código](#cobertura-de-código)

---

## Instalação e Setup

### Dependências Necessárias

```bash
pip install pytest==7.4.3
pip install pytest-cov==4.1.0
pip install pytest-asyncio==0.23.1
pip install pytest-benchmark==4.0.0
pip install pytest-httpserver==1.0.10
pip install pytest-mock==3.12.0
pip install requests==2.31.0
pip install fastapi==0.109.0
pip install uvicorn==0.27.0
pip install httpx==0.25.2
pip install faker==22.0.0
pip install locust==2.19.0
```

### Arquivo: requirements.txt

```
pytest==7.4.3
pytest-cov==4.1.0
pytest-asyncio==0.23.1
pytest-benchmark==4.0.0
pytest-httpserver==1.0.10
pytest-mock==3.12.0
requests==2.31.0
fastapi==0.109.0
uvicorn==0.27.0
httpx==0.25.2
faker==22.0.0
locust==2.19.0
python-multipart==0.0.6
```

### Arquivo: pytest.ini

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
    --disable-warnings
markers =
    unit: Testes de unidade
    integration: Testes de integração
    performance: Testes de performance/carga
    security: Testes de segurança
    slow: Testes lentos
    asyncio: Testes assíncronos
```

### Arquivo: .coveragerc

```ini
[run]
source = src
omit = 
    */tests/*
    */venv/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
    if TYPE_CHECKING:
    @abstractmethod
```

---

## Estrutura de Projeto

```
projeto_api/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   ├── database.py
│   └── exceptions.py
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   ├── conftest.py
│   │   ├── test_models.py
│   │   └── test_services.py
│   ├── integration/
│   │   ├── conftest.py
│   │   └── test_api.py
│   ├── performance/
│   │   └── test_performance.py
│   └── security/
│       └── test_security.py
├── requirements.txt
├── pytest.ini
└── .coveragerc
```

---

## Tipos de Testes Implementados

### 1. Testes de Unidade (Unit Tests) - Métodos de Classe

**Objetivo:** Verificar se cada classe/método retorna o esperado

**Técnica:** Manual e Automática
**Estágio:** Unidade
**Abordagem:** Caixa Branca e Preta

#### Exemplo: src/services.py
-----
```python
# src/services.py


### 3. Integração de Componentes (Integration Tests)

**Objetivo:** Verificar se componentes funcionam juntos corretamente

**Técnica:** Manual e Automática
**Estágio:** Integração
**Abordagem:** Caixa Branca e Preta

#### Exemplo: src/main.py


# src/main.py

```

#### Exemplo: tests/integration/test_api.py

```python
# tests/integration/test_api.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from src.main import app

@pytest.fixture
def client():
    """Fixture para cliente de teste da API"""
    return TestClient(app)

class TestUserAPI:
    """Testes de integração da API de usuários"""
    
    def test_create_user_success(self, client):
        """Teste: criar usuário via API"""
        response = client.post("/users", json={
            "name": "João Silva",
            "email": "joao@email.com"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "João Silva"
        assert data["email"] == "joao@email.com"
    
    def test_create_user_validation_error(self, client):
        """Teste: erro de validação ao criar usuário"""
        response = client.post("/users", json={
            "name": "João",
            "email": "email_invalido"
        })
        
        assert response.status_code == 400
        assert "Email inválido" in response.json()["detail"]
    
    def test_get_user_by_id(self, client):
        """Teste: obter usuário por ID"""
        # Criar usuário
        create_response = client.post("/users", json={
            "name": "Maria",
            "email": "maria@email.com"
        })
        user_id = create_response.json()["id"]
        
        # Obter usuário
        get_response = client.get(f"/users/{user_id}")
        
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["id"] == user_id
        assert data["name"] == "Maria"
    
    def test_get_user_not_found(self, client):
        """Teste: usuário não encontrado"""
        response = client.get("/users/9999")
        
        assert response.status_code == 404
        assert "não encontrado" in response.json()["detail"]
    
    @pytest.mark.parametrize("user_data", [
        {"name": "User1", "email": "user1@email.com"},
        {"name": "User2", "email": "user2@email.com"},
        {"name": "User3", "email": "user3@email.com"},
    ])
    def test_create_multiple_users(self, client, user_data):
        """Teste: criar múltiplos usuários"""
        response = client.post("/users", json=user_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == user_data["name"]
        assert data["email"] == user_data["email"]
```

---

### 4. Testes de Performance e Tempo de Resposta

**Objetivo:** Verificar se tempo de resposta é aceitável

**Técnica:** Manual e Automática
**Estágio:** Sistema
**Abordagem:** Caixa Preta

#### Exemplo: tests/performance/test_performance.py

```python
# tests/performance/test_performance.py
import pytest
import time
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

class TestPerformance:
    """Testes de performance"""
    
    @pytest.mark.benchmark
    def test_create_user_performance(self, client, benchmark):
        """Teste: performance ao criar usuário"""
        def create_user():
            return client.post("/users", json={
                "name": "Performance Test",
                "email": "perf@email.com"
            })
        
        result = benchmark(create_user)
        assert result.status_code == 200
    
    def test_create_user_response_time(self, client):
        """Teste: tempo de resposta ao criar usuário"""
        start_time = time.time()
        
        response = client.post("/users", json={
            "name": "Timing Test",
            "email": "timing@email.com"
        })
        
        elapsed_time = time.time() - start_time
        
        # Deve responder em menos de 1 segundo
        assert elapsed_time < 1.0
        assert response.status_code == 200
    
    def test_list_users_response_time(self, client):
        """Teste: tempo de resposta ao listar usuários"""
        # Criar alguns usuários
        for i in range(10):
            client.post("/users", json={
                "name": f"User{i}",
                "email": f"user{i}@email.com"
            })
        
        start_time = time.time()
        response = client.get("/users")
        elapsed_time = time.time() - start_time
        
        # Deve responder em menos de 2 segundos
        assert elapsed_time < 2.0
        assert response.status_code == 200
    
    @pytest.mark.parametrize("num_requests", [10, 50, 100])
    def test_concurrent_requests(self, client, num_requests):
        """Teste: múltiplas requisições sequenciais"""
        import concurrent.futures
        
        def make_request(index):
            return client.post("/users", json={
                "name": f"ConcurrentUser{index}",
                "email": f"concurrent{index}@email.com"
            })
        
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(make_request, range(num_requests)))
        
        elapsed_time = time.time() - start_time
        
        # Verificar que todas as requisições foram bem-sucedidas
        assert all(r.status_code == 200 for r in results)
        print(f"\n{num_requests} requisições em {elapsed_time:.2f}s ({num_requests/elapsed_time:.2f} req/s)")
```

### 6. Testes de Carga (Load Testing)

**Objetivo:** Verificar comportamento sob carga

**Arquivo: tests/performance/locustfile.py**

```python
# tests/performance/locustfile.py
from locust import HttpUser, task, between
import random

class APIUser(HttpUser):
    """Simula usuários interagindo com a API"""
    
    wait_time = between(1, 3)  # Aguardar entre 1-3 segundos
    
    def on_start(self):
        """Executado quando usuário inicia"""
        self.user_count = random.randint(1000, 9999)
    
    @task(3)  # Peso 3 - executado 3x mais frequentemente
    def create_user(self):
        """Tarefa: criar usuário"""
        self.client.post("/users", json={
            "name": f"LoadTestUser{self.user_count}",
            "email": f"loadtest{self.user_count}@email.com"
        })
    
    @task(1)  # Peso 1
    def get_users(self):
        """Tarefa: listar usuários"""
        self.client.get("/users")
    
    @task(2)  # Peso 2
    def get_specific_user(self):
        """Tarefa: obter usuário específico"""
        user_id = random.randint(1, 100)
        self.client.get(f"/users/{user_id}")
```

**Comando para executar teste de carga:**
```bash
locust -f tests/performance/locustfile.py -u 100 -r 10 -t 5m --headless
```

---

## Executando os Testes

### Executar todos os testes
```bash
pytest tests/
```

### Executar apenas testes de unidade
```bash
pytest tests/unit -v
```

### Executar testes com marcadores específicos
```bash
pytest -m unit              # Apenas unit tests
pytest -m integration       # Apenas testes de integração
pytest -m performance       # Apenas testes de performance
```

### Executar testes com output verboso
```bash
pytest -v tests/
```

### Executar com parada em primeira falha
```bash
pytest -x tests/
```

### Executar teste específico
```bash
pytest tests/unit/test_services.py::TestUserService::test_create_user_success -v
```

### Executar com cobertura de código
```bash
pytest --cov=src --cov-report=html --cov-report=term-missing tests/
```

---

## Cobertura de Código

### Gerar relatório de cobertura em HTML
```bash
pytest --cov=src --cov-report=html tests/
# Abrir htmlcov/index.html no navegador
```

### Gerar relatório no terminal com linhas não cobertas
```bash
pytest --cov=src --cov-report=term-missing tests/
```

### Gerar relatório em XML (para CI/CD)
```bash
pytest --cov=src --cov-report=xml tests/
```

### Definir limite mínimo de cobertura
```bash
pytest --cov=src --cov-fail-under=80 tests/
```
