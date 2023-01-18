from flask import Flask, render_template, request


app=Flask("copy")
@app.route("/")
def home():
    return render_template('pl_home.html')

@app.route("/pl_search")
def search():
    keyword = request.args.get('keyword')

app.run('127.0.0.1')