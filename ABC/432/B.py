def main():
	x = int(input())

	x = list(str(x))
	x = [int(i) for i in x]
	x.sort()

	if x[0] != 0:
		print(''.join(str(i) for i in x))
	else:
		for i in x:
			if i != 0:
				tmp = i
				x.remove(i)
				break
		print(str(tmp) + ''.join(str(i) for i in x))


if __name__ == "__main__":
	main()
