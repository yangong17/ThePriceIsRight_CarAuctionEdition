# 🚗 The Price Is Right: Car Auction Edition

This project is a Flask-based web game developed as a homework assignment for **STATS404 – Statistical Computing** at UCLA.

Players are presented with 5 rare and expensive cars sold at auction. For each car, players are shown:
- The **model year**
- The **car name**
- The **date it was sold**
- A **photo** scraped live from Wikipedia

The objective is to guess the car's **original auction price** from 5 options. After each round, players receive immediate feedback, and a detailed summary is shown at the end of the game.

---

## 🔧 Features

- ✅ 5 randomly selected cars per game (no duplicate titles)
- 🚀 Multithreaded image scraping for faster load time
- 🟢 Highlights correct/incorrect answers after each guess
- 📊 End-of-game summary of guesses and results
- 🖼️ Real car photos pulled directly from Wikipedia
- 🧠 Clean and interactive design using Flask + Jinja

---

## 🗂️ Folder Structure
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
