# Web Scraper CSV 🕸️📄  
A beginner-friendly Python script that scrapes quotes and authors from any site structured like [quotes.toscrape.com](http://quotes.toscrape.com), and exports the results into a clean CSV file.

---

## 🔧 Features
- Scrapes quotes and authors from multiple pages  
- Automatically formats and saves to a `.csv` file  
- User selects the number of pages to scrape  
- Menu interface for repeat use without restarting the program  

---

## 📦 Requirements
- Python 3.7+  
- `requests`  
- `beautifulsoup4`  

### Install dependencies:
```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Run

1. **Clone the repo:**
```bash
git clone https://github.com/gandalf-ddj/web_scraper_csv.git
cd web_scraper_csv
```

2. **Run the script:**
```bash
python main.py
```

3. **Follow the prompts:**
- Enter the base URL  
- Choose how many pages to scrape  
- Name your CSV file  

---

## 💡 Example Output
Sample CSV output format:
```
Quote,Author
"The world as we have created it is a process of our thinking...",Albert Einstein
"It is our choices, Harry, that show what we truly are...",J.K. Rowling
```

---

## 🔍 Notes
- The program appends `/page/X` to paginate automatically.  
- Meant for educational purposes — always respect `robots.txt` and site terms when scraping.

---

## 🧠 Made With Learning In Mind
This project is part of a growing Python portfolio, built with a focus on:
- Real-world use cases  
- User interaction  
- Dynamic content parsing
