conda create -n virtualenv python=3.6 anaconda

source activate virtualenv

conda install -n virtualenv [package_name] # to install new package in virtualenv

source deactivate # to deactivate


# other examples

conda create --name python35 --no-default-packages --no-pin python=3.5

conda create --name python3 python=3
# python3 virtualenv has many packages installed now for python 3
