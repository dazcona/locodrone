from flask import Flask
from flask import render_template
import tello
import time
from PIL import Image


app = Flask(__name__) 
  
@app.route('/') 
def index(): 
    return render_template('index.html')


@app.route('/video') 
def video():

    drone = tello.Tello('', 8889) 

    drone.takeoff()

    time.sleep(5)

    while True:

        print('Reading drone!')
        frame = drone.read()

        if frame is None or frame.size == 0:
            print('Nothing!')
            continue

        print('Get Image!')
        image = Image.fromarray(frame)

        print('Save Image!')
        image.save("drone.jpg")

        time.sleep(3)


    return render_template('video.html')

  
if __name__ == '__main__': 
  
    app.run(debug=True, host='0.0.0.0') 