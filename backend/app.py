from flask import Flask

#test test

@app.route('/')
def home():
    return '<h1>Api</h1>'

if __name__ == '__main__':
    app.run(debug=true, host='localhost', port=5000)
