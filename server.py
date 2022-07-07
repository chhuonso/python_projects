from flask import Flask
app=Flask(__name__)


@app.route("/")
def index():
    return "Hello World!!"

@app.route('/dojo')
def hello_dojo():
    return 'Dojo'

@app.route('/say/<phrase>')
def say_phrase(phrase):
    return f'have it say: Hi {phrase}!'

@app.route('/repeat/<int:times>/<phrase>')
def repeat_times(times, phrase):
    return (phrase + " ") * times

if __name__=="__main__":
    app.run(debug=True)