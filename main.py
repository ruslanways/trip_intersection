from flask import Flask
from flask import render_template
from flask import request
import os
import re
from count_days import countDaysTogether
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        arriveAlice = request.form['arriveAlice'][5:]
        leaveAlice = request.form['leaveAlice'][5:]
        arriveBob = request.form['arriveBob'][5:]
        leaveBob = request.form['leaveBob'][5:]
        try:
            res = countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
        except:
            return render_template('try_again.html')
        return render_template('res.html', res=res)
    return render_template('trip.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))