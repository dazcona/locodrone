from flask import Flask
from flask import render_template
from flask import Response
import tello
import time
import cv2
from PIL import Image
from VideoDrone import VideoDrone


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class Fly:
	def __init__(self):
		self.drone = None
	@property
	def empty(self):
		return self.drone == None

fly = Fly()


def check_drone():
	if fly.empty:
		print("Initializing drone...")
		fly.drone = tello.Tello('', 8889)


@app.route('/')
def index():
	check_drone()
	return render_template('index.html')


@app.route('/admin')
def admin():
	check_drone()
	return render_template('admin.html')


@app.route('/action/<action>')
def action(action):
	print(action)
	if action == 'land':
		result = fly.drone.land()
	elif action == 'takeoff':
		result = fly.drone.takeoff()
	else:
		result = fly.drone.move(action, 1.5)
	print("Action result: ", result)
	return "200"


@app.route('/streaming')
def streaming():
	check_drone()
	return Response(gen(VideoDrone(fly.drone)),
		mimetype = "multipart/x-mixed-replace; boundary=frame")


# CAMERA GET FRAME
def gen(camera):
	while True:
		frame = camera.get_frame()
		# print(frame)
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


if __name__ == '__main__':

	app.run(debug=True, host='0.0.0.0', port=5000, threaded=True, use_reloader=False)
