import cv2


class VideoDrone(object):
	def __init__(self, drone):
		self.cap = drone

	def __del__(self):
		self.cap.release()

	def get_frame(self):
		frame = self.cap.read()

		if frame is None or frame.size == 0:
			return ''
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		print(frame.shape)
		(flag, encodedImage) = cv2.imencode(".jpg", frame)
		return encodedImage.tobytes()
