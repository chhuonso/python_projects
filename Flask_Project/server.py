from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play")
def play_level_one():
    return render_template("index.html", repeat=3, color="skyblue")

@app.route("/play/<int:repeat>")
def play_level_two(repeat):
    return render_template("index.html", repeat=repeat, color="skyblue")

@app.route("/play/<int:repeat>/<color>")
def play_level_three(repeat, color):
    return render_template("index.html", repeat=repeat, color=color)


if __name__=="__main__":
    app.run(debug=True)