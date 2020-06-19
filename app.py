from chatbot import chatbot
from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/chat")
def chat():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("main.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))



if __name__ == "__main__":
    app.run()  