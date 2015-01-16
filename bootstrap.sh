unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
  # build for linux using lib
  echo 'Linux'
  sudo apt-get install build-essential python-dev python-setuptools \
   python-numpy python-scipy \
   libatlas-dev libatlas3gf-base
elif [[ "$unamestr" == 'Darwin' ]]; then
  echo 'Retrieving dependencies for Mac OSX'

  # build numpy from source due to issues with pip
  cd lib/numpy-1.9.1; python setup.py install --prefix=$HOME/.pyenv/versions/ml; cd ../..

  # use my virtualenv's pip to install the rest
  $HOME/.pyenv/versions/ml/bin/pip install -U -r requirements.txt
fi
