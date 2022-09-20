import cv2
from cv2 import rectangle
import numpy

redimensionamento = .2

base = cv2.imread('img/28-06/3-pontos-1.jpg', cv2.IMREAD_UNCHANGED)
base = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
base = cv2.resize(base, (int(base.shape[1] * redimensionamento), int(base.shape[0] * redimensionamento)))

cv2.imshow('Base', base)
cv2.waitKey()
cv2.destroyAllWindows()

locs = [
  [160, 371],
  [191, 409],
  [231, 467],
  [259, 355],
  [301, 385],
  [344, 342],
  [359, 435],
  [392, 371],
  [462, 408],
]

margemErro = 120
percentualAcerto = .7

video = cv2.VideoCapture('vid/cancha-1-pontos-8.mp4')

if (video.isOpened()== False):
  print("Error opening video stream or file")

redimensionamento = .3

while(video.isOpened()):
  imagem = video.read()[1]
  imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  imagem = cv2.resize(imagem, (int(imagem.shape[1] * redimensionamento), int(imagem.shape[0] * redimensionamento)))


  retangulos = []
  for index in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    agulha = cv2.imread('img/cancha-1/%s.png' % index, cv2.IMREAD_UNCHANGED)
    agulha = cv2.cvtColor(agulha, cv2.COLOR_BGR2GRAY)

    match = cv2.matchTemplate(imagem, agulha, cv2.TM_CCOEFF_NORMED)

    yloc, xloc = numpy.where(match >= percentualAcerto)

    # loc = locs[index - 1]

    for (x, y) in zip(xloc, yloc):
      # if (int(x) < loc[0] + margemErro and int(x) > loc[0] - margemErro
      # and int(y) < loc[1] + margemErro and int(y) > loc[1] - margemErro):
        retangulos.append([int(x), int(y), int(agulha.shape[1]), int(agulha.shape[0])])
        retangulos.append([int(x), int(y), int(agulha.shape[1]), int(agulha.shape[0])])


  groupRetangulos = cv2.groupRectangles(retangulos, 1, 0.2)
  for (x, y, wei, hei) in groupRetangulos[0]:
      cv2.rectangle(imagem, (x, y), (x + wei, y + hei), (255, 0, 0,), 2)

  cv2.imshow('Base', imagem)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video.release()
cv2.waitKey()
cv2.destroyAllWindows()
