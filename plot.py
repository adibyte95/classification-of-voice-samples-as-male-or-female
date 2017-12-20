import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = "data.csv"
df = pd.read_csv(data_path)

# we will plot these values so as to find out which of the variables is perfect
# to classify between our models

# mean freq
plt.hist(df[df['label']=='male']['meanfreq'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['meanfreq'],200,color='pink', label = 'female')
plt.title('MEAN FREQ')
plt.legend()
plt.savefig('pictures/MEAN FREQ')
plt.clf()
print(1)

#sd 
plt.hist(df[df['label']=='male']['sd'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['sd'],200,color='pink', label = 'female')
plt.title('SD')
plt.legend()
plt.savefig('pictures/SD')
plt.clf()
print(2)

#median
plt.hist(df[df['label']=='male']['median'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['median'],200,color='pink', label = 'female')
plt.title('median')
plt.legend()
plt.savefig('pictures/median')
plt.clf()
print(3)
#Q25
plt.hist(df[df['label']=='male']['Q25'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['Q25'],200,color='pink', label = 'female')
plt.title('Q25')
plt.legend()
plt.savefig('pictures/Q25')
plt.clf()
print(4)
#Q75
plt.hist(df[df['label']=='male']['Q75'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['Q75'],200,color='pink', label = 'female')
plt.title('Q75')
plt.legend()
plt.savefig('pictures/Q75')
plt.clf()
print(5)
#skew
plt.hist(df[df['label']=='male']['skew'],10,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['skew'],10,color='pink', label = 'female')
plt.title('skew')
plt.legend()
plt.savefig('pictures/skew')
plt.clf()
print(6)
#kurt
plt.hist(df[df['label']=='male']['kurt'],2,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['kurt'],2,color='pink', label = 'female')
plt.title('kurt')
plt.legend()
plt.savefig('pictures/kurt')
plt.clf()
print(7)

#sp.ent
'''
plt.hist(np.asarray(df[df['label']=='male']['sp.ent'], dtype='float'),1,color='blue',label = 'male', normalized = True)
plt.hist(np.asarray(df[df['label']=='female']['sp.ent'], dtype='float'),1,color='pink', label = 'female', normalized = True)
plt.title('sp.ent')
plt.legend()
plt.savefig('pictures/sp.ent')
plt.clf()
print(8)
'''
#sfm 
plt.hist(df[df['label']=='male']['sfm'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['sfm'],200,color='pink', label = 'female')
plt.title('sfm')
plt.legend()
plt.savefig('pictures/sfm')
plt.clf()
print(9)
#mode
plt.hist(df[df['label']=='male']['mode'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['mode'],200,color='pink', label = 'female')
plt.title('mode')
plt.legend()
plt.savefig('pictures/mode')
plt.clf()
print(10)
#centroid
plt.hist(df[df['label']=='male']['centroid'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['centroid'],200,color='pink', label = 'female')
plt.title('centroid')
plt.legend()
plt.savefig('pictures/centroid')
plt.clf()
print(11)
#meanfun
plt.hist(df[df['label']=='male']['meanfun'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['meanfun'],200,color='pink', label = 'female')
plt.title('meanfun')
plt.legend()
plt.savefig('pictures/meanfun')
plt.clf()
print(12)
#minfun
plt.hist(df[df['label']=='male']['minfun'],5,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['minfun'],5,color='pink', label = 'female')
plt.title('minfun')
plt.legend()
plt.savefig('pictures/minfun')
plt.clf()
print(13)
#maxfun 
plt.hist(df[df['label']=='male']['maxfun'],20,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['maxfun'],20,color='pink', label = 'female')
plt.title('maxfun')
plt.legend()
plt.savefig('pictures/maxfun')
print(14)
plt.clf()
#meandom
plt.hist(df[df['label']=='male']['meandom'],100,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['meandom'],100,color='pink', label = 'female')
plt.title('meandom')
plt.legend()
plt.savefig('pictures/meandom')
print(15)
plt.clf()
#mindom
plt.hist(df[df['label']=='male']['mindom'],20,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['mindom'],20,color='pink', label = 'female')
plt.title('mindom')
plt.legend()
plt.savefig('pictures/mindom')
print(16)
plt.clf()
#maxdom
plt.hist(df[df['label']=='male']['maxdom'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['maxdom'],200,color='pink', label = 'female')
plt.title('maxdom')
plt.legend()
plt.savefig('pictures/maxdom')
print(17)

#dfrange
plt.hist(df[df['label']=='male']['dfrange'],50,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['dfrange'],50,color='pink', label = 'female')
plt.title('dfrange')
plt.legend()
plt.savefig('pictures/dfrange')
plt.clf()
print(18)

#modindx
plt.hist(df[df['label']=='male']['modindx'],200,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['modindx'],200,color='pink', label = 'female')
plt.title('modindx')
plt.legend()
plt.savefig('pictures/modindx')
plt.clf()
print(19)

#IQR
plt.hist(df[df['label']=='male']['IQR'],20,color='blue',label = 'male')
plt.hist(df[df['label']=='female']['IQR'],20,color='pink', label = 'female')
plt.title('IQR')
plt.legend()
plt.savefig('pictures/IQR')
plt.clf()
print(20)
