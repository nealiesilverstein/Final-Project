import sqlite3
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"finaldb.db")
cur = conn.cursor()

countries = []
populations = []
cur.execute("SELECT Countries.country, Countries.country_population FROM Countries")
for t in cur:
    if len(countries) < 100:
        countries.append(t[0])
        populations.append(t[1])

print(countries)
print(populations)


#fig, ax = plt.subplots()
#ax.bar(populations[0:10], countries[0:10])
#ax.set(title="Country vs Population")
plt.figure()
plt.barh(populations[0:10], countries[0:10], align = 'center', alpha = 0.5)
plt.title('Country vs Population')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()




#plt.barh(y_pos, performance, align='center', alpha=0.5)
#plt.yticks(y_pos, objects)