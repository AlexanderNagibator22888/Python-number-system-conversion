from sys import argv
argo = ("PyConventor v1.1 final", "by A. S. Zaykov", "program (parament) [alphabet [dd]] input-notation number out-notation\nParament's\n-v --version\tVersion\n-a --about\tAbout\n-h --help\tHelp\n-A --alphabet\tAlphabet\n-d --detail\tDetail\n-D --detail2\tDetail2")

if len(argv) == 1:
	print("No args")
	print(argo[2])
	exit(100)

from math import log
from numpy import zeros
from pathlib import Path
from os import path

listen, number, out = [[], []], 0, ''
notation, nind, alph = [0, 0], [0, 0, 0], 'dd'
argb, alphabet = zeros((9), dtype = bool), tuple()
file_path = str(Path(__file__).resolve().parents[0] / 'conventor.txt')
ns = lambda x, y = 10: int(log(x) / log(y))

def error_args(exit_code):
	print("Error's arg's")
	exit(exit_code)

def args_two(index, exit_code):
	if argb[index]:
		error_args(exit_code)
	else:
		argb[index] = True

def args_three(res):
	if len(res) < 1 and len(res) > 2:
		error_args(112)
	return res

def args_int(number, exit_code):
	try:
		return int(number)
	except ValueError:
		error_args(exit_code)

def alphabet_file(name):
	file_name, res = open(file_path, 'r', encoding = 'utf-8'), None
	for line in file_name:
		if line[0] == name:
			if len(line) > 3 and line[3] != '\n' and line[1] == ' ':
				res = tuple(line[2::].splitlines())
			else:
				print("Error's file")
				exit(201)
	file_name.close()
	if res == None:
		print("No alphabet line", name)
		exit(202)
	return res

def uncov():
	global number; temp = 0
	for element in argv[nind[0] + 1]:
		temp = alphabet[nind[1]].find(element)
		if temp == -1:
			temp = alphabet[nind[1] + 1].find(element)
			if temp == -1:
				print("Uncov error")
				exit(300)
		if temp > notation[0]:
			print("number", temp, "> notation")
			exit(301)
		if argb[3]:
			listen[0].append(temp)
		number = number * notation[0] + temp

def conv():
	global number, listen, out; temp = 0
	while True:
		number, temp = divmod(number, notation[1])
		out += alphabet[nind[2]][temp]
		if argb[3]:
			listen[1].append(temp)
		if number == 0:
			break
	listen[1] = listen[1][::-1]
	out = out[::-1]

def out_f0():
	temp, res0, res1 = 1, '|', ''
	for index in range(1, len(out)):
		if out[index - 1] == out[index]:
			temp += 1; res0 += ' '
		else:
			res1 += str(temp)
			temp -= ns(temp)
			for i in range(1, temp):
				res1 += ' '
			res0 += '|'
			temp = 1
	res1 += str(temp)
	print(res0); print(res1)

def out_f1(ind, ot):
	temp, res0, res1, res2 = 0, '', '', ''
	for index, element in enumerate(listen[ind]):
		if element > 0:
			if index > 0:
				res0 += ' + '; res1 += ' + '; res2 += ' + '
			temp = len(listen[ind]) - index - 1
			res0 += str(element) + '*' + str(notation[ind]) + '^' + str(temp)
			res1 += str(element * (notation[ind] ** temp))
			res2 += ot[index]
	return res0 + ' = ' + res1 + ' = ' + res2

def main():
	global alphabet, file_path, alph
	index0, index1 = 1, 0
	while index0 != len(argv):
		if argv[index0][0] == '-':
			if len(argv[index0]) == 1:
				error_args(102)
			if argv[index0][1] == '-':
				if argv[index0] == '--version':
					argb[0] = True
				elif argv[index0] == '--about':
					argb[1] = True
				elif argv[index0] == '--help':
					argb[2] = True
				elif argv[index0] == '--detail2':
					argb[3] = True
				elif argv[index0] == '--detail':
					argb[8] = True
				elif len(argv) - index0 > 1:
					if argv[index0] == '--path':
						args_two(4, 110); index1 += 1
						file_path = argv[index0 + index1]
					elif argv[index0] == '--alphabet':
						args_two(5, 111); index1 += 1
						alph = args_three(argv[index0 + index1])
					else:
						error_args(109)
				else:
					error_args(108)
			else:
				for element in argv[index0][1::]:
					if element == 'v':
						argb[0] = True
					elif element == 'a':
						argb[1] = True
					elif element == 'h':
						argb[2] = True
					elif element == 'D':
						argb[3] = True
					elif element == 'd':
						argb[8] = True
					elif len(argv) - index0 - index1 > 1:
						if element == 'p':
							args_two(4, 104); index1 += 1
							file_path = argv[index0 + index1]
						elif element == 'A':
							args_two(5, 105); index1 += 1
							alph = args_three(argv[index0 + index1])
						else:
							error_args(106)
					else:
						error_args(103)
			if index1 > 0:
				index0, index1 = index0 + index1, 0
		elif len(argv) - index0 > 2:
			args_two(6, 107)
			nind[0] = index0
			index0 += 2
		else:
			error_args(101)
		index0 += 1

	for index in range(0, 3):
		if argb[index]:
			print(argo[index])
			argb[7] = True
	if argb[7] or not argb[6]:
		exit()

	if not path.exists(file_path):
		print("No alphabet file")
		exit(200)

	notation[0] = args_int(argv[nind[0]], 113)
	notation[1] = args_int(argv[nind[0] + 2], 114)

	if notation[0] < 2 or notation[1] < 2:
		print("notation < 2")
		exit(400)

	alphabet = alphabet_file(alph[0])
	alphabet += tuple(alphabet[0].lower().splitlines())
	if len(alph) == 2 and alph[0] != alph[1]:
		alphabet += alphabet_file(alph[1]); nind[2] = 2

	if notation[0] > len(alphabet[nind[1]]) or notation[1] > len(alphabet[nind[2]]):
		print("notation > len alphabet")
		exit(401)

	uncov(); conv(); print(out)
	if argb[8]:
		out_f0()
	if argb[3]:
		if not argb[8]:
			out_f0()
		print("Input size =", len(argv[nind[0] + 1]))
		print("Out size =", len(out))
		print("Input =", out_f1(0, argv[nind[0] + 1]));
		print("Out =", out_f1(1, out));

if __name__ == "__main__":
	main()