from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now()
    return render_template('index.html', year=now.year)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
