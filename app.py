from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/planetary/apod"

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    error = None

    if request.method == "POST":
        date_input = request.form.get("date", "").strip()
        params = {"api_key": API_KEY}
        if date_input:
            params["date"] = date_input

        response = requests.get(url, params=params)
        result = response.json()

        if response.status_code != 200:
            error = result.get("error", {}).get("message", "Unknown error")
        else:
            data = result

    return render_template("index.html", data=data, error=error)

if __name__ == "__main__":
    app.run(debug=True)