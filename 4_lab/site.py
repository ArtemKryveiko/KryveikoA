from flask import Flask, render_template
from your_previous_module import MyClass  # Підставте реальну назву вашого модуля

app = Flask(__name__)

@app.route('/')
def home():
    obj = MyClass()
    obj.say_hello()  # Викликайте метод із попереднього завдання
    return render_template('index.html', greeting=f"Hello from Flask: {obj.this_is_lambda('Flask', 'User')}")

if __name__ == '__main__':
    app.run(debug=True)
