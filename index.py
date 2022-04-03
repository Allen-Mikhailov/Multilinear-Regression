import CSV
import matplotlib.pyplot as plt

csv = CSV.opencsv("./Cars.csv")

weightedParams = []

y = CSV.getCollum(csv, "price")

plt.figure()
plt.plot(CSV.getCollum(csv, "compressionratio"), y)