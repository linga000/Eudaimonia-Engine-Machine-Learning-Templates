from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('happy.joblib')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    infoavail = float(request.form['infoavail'])
    housecost = float(request.form['housecost'])
    schoolquality = float(request.form['schoolquality'])
    policetrust = float(request.form['policetrust'])
    streetquality = float(request.form['streetquality'])
    events = float(request.form['events'])
    
    # Create a feature array for prediction
    features = [[infoavail, housecost, schoolquality, policetrust, streetquality, events]]
    
    # Predict happiness level
    prediction = model.predict(features)
    predict_value = prediction[0]
    
    # Convert prediction to "happy" or "unhappy"
    result = "happy" if predict_value == 1 else "unhappy"
    
    return render_template('submit.html', predict=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
