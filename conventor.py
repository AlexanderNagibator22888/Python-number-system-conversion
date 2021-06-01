from sys import argv
from math import log
from pathlib import Path

if len(argv) < 5:
	exit()

file_name = "conventor.txt"
name = str(Path(__file__).resolve().parents[0] / file_name)
ux, ue, uu = None, [ None, None ], None

def args(res):
	f, temp = open(name, "r"), 1
	
	for i in f:
		if len(i) < 5 or i[1] != ' ':
			exit()
		if res == i[0]:
			temp = tuple(i[2::].splitlines())
			break
	
	f.close()
	if temp == -1:
		exit()
	return temp

def uncov(x1, x2):
	res, temp = 0, 0
	
	for i in argv[3]:
		temp = x1.find(i)
		if temp == -1:
			temp = x2.find(i)
			if temp == -1:
				exit()
		res = res * ue[0] + temp
	
	return res
	
def conv(num, lis):
	res, temp = "", 0
	
	while True:
		num, temp = divmod(num, ue[1])
		res += lis[temp]
		if num == 0:
			break
	
	return res[::-1]

ns = lambda m, t = 10: int(log(m) / log(t)) + 1

def f_out(res):
	print(res)
	stemp1, stemp2, temp = "|", "", 1
	
	for i in range(1, len(res)):
		if res[i-1] == res[i]:
			stemp1 += ' '
			temp += 1
		else:
			stemp1 += '|'
			stemp2 += str(temp)
			for j in range(0, temp - ns(temp)):
				stemp2 += ' '
			temp = 1
	stemp2 += str(temp)
	
	print(stemp1)
	print(stemp2)
	
	print("Input size =", len(argv[3]))
	print("Out Size =", len(res))

def f_out2(res, les, les2, j, out):
	stemp1 = str(res) + " ="
	stemp2 = str(res) + " ="
	n_temp, p_temp, s_temp = 0, 0, str(j)
	
	for i in range(0, len(res)):
		n_temp = les.find(res[i])
		if n_temp == -1:
			n_temp = les2.find(res[i])
		p_temp = len(res) - i - 1
		if i != 0:
			stemp1 += " +"
			stemp2 += " +"
		stemp1 += ' ' + str(n_temp);
		stemp1 += '*' + str(p_temp);
		stemp1 += '^' + s_temp
		stemp2 += ' ' + str(n_temp * j ** p_temp)
	print(stemp1, '=', out)
	print(stemp2, '=', out)

def main():
	if len(argv[1]) == 3 and argv[1][0] == '-':
		ux = args(argv[1][1])
		ux += tuple(ux[0].lower().splitlines())
		if argv[1][1] != argv[1][2]:
			ux += args(argv[1][2])
			uu = 2
		else:
			uu = 0
	else:
		exit()
	
	if argv[2].isdigit():
		ue[0] = int(argv[2])
		if ue[0] > len(ux[0]) or ue[0] < 2:
			exit()
	else:
		exit()
	
	if argv[4].isdigit():
		ue[1] = int(argv[4])
		if ue[1] > len(ux[uu]) or ue[1] < 2:
			exit()
	else:
		exit()
	
	if ue[0] == ue[1] and uu == 0:
		exit()
	
	num = uncov(ux[0], ux[1])
	out = conv(num, ux[uu])
	
	f_out(out)
	print()
	print("Вывод исходного числа")
	f_out2(argv[3], ux[0], ux[1], ue[0], num)
	print()
	print("Вывод преобразованеого числа")
	f_out2(out, ux[uu], ux[1], ue[1], num)

if __name__ == "__main__":
	main()