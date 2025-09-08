# TODO: review

def main():
	s = input()

	world = int(s[0])
	stage = int(s[2])

	if stage < 8:
		print(f"{world}-{stage + 1}")
	else:
		print(f"{world + 1}-1")


if __name__ == "__main__":
	main()
