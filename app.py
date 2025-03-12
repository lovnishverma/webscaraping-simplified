from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Home Route - Display the Form
@app.route("/")
def index():
    return render_template("index.html")

  
# Scraping Route - Process URL and Display Results Based on User Input
@app.route("/scrape", methods=["POST"])
def scrape():
    if request.method == "POST":
        # Safely get URL and tag from the Form using .get()
        url = request.form.get("url")
        tag = request.form.get("tag")

        # Check if both URL and tag are provided
        if not url or not tag:
            error_message = "Both URL and Tag are required fields."
            return render_template("result.html", error=error_message)

        try:
            # Custom headers to mimic a real browser request to bypass 403 Client Error: Forbidden for url: such errors
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            # Fetch page content with custom headers
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise exception for invalid responses
            
            # Parse content with BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract content based on user-defined tag
            elements = [element.get_text() for element in soup.find_all(tag)]
            title = soup.title.string if soup.title else "No Title Found"
            
            return render_template("result.html", title=title, elements=elements, tag=tag, url=url)
        
        except Exception as e:
            error_message = "An error occurred: {}".format(str(e))  # Using str.format()
            return render_template("result.html", error=error_message)


if __name__ == "__main__":
    app.run(debug=True)