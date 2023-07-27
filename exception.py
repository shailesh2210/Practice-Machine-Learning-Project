from flask import Flask
import sys
sys.path.append(r"D:\Practice-Machine-Learning-Project")

from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)

@app.route("/")
def home():
    try:
        raise Exception("we are testing Exxception Handling")
    except Exception as e:
        ML = CustomException(e,sys)
        logging.info(ML.error_message)
    logging.info("Logging as started!")

    return "Hello Shailesh Gaddam"

if __name__ == "__main__":
    app.run(debug =True)