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
 - **Clusters**: set of computers to execute code from **notebook** on **table**.
 
Databricks enables the separation of notebooks and clusters. One creates notebooks and saves in workspace; one creates clusters to run the notebooks; these notebooks can be attached to (and detached from) any cluster created.


## To install package (on cluster)

```bash
%sh /databricks/python/bin/pip install package_name
```

## To 
