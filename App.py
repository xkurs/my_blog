from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/secret/<name>/")
def secret(name):
    my_dict = {"alex": "Hi, Alex!", "ivan": "Hello, Ivan!"}
    return f'<h1>{my_dict.get(name, "Привет, незнакомец!")}</h1> <p>Тебе сюда:</p> <a href={url_for("index")}>Главная</a>'


@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/blog/")
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run(debug=True)
