
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,10)
b = np.sin(a)

# plt.stem(a,b)
#
# plt.text(4,.5,'Amir khan')

plt.plot(a,b,'r^')
plt.title('sin graph ')
plt.grid(True)


plt.show()


