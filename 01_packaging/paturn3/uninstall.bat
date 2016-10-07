SET PACKAGENAME=fifilib
SETLOCAL
cat report.txt | xargs rm -rf
python setup.py clean --all
pip uninstall -y %PACKAGENAME%
pip list | grep -i %PACKAGENAME%
ENDLOCAL
rem cd tests
rem test.bat
rem cd ..
pause
