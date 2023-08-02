from flask import Flask, render_template, request

app = Flask(__name__)

def process_value(value):
    # Your processing logic here
    # For example, let's just return the square of the value
    result = value ** 2
    return result

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        value = int(request.form['value'])
        result = process_value(value)
        return render_template('result.html', value=value, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
