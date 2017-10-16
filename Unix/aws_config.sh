#install git
sudo yum install -y git

#proxy, in case needed
curl https://github.com/peng19880925/code/blob/master/Unix/aws_proxies.sh >> ~/proxies.sh
echo "source ~/proxies.sh" >> ~/.bash_profile

source ~/.bash_profile

proxy_on

#tool (yum is the command for apt-get on AWS linux)
sudo yum list installed | grep wget
sudo yum list installed | grep bzip2

sudo yum install wget
sudo yum install bzip2
sudo yum install nano

#anaconda
#check https://repo.continuum.io/archive/index.html
wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-4.0.0-Linux-x86_64.sh

bash Anaconda3-4.0.0-Linux-x86_64.sh

source ~/.bashrc

which python

#xgboost
sudo yum install gcc gcc-c++ libXt-devel cairo-devel pango-devel pango libpng-devel curl-devel unixODBC-devel python-devel java-1.7.0-openjdk-devel bzip2 --skip-broken

git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; make -j4

#packages
pip install pyodbc==3.0.10 # should work on AWS for Python 3
conda install psycopg2
pip install sqlalchemy-redshift
pip install seaborn

#h2o (add --user after pip might work if other breaks down, e.g. pip install package --user)
pip install requests
pip install tabulate
pip install scikit-learn
pip install http://h2o-release.s3.amazonaws.com/h2o/rel-ueno/1/Python/h2o-3.10.4.1-py2.py3-none-any.whl
pip install h2o --upgrade
conda install pymc3 #py bayesian

import pandas as pd
import xgboost
import pyodbc
import psycopg2
import sqlalchemy
import hubble
import requests
import tabulate
import sklearn
import h2o
import seaborn as sns
