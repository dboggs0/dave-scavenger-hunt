from flask import Flask, render_template, make_response

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
	return render_template('question6.html')


@app.route('/4531361')
def puzzle2():
	return 'Hello, World!'


@app.route('/4776762')
def puzzle3():
	answer = "anything"
	return 'Hello, World!'


@app.route('/7256119')
def puzzle4():
	answer = "11"
	return 'Hello, World!'


@app.route('/6131894')
def puzzle5():
	answer = "Ben Afquack"
	return 'Hello, World!'


@app.route('/3611839')
def puzzle6():
	answer = "1999"
	return 'Hello, World!'


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=environ.get("PORT", 80))
