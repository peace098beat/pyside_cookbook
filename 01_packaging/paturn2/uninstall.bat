SET PACKAGENAME=fifilib
SETLOCAL
cat report.txt | xargs rm -rf
python setup.py clean --all
pip uninstall -y %PACKAGENAME%
pip list | grep -i %PACKAGENAME%
ENDLOCAL
cd tests
test.bat
pause
cd ..
