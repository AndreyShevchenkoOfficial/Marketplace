from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def search():
    search_term = request.form.get('search')
    # здесь должен быть ваш код для сравнения цен на товары на разных маркетплейсах
    return render_template('result.html')


if __name__ == '__main__':
    app.run(port=5000)
