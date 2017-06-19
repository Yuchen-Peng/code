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

### dbutils.fs: to access DBFS
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

### To run stored notebook

```sh
%run "/Users/path/notebook_name"
```

## Spark dataframe

### To read data from S3 (bucket policy need to be added in AWS console) as a spark dataframe

First let's read a parquet format table.
```python
df = spark.read.parquet('s3a://s3_bucket_name/path/filename')  
```

Some descriptive code:
```python
df.head(k) # the first k records 
df.show(k) # the first k row, prettier look
df.printSchema() # prints out the schema for the DataFrame, the data types for each column and whether a column can be null
df.count() # return the number of rows
display(df) # print the dataframe as a table
df.columns
df.select('category_col').distinct().show(k) # show (top k) different categories in a column
df.select('category_col').distinct().count() # count number of different categories in a column
```

To read csv format table one needs to specify the schema of the table. Spark enables automatical schema infer by looking at the table, by setting the argument ```inferSchema=Ture``` (which takes time for big table).

```python
# to read csv
# Set "header=True" so the first row would be read in as header
df = spark.read.csv('s3a://s3_bucket_name/path/filename.csv', inferSchema=True, header=True) 
```

One can pass a user defined schema to the ```read.csv``` so that Spark won't infer the schema. 

```python
import pyspark.sql.types as typ
fields = [
typ.StructField('MODEL_NAME', typ.StringType(), True),
typ.StructField('SCORE_NAME', typ.StringType(), True),
typ.StructField('REPORT_LEVEL', typ.StringType(), True),
typ.StructField('BMM_SEGMENT', typ.StringType(), True),
typ.StructField('CUSTOM_BUCKET', typ.IntegerType(), True),
typ.StructField('PROD_BUCKET_START', typ.IntegerType(), True),
typ.StructField('PROD_BUCKET_END', typ.IntegerType(), True),
typ.StructField('METRIC_INCLUDE', typ.IntegerType(), True)
]

schema = typ.StructType(fields)
df = spark.read.csv('s3a://s3_bucket_name/path/filename.csv', schema=schema, inferSchema=False, header=True) 
```

In practice, the best way to read a big table is to create a small sample and infer the schema using the sample table, and pass the inferred schema when reading the big table.

```python
import json
df_sample = spark.read.csv('s3a://s3_bucket_name/path/sample_table.csv', inferSchema=True, header=True) 
schema_json = df_sample.schema.json()
schema = typ.StructType.fromJson(json.loads(schema_json))
df = df = spark.read.csv('s3a://s3_bucket_name/path/big_table.csv', schema=schema, inferSchema=False, header=True) 
```

To write dataframe to S3
```python
df.write.format("csv").option("header","true").save("s3a://path/table.csv")
df.write.parquet("s3a://path/table.parquet")
```

One can also partition a big table into pieces by a certain column
```python
df_part = df.repartition("col_bkt")
df_part.write.partitionBy('col_bkt').parquet("s3a://path/table.parquet")
```

### To aggregate

```python
apps_by_date_df = (apps_df.
    select('DATE_APPLICATION_RECEIVED', 'APPLICATION_ID').             # transformation
    groupBy('DATE_APPLICATION_RECEIVED').                              # transformation
    agg({'APPLICATION_ID':'count'}).                                   # transformation
    orderBy('count(APPLICATION_ID)', ascending=False).                 # transformation
    show(31)                                                           # action
)
```

### To subset: filter, order by

```python
apps_df_fico = apps_df.filter(apps_df['APP_AVG_FICO']>700)
display(apps_df_fico.orderBy('APP_AVG_FICO', ascending=False))
```

### Create SQL table
```python
df.createOrReplaceTempView("sql_table")
%sql select * from sql_table limit 10;   # we can run SQL now
```

### Dataframe vs. Redshift
