from flask import Flask
from random_choice import choose_a_word

app = Flask(__name__)

@app.route('/')
def new_page():
	return choose_a_word()
    