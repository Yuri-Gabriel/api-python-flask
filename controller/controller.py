from flask import Blueprint, jsonify, request

user_bp = Blueprint('user_bp', __name__, url_prefix='/')

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

@user_bp.route('/livros', methods=['GET'])
def consultar_livros():
    """Retorna todos os livros"""
    return jsonify([livro.to_dict() for livro in livros_db]), 200

@user_bp.route('/livros/<int:livro_id>', methods=['GET'])
def consultar_livro_por_id(livro_id):
    """Retorna um livro específico"""
    for livro in livros_db:
        if livro.id == livro_id:
            return jsonify(livro.to_dict()), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

@user_bp.route('/livros', methods=['POST'])
def cadastrar_livro():
    """Cadastra um novo livro"""
    data = request.get_json()
    
    if not data or not all(k in data for k in ['titulo', 'autor', 'ano', 'isbn']):
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400
    
    if not isinstance(data['ano'], int) or data['ano'] < 1000:
        return jsonify({"erro": "Ano inválido"}), 400
    
    novo_id = len(livros_db) + 1
    livro = Livro(novo_id, data['titulo'], data['autor'], data['ano'], data['isbn'])
    livros_db.append(livro)
    
    return jsonify(livro.to_dict()), 201

@user_bp.route('/livros/<int:livro_id>', methods=['PUT'])
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

@user_bp.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    """Deleta um livro"""
    global livros_db
    for i, livro in enumerate(livros_db):
        if livro.id == livro_id:
            livros_db.pop(i)
            return jsonify({"mensagem": "Livro deletado"}), 200
    
    return jsonify({"erro": "Livro não encontrado"}), 404
