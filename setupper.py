from cx_Freeze import setup, Executable
import sys

options = {
'build_exe': {'path': sys.path + ['modules']}
}

exe = [
    Executable(script="INformationProt.py",),
    Executable(script="installer.py")]
setup(
    name="Product",
    version="1.0",
    author="Ivan",
    description="Copyright 2019",
    options = options,
    executables=exe
    )