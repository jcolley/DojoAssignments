from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)

app.secret_key = "sadfhijfiu*&#3#79#ih#(78!"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(name) < 1:
        flash("Name cannot be blank!")
        return redirect('/')
    elif len(comment) < 1:
        flash("You must provide a comment!")
        return redirect('/')
    elif len(comment) > 120:
        flash("You talk too much!")
        return redirect('/')
    return render_template(
        'result.html',
        name=name,
        location=location,
        language=language,
        comment=comment
    )


app.run(debug=True)
