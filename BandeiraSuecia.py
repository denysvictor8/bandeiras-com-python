import numpy as np
import cv2

# gera uma vetor de pixels, onde tem 300 px de altura
# 600 px de largura
# os pixels possuem 3 dimensoes, referentes ao rgb
bd_suecia = np.zeros((300, 600, 3), np.uint8)

# preenche todos os pixels com a cor azul
bd_suecia[:, :, 0] = 255;

# faixa vertical amarela
bd_suecia[120:181, :, 1] = 255;
bd_suecia[120:181, :, 2] = 255;
bd_suecia[120:181, :, 0] = 0;

# faixa horizontal amarela
bd_suecia[:, 150:211, 1] = 255;
bd_suecia[:, 150:211, 2] = 255;
bd_suecia[:, 150:211, 0] = 0;

if bd_suecia is None:
    print('ocorreu um erro')
else:
    cv2.imshow("Bandeira da italia", bd_suecia)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite('./bandeiras-geradas/italia_bandeira.jpg', bd_suecia)