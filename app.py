
from flask import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'shajal'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/hello/',methods=['GET'])
@app.route('/hello/<name>',methods=['GET'])
def hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)