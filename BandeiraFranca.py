import numpy as np
import cv2

# bandeira completa, mesma logica da italia
bd_franca = np.zeros((400, 600, 3), dtype=np.uint8)

# as faixas da bandeira
faixas = np.zeros((400, 600), dtype=int)
# faixa do meio, atinge os pixels 200 ate 399
faixas[:, 200:400] = 1
# faixa direita, vai do 400 ate o 599
faixas[:, 400:] = 2

bd_franca[faixas == 0] = [255, 0, 0]
bd_franca[faixas == 1] = [255, 255, 255]
bd_franca[faixas == 2] = [0, 0, 255]

if bd_franca is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira da Italia", bd_franca)
    cv2.waitKey(0)
    cv2.imwrite('./bandeiras-geradas/franca_bandeira.jpg', bd_franca)

