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