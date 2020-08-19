import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [ 2.525, 2.758, 3.018, 3.322, 3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520, 6.930, 7.349]
deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]

lines = plt.plot(years, pops, years, deaths)
plt.grid(True)
plt.setp(lines, color=(1, .4, .4), marker="+")
plt.show()