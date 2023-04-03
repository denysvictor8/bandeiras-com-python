import numpy as np
import cv2

# bandeira completa
bd_brasil = np.zeros((500, 500, 3), dtype=np.uint8)

faixas = np.zeros((500, 500), dtype=int)
bd_brasil[:, :, 0] = bd_brasil[:, :, 2] = 000;
bd_brasil[:, :, 1] = 255;

vertical = int(len(bd_brasil[0])/2)
horizontal = int(len(bd_brasil[1])/2)

# primeira parte do losango amarelo
for i in range(250):
    for j in range(250):
        if j >= 250 - i:
            bd_brasil[i, j] = [0, 255, 255]

# segunda parte do losango amarelo
for i in range(250, 500):
    for j in range(250):
        if j <= i - 250:
            bd_brasil[i-250, j-250] = [0, 255, 255]

# terceira parte do losango amarelo
for i in range(250):
    for j in range(i+1):
        bd_brasil[250 + i - j, 250 + j] = [0, 255, 255]

# quarta parte do losango amarelo
for i in range(250):
    for j in range(i+1):
        bd_brasil[250 + i-j, 250 - j] = [0, 255, 255]


# pega as dimensões da imagem
alt, larg, channels = bd_brasil.shape

# Calcula o raio do circulo
radius = min(alt, larg) // 4

# Calcula as coordenadas do centro da imagem
centro_x = larg // 2
centro_y = alt // 2

# Desenha o círculo no centro da imagem
cv2.circle(bd_brasil, (centro_x, centro_y), radius, (255, 0, 0), thickness =- 1)


if bd_brasil is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira do Brasil", bd_brasil)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./bandeiras-geradas/brasil_bandeira.jpg', bd_brasil)