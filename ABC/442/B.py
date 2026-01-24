def main():
	q = int(input())

	volume = 0
	playing = False

	for _ in range(q):
		match int(input()):
			case 1:
				volume += 1
			case 2:
				if volume >= 1:
					volume -= 1
			case 3:
				playing = not playing

		if volume >= 3 and playing:
			print("Yes")
		else:
			print("No")


if __name__ == "__main__":
	main()
