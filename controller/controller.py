from flask import Blueprint, jsonify, request

user_bp = Blueprint('user_bp', __name__, url_prefix='/')

books = [
    {
        'id' : 1,
        'title' : 'Código Limpo',
        'author' : 'Robert Cecil Martin'
    },
    {
        'id' : 2,
        'title' : 'Pense em Python',
        'author' : 'Allen B. Downey'
    }
]

@user_bp.route('/', methods=['GET'])
def index():
    return '<h1>Books API</h1><br><h1>TESTE API</h1>' 

@user_bp.route('/book', methods=['GET'])
def show_books():
    return jsonify(books)

@user_bp.route('/book', methods=['POST'])
def store_book():
    books.append(request.get_json())
    return jsonify(books[-1])

@user_bp.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    update = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(update)
            return jsonify(books[index])
    
    return jsonify({})
    
    

@user_bp.route('/book/<int:id>', methods=['GET'])
def find_book(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)
        
@user_bp.route('/book/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    
    return jsonify(books)
