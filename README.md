# AtCoder

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FResend1298%2FAtCoder%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&logo=python)
![GitHub License](https://img.shields.io/github/license/Resend1298/AtCoder)

![Accepted Count](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fkenkoooo.com%2Fatcoder%2Fatcoder-api%2Fv3%2Fuser%2Fac_rank%3Fuser%3DThrottle7915&query=%24.count&label=Accepted%20Count&color=5cb85c)

This repository contains my personal solutions to problems from [AtCoder](https://atcoder.jp/).

All solutions are implemented in Python.
Unless it is explicitly mentioned at the beginning of the file that submit using PyPy is necessary,
all solutions are accepted when submitted using CPython.

## Setup

This repository uses [uv](https://docs.astral.sh/uv/) for Python package and environment management.

```shell
paru -S uv # or your preferred installation method depending on your environment
git clone https://github.com/Resend1298/AtCoder.git
cd AtCoder
uv sync
```

Now you can run the code in this repository.

```shell
uv run ABC/123/example.py
```

## Dependencies

- [sortedcontainers](https://grantjenks.com/docs/sortedcontainers/)
- [tqdm](https://tqdm.github.io/)

## License

This repository is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
