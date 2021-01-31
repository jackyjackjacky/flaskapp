from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html', hostname= request.headers.get('Host'), user_IP= request.remote_addr)

if __name__ == "__main__":
    app.run()
