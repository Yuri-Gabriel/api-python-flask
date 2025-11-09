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
        client.post('/livros',
                   data=json.dumps(livro_exemplo),
                   content_type='application/json')
        
        start_time = time.time()
        response = client.get('/livros/1')
        elapsed_time = time.time() - start_time
        
        assert response.status_code == 200
        assert elapsed_time < 0.5, f"Tempo: {elapsed_time}s"
    
    def test_listar_livros_tempo_resposta(self, client, cleanup_db, livros_multiplos):
        """Teste: listar livros em menos de 1s"""
        for livro in livros_multiplos:
            client.post('/livros',
                       data=json.dumps(livro),
                       content_type='application/json')
        
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
        cont = 5000
        
        results = list(map(criar_livro, range(cont)))
        
        elapsed_time = time.time() - start_time
        
        assert all(r.status_code == 201 for r in results)
        print(f"\n50 requisições em {elapsed_time:.2f}s ({cont/elapsed_time:.2f} req/s)")