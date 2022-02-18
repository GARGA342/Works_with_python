from matplotlib import pyplot as plt
import numpy as np

#VALUES OF PRODUCT A
prod_a = [12,22,16,4,4]

#VALUES OF PRODUCT B
prod_b = [3,5,7,36,21.7]

#X AXIS WITCH 0.5 SPACE
x1 = np.arange(len(prod_a))
x2 = [x + 0.25 for x in x1]

#BARS
plt.bar(x1, prod_a, width=0.25, label = "PRODUCT A", color= "deepskyblue")
plt.bar(x2, prod_b, width=0.25, label = "PRODUCT B", color= "mediumseagreen")

#NAME OF MONTHS IN X AXIS
months = ['Jan','Fev','Mar','Apr','Mai']
plt.xticks([x + 0.25 for x in range(len(prod_a))], months)

#INSERT A GRAPHIC LEGEND
plt.legend()

#SHOW WITH TITLE
plt.title("NUMBER OF SALES")
plt.show()