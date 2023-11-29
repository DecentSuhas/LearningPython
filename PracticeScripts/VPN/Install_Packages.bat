echo off
python -c "import os, sys; print(os.path.dirname(sys.executable))"
if %errorlevel% EQU 0 (
	python Install_package.py
) else (
	echo python is not installed in this system
)
pause