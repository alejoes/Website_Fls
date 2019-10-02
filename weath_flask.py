from flask import Flask, render_template, url_for
app = Flask(__name__)






@app.route("/")
@app.route("/home")
def home():
    return render_template('homeW.html')

@app.route("/maxTemp")
def maxT():
    return render_template('maxTemp.html')

@app.route("/Humidity")
def Humid():
    return render_template('humidity.html')

@app.route("/Cloudiness")
def Cloud():
    return render_template('cloudiness.html')

@app.route("/WindSpeed")
def WindSpeed():
    return render_template('windsp.html')

@app.route("/Comparison")
def Compare():
    return render_template('comparisons.html')

@app.route("/Data")
def data():
    return render_template('data.html')

if __name__=='__main__':
    app.run(debug=True)
