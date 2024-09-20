from flask import Flask

app = Flask(__name__)
def homepage():
    return "myPinterest Page"

if __name__ == "__main__":
    app.run(debug=True)
    