#set up
sudo pip install --upgrade virtualenv 

virtualenv --system-site-packages targetDirectory # for Python 2.7
virtualenv --system-site-packages -p python3 targetDirectory # for Python 3.n

source ~/tensorflow/bin/activate      # Activate the virtualenv environment (e.g. for tensorflow); If using bash, sh, ksh, or zsh

# this would takes to 
(tensorflow)$ 

# then install packages...

pip install --upgrade tensorflow      # for Python 2.7

# to deactive the virtualenv
 (tensorflow)$ deactivate 

'''
Use conda env
'''

conda create -n tensorflow
source activate tensorflow
 (tensorflow)$  # Your prompt should change
 
(tensorflow)$ pip install --ignore-installed --upgrade $TF_PYTHON_URL

# here TF_PYTHON_URL is the tensorflow URL; e.g. this install tensorflow for CPU only

(tensorflow)$ pip install --ignore-installed --upgrade \
 https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.1.0-py2-none-any.whl
 
 # then start python in virtualenv; import tensorflow, ...
