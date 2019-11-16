from flask import Flask
from flask import render_template
import tello
import time
from PIL import Image

app = Flask(__name__)

class Fly:
    def __init__(self):
        self.drone = None


fly = Fly()

@app.route('/')
def index():
    fly.drone = tello.Tello('', 8989)
    # vplayer = TelloUI(drone, '/code')
    # time.sleep(3)
    # vplayer.onClose()
    return render_template('index.html')

@app.route('/action/<action>')
def action(action):
    print(action)
    if action == 'land':
        fly.drone.land()
    elif action == 'takeoff':
        fly.drone.takeoff()
    else:
        fly.drone.move(action, .02)
    return "200"


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5001)
