from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():

    # query parameters (?name=niklas) can be accessed by the requests module
    # then rendered on the website
    name = request.args.get("name", "world")

    return render_template('index.html', NAME=name)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 