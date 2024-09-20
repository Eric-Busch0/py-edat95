

set -e
if [[ $OSTYPE == 'darwin'* ]]; then

pip3 install --upgrade build --break-system-packages
python3 -m build
pip3 install dist/*.whl --force-reinstall --break-system-packages

else
pip3 install --upgrade build 
python3 -m build
pip3 install dist/*.whl --force-reinstall
fi

python3 -c "import edat95"
set +e
