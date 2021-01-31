from flask import Flask, jsonify, redirect, render_template, session, url_for, Response, request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html', user_ip= flask.request.remote_addr, hostname= request.headers.get('Host'))

if __name__ == "__main__":
    app.run()
