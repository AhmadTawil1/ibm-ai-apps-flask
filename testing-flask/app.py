from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', name="Ahmad")  

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user = request.form['username']
        return f"Submitted by {user}"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
