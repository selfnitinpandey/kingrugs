from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.route("/")
def home():
    return render_template("home.html", title="Home | The King Rugs")

@app.route("/products")
def products():
    return render_template("products.html", title="Products | The King Rugss")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us | The King Rugs")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us | The King Rugs")

if __name__ == "__main__":
    app.run(debug=True)
