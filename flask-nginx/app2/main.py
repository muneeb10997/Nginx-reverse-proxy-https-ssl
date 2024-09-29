from flask import Flask

app2 = Flask(__name__)

@app2.route('/home')
def home():
    return 'Hello from the home page of App2!'

if __name__ == '__main__':
    app2.run(debug=True, host='0.0.0.0', port=5000)
