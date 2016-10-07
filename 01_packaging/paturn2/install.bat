SET PACKAGENAME=fifilib
pip uninstall -y %PACKAGENAME%
python setup.py clean --all
python setup.py build   --force
python setup.py install --record report.txt --force
python setup.py test
cd tests
test.bat
cd ..
pip list | grep -i %PACKAGENAME%
