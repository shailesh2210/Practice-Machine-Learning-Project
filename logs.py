from flask import Flask
import sys
sys.path.append(r"D:\Practice-Machine-Learning-Project")

from src.logger import logging

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Logging as started!")

    return "Hello Shailesh Gaddam"

if __name__ == "__main__":
    app.run(debug =True)