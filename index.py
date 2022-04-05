import CSV
import matplotlib.pyplot as plt

csv = CSV.opencsv("./Cars.csv")

csvHeaders = CSV.getHeaders(csv)

weightedParams = [
    "symboling",
    "wheelbase",
    "carlength",
    "carwidth",
    "carheight",
    "curbweight",
    "enginesize",
    "boreratio",
    "stroke",
    "compressionratio",
    "horsepower",
    "peakrpm",
    "citympg",
    "highwaympg"
]
yParam = "price"

collums = []
for collum in weightedParams:
    collums.append(CSV.num(CSV.getCollum(csv, collum)))
print(collums)

weightCount = len(weightedParams)
weights = []
for i in range(weightCount):
    weights.append(1)
yintercept = 1

n = len(collums[0])
itterations = 1000

weightRange = range(weightCount)
nRange = range(n)

yCollum = CSV.num(CSV.getCollum(csv, yParam))

alpha = 1 #Learning Rate

for j in range(itterations):
    for i in weightRange:
        weight = weights[i]
        err = 0
        collum = collums[i]
        for n in nRange:
            err += 2*collum[n] * (weight*collum[n]+yintercept - yCollum[n])
        weights[i] -= alpha * err / n

plt.figure()
for i in weightRange:
    plt.plot([0, weights[i]])
plt.show()



# https://towardsdatascience.com/master-machine-learning-multiple-linear-regression-from-scratch-with-python-ac716a9b78a4

# plt.figure()
# plt.plot(y)
# plt.show()
