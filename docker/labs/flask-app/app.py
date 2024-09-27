from flask import Flask
import redis

app = Flask(__name__)

client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/count')
def visit_count():
    visit_count = client.incr('visit_count')
    return f'This page has been visited {visit_count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)