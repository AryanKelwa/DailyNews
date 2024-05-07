from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route('/')
def index():
    url='https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=95c19a5114864affb261c7a7dae653f6'
    res=requests.get(url).json()
    return render_template('index.htm',data=res['articles'])

if __name__ =='__main__':
    app.run(debug=True)