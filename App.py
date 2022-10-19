from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html')


@app.route("/secret/")
def secret():
    my_dict = {"alex": "Hi!", "ivan": "Hello!"}
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/blog/")
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run(debug=True)
