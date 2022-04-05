import CSV
import matplotlib.pyplot as plt

csv = CSV.opencsv("./Cars.csv")

weightedParams = []

x = CSV.num(CSV.getCollum(csv, "compressionratio"))
y = CSV.num(CSV.getCollum(csv, "price"))

#https://towardsdatascience.com/master-machine-learning-multiple-linear-regression-from-scratch-with-python-ac716a9b78a4

plt.figure()
plt.plot(y)
plt.show()