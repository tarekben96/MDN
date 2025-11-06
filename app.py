from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "نقص وزن"
    elif bmi < 25:
        return "وزن مثالي"
    elif bmi < 30:
        return "زيادة وزن"
    else:
        return "سمنة"

def classify_endurance(distance):
    if distance < 1800:
        return "ضعيف"
    elif distance <= 2200:
        return "متوسط"
    elif distance <= 2500:
        return "جيد"
    else:
        return "جيد جدًا"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    rank = request.form['rank']
    gender = request.form['gender']
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    distance = float(request.form['distance'])

    bmi = calculate_bmi(weight, height)
    bmi_eval = classify_bmi(bmi)
    endurance = classify_endurance(distance)

    return render_template('results.html', name=name, rank=rank, gender=gender,
                           age=age, height=height, weight=weight, distance=distance,
                           bmi=bmi, bmi_eval=bmi_eval, endurance=endurance)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)
