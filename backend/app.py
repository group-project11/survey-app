from flask import Flask, Blueprint

def getBluePrints():
    blue_prints = []
    for blue_print in blue_prints:
        app.register_blue_print(blue_print)
    return blue_prints

@app.route('/')
def home():
    return '<h1>Api</h1>'

if __name__ == '__main__':
    app.run(debug=true, host='localhost', port=5000)
