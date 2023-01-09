from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ContactUs')
def ContactUs():
    return render_template('Contactus.html')

@app.route('/Login')
def Login():
    return render_template('login.html')

@app.route('/Register')
def Register():
    return render_template('Register.html')
if __name__=='__main__':
    app.run(host='0.0.0.0', deabug=True)
