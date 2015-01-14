import sys
if 'lib/' not in sys.path:
    sys.path.insert(0, 'lib/')

from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
