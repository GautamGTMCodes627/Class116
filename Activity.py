from flask import Flask, render_template
app = Flask(__name__)
@app.route("/index")
def first_flask():
    name = "Gautam"
    return render_template('index.html', s_name=name)
app.run(debug=True)