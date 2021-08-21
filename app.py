from flask import Flask,request

app = Flask("Minerando")

@app.route("/")
def HomePage():
    return "<h1>Hello World</h1>"



if __name__ == "__main__":
    app.run(debug=True)