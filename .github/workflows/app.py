from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "https://devopsaws-gitactions.s3.us-east-1.amazonaws.com/index.html"

@app.route("/about")
def about():
    return "https://devopsaws-gitactions.s3.us-east-1.amazonaws.com/netflixstyles.css"

@app.route("/service")
def service():
    return "<h1>Welcome to  our Service page.....</h1>"

if __name__ =='__main__':
    app.run(host="0.0.0.0",port=5000)