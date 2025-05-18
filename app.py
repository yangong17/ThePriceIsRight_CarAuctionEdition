from flask import Flask, render_template, request, session, redirect
from car_data import scrape_expensive_cars_with_images
import random

app = Flask(__name__)
app.secret_key = "secret-key"

@app.route("/")
def loading():
    session["cars"] = scrape_expensive_cars_with_images(limit=5)
    session["round"] = 0
    session["answers"] = []
    return render_template("start.html")


@app.route("/game", methods=["GET", "POST"])
def game():
    if "round" not in session or "cars" not in session:
        return redirect("/")

    index = session["round"]

    if request.method == "POST":
        # Stay on current index to show feedback before advancing
        car_data = session["cars"][index]
        correct_price = car_data["price"]
        guess = int(request.form["guess"])
        is_correct = guess == correct_price

        options = [int(val) for val in request.form.getlist("options")]

        session["answers"].append({
            "car": car_data["car"],
            "date": car_data["date"],
            "model_year": car_data["model_year"],
            "guess": guess,
            "correct": correct_price,
            "image_url": car_data["image_url"],
            "correct_answered": is_correct
        })

        # Advance round AFTER feedback
        session["round"] += 1

        return render_template("game.html", reveal=True, guess=guess,
            correct_price=correct_price,
            options=options,
            round=index + 1,
            total=len(session["cars"]),
            **car_data
        )

    # If game is finished
    if index >= len(session["cars"]):
        return redirect("/result")

    car_data = session["cars"][index]
    correct_price = car_data["price"]

    # Create price options
    distractors = set()
    while len(distractors) < 4:
        offset = int(correct_price * random.uniform(0.1, 0.25))
        fake = random.choice([correct_price + offset, correct_price - offset])
        if fake != correct_price and fake > 0:
            distractors.add(fake)

    options = list(distractors) + [correct_price]
    random.shuffle(options)

    return render_template("game.html",
        reveal=False,
        options=options,
        correct_price=correct_price,
        round=index + 1,
        total=len(session["cars"]),
        **car_data
    )

@app.route("/result")
def result():
    return render_template("result.html", answers=session.get("answers", []))

if __name__ == "__main__":
    app.run(debug=True)

#

