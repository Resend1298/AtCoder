def main():
	q = int(input())

	playing = False
	volume = 0

	for _ in range(q):
		match int(input()):
			case 1:
				volume += 1
			case 2:
				volume -= 1
				volume = max(0, volume)
			case 3:
				playing = not playing

		if playing and volume >= 3:
			print("Yes")
		else:
			print("No")


if __name__ == "__main__":
	main()
