# Guia Passo a Passo: Rodar Testes da Book API

## ⚡ TL;DR (Resumo Executivo)

Se você quer começar **AGORA**:

```bash
# 1. Instalar
pip install pytest pytest-cov faker

# 2. Copiar os arquivos dos testes para pasta tests/
# (veja arquivo: testes_book_api_completo.md)

# 3. Rodar tudo
pytest -v

# 4. Ver cobertura
pytest --cov=. --cov-report=html
```

---

## Passo 1: Preparar ambiente

### 1.1 Verificar Python instalado

```bash
python --version
# Deve retornar Python 3.8+
```

### 1.2 Criar ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 1.3 Instalar dependências

Crie arquivo `requirements.txt` na raiz do projeto:

```
Flask==2.3.3
pytest==7.4.3
pytest-cov==4.1.0
pytest-benchmark==4.0.0
requests==2.31.0
faker==22.0.0
```

Instale:

```bash
pip install -r requirements.txt
```

---

## Passo 2: Criar estrutura de pastas

```bash
# Criar pasta de testes
mkdir tests

# Criar arquivo vazio para Python reconhecer como pacote
touch tests/__init__.py
```

Sua estrutura deve ficar assim:

```
seu_projeto/
├── app.py
├── requirements.txt
├── pytest.ini
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_unit.py
    ├── test_persistence.py
    ├── test_integration.py
    ├── test_performance.py
    ├── test_security.py
    └── test_load.py
```

---

## Passo 3: Copiar os arquivos de teste

### 3.1 Criar arquivo: tests/conftest.py

Este arquivo contém fixtures (preparação) compartilhadas por todos os testes.

**Copie o conteúdo de "conftest.py" do documento testes_book_api_completo.md**

### 3.2 Criar arquivo: tests/test_unit.py

Testes de unidade (validar classe Livro isoladamente).

**Copie o conteúdo de "test_unit.py" do documento testes_book_api_completo.md**

### 3.3 Criar arquivo: tests/test_integration.py

Testes de integração (testar endpoints da API completos).

**Copie o conteúdo de "test_integration.py" do documento testes_book_api_completo.md**

### 3.4 Criar arquivo: tests/test_persistence.py

Testes de persistência de dados.

**Copie o conteúdo de "test_persistence.py" do documento testes_book_api_completo.md**

### 3.5 Criar arquivo: tests/test_performance.py

Testes de performance e tempo de resposta.

**Copie o conteúdo de "test_performance.py" do documento testes_book_api_completo.md**

### 3.6 Criar arquivo: tests/test_security.py

Testes de segurança.

**Copie o conteúdo de "test_security.py" do documento testes_book_api_completo.md**

### 3.7 Criar arquivo: tests/test_load.py

Testes de carga.

**Copie o conteúdo de "test_load.py" do documento testes_book_api_completo.md**

---

## Passo 4: Criar arquivo pytest.ini

Na **raiz do projeto**, crie arquivo `pytest.ini`:

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

## Passo 5: Rodar os testes

Abra terminal na **raiz do projeto** e rode:

### 5.1 Rodar TODOS os testes

```bash
pytest
```

Você verá algo como:

```
tests/test_unit.py::TestLivroModel::test_livro_criacao_sucesso PASSED
tests/test_unit.py::TestLivroModel::test_livro_to_dict PASSED
...
tests/test_integration.py::TestIntegracaoAPI::test_criar_e_consultar_livro PASSED
...
==================== 25 passed in 1.23s ====================
```

### 5.2 Rodar com MAIS detalhes

```bash
pytest -v
```

Mostra nome completo de cada teste.

### 5.3 Rodar UM arquivo de teste

```bash
# Apenas testes de unidade
pytest tests/test_unit.py

# Apenas testes de integração
pytest tests/test_integration.py

# Apenas testes de performance
pytest tests/test_performance.py
```

### 5.4 Rodar UM teste específico

```bash
pytest tests/test_unit.py::TestLivroModel::test_livro_criacao_sucesso -v
```

### 5.5 Rodar com cobertura de código

```bash
# Mostrar no terminal
pytest --cov=. --cov-report=term-missing

# Gerar arquivo HTML (melhor visualização)
pytest --cov=. --cov-report=html
```

Depois abra o arquivo `htmlcov/index.html` no navegador para ver:
- Qual % do código foi testado
- Quais linhas NÃO foram testadas

### 5.6 Parar em primeira falha

```bash
pytest -x
```

Útil quando muitos testes falham e você quer corrigir o primeiro.

### 5.7 Mostrar prints (output dos testes)

```bash
pytest -s
```

Mostra qualquer `print()` que você colocou no código.

---

## Passo 6: Entender os resultados

Quando você roda `pytest -v`, verá algo assim:

```
tests/test_unit.py::TestLivroModel::test_livro_criacao_sucesso PASSED     [ 4%]
tests/test_unit.py::TestLivroModel::test_livro_to_dict PASSED             [ 8%]
tests/test_unit.py::TestValidacaoLivro::test_ano_valido PASSED            [12%]
tests/test_integration.py::TestIntegracaoAPI::test_criar_e_consultar_livro PASSED [16%]
tests/test_integration.py::TestIntegracaoAPI::test_fluxo_completo_crud PASSED [20%]
...
==================== 25 passed in 1.23s ====================
```

**Explicação:**

- ✅ **PASSED**: Teste passou
- ❌ **FAILED**: Teste falhou
- ⚠️ **SKIPPED**: Teste foi pulado
- `[4%]`: Progresso geral dos testes

---

## Passo 7: Rotina de desenvolvimento

### Quando escrever novo código:

```bash
# 1. Escrever o teste PRIMEIRO
# (ou escrever o código depois)

# 2. Rodar para confirmar que falha
pytest tests/test_unit.py -v

# 3. Escrever o código para fazer passar
# (editar seu app.py, etc)

# 4. Rodar novamente para confirmar que passa
pytest tests/test_unit.py -v

# 5. Rodar todos os testes para confirmar que nada quebrou
pytest -v
```

### Antes de fazer push/commit:

```bash
# 1. Rodar todos os testes
pytest -v

# 2. Verificar cobertura
pytest --cov=. --cov-report=term-missing

# 3. Se tudo passou, pode fazer commit
git add .
git commit -m "Add novos testes"
```

---

## Passo 8: Troubleshooting (resolvendo problemas)

### Problema: "ModuleNotFoundError: No module named 'pytest'"

**Solução:**
```bash
pip install pytest
```

### Problema: "ModuleNotFoundError: No module named 'flask'"

**Solução:**
```bash
pip install -r requirements.txt
```

### Problema: Testes não encontrados

**Solução:**
- Confirme que os arquivos estão em pasta `tests/`
- Confirme que nomes começam com `test_` (ex: `test_unit.py`)
- Confirme que funções de teste começam com `test_` (ex: `def test_criar()`)

### Problema: "FAILED - AssertionError"

Significa que o teste falhou. Procure pela mensagem de erro:

```
AssertionError: assert 'algo' == 'outra coisa'

E       assert 'algo' == 'outra coisa'
E         - outra coisa
E         + algo
```

Veja o que foi diferente do esperado e corrija no `app.py`.

### Problema: Pytest não encontra imports

**Solução:**
Confirme que sua estrutura está assim:

```
projeto/
├── app.py
├── tests/
│   ├── __init__.py     ← arquivo vazio mas IMPORTANTE
│   └── test_unit.py
└── pytest.ini
```

---

## Referência Rápida de Comandos

| Comando | O que faz |
|---------|-----------|
| `pytest` | Roda todos os testes |
| `pytest -v` | Roda com nomes completos visíveis |
| `pytest -x` | Para na primeira falha |
| `pytest -s` | Mostra prints do código |
| `pytest tests/test_unit.py` | Roda apenas 1 arquivo |
| `pytest -k "criar"` | Roda apenas testes que têm "criar" no nome |
| `pytest --cov=.` | Mostra cobertura no terminal |
| `pytest --cov=. --cov-report=html` | Gera relatório HTML de cobertura |
| `pytest --lf` | Roda apenas último teste que falhou |
| `pytest -x --lf -v` | Para na 1ª falha e mostra verboso |

---

## Checklist Final

Antes de considerar pronto:

- [ ] `pip install -r requirements.txt` funcionou
- [ ] Pasta `tests/` criada com arquivo `__init__.py`
- [ ] Arquivo `pytest.ini` criado na raiz
- [ ] Todos os 7 arquivos de teste copiados (conftest.py, test_unit.py, etc)
- [ ] `pytest` roda sem erro
- [ ] Todos os testes passaram (ou a maioria)
- [ ] `pytest --cov=. --cov-report=html` gerou pasta `htmlcov/`
- [ ] Abri `htmlcov/index.html` e vi o relatório

---

## Próximos passos

1. **Entender cada tipo de teste** (leia comentários nos arquivos)
2. **Adicionar mais testes** conforme adiciona features
3. **Manter cobertura acima de 80%** (boa prática)
4. **Usar CI/CD** (GitHub Actions, GitLab CI) para rodar testes automaticamente
5. **Documentar testes** no README do projeto

---

## Links úteis

- Documentação Pytest: https://docs.pytest.org/
- Documentação Flask Testing: https://flask.palletsprojects.com/testing/
- Pytest fixtures: https://docs.pytest.org/en/stable/how-to-use-fixtures.html

