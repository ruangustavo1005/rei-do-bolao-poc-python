import psycopg2
import numpy
import cv2
import base64

connection = psycopg2.connect("host=%s port=%s dbname=%s user=%s password=%s" % (
  "localhost",
  "54321",
  "postgres",
  "postgres",
  "admin"
))

cursor = connection.cursor()
cursor.execute("""
SELECT imagem FROM configuracao_pino
""")

[bytea] = cursor.fetchone()
file_bytes = numpy.asarray(bytearray(bytea), dtype=numpy.uint8)
img = cv2.imdecode(file_bytes, 0)
cv2.imshow('Imagem', img)
cv2.waitKey()
cv2.destroyAllWindows()