"""
Step1 : importing package flask
Step2 : Defining Functionality
Step3 : Calling Functionality using URL

"""
from flask import Flask, redirect
app = Flask(__name__)
@app.route('/')
def main():
    return  ' Hi there from Default function'

@app.route('/hello/<username>')#URL with a Variable
def hello_Username(username): #The Function shall take the URL variable as parameter
    return "Hello,{}".format(username)

@app.route('/hello/<int:userid>')
def Hello_UserID(userid):
    return '<h1>Hello, Your ID is : {:d}'.format(userid)


if __name__ =='__main__':# if script is executing directly
    app.run() #launching build in server