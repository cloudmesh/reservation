from flask import Flask, request
from flask import render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__,
            static_folder='static',
            static_url_path='')
Bootstrap(app)
app.debug = True

def main():
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    main()




