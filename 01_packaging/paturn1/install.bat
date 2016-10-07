rem pip uninstall -y ffp2
python setup.py clean --all
python setup.py build   --force
python setup.py install --record report.txt --force
pip list | grep -i ffp2
python setup.py test
