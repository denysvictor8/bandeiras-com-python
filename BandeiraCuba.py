import numpy as np
import cv2

# bandeira completa
bd_cuba = np.zeros((500, 500, 3), dtype=np.uint8)
faixas = np.zeros((500, 500), dtype=int)
# indices das faixas azuis
faixas[0:100, :], faixas[200:300, :], faixas[400:500, :] = 0,2,4
# indices das faixas brancas
faixas[100:200, :], faixas[300:400, :] = 1,3
# faixas azuis e brancas
bd_cuba[faixas == 0] = bd_cuba[faixas == 2] = bd_cuba[faixas == 4]= [255, 0, 0]
bd_cuba[faixas == 1] = bd_cuba[faixas == 3] = [255, 255, 255]

vertical = int(len(bd_cuba[0])/2)
horizontal = int(len(bd_cuba[1])/2)

# primeira parte do triangulo vermelho
for i in range(vertical):
    for j in range(horizontal):
        if(i > j and j < vertical):
            bd_cuba[i][j] = [0, 0, 255]
        j += 1
    i += 1

# segunda parte do triangulo vermelho
cont = len(bd_cuba[0])
for i in range(250):
    for j in range(250, cont):
        bd_cuba[i-250][j-250] = [0, 0, 255]
    cont -= 1


if bd_cuba is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira de Cuba", bd_cuba)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./bandeiras-geradas/cuba_bandeira.jpg', bd_cuba)
