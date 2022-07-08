from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", row=8)

@app.route("/<int:row>")
def row_input(row):
    return render_template("index.html", row=row)

@app.route("/<int:row>/<int:col>")
def col_input(row, col):
    return render_template("index.html", row=row, col=col)



if __name__ == "__main__":
    app.run(debug=True)



