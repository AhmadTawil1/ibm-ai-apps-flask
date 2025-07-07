from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    return f"You searched for: {query}"

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        user = request.form['username']
        return f"Welcome, {user}!"
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
