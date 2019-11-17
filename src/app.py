from flask import Flask
from flask import render_template
from flask import Response
import tello
import time
import cv2
from PIL import Image
from VideoDrone import VideoDrone

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

	return render_template('streaming.html')

@app.route('/admin')
def admin():
	# if fly.empty:
	# 	print("Initializing drone...")
	# 	fly.drone = tello.Tello('', 8889)

	return render_template('admin.html')

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

@app.route('/photo')
def photo():
	fly.player.takeSnapshot()
	return "200"

@app.route('/streaming')
def streaming():

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

	app.run(debug=True, host='0.0.0.0', port=5000)
