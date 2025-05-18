# 🚗 The Price Is Right: Car Auction Edition

This project is a Flask-based web game developed as a homework assignment for **STATS404 – Statistical Computing** at UCLA.

---

## 🎯 Assignment Objective

The objective of this assignment was to demonstrate the ability to:
- **Scrape real-world data from Wikipedia**
- **Clean and structure it programmatically**
- **Incorporate the data into an interactive Flask application**

---

## 🕹️ About the Game

Players are presented with 5 rare and expensive cars sold at public auction. For each car, players see:
- The **model year**
- The **car name**
- The **date it was sold**
- A **live image** scraped from Wikipedia

Players must guess the car’s **original auction price** from 5 options. Immediate feedback is provided, and a final summary is displayed at the end.

---

## ✅ Features

- 🔁 5 randomly selected, non-duplicate cars each game
- ⚡ Multithreaded scraping for faster image loading
- 🟢 Highlights correct/incorrect answers after each guess
- 📊 Final summary showing all responses and results
- 🧠 Clean UI using Flask and Jinja2 templates

---

## 📁 Folder Structure


```
ThePriceIsRight_CarAuctionEdition/
├── app.py # Flask app logic and game flow
├── car_data.py # Web scraping with image fetching
└── templates/
├── start.html # Game instructions + start button
├── game.html # Gameplay interface
└── result.html # Final score summary
```


---

## 🚀 How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ThePriceIsRight_CarAuctionEdition.git
    cd ThePriceIsRight_CarAuctionEdition
    ```

2. Install dependencies:
    ```bash
    pip install flask requests beautifulsoup4
    ```

3. Run the app:
    ```bash
    python app.py
    ```

4. Open your browser and go to:
    ```
    http://localhost:5000
    ```

---

## 📚 Data Source

All data is scraped live from:
[Wikipedia – List of most expensive cars sold at auction](https://en.wikipedia.org/wiki/List_of_most_expensive_cars_sold_at_auction)

---

## 📘 Academic Context

- **Course:** STATS404 – Statistical Computing  
- **Instructor:** [Insert instructor name if needed]  
- **Objective:** Practice Python web development, real-time data integration, and interactive interfaces using Flask

---

## 💡 Potential Extensions

- Add a countdown timer or scoring system
- Deploy the game online (e.g., with PythonAnywhere, Render, or Heroku)
- Track high scores in a leaderboard
- Export results to CSV for analysis

---

## 📄 License

This project is for educational use only.
