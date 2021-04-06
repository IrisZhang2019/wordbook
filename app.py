from flask import Flask, jsonify, render_template, request
from random_choice import choose_a_word

app = Flask(__name__)

'''
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)
'''

@app.route('/')
def new_page():
	return render_template("index.html", word=choose_a_word())


if __name__ == '__main__':
   app.run(debug = True)


