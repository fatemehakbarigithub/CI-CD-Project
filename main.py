from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World From Fatemeh and Marziyeh"

if __name__ == "__main__":
    app.run(debug = True, port = 80, host = "0.0.0.0")
