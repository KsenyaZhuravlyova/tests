#Как округлить Вверх массив с плавающей запятой?
#(Необходимо реализовать не классическое математическое округление, а округление вверх
# по абсолютному значению (round(0)=0, round(0.1)=1, round(1)=1, round(-0.1)=-1 и round(-1)=-1)
# то есть любое значение больше нуля это единица.)

import numpy as np

n = np.arange(0, 5, 0.5)
m = np.ceil(n)
print(n)
print('Числа с округлением: ', m)