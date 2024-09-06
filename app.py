from flask import Flask, render_template

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка меню
@app.route('/menu')
def menu():
    # Дані для таблиці
    pizzas = [
        {"name": "Маргарита", "ingredients": "Сир, томати, базилік", "price": "150 грн"},
        {"name": "Пепероні", "ingredients": "Сир, томатний соус, пепероні", "price": "180 грн"},
        {"name": "Гавайська", "ingredients": "Сир, шинка, ананаси", "price": "200 грн"},
        {"name": "4 Сезони", "ingredients": "Сир, шинка, гриби, артишоки, оливки", "price": "220 грн"}
    ]
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
