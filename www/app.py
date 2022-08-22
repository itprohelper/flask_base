from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Hola!'

@app.route('/otro')
def otro_hello_world():
    return 'Otro HOla!'