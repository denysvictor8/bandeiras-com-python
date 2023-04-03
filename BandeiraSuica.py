import numpy as np
import cv2

# bandeira completa
bd_suica = np.zeros((400, 400, 3), dtype=np.uint8)

# preenche todos os pixels com a cor vermelha
bd_suica[:, :, 2] = 255;

cruz = np.zeros((400, 400), dtype=np.uint8)
cruz[50:350, 150:250] = 1
cruz[150:250, 50:350] = 2

bd_suica[cruz == 1] = [255, 255, 255]
bd_suica[cruz == 2] = [255, 255, 255]

if bd_suica is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira da Suica", bd_suica)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./bandeiras-geradas/suica_bandeira.jpg', bd_suica)
