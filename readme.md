# Flask Web Scraper

## Overview
This is a simple **Flask-based web scraping application** that allows users to enter a URL and an HTML tag to extract and display content from that webpage.

## Features
✅ **User-friendly Web Interface:** Enter URL and tag to scrape data.
✅ **Web Scraping with BeautifulSoup:** Extracts text from specified HTML tags.
✅ **Error Handling:** Displays an error if URL or tag is missing.
✅ **Minimal and Lightweight:** Uses Flask for the backend.

## Requirements
Ensure you have the following installed before running the project:

- 🐍 Python
- 🌐 Flask
- 🔗 Requests
- 🏗️ BeautifulSoup4 (bs4)

You can install dependencies using:
```sh
pip install flask requests beautifulsoup4
```

## Project Structure
📂 **Project Directory:**
```
/your_project_directory
│── app.py               # 🏗️ Main Flask application
│── templates/
│   │── index.html       # 📄 Home page with form
│   │── result.html      # 📄 Page to display scraped data
│── static/              # 🎨 (Optional) CSS/JS files
│── README.md            # 📖 Project Documentation
```

## Usage
🚀 **Run the Flask Application:**

Create start.sh file and write:

```sh
python app.py
```

🌍 **Access the Web App:**
Open your browser and visit:
```
http://yourprojectname.glitch.me/
```

📝 **Enter URL and Tag:**
1. Provide a valid URL.
2. Specify an HTML tag (e.g., `p`, `h1`, `div`).
3. Click submit to fetch and display the data.

## Code
```python
from flask import Flask, render_template, request  # Flask ka use web app banane ke liye ho raha hai
import requests  # HTTP requests bhejne ke liye
from bs4 import BeautifulSoup  # Web scraping ke liye BeautifulSoup library

app = Flask(__name__)  # Flask ka object bana rahe hain

# Home route - Form dikhane ke liye
@app.route("/")
def index():
    return render_template("index.html")  # index.html template render kar raha hai

# Scraping route - User ke input ke basis pe scraping karega
@app.route("/scrape", methods=["POST"])
def scrape():
    url, tag = request.form.get("url"), request.form.get("tag")  # Form se URL aur tag le rahe hain
    if not url or not tag:  # Agar koi value missing hai toh error return karenge
        return render_template("result.html", error="Both URL and Tag are required.")

    # HTTP request bhej rahe hain webpage ke content ko fetch karne ke liye
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()  # Agar request fail hoti hai toh error raise hoga

    # Page ka HTML content parse kar rahe hain
    soup = BeautifulSoup(response.text, "html.parser")

    # Diye gaye tag ke andar jo bhi text milega, use extract kar rahe hain
    elements = [e.get_text() for e in soup.find_all(tag)]

    # Result page ko render kar rahe hain extracted data ke saath
    return render_template("result.html", tag=tag, url=url, title=soup.title.string or "No Title", elements=elements)

# Flask server ko run karne ke liye
if __name__ == "__main__":
    app.run(debug=True)  # Debug mode enable hai, taaki errors console me show ho sakein
```

## Notes
⚠️ **Important Considerations:**
- Works only with publicly accessible websites.
- Some websites may block requests (**Use user-agent headers to avoid 403 errors**).
- Handles missing input errors but does not handle all exceptions.

## Future Improvements
✨ **Potential Enhancements:**
- 🔄 Add support for multiple tags.
- 📜 Implement pagination for large data sets.
- 💾 Store scraped data in a database.

---
🎉 **Happy Coding! 🚀**