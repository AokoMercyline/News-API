from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 style="color:red; text-align:center; font-size:70px; background-color:grey; height:20vh;" > World News </h1>'

if __name__ == '__main__':
    app.run(debug = True)