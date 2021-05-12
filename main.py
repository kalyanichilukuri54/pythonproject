# THE N VALUE IS value in the range between 2 to 2*10^3
# THE CONTRAINTS 1<=t<=100
# 2<=n<=2*10^3
# -10^3<=xiyi<=10^3
# 1<=hi<=10^3

t = input("Enter t value in between the range from 1 to 100\n")
listx = []
listy = []
listh = []
for i in range(0, int(t)):
	n = input()
	listx = [int(n) for n in input('').split()]
	listy = [int(n) for n in input('').split()]
	listh = [int(n) for n in
    input('').split()]
	if listx != listh:
		if listx == listy:
			print("NO")
		else:
			print("YES")
	else:
		print("YES")