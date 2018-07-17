from flask import Flask
app = Flask(__name__)
app.debug = True
    
@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/hello')
def hello_path():
    return "HELLO FROM PATH"
    
if __name__ == '__main__':
    app.run()
