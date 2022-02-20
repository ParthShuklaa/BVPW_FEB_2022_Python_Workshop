from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def main():
    return  render_template('query.html')

@app.route('/process',methods=['GET'])
def process():
    _username = request.form.get('username')
    if _username:
        return  render_template('response.html',username= _username)
    else:
        return '<h1> PLease go back and enter Your Name .....400</h1>'

if __name__ == '__main__':
    app.run(debug=True)