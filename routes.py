from flask import Flask, render_template, make_response, request, url_for, redirect
from os import environ

app = Flask(__name__, template_folder='templates')

answerKey = {'1': '2',
             '2': 'dark souls',
             '4': '11',
             '5': "ben afquack",
             '6': '1999'}


@app.route('/echo')
def echo():
	answer = request.args['answer']
	return answer


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/puzzle1')
def puzzle1():
	if "answer" in request.args:
		# check the answer
		if answerCheck('1', request.args['answer']):
			return redirect(url_for('puzzle2'))
		else:
			return render_template('puzzle1.html', returnRoute=url_for('puzzle1'))
	else:
		return render_template('puzzle1.html', returnRoute=url_for('puzzle1'))


@app.route('/4531361')
def puzzle2():
	if "answer" in request.args:
		if answerCheck('2', request.args['answer']):
			return redirect(url_for('puzzle3'))
		else:
			return render_template('puzzle2.html', returnRoute=url_for('puzzle2'))
	else:
		return render_template('puzzle2.html', returnRoute=url_for('puzzle2'))


@app.route('/4776762')
def puzzle3():
	return render_template('puzzle3.html')


@app.route('/7256119')
def puzzle4():
	# answer = "11"
	if "answer" in request.args:
		# check the answer
		if answerCheck('4', request.args['answer']):
			return redirect(url_for('puzzle5'))
		else:
			return render_template('puzzle4.html', returnRoute=url_for('puzzle4'))
	else:
		return render_template('puzzle4.html', returnRoute=url_for('puzzle4'))


@app.route('/6131894')
def puzzle5():
	# answer = "Ben Afquack"
	if "answer" in request.args:

		if answerCheck('5', request.args['answer']):
			return redirect(url_for('puzzle6'))
		else:
			return render_template('puzzle5.html', returnRoute=url_for('puzzle5'))
	else:
		return render_template('puzzle5.html', returnRoute=url_for('puzzle5'))


@app.route('/3611839')
def puzzle6():
	answer = "1999"
	if "answer" in request.args:
		if answerCheck('6', request.args['answer']):
			return redirect(url_for('goodbye'))
		else:
			return render_template('puzzle6.html', returnRoute=url_for('puzzle6'))
	else:
		return render_template('puzzle6.html', returnRoute=url_for('puzzle6'))


@app.route('/1839361')
def goodbye():
	return render_template('goodbye.html')


def answerCheck(puzzle_number, answer):
	# TODO switch answer to lower case
	if answerKey[puzzle_number] == answer.lower():
		return True
	else:
		return False


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=environ.get("PORT", 80))
