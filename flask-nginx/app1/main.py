from flask import Flask

app1 = Flask(__name__)

@app1.route('/')
def home():
    return 'Hello from the home page of App1!'

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=5000)
