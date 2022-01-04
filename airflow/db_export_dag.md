# About db_export_dag.py

It exports live run dag information from Airflow meta-database and load into csv file, then csv file is used to load into redshift database.

### Task to do:
- Create ETL DAG for each MWAA environment to export csv and load into redshift database
- Use **S3ToRedshiftOperator** to load file into table
- Used AWS documentation to export airflow dag details





