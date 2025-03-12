from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url, tag = request.form.get("url"), request.form.get("tag")
    if not url or not tag:
        return render_template("result.html", error="Both URL and Tag are required.")

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()  # This will automatically raise an error if the request fails

    soup = BeautifulSoup(response.text, "html.parser")
    elements = [e.get_text() for e in soup.find_all(tag)]

    return render_template("result.html", tag=tag, url=url, title=soup.title.string or "No Title", elements=elements)

if __name__ == "__main__":
    app.run(debug=True)
