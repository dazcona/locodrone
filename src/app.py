from flask import Flask
from flask import render_template
import tello
import time
from PIL import Image

app = Flask(__name__)

class Fly:
    def __init__(self):
        self.drone = None

    @property
    def empty(self):
        return self.drone == None

fly = Fly()


@app.route('/')
def index():
    if fly.empty:
        print("Initializing drone...")
        fly.drone = tello.Tello('', 8889)
    # vplayer = TelloUI(drone, '/code')
    # time.sleep(3)
    # vplayer.onClose()
    return render_template('index.html')

@app.route('/action/<action>')
def action(action):
    print(action)
    if action == 'land':
        result = fly.drone.land()
    elif action == 'takeoff':
        result = fly.drone.takeoff()
    else:
        result = fly.drone.move(action, 3)
    print("Action result: ", result)
    return "200"




if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
