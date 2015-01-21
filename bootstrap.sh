unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
  # build for linux using lib
  echo 'Retrieving dependencies for Linux'
  sudo apt-get update

  # Install scikit-learn
  sudo apt-get install build-essential \
    python-pip \
    python-dev \
    python-numpy \
    python-scipy \
    
  sudo pip install -U scikit-learn
elif [[ "$unamestr" == 'Darwin' ]]; then
  echo 'Retrieving dependencies for Mac OSX'
  pip install -U numpy scipy scikit-learn
fi
