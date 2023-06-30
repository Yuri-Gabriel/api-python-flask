from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def index():
    return 'Books API' 

@app.route('/book', methods=['GET'])
def show_books():
    return jsonify(books)

@app.route('/book', methods=['POST'])
def store_book():
    books.append(request.get_json())
    return jsonify(books[-1])

@app.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    update = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(update)
    
    return jsonify(books[index])

@app.route('/book/<int:id>', methods=['GET'])
def find_book(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)
        
@app.route('/book/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    
    return jsonify(books)

app.run(port=8000, host='localhost', debug=True)