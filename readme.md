# Flask Web Scraper

Live Demo: https://webscaraping-simplified.glitch.me/

## Overview
This is a simple **Flask-based web scraping application** that allows users to enter a URL and an HTML tag to extract and display content from that webpage.

![image](https://github.com/user-attachments/assets/13838a50-71e5-411d-ac7c-034e5caac405)


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
from flask import Flask, render_template, request  # Flask is used to create a web app
import requests  # To send HTTP requests
from bs4 import BeautifulSoup  # BeautifulSoup is used for web scraping

app = Flask(__name__)  # Creating a Flask app instance

# Home route - Displays the form
@app.route("/")
def index():
    return render_template("index.html")  # Renders the index.html template

# Scraping route - Scrapes data based on user input
@app.route("/scrape", methods=["POST"])
def scrape():
    url, tag = request.form.get("url"), request.form.get("tag")  # Get URL and tag from the form
    if not url or not tag:  # If any value is missing, return an error
        return render_template("result.html", error="Both URL and Tag are required.")

    # Send an HTTP request to fetch the webpage content
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()  # Raise an error if the request fails

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract text from all occurrences of the given tag
    elements = [e.get_text() for e in soup.find_all(tag)]

    # Render the result page with extracted data
    return render_template("result.html", tag=tag, url=url, title=soup.title.string or "No Title", elements=elements)

# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)  # Debug mode is enabled to show errors in the console

```

![image](https://github.com/user-attachments/assets/1a81b045-6962-4d62-92b9-ea3260705df2)


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
