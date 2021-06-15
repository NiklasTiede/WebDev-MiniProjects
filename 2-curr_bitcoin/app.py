
from flask import Flask, render_template
from bitcoin import bitcoin_value


app = Flask(__name__)

BC_DOLLAR, BC_EURO = bitcoin_value()
print(BC_DOLLAR, BC_EURO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bitcoin')
def bc_value():
    return render_template('value.html', BC_dollar=BC_DOLLAR, BC_euro=BC_EURO)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 



