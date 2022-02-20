"""
Step1: Importing Flask
Step2: Defining Route/Function of Page
Step3: Running application

"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!!"

@app.route("/Hello")
def Hello():
    return "<h1>Hello Every One..... Hope you are learning something new in python</h1> "

if __name__ == "__main__":
    app.run(debug=True)