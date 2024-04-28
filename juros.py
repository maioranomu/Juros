from matplotlib import pyplot as plt
def main():
    while True:
        try:
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
                    graphy.append(add)
            elif feetype == "s":
                for time in graphx:
                    add = c + (c  * i * time)
                    graphy.append(add)
            plt.plot(graphx, graphy)
            print(f"O valor final será de: {graphy[-1]}")
            input("Aperte [ENTER] para ver o grafico. \n")
            plt.show()
            break
        except ValueError:
            print("Error")
main()
