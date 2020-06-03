import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Local variables
x = [1,2,3,5,8,11,16,20,22,44,52,65,74,105,111]
y = [1,3,5,8,4,7,9,13,16,30,53,38,85,32,100]


x_sm = np.array(x)
y_sm = np.array(y)

x_smooth = np.linspace(x_sm.min(), x_sm.max(), 200)
a_BSpline = make_interp_spline(x, y)
y_smooth = a_BSpline( x_smooth)

# Show the plot/image
plt.xlabel('X axis')
plt.plot(x_smooth,y_smooth,label='Smooth Line')
plt.plot(x,y,label='Actual Line')
plt.ylabel('Y axis')
plt.legend()
plt.tight_layout()
plt.grid(alpha=0.8)
plt.savefig("example6.eps")
plt.show()















