
conda create -n dp_env3 python=3.5 bokeh seaborn jupyter ipywidgets pyodbc teradata pandas pyodbc python-dateutil 
#Python 3.5

source activate dp_env3
#only work in bash; to enter dp_environment
#and add /prod/user/sam/$LOB/$USER/python/conda_envs/dp_env/bin to PATH in .bashrc
#in this environment packages can be added easily.


conda create env
#create virtual environment
source activate env
