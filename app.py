from flask import Flask, render_template
from ipo_scraper import get_ipos
from excel_export import save_excel

app = Flask(__name__)

@app.route("/")
def home():

    ipo_data = get_ipos()

    save_excel(ipo_data)

    return render_template("index.html", ipos=ipo_data)

if __name__ == "__main__":
    app.run(debug=True)