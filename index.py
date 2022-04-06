import CSV
import matplotlib.pyplot as plt

csv = CSV.opencsv("./Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv")

csvHeaders = CSV.getHeaders(csv)

weightedParams = [
    # "symboling",
    # "wheelbase",
    # "carlength",
    # "carwidth",
    # "carheight",
    # "curbweight",
    # "enginesize",
    # "boreratio",
    # "stroke",
    # "compressionratio",
    # "horsepower",
    # "peakrpm",
    # "citympg",
    # "highwaympg"
]
# yParam = "price"

collums = []
for collum in weightedParams:
    collums.append(CSV.num(CSV.getCollum(csv, collum)))

weightCount = len(weightedParams)
weights = []
for i in range(weightCount):
    weights.append(1)
b = 1

n = len(collums[0])
itterations = 1000

weightRange = range(weightCount)
nRange = range(n)

yCollum = CSV.num(CSV.getCollum(csv, yParam))

alpha = 1  # Learning Rate

errors = []

def yHat(x):
    v = b
    for w in weights:
        v += x*2
    return v
    

for j in range(itterations):
    averageerror = 0

    # Bias
    # err = 0
    # for j in nRange:
    #     y = yCollum[j]
    #     err += 2 * (b - y)
    # b -= alpha * err/n

    for i in weightRange:
        w = weights[i]
        err = 0
        collum = collums[i]

        # Weights
        for j in nRange:
            x = collum[j]
            y = yCollum[j]
            err += (yHat(x) - y)*x

        averageerror += err
        # print("Offset: " + str(alpha * err / n))
        weights[i] -= alpha * (err / n)
    errors.append(averageerror/weightCount)

plt.figure()
plt.plot(errors)
plt.show()


# https://towardsdatascience.com/master-machine-learning-multiple-linear-regression-from-scratch-with-python-ac716a9b78a4

# plt.figure()
# plt.plot(y)
# plt.show()
