n = int(input("digite um numero para a tabuada: "))
print("=-" * 49)
print(f"TABUADA DO {n}\n".center(84))
for i in range(0, 10 + 1):
    print(f"{n} x {i} = {n*i}\n".center(84))
print("=-" * 49)
