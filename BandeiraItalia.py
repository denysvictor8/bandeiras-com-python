import numpy as np
import cv2

# bandeira completa
bd_italia = np.zeros((400, 600, 3), dtype=np.uint8)

# as faixas da bandeira
faixas = np.zeros((400, 600), dtype=int)
# faixa do meio, atinge os pixels 200 ate 399
faixas[:, 200:400] = 1
# faixa direita, vai do 400 ate o 599
faixas[:, 400:] = 2

bd_italia[faixas == 0] = [0, 255, 0]
bd_italia[faixas == 1] = [255, 255, 255]
bd_italia[faixas == 2] = [0, 0, 255]

if bd_italia is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira da Italia", bd_italia)
    cv2.waitKey(0)
    cv2.imwrite('./bandeiras-geradas/italia_bandeira.jpg', bd_italia)

