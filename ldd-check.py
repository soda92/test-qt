#!/usr/bin/python
# %%
import os
from pathlib import Path
import subprocess
import sys
# import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-cp", "--copy", help="copy found dll",
                    action="store_true")
parser.add_argument("path", help="program path")
args = parser.parse_args()

# %%
output = ""
try:
    output = subprocess.check_output(
        "ldd " + args.path, stderr=subprocess.STDOUT, shell=True)
    output = output.decode()
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit(1)
# print results for current executable

# %%
path = Path(args.path).resolve().parent
# print(path)

# MSYS_ROOT = Path(os.environ.get('MINGW_PREFIX')).resolve()
MSYS_ROOT = Path(os.environ.get('HOME')).resolve().parent.parent
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
        if args.copy:
            shutil.copy(p, path)

# %%
