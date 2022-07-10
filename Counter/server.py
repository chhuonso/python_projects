from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key= "secret"

@app.route("/")
def index():
    if 'count' not in session:
        session['count'] = 1
    session['count'] += 1
    print(session['count'])
    return render_template("/counter.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    if 'count' not in session:
        session['count'] = 1
    return render_template('/counter.html')

@app.route('/increment', methods=['POST'])         
def add():
    session['increment'] = 1
    session['count'] += session['increment']
    return render_template('/counter.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('count')
    session['count'] = 0
    return render_template("/counter.html")


if __name__== "__main__":
    app.run(debug=True)