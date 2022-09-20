import cv2
from cv2 import rectangle
import numpy

redimensionamento = .9
redimensionamentoAgulha = 1
percentualMatch = .5

agulha = cv2.imread('img/needle-2.png', cv2.IMREAD_UNCHANGED)
agulha = cv2.cvtColor(agulha, cv2.COLOR_BGR2GRAY)
agulha = cv2.resize(agulha, (int(agulha.shape[1] * redimensionamentoAgulha), int(agulha.shape[0] * redimensionamentoAgulha)))

h, w = agulha.shape

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('vid/cancha-1-pontos-8.mp4')

if (video.isOpened()== False):
  print("Error opening video stream or file")


# while(True):
while(video.isOpened()):
	imagem = video.read()[1]
	imagem = cv2.resize(imagem, (int(imagem.shape[1] * redimensionamento), int(imagem.shape[0] * redimensionamento)))

	imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
	match = cv2.matchTemplate(imagemCinza, agulha, cv2.TM_CCOEFF_NORMED)
	minVal, maxVal, minLocation, maxLocation = cv2.minMaxLoc(match)
	
	print(maxVal)

	# if (maxVal > .60):
	# 	x, y = maxLocation
	# 	cv2.rectangle(imagem, (x, y), (x + w, y + h), (255, 0, 0,), 2)

	# yloc, xloc = numpy.where(match >= percentualMatch)

	# retangulos = []
	# for (x, y) in zip(xloc, yloc):
	# 		retangulos.append([int(x), int(y), int(
	# 				agulha.shape[1]), int(agulha.shape[0])])
	# 		retangulos.append([int(x), int(y), int(
	# 				agulha.shape[1]), int(agulha.shape[0])])

	# groupRetangulos = cv2.groupRectangles(retangulos, 1, 0.2)
	# for (x, y, wei, hei) in groupRetangulos[0]:
	# 	cv2.rectangle(imagem, (x, y), (x + wei, y + hei), (255, 0, 0,), 2)

	cv2.imshow('frame', imagem)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video.release()
cv2.destroyAllWindows()