import matplotlib.pyplot as plt
import numpy as np

Y1 = np.array([3,8,1,10])
Y2 = np.array([6,2,7,11])
Y3 = np.array([3, 5, 7, 9])

plt.plot(Y1, label='Garis 1')
plt.plot(Y2, label='Garis 2')
plt.plot(Y3, label='Garis 3')

plt.title('Plot Banyak Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.legend()
plt.show()
