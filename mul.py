import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
figure, axis = plt.subplots(2, 2)

axis[0, 0].bar(x, x * 2)
axis[0, 0].set_title("x*2")

axis[0, 1].plot(x, x * 3, color="Lightblue")
axis[0, 1].set_title("x*3")

axis[1, 1].barh(x, x * 4, color="yellow")
axis[1, 1].set_title("x*4")

axis[1, 0].bar(x, x * 5, color="purple")
axis[1, 0].set_title("x*5")

plt.tight_layout()
plt.show()