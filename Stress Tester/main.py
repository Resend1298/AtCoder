SOLVE_FILE = "../ABC/123/A.py"

from itertools import count
from subprocess import run
from sys import executable

from tqdm import tqdm


def main():
	for _ in tqdm(count()):
		with open("test_data.in", 'w') as f:
			run([executable, "gen.py"], stdout=f)

		with open("test_data.in") as f_in, open("test_data_solve.out", 'w') as f_out:
			run([executable, SOLVE_FILE], stdin=f_in, stdout=f_out)
		with open("test_data.in") as f_in, open("test_data_bf.out", 'w') as f_out:
			run([executable, "bf.py"], stdin=f_in, stdout=f_out)

		with open("test_data_solve.out") as f1, open("test_data_bf.out") as f2:
			assert f1.read() == f2.read()


if __name__ == "__main__":
	main()
