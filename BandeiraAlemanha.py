import numpy as np
import cv2

# bandeira completa
bd_alemanha = np.zeros((450, 600, 3), dtype=np.uint8)
# as faixas da bandeira
faixas = np.zeros((450, 600), dtype=int)
faixas[150:300, :] = 1 # faixa mediana
faixas[300:450, :] = 2 # faixa inferior

# sistema de cores é dado em BGR = blue, green e red
bd_alemanha[faixas == 0] = [0, 0, 0] #preto
bd_alemanha[faixas == 1] = [0, 0, 255] #vermelho
bd_alemanha[faixas == 2] = [0, 255, 255] #amarelo

if bd_alemanha is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira da Alemanha", bd_alemanha)
    cv2.waitKey(0)
    cv2.imwrite('./bandeiras-geradas/alemanha_bandeira.jpg', bd_alemanha)