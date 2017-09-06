brew install gcc --without-multilib    
git clone --recursive https://github.com/dmlc/xgboost 

cd <directory>/xgboost
cd make

# uncomment these two line in make/config.mk
# export CC = gcc
# export CXX = g++

cd <directory>/xgboost
cp make/config.mk .
make -j4

cd <directory>/xgboost/python-package
sudo python setup.py install

