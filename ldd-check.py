#!/usr/bin/python
# %%
from pathlib import Path
import subprocess
import sys
# import os
import shutil

# %%
output = ""
try:
    output = subprocess.check_output(
        "ldd " + sys.argv[1], stderr=subprocess.STDOUT, shell=True)
    output = output.decode()
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit(1)
# print results for current executable

# %%
path = Path(sys.argv[1]).resolve().parent
print(path)
MSYS_ROOT = Path('D:/msys64/')
outputlines = output.splitlines()
for exe in outputlines:
    arr = exe.split()
    # breakpoint()
    lib = arr[2]
    if lib.startswith("/mingw64"):
        # print(lib)
        # breakpoint()
        p = Path.joinpath(MSYS_ROOT, lib[1:])
        print(p)
        shutil.copy(p, path)

# %%
