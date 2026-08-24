from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to CloudOps Chronicle</h1>
    <h2>My First Flask Docker Application</h2>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
