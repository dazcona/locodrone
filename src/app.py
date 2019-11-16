from flask import Flask
from flask import render_template
  
app = Flask(__name__) 
  
@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/forward') 
def forward(): 
    print('forward!!')
    return "200"

@app.route('/right') 
def right(): 
    print('right!!')
    return "200"

@app.route('/back') 
def back(): 
    print('back!!')
    return "200"

@app.route('/left') 
def left(): 
    print('left!!')
    return "200"

if __name__ == '__main__': 
  
    app.run(debug=True, host='0.0.0.0') 