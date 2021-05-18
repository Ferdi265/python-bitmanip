from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("bitmanip/version.py", "r") as f:
    exec(f.read(), globals())

setup(
    name = "bitmanip",
    description = "bit manipulation functions based on the RISC-V BitManip extension",
    version = __version__,
    author = "Ferdinand Bachmann",
    author_email = "theferdi265@gmail.com",
    packages = ["bitmanip"],
    entry_points = {},
    python_requires = ">=3.5",
    install_requires = requirements
)
