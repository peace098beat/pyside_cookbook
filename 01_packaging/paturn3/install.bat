SET PACKAGENAME=fifilib
pip uninstall -y %PACKAGENAME%
python setup.py clean --all
python setup.py build   --force
python setup.py install --record report.txt --force
python setup.py test
rem cd tests
rem test.bat
rem cd ..
pip list | grep -i %PACKAGENAME%
pause