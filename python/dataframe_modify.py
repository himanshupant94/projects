import pandas as pd
import sys,os

df = pd.read_csv (r'C:\Users\hpant\Downloads\airflow.models.dagrun.DagRun (8).csv')  #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print (df)
print(df.columns)
df=df[['id','start_date','data_interval_end','_state','end_date','last_scheduling_decision','run_id','dag_hash','creating_job_id','dag_id','external_trigger','queued_at','run_type','execution_date','conf','data_interval_start','_sa_instance_state']]
print(df)