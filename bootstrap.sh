unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
  # build for linux using lib
  echo 'Retrieving dependencies for Linux'
  sudo apt-get update
  sudo apt-get install gfortran libopenblas-dev liblapack-dev
  sudo update-alternatives --set libblas.so.3 \
    /usr/lib/atlas-base/atlas/libblas.so.3
  sudo update-alternatives --set liblapack.so.3 \
    /usr/lib/atlas-base/atlas/liblapack.so.3
  sudo apt-get install build-essential python-pip python-dev python-setuptools \
   python-numpy python-scipy \
   libatlas-dev libatlas3gf-base python-sklearn

  sudo pip install -U numpy scipy scikit-learn
elif [[ "$unamestr" == 'Darwin' ]]; then
  echo 'Retrieving dependencies for Mac OSX'

  # build numpy from source due to issues with pip
  cd lib/numpy-1.9.1; python setup.py install --prefix=$HOME/.pyenv/versions/ml; cd ../..

  # use my virtualenv's pip to install the rest
  $HOME/.pyenv/versions/ml/bin/pip install -U -r requirements.txt
fi
