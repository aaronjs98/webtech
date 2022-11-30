from flask import Flask, render_template
import os

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
@app.route('/')
def index():
    IMG_LIST = os.listdir('static/images')
    IMG_LIST = ['images/'+ i for i in IMG_LIST]
    return render_template('index.html', imagelist=IMG_LIST)
if __name__=='__main__':
    app.run(host='0.0.0.0', deabug=True)
