from flask import Flask, session, redirect, render_template, request
from datetime import datetime
import random
app = Flask(__name__)

app.secret_key = 'skds829298ejf9d@*(498#9821)'


@app.route('/')
def index():
    if 'curGold' not in session:
        session['curGold'] = 0

    if 'activities' not in session:
        session['activities'] = ""

    return render_template('index.html', curGold=session['curGold'], activities=session['activities'])


@app.route('/process_money', methods=['POST'])
def process_money():

    bldg = request.form['building']
    curGold = session['curGold']
    newGold = 0

    if bldg == 'farm':
        newGold = random.randint(10,20)

    elif bldg == 'cave':
        newGold = random.randint(5,10)

    elif bldg == 'house':
        newGold = random.randint(2,5)

    elif bldg == 'casino':
        newGold = random.randint(-50,50)
    else:
        session['curGold'] = 0
    
    session['curGold'] += newGold
    session['activities'] += buildActivities(bldg, curGold, newGold)
    return redirect('/')

def buildActivities(bldg,cur,new):
    msg = ""
    i = datetime.now()
    if new < 0:
        msg = '<span class="lost"> Entered a ' + bldg + ' and lost ' + str(new) + '... Ouch..' + i.strftime('%Y/%m/%d %I:%M:%S%p') + '</span><br>'
    else:
        msg = '<span class="won"> Earned ' + str(new) + ' gold from the ' + bldg + '! ' + i.strftime('%Y/%m/%d %I:%M:%S%p') + '</span><br>'
    
    return msg

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
