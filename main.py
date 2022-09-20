import cv2
import numpy

redimensionamento = .2

# carregamos a imagem
# imagemBase = cv2.imread('img/bolao.jpeg', cv2.IMREAD_UNCHANGED)
imagemBase = cv2.imread('img/28-06/8-pontos-1.jpg', cv2.IMREAD_UNCHANGED)
imagemBase = cv2.resize(imagemBase, (int(
    imagemBase.shape[1] * redimensionamento), int(imagemBase.shape[0] * redimensionamento)))

# fazermos uma cópia da imagem cinza, pra diminuirmos o processamento da imagem por 3
imagemBaseCinza = cv2.cvtColor(imagemBase, cv2.COLOR_BGR2GRAY)

# carregamos a agulha
# agulha = cv2.imread('img/needle.PNG', cv2.IMREAD_UNCHANGED)
agulha = cv2.imread('img/28-06/agulha.jpg', cv2.IMREAD_UNCHANGED)
agulha = cv2.cvtColor(agulha, cv2.COLOR_BGR2GRAY)
agulha = cv2.resize(agulha, (int(
    agulha.shape[1] * redimensionamento), int(agulha.shape[0] * redimensionamento)))

# procuramos a agulha no palheiro
match = cv2.matchTemplate(imagemBaseCinza, agulha, cv2.TM_CCOEFF_NORMED)

print (match)

# valor que define o quão parecido o recorte da imagem tem que ser da agulha
percentualMatch = .55

# pegamos todos os valores onde ocorre essa semelhança
yloc, xloc = numpy.where(match >= percentualMatch)

# criamos uma lista com todas estas posições
retangulos = []
for (x, y) in zip(xloc, yloc):
    retangulos.append([int(x), int(y), int(
        agulha.shape[1]), int(agulha.shape[0])])
    retangulos.append([int(x), int(y), int(
        agulha.shape[1]), int(agulha.shape[0])])

# agrupados esses retângulos, filtrando a lista
groupRetangulos = cv2.groupRectangles(retangulos, 1, 0.2)
for (x, y, wei, hei) in groupRetangulos[0]:
    cv2.rectangle(imagemBase, (x, y), (x + wei, y + hei), (255, 0, 0,), 2)

# quantidade de pinos em pé
print(len(groupRetangulos[0]))

# mostramos a imagem final com as localizações, ilustrando os pinos de pé
cv2.imshow('Base Image', imagemBase)
cv2.waitKey()
cv2.destroyAllWindows()
