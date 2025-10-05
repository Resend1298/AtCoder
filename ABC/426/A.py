def main():
	x, y = input().split()

	versions = {"Ocelot": 1, "Serval": 2, "Lynx": 3}

	if versions[x] >= versions[y]:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
