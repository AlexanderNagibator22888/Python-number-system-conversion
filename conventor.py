#Number system conversion
#by A. S. Zaykov

import sys
import math
from pathlib import Path

if len(sys.argv) < 5:
	sys.exit()

file_name = "conventor.txt"
name = str(Path(__file__).resolve().parents[0] / file_name)

ux = [ 0, 0 ]
ue = [ 0, 0 ]

def args(res):
	f = open(name, "r")
	temp = -1
	
	for i in f:
		if len(i) < 4 or i[1] != ' ':
			sys.exit()
		
		if res == i[0]:
			temp = tuple(i[2::].splitlines())
			break
	
	f.close()
	if temp != -1:
		return temp
	else:
		sys.exit()

def uncov():
	res = 0
	temp = 0
	
	for i in sys.argv[3]:
		temp = ux[0][0].index(i)
		if temp == -1:
			sys.exit()
		elif temp >= ue[0]:
			sys.exit()
		res = res * ue[0] + temp;
		
	return res
	
def conv(num):
	res = ""
	temp = 0
	
	while True:
		num, temp = divmod(num, ue[1])
		res += ux[1][0][temp]
		if num == 0:
			break
	
	return res[::-1];
	
ns = lambda m, t = 10: int(math.log(m) / math.log(t)) + 1

def f_out(res):
	temp = [ 1, 1 ]
	ot = [ "|", "" ]
	print(res)
	
	while temp[0] < len(res):
		if res[temp[0] - 1] == res[temp[0]]:
			ot[0] += ' '
			temp[1] += 1
		else:
			ot[0] += '|'
			ot[1] += str(temp[1])
			temp[1] -= ns(temp[1])
			for i in range(0, temp[1]):
				ot[1] += ' '
			temp[1] = 1
		temp[0] += 1
	ot[1] += str(temp[1])
	
	print(ot[0])
	print(ot[1])
	print("Input size =", len(sys.argv[3]))
	print("Out size =", len(res))

def f_out2(res, num, t):
	temp = str(res) + " ="
	temp_i = int()
	temp_s = str(res) + " ="
	temp_t = int()
	
	for i in range(0, len(res)):
		temp_i = ux[t][0].index(res[i])
		temp += " " + str(temp_i) + "*" + str(ue[t])
		temp_t = len(res) - 1 - i
		temp += "^" + str(temp_t)
		temp_s += " " + str(temp_i * ue[t] ** temp_t)
		if (i != len(res) - 1):
			temp += " +"
			temp_s += " +"
	
	temp_s += " = " + str(num)
	temp += " = " + str(num)
	print(temp)
	print(temp_s)

def main():
	if len(sys.argv[1]) == 3:
		if sys.argv[1][0] == '-':
			ux[0] = args(sys.argv[1][1])
			if sys.argv[1][1] != sys.argv[1][2]:
				ux[1] = args(sys.argv[1][2])
			else:
				ux[1] = ux[0]
	else:
		sys.exit()
	
	if sys.argv[2].isdigit():
		ue[0] = int(sys.argv[2])
		if ue[0] > len(ux[0][0]) or ue[0] < 2:
			sys.exit()
	else:
		sys.exit()
	
	if sys.argv[4].isdigit():
		ue[1] = int(sys.argv[4])
		if ue[1] > len(ux[1][0]) or ue[1] < 2:
			sys.exit()
	else:
		sys.exit()
	
	if ue[0] == ue[1] and sys.argv[1][1] == sys.argv[1][2]:
		sys.exit()
	
	num = uncov()
	out = conv(num)
	f_out(out)
	
	if len(sys.argv) > 5 and sys.argv[5] == "-o":
		print()
		print("Вывод преобразованного числа")
		f_out2(out, num, 1)
		print()
		print("Вывод исходного числа")
		f_out2(sys.argv[3], num, 0)

if __name__ == "__main__":
	main()