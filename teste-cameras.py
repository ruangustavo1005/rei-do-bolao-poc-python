import cv2

index = 0
arr = []
i = 30
while i > 0:
  cap = cv2.VideoCapture(index)
  if cap.read()[0]:
    arr.append(index)
    cap.release()
  index += 1
  i -= 1
print(arr)

for index in arr:
  video = cv2.VideoCapture(index)

  if (video.isOpened()== False):
    print("Error opening video stream or file")


  # while(True):
  while(video.isOpened()):
    imagem = video.read()[1]
    cv2.imshow('frame', imagem)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  video.release()
  cv2.destroyAllWindows()