from flask import Flask
from flask import render_template
import tello
import time
from PIL import Image
from control

app = Flask(__name__)


@app.route('/')
def index():
    drone = tello.Tello('', 8989)
    vplayer = TelloUI(drone, '/code')
    return render_template('index.html')

@app.route('/forward')
def forward():
    drone.move('forward', .02)
    return "200"

@app.route('/right')
def right():
    drone.move('right', .02)
    return "200"

@app.route('/back')
def back():
    drone.move('back', .02)
    return "200"

@app.route('/left')
def left():
    drone.move('left', .02)
    return "200"

@app.route('/land')
def land():
    drone.land()
    return "200"

@app.route('/takeoff')
def takeoff():
    drone.takeoff()
    return "200"

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5001)
