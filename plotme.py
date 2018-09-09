# Plotting example with matplotlib

from matplotlib import pyplot as plt
from matplotlib import style

# style.use('ggplot')
style.use('dark_background')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# can plot specifically, after just showing the defaults:

# plt.plot(x,y,linewidth=5)
plt.plot(x,y,'g',linewidth=7) #changing line color to green
plt.plot(x2,y2,linewidth=5) #We can also use plt.bar and plt.scatter for different types of graphs\


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
