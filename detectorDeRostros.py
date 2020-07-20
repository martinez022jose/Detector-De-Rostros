import cv2 

def mostrarImagen(imagen):
    cv2.imshow('Output', imagen)
    print("\nMostrando resultado. Pulsa cualquier tecla para encontrar nuevos resultaods.\n")
    cv2.waitKey(0)

def buscarRostro(coordenadasDeRostros):
    contador = 1
    for (x,y,ancho,alto) in coordenadasDeRostros:
        cv2.rectangle(imagen, (x,y), (x+ancho, y+alto), (0,255,0) , 3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        mensaje = "N"+ str(contador)
        cv2.putText(imagen,mensaje,(x+20,y+20), font, 0.75,(0,0,0),1,cv2.LINE_AA)
        contador+=1
        mostrarImagen(imagen)
        

imagen = cv2.imread("elonMusk2.jpeg")
imagenGrises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

cascadaAUtilizar= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

coordenadasDeRostros = cascadaAUtilizar.detectMultiScale(imagenGrises,scaleFactor=1.3,minNeighbors=4,minSize=(20,20),maxSize=(300,300))
  
buscarRostro(coordenadasDeRostros)

cv2.destroyAllWindows()