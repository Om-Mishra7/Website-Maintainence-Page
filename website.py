from flask import Flask,render_template,request
import uuid
import datetime
from waitress import serve
import requests

app = Flask(__name__)


@app.route('/')
def index():
    quote = requests.get('https://api.quotable.io/random').json()["content"]
    return render_template('index.html',uuid=uuid.uuid4(),user_ip=request.headers.get('X-Forwarded-For', request.remote_addr),year=datetime.datetime.today().year,quote=quote)

@app.route('/ping',methods=['GET','POST'])
def ping():
    return ('pong')

@app.route('/webhook',methods=['GET','POST'])
def ping():
    return ('okay')

if __name__ == '__main__':
    serve(app,host='0.0.0.0',port=80)
