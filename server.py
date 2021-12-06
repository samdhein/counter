from typing import Counter
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "lmao"

@app.route('/')
def count():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1 
    return render_template("index.html", count = session['count'])

@app.route('/clear_count', methods=['POST'])
def clear_count():
    session.pop('count')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

