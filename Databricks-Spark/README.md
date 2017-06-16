This repo reviews using databricks

# Apache Spark

Apache Spark is a sophisticated distributed computation framework for executing code in parallel across many different machines. 

# Databricks

Databricks is a managed platform for running Apache Spark. 

## Terminologies:

 - **Workspace**: to save **notebooks** and libraries
 - **Notebook**: to hold cells of code to be executed; including `%[language name]` in the beginning to specify the code in each cell (one can specify a default language when creating a notebook). 
 Notebook reads data from **table**, and needs to be connected to **clusters** to be executed.
 - **Table**: to store data for **notebook** to read, usually in S3.
 - **Clusters**: set of computers to execute code from **notebook** on **table**. Each cluster has a driver node and multiple worker nodes. The driver node reads code and distributes data and tasks to the worker nodes (via Spark). One may enable **autoscaling** so that number of workers could vary based on how many tasks are being executed.
 - **DBFS**: Databricks File System, a file system utility layer on S3 that is installed on Spark cluster. 
 
Databricks enables the separation of notebooks, clusters and data. One creates notebooks and saves in workspace; one creates clusters to run the notebooks; these notebooks can be attached to (and detached from) any cluster created. Data are stored on S3 and can be read to cluster, or be cached to cluster SSD by using DBFS.

### dbutils.fs ##: to access DBFS
e.g. to list files under an S3 folder
```sh
dbutils.fs.ls('s3a://path/folder')
%fs ls 's3a://path/folder'
```
The two lines above are equivalent. By typing ```%fs``` on enables dbutils in that cell.

### To install package (on cluster)

```sh
%sh /databricks/python/bin/pip install package_name
```

## Spark dataframe

### To read data from S3 (bucket policy need to be added in AWS console) as a spark dataframe

```python
df = spark.read.parquet('s3a://s3_bucket_name/path/filename')  # to read parquet
df = spark.read.csv('s3a://s3_bucket_name/path/filename.csv', inferSchema=True, header=True) # to read csv
```
