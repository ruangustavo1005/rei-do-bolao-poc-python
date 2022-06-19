import cv2
from cv2 import rectangle

agulha = cv2.imread('img/rue.jpeg', cv2.IMREAD_UNCHANGED)
agulha = cv2.cvtColor(agulha, cv2.COLOR_BGR2GRAY)

h, w = agulha.shape

video = cv2.VideoCapture(0)

while(True):
	imagem = video.read()[1]

	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	match = cv2.matchTemplate(imagemCinza, agulha, cv2.TM_CCOEFF_NORMED)
	minVal, maxVal, minLocation, maxLocation = cv2.minMaxLoc(match)
	
	print(maxVal)

	if (maxVal > .60):
		x, y = maxLocation
		cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 0, 0,), 2)

	cv2.imshow('frame', imagem)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video.release()
cv2.destroyAllWindows()