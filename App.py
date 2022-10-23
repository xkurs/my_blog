from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html')


@app.route("/secret/<name>/")
def secret(name):
    my_dict = {"alex": "Hi, Alex!", "ivan": "Hello, Ivan!"}
    result = my_dict.get(name, "Привет, незнакомец!")
    return f'<h1>{result}</h1> <p>Тебе сюда: </p> <a href="../index">Главная</a>'


@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/blog/")
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run(debug=True)
