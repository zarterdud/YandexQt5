a = int(input())
for i in range(1, a + 1):
    for _ in range(1, a + 1):
        print(i * _, end="\t")
    print()
