from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/eksempler')
def memes():
    memes_dir = os.path.join(app.static_folder, 'images', 'memes')
    if not os.path.exists(memes_dir):
        os.makedirs(memes_dir)
    memes = [f for f in os.listdir(memes_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('memes.html', memes=memes)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="1331") 
