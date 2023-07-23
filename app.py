from flask import Flask, render_template, request, jsonify
from chat import get_response
import subprocess

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/About')
def about():
    return render_template("about.html")

@app.route('/Features')
def features():
    return render_template("features.html")

@app.route('/Contact')
def contact():
    return render_template("contact.html")

@app.route('/Chatbot')
def home():
    return render_template("base.html")





if __name__ == "__main__":
    app.run(debug=True)