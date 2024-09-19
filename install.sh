
set -e

if [[ $OSTYPE == 'darwin'* ]]; then
brew install pipx
pipx install --upgrade build 
python3 -m build
pipx install dist/*.whl --force-reinstall
set +e
else
pip3 install --upgrade build 
python3 -m build
pip3 install dist/*.whl --force-reinstall
fi

python3 -c "import edat95"
set +e
