export LOB="/us/card/cca/non_npi"
export USER="eid"
mkdir /prod/user/sam/$LOB/$USER/python
mkdir /prod/user/sam/$LOB/$USER/python/conda_envs
conda config --add envs_dirs /prod/user/sam/$LOB/$USER/python/conda_envs
conda create -n dp_env python=3.5 bokeh seaborn jupyter ipywidgets pyodbc teradata pandas pyodbc python-dateutil 
#Python 3.5

source activate dp_env
#only work in bash; to enter dp_environment
#and add /prod/user/sam/$LOB/$USER/python/conda_envs/dp_env/bin to PATH in .bashrc
#in this environment packages can be added easily.


conda create env
#create virtual environment
source active env
