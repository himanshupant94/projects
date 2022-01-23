# About db_export_dag.py

It exports live run dag information from Airflow meta-database and load into csv file, then csv file is used to load into redshift database.

### Task to do:
- Create ETL DAG in MWAA environment to export csv and load into redshift database
- Use **S3ToRedshiftOperator** to load files into tables
- Use **XCOM** to push and pull values from other task.
- Used AWS documentation to export airflow dag details: [Click here](https://docs.aws.amazon.com/mwaa/latest/userguide/samples-dag-run-info-to-csv.html)




