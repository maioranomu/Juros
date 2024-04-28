from matplotlib import pyplot as plt
def main():
    c = float(input("Qual valor inicial? "))
    i = float(input("Qual o valor da taxa? \n %"))
    i = i / 100
    t = int(input("Quantos meses/anos o juros será acumulado? "))
    feetype = input("Juros composto ou simples? [C/S]").lower()
    graphy = []
    graphx = []
    for date in range(t + 1):
        graphx.append(date)
    if feetype == "c":
        for time in graphx:
            add = c * (1 + i) ** time
            # print(add)
            graphy.append(add)
    elif feetype == "s":
        for time in graphx:
            add = c + (c  * i * time)
            # print(add)
            graphy.append(add)
    plt.plot(graphx, graphy)
    print(f"O valor final será de: {graphy[-1]}")
    plt.show()

main()