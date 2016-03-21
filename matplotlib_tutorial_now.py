from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
		llcrnrlat = 20,
		llcrnrlon = -135,
		urcrnrlat = 50,
		urcrnrlon = -50,
		resolution='l')
m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
#m.drawcounties(color='r')
m.etopo()
#m.bluemarble()
plt.title('Basemap Tutorial')
plt.show()
#m.bluemarble()
#m.bluemarble()

plt.title('Basemap Tutorial')
plt.title('Basemap Tutorial')
plt.title('Basemap Tutorial')




