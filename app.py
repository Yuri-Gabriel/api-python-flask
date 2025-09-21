from flask import Flask
from controller.controller import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(port=8000, host="localhost", debug=True)
