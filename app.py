from flask import Flask, render_template
import pyjokes
import random

app = Flask(__name__)

@app.route('/')
def index():
	c = random.choice(['neutral','all'])
	jokes = pyjokes.get_jokes(category=c)
	jokes = random.choice(jokes)
	return render_template('index.html', jokes=jokes)

if __name__ == '__main__':
	app.run()