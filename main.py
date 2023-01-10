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
        arriveAlice = request.form['arriveAlice']
        leaveAlice = request.form['leaveAlice']
        arriveBob = request.form['arriveBob']
        leaveBob = request.form['leaveBob']

        if not re.match(r'^\d\d-\d\d$', arriveAlice) \
        or not re.match(r'^\d\d-\d\d$', leaveAlice) \
        or not re.match(r'^\d\d-\d\d$', arriveBob) \
        or not re.match(r'^\d\d-\d\d$', leaveBob):
            return render_template('try_again.html')
        res = countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
        return render_template('res.html', res=res)
    return render_template('trip.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))