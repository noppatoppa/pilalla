from flask import Flask
from pilalla import pilalla
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    pilalla()
    return '''<img src="static/pil_red.png">'''

if __name__ == "__main__":
    app.run()