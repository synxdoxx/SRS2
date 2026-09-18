from flask import Flask, render_template, request
import random

app = Flask(__name__)

ORACLE_ANSWERS = [
    "Звёзды говорят — да.",
    "Не торопи события.",
    "Ответ скрыт в твоём сердце.",
    "Всё зависит только от тебя.",
    "Луна шепчет: будь осторожен.",
    "Да, но не так, как ты думаешь.",
    "Ты не готов к ответу.",
    "Путь будет трудным, но результат того стоит.",
    "Оракул говорит - нет.",
    "Вселенная услышала тебя.",
    "Ищи знак в ближайших трёх днях.",
    "То, что ты ищешь, уже ищет тебя.",
]

COMPATIBILITY_ANSWERS = [
    "Ваша совместимость-10%",
    "Ваша совместимость-20%",
    "Ваша совместимость-30%",
    "Ваша совместимость-40%",
    "Ваша совместимость-50%",
    "Ваша совместимость-60%",
    "Ваша совместимость-70%",
    "Ваша совместимость-80%",
    "Ваша совместимость-90%",
    "Ваша совместимость-100%. Вау! Вы созданы друг для друга!",
    "Ваша совместимость-15%",
    "Ваша совместимость-25%",
    "Ваша совместимость-35%",
    "Ваша совместимость-0%. Держитесь друг от друга подальше",
    "Ваша совместимость-45%",
    "Ваша совместимость-55%",
    "Ваша совместимость-99%",
    "Ваша совместимость-88%",
    "Ваша совместимость-67%",
    "Ваша совместимость-12%",
    "Ваша совместимость-17%",
    "Ваша совместимость-73%",
    "Ваша совместимость-48%",
    "Ваша совместимость-23%",
]
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/oracle", methods=['GET', 'POST'])
def oracle():
    if request.method == 'POST':
        question = request.form.get('question', '').strip()

        if not question:
            error = "Пожалуйста, введи свой вопрос."
            return render_template("oracle.html", error=error)

        answer = random.choice(ORACLE_ANSWERS)
        return render_template("oracle.html", question=question, answer=answer)

    return render_template("oracle.html")


@app.route("/compatibility", methods=['GET', 'POST'])
def compatibility():
    if request.method == 'POST':
        person1 = request.form.get('person1', '')
        person2 = request.form.get('person2', '')

        if not person1 or not person2:
            error = "Заполни обе даты рождения."
            return render_template("compatibility.html", error=error)

        answer = random.choice(COMPATIBILITY_ANSWERS)

        return render_template("compatibility.html",
                               person1=person1,
                               person2=person2,
                               answer=answer)

    return render_template("compatibility.html")


if __name__ == "__main__":
    app.run(debug=True)