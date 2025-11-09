import pytest
import json

class TestIntegracaoAPI:
    """Testes de integração da API completa"""
    
    def test_criar_e_consultar_livro(self, client, cleanup_db, livro_exemplo):
        """Teste: criar livro e recuperar"""
        response_create = client.post('/livros',
                                     data=json.dumps(livro_exemplo),
                                     content_type='application/json')
        assert response_create.status_code == 201
        
        response_get = client.get('/livros/1')
        assert response_get.status_code == 200
        
        data = json.loads(response_get.data)
        assert data['titulo'] == livro_exemplo['titulo']
    
    def test_fluxo_completo_crud(self, client, cleanup_db, livro_exemplo):
        """Teste: fluxo completo de CRUD"""
        response_create = client.post('/livros',
                                     data=json.dumps(livro_exemplo),
                                     content_type='application/json')
        assert response_create.status_code == 201
        
        response_read = client.get('/livros/1')
        assert response_read.status_code == 200
        
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
        
        response_delete = client.delete('/livros/1')
        assert response_delete.status_code == 200
        
        response_verify = client.get('/livros/1')
        assert response_verify.status_code == 404
    
    def test_listar_multiplos_livros(self, client, cleanup_db, livros_multiplos):
        """Teste: listar múltiplos livros"""
        # Criar múltiplos
        for livro in livros_multiplos:
            client.post('/livros',
                       data=json.dumps(livro),
                       content_type='application/json')
        
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