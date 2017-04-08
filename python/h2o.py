#import H2o package
import h2o
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.grid.grid_search import H2OGridSearch
 
#Initial h2o
h2o.init()

#Example code to read data: the build and validation sample
from h2o.utils.shared_utils import _locate # private function. used to find files within h2o git project directory.
val = h2o.import_file(path=_locate("/home/ec2-user/build.csv"))
build = h2o.import_file(path=_locate("/home/ec2-user/validation.csv"))
 
#input variable list
input_var=['var1',
'var2',
'var3',
'var4',
'var5',
'var6',
'var7']
 
#target variable name
target=['target']
 
#To use target as enum type or factor type
build['target'] = build['target'].asfactor()
val['target'] = val['target'].asfactor()
 
#These are the fixed parameters and not the search criteria; could be also be set in the hyper parameters section
search_criteria={
    'sample_rate': 0.5,
    'col_sample_rate': 0.15,
    'distribution' : "bernoulli",
    'nbins': 100,
    'stopping_metric': "logloss",
    'stopping_tolerance': 0.001,
    'seed': 1625318,
              }
 
#Hyper parameters
hyper_params={
    'max_depth': [2,3,4,5],
        'ntrees': [1000, 2000],
        'learn_rate': [0.05, 0.04, 0.03, 0.02, 0.01],             
        'min_rows': [8000, 4000,800]
              }
#GBM gridsearch
grid_search = H2OGridSearch(H2OGradientBoostingEstimator, hyper_params, search_criteria)
grid_search.train(x=input_var, y=target, training_frame=build, validation_frame=val)
 
#List all the models and their hyper parameters, sorted by their performance (AUC) on the validation sample
auc_table = grid_search.sort_by('auc(valid=True)',increasing=False)
 
#Change the h2o table to pandas dataframe and output it to a csv file
auc_table_pd=auc_table.as_data_frame()
auc_table_pd.to_csv('/home/ec2-user/gridsearch.csv', index=False)
