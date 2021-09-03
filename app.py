
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "host sever on heroku!"
    
if __name__ == "__main__":
    app.run()

