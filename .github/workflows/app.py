from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # Redirect to the 'about' route instead of returning text
    return redirect(url_for("https://devopsaws-gitactions.s3.us-east-1.amazonaws.com/netflixstyles.css"))

@app.route("/netflixstyles")
def netflixstyles():
    return "<h2>Welcome to our About Page....</h2>"

@app.route("/service")
def service():
    # Redirect to an external URL or another internal route if needed
    return redirect("https://devopsaws-gitactions.s3.us-east-1.amazonaws.com/netflixstyles.css")  # For an external site

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
