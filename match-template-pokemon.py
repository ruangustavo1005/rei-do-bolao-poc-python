import cv2
from cv2 import rectangle

imagemBase = cv2.imread('img/pokemons.jpg', cv2.IMREAD_UNCHANGED)
imagemBase = cv2.cvtColor(imagemBase, cv2.COLOR_BGR2GRAY)

agulha = cv2.imread('img/bulbajaison.jpg', cv2.IMREAD_UNCHANGED)
agulha = cv2.cvtColor(agulha, cv2.COLOR_BGR2GRAY)

match = cv2.matchTemplate(imagemBase, agulha, cv2.TM_CCOEFF_NORMED)

cv2.imshow('imagem base', imagemBase)
cv2.imshow('agulha', agulha)
cv2.imshow('match', match)
cv2.waitKey()
cv2.destroyAllWindows()