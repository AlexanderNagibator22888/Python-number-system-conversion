from sys import argv
from numpy import zeros
from pathlib import Path
import os.path

number = 0
listen = [[], []]
alphabet = tuple()
out_number = str("")
num = [10, 10, 0, 0]
file_name = 'Conventor.txt'
argb = zeros((8), dtype = bool)
file_path = str(Path(__file__).resolve().parents[0] / file_name)
argo = ("PyConventor v0.2", "by A. S. Zaykov", "Program parament\n-v --version\tVersion\n-a --about\tAbout\n-h --help\tHelp\n--path=\t\t+ file alphabet path\n--alphabet=\t+ file line alphabet")

def err_args(exit_code):
	print("Error's arg's")
	print(argo[2])
	exit(exit_code)

def args_number(number, exit_code):
	try:
		return_number = int(number)
		return return_number
	except ValueError:
		err_args(exit_code)

def file_alphabet(name):
	file_name_temp, res = open(file_path, "r", encoding = 'utf-8'), 0
	for line in file_name_temp:
		if len(line) < 5 or line[1] != ' ':
			print("Error's file")
			exit(7)
		if name == line[0]:
			res = tuple(line[2::].splitlines())
			break
	file_name_temp.close()
	if res == 0:
		print("Error's file, no line")
		exit(8)
	return res

def err_alphabet(data0, data1, exit_code):
	if data0 < 2 or data0 > data1:
		print("Error's number > alphabet or number < 2")
		exit(exit_code)

def uncov():
	res, temp = 0, 0
	for element in argv[num[2]]:
		temp = alphabet[0].find(element)
		if temp == -1:
			temp = alphabet[1].find(element)
			if temp == -1:
				print("Error's number's")
				exit(9)
		listen[0].append(temp)
		res = res * num[0] + temp
	return res

def conv(data):
	res, temp = str(""), 0
	while True:
		data, temp = divmod(data, num[1])
		res += alphabet[num[3]][temp]
		listen[1].append(temp)
		if data == 0:
			break
	listen[1] = listen[1][::-1]
	return res[::-1]

def out_f0():
	print(out_number)
	res, res2, temp, index = "|", "", 1, 1
	while index < len(out_number):
		if out_number[index - 1] == out_number[index]:
			temp += 1
			res += ' '
		else:
			res += '|'
			res2 += str(temp)
			while temp != 1:
				res2 += ' '
				temp -= 1
		index += 1
	res2 += str(temp)
	print(res)
	print(res2)
	print("Input size =", len(argv[num[2]]))
	print("Out size =", len(out_number))

def out_f1(index):
	temp0, temp2, res0, res1, res2 = 0, 0, "", "", ""
	if index == 1:
		temp2 = num[3]
	for ind, element in enumerate(listen[index]):
		if element > 0:
			temp0 = len(listen[index]) - ind - 1
			res0 += str(element) + '*' + str(num[index]) + '^' + str(temp0)
			res1 += str(element * num[index] ** temp0)
			res2 += alphabet[temp2][element]
			if ind + 1 != len(listen[index]):
				res0 += ' + '
				res1 += ' + '
	return res0 + ' = ' + res1 + ' = ' + res2

def main():
	global out_number, file_path, alphabet
	index = 1
	while index < len(argv):
		if argv[index][0] == '-':
			if len(argv[index]) == 1:
				err_args(1)
			if argv[index][1] == '-':
				if argv[index] == "--version":
					argb[0] = True
				elif argv[index] == "--about":
					argb[1] = True
				elif argv[index] == "--help":
					argb[2] = True
				elif argv[index] == "--detail":
					argb[7] = True
				elif argv[index][:7:] == "--path=":
					if argb[6]:
						err_args(13)
					else:
						argb[6] = True
					file_path = argv[index][7::]
				elif argv[index][:11:] == "--alphabet=":
					if argb[5]:
						err_args(12)
					else:
						argb[5] = True
					if not os.path.exists(file_path):
						print("Error no file alphabet")
						exit(14)
					if len(argv[index]) < 14 and len(argv[index]) > 11:
						alphabet = file_alphabet(argv[index][11])
						alphabet += tuple(alphabet[0].lower().splitlines())
						if len(argv[index]) == 13 and argv[index][11] != argv[index][12]:
							alphabet += file_alphabet(argv[index][12])
							num[3] = 2
					else:
						err_args(6)
				else:
					err_args(2)
			else:
				for element in argv[index][1::]:
					if element == 'v':
						argb[0] = True
					elif element == 'a':
						argb[1] = True
					elif element == 'h':
						argb[2] = True
					elif element == 'd':
						argb[7] = True
					else:
						err_args(3)
		else:
			if len(argv) - index > 2:
				num[0] = args_number(argv[index], 4)
				num[1] = args_number(argv[index + 2], 5)
				num[2] = index + 1
				index += 2
				argb[4] = True
			else:
				err_args(3)
		index += 1

	for index in range(0, 3):
		if argb[index]:
			print(argo[index])
			argb[3] = True
	if argb[3] or not argb[4]:
		exit(0)
	if not argb[5]:
		print("Not alphabet")
		exit(15)

	err_alphabet(num[0], len(alphabet[0]), 10)
	err_alphabet(num[1], len(alphabet[num[3]]), 11)

	number = uncov()
	out_number = conv(number)
	out_f0()

	if argb[7]:
		print('\nInput =', out_f1(0))
		print('\nOut =', out_f1(1))

if __name__ == "__main__":
	main()