import flask
from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/plusOptions')
def plus_options():  # put application's code here
    return render_template('plusOptions.html')

@app.route('/plus0-10')
def plus0to10():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    return render_template('plus0-10.html', num_a=a, num_b=b)

@app.route('/plus0-20')
def plus0to20():  # put application's code here
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    return render_template('plus0-20.html', num_a=a, num_b=b)

@app.route('/plus0-30')
def plus0to30():  # put application's code here
    a = random.randint(0, 30)
    b = random.randint(0, 30)
    return render_template('plus0-30.html', num_a=a, num_b=b)

@app.route('/plus0-40')
def plus0to40():  # put application's code here
    a = random.randint(0, 40)
    b = random.randint(0, 40)
    return render_template('plus0-40.html', num_a=a, num_b=b)

@app.route('/plus0-50')
def plus0to50():  # put application's code here
    a = random.randint(0, 50)
    b = random.randint(0, 50)
    return render_template('plus0-50.html', num_a=a, num_b=b)

@app.route('/plus0-60')
def plus0to60():  # put application's code here
    a = random.randint(0, 60)
    b = random.randint(0, 60)
    return render_template('plus0-60.html', num_a=a, num_b=b)

@app.route('/plus0-70')
def plus0to70():  # put application's code here
    a = random.randint(0, 70)
    b = random.randint(0, 70)
    return render_template('plus0-70.html', num_a=a, num_b=b)

@app.route('/plus0-80')
def plus0to80():  # put application's code here
    a = random.randint(0, 80)
    b = random.randint(0, 80)
    return render_template('plus0-80.html', num_a=a, num_b=b)

@app.route('/plus0-90')
def plus0to90():  # put application's code here
    a = random.randint(0, 90)
    b = random.randint(0, 90)
    return render_template('plus0-90.html', num_a=a, num_b=b)

@app.route('/plus')
def plus():  # put application's code here
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    return render_template('plus.html', num_a=a, num_b=b)

@app.route('/minOptions')
def minOptions():  # put application's code here
    return render_template('minOptions.html')

@app.route('/min0-10')
def min0to10():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    return render_template('min0-10.html', num_a=a, num_b=b)

@app.route('/min0-20')
def min0to20():  # put application's code here
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    return render_template('min0-20.html', num_a=a, num_b=b)

@app.route('/min0-30')
def min0to30():  # put application's code here
    a = random.randint(0, 30)
    b = random.randint(0, 30)
    return render_template('min0-30.html', num_a=a, num_b=b)

@app.route('/min0-40')
def min0to40():  # put application's code here
    a = random.randint(0, 40)
    b = random.randint(0, 40)
    return render_template('min0-40.html', num_a=a, num_b=b)

@app.route('/min0-50')
def min0to50():  # put application's code here
    a = random.randint(0, 50)
    b = random.randint(0, 50)
    return render_template('min0-50.html', num_a=a, num_b=b)

@app.route('/min0-60')
def min0to60():  # put application's code here
    a = random.randint(0, 60)
    b = random.randint(0, 60)
    return render_template('min0-60.html', num_a=a, num_b=b)

@app.route('/min0-70')
def min0to70():  # put application's code here
    a = random.randint(0, 70)
    b = random.randint(0, 70)
    return render_template('min0-70.html', num_a=a, num_b=b)

@app.route('/min0-80')
def min0to80():  # put application's code here
    a = random.randint(0, 80)
    b = random.randint(0, 80)
    return render_template('min0-80.html', num_a=a, num_b=b)

@app.route('/min0-90')
def min0to90():  # put application's code here
    a = random.randint(0, 90)
    b = random.randint(0, 90)
    return render_template('min0-90.html', num_a=a, num_b=b)

@app.route('/minus')
def minus():  # put application's code here
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    return render_template('minus.html', num_a=a, num_b=b)

@app.route('/multiplyOptions')
def multiplyOptions():  # put application's code here
    return render_template('multiplyOptions.html')

@app.route('/multiply-1')
def multiply1():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(1, 1)
    return render_template('multiply1.html', num_a=a, num_b=b)

@app.route('/multiply-2')
def multiply2():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(2, 2)
    return render_template('multiply2.html', num_a=a, num_b=b)

@app.route('/multiply-3')
def multiply3():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(3, 3)
    return render_template('multiply3.html', num_a=a, num_b=b)

@app.route('/multiply-4')
def multiply4():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(4, 4)
    return render_template('multiply4.html', num_a=a, num_b=b)

@app.route('/multiply-5')
def multiply5():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(5, 5)
    return render_template('multiply5.html', num_a=a, num_b=b)

@app.route('/multiply-6')
def multiply6():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(6, 6)
    return render_template('multiply6.html', num_a=a, num_b=b)

@app.route('/multiply-7')
def multiply7():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(7, 7)
    return render_template('multiply7.html', num_a=a, num_b=b)

@app.route('/multiply-8')
def multiply8():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(8, 8)
    return render_template('multiply8.html', num_a=a, num_b=b)

@app.route('/multiply-9')
def multiply9():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(9, 9)
    return render_template('multiply9.html', num_a=a, num_b=b)

@app.route('/multiply-10')
def multiply10():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(10, 10)
    return render_template('multiply10.html', num_a=a, num_b=b)

@app.route('/multiply')
def multiply():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    return render_template('multiply.html', num_a=a, num_b=b)

@app.route('/divide1')
def divide1():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(1, 1)

    c = a * b
    d = round(c / b)
    return render_template('divide1.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide2')
def divide2():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(2, 2)

    c = a * b
    d = round(c / b)
    return render_template('divide2.html', num_a=c, num_b=b, answer=d, total=c)


@app.route('/divide3')
def divide3():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(3, 3)

    c = a * b
    d = round(c / b)
    return render_template('divide3.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide4')
def divide4():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(4, 4)

    c = a * b
    d = round(c / b)
    return render_template('divide4.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide5')
def divide5():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(5, 5)

    c = a * b
    d = round(c / b)
    return render_template('divide5.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide6')
def divide6():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(6, 6)

    c = a * b
    d = round(c / b)
    return render_template('divide6.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide7')
def divide7():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(7, 7)

    c = a * b
    d = round(c / b)
    return render_template('divide7.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide8')
def divide8():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(8, 8)

    c = a * b
    d = round(c / b)
    return render_template('divide8.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide9')
def divide9():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(9, 9)

    c = a * b
    d = round(c / b)
    return render_template('divide9.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divide10')
def divide10():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(10, 10)

    c = a * b
    d = round(c / b)
    return render_template('divide10.html', num_a=c, num_b=b, answer=d, total=c)


@app.route('/divide')
def divide():  # put application's code here
    a = random.randint(0, 10)
    b = random.randint(1, 10)

    c = a * b
    d = round(c / b)
    return render_template('divide.html', num_a=c, num_b=b, answer=d, total=c)

@app.route('/divideOptions')
def divideOptions():  # put application's code here
    return render_template('divideOptions.html')


if __name__ == '__main__':
    app.run()
