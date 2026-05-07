import matplotlib.pyplot as plt
import numpy as np
overs=np.arange(1,15 )
runs=[18,12,5,9,10,14,7,10,11,3,0,17,14,18]
plt.bar(overs,runs,color='blue')
plt.title('Scorecard')
plt.xlabel("overs",color='red')
plt.ylabel("Runs Scored",color='red')
plt.xticks(overs)
plt.grid(axis='y',linestyle='-',color='Green')
plt.show()