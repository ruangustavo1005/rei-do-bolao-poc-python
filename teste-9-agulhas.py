import cv2
from cv2 import rectangle
import numpy

redimensionamento = .2

# base = cv2.imread('img/28-06/3-pontos-1.jpg', cv2.IMREAD_UNCHANGED)
# base = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
# base = cv2.resize(base, (int(base.shape[1] * redimensionamento), int(base.shape[0] * redimensionamento)))

locs = [
  [126, 93],
  [164, 121],
  [202, 161],
  [218, 73],
  [259, 93],
  [321, 123],
  [285, 64],
  [350, 69],
  [415, 89],
]

margemErro = 25
percentualAcerto = .7

video = cv2.VideoCapture('vid/cancha-1-pontos-8.mp4')

if (video.isOpened()== False):
  print("Error opening video stream or file")

redimensionamento = .3

while(video.isOpened()):
  imagem = video.read()[1]
  imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  imagem = cv2.resize(imagem, (int(imagem.shape[1] * redimensionamento), int(imagem.shape[0] * redimensionamento)))
  # imagem = cv2.rotate(imagem, cv2.ROTATE_180)

  # cv2.imshow('Base', imagem)
  # cv2.waitKey()
  # cv2.destroyAllWindows()

  # break

  retangulos = []
  for index in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    agulha = cv2.imread('img/cancha-1 (2)/%s.png' % index, cv2.IMREAD_UNCHANGED)
    agulha = cv2.cvtColor(agulha, cv2.COLOR_BGR2GRAY)
    hei, wei = agulha.shape

    match = cv2.matchTemplate(imagem, agulha, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
    x, y = max_loc

    # loc = locs[index - 1]

    # a, b = loc
    # cv2.rectangle(imagem, (a - margemErro, b - margemErro), (a + margemErro, b + margemErro), (0, 255, 0,), 2)

    # print ('agulha %s: %s, %s (%s, %s)' % (index, x, y, a, b))

    # cv2.rectangle(imagem, (x, y), (x + wei, y + hei), (0, 0, 255,), 1)

    # if (int(x) < a + margemErro and int(x) > a - margemErro
    # and int(y) < b + margemErro and int(y) > b - margemErro):
    #   # print('achou a agulha %s no range' % index)
    #   if (max_val >= percentualAcerto):
    #     # cv2.rectangle(imagem, (int(x - (wei / 2)), y), (int(x + (wei / 2)), y + hei), (255, 0, 0,), 2)
    #     cv2.rectangle(imagem, (x, y), (x + wei, y + hei), (255, 0, 0,), 2)


    yloc, xloc = numpy.where(match >= percentualAcerto)

    loc = locs[index - 1]

    for (x, y) in zip(xloc, yloc):
      if (int(x) < loc[0] + margemErro and int(x) > loc[0] - margemErro
      and int(y) < loc[1] + margemErro and int(y) > loc[1] - margemErro):
        retangulos.append([int(x), int(y), int(agulha.shape[1]), int(agulha.shape[0])])
        retangulos.append([int(x), int(y), int(agulha.shape[1]), int(agulha.shape[0])])
  

  groupRetangulos = cv2.groupRectangles(retangulos, 1, 0.2)
  # print('-----')
  for (x, y, wei, hei) in groupRetangulos[0]:
    # print([x, y])
    cv2.rectangle(imagem, (x, y), (x + wei, y + hei), (255, 0, 0,), 2)

  cv2.imshow('Base', imagem)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video.release()
cv2.waitKey()
cv2.destroyAllWindows()
