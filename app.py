from flask import Flask, render_template
from random_choice import choose_a_word

app = Flask(__name__)

@app.route('/')
def new_page():
	return render_template("index.html")#choose_a_word()


if __name__ == '__main__':
   app.run(debug = True)
    