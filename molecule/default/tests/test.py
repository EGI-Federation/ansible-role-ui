import subprocess

listfile = open("list.txt", "rw")
files = subprocess.call(["repoquery", "--requires", "ui"], stdout=listfile)
packages = listfile.read().splitlines()
print(packages)

for p in packages:
    print(p.rsplit(".")[0])
