import boto3
import pymysql
import os
s3_cient = boto3.client('s3')

# Read CSV file content from S3 bucket
def read_data_from_s3(event):
    bucket_name =  "sfly-aws-dwh"
    s3_file_name = "mwaa_status/data-pipeline-v2/files/export/airflow.models.dagrun.DagRun.csv"
    resp = s3_cient.get_object(Bucket=bucket_name, Key=s3_file_name)

    data = resp['Body'].read().decode('utf-8')
    data = data.split("\n")
    return data

def lambda_handler(event, context):
### Define env variable in lambda function & add layer of mysql 
    username=os.environ['username']
    password=os.environ['password']
    hostname=os.environ['hostname']
    port=3306
    db="dwhops"
    conn = None
    try:
        conn = pymysql.connect(host=hostname,port=port,user=username,passwd=password,db=db,connect_timeout=5)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")

    data = read_data_from_s3(event)
    print(data)
    try:
        cur = conn.cursor()
        cur.execute("truncate dwhops.stg_dag_run_oa")
        conn.commit()
    except:
        pass

    with conn.cursor() as cur:
        for row in data: # Iterate over S3 csv file content and insert into MySQL database
            try:
                row = row.replace("\n","").split(",")
                print (">>>>>>>"+str(row))
                #cur.execute('insert into dwhops.stg_dag_run_sf #(sa_instance_state,id,dag_id,start_date,run_id,external_trigger,conf,dag_hash,state,execution_date,end_date,creating_job_id,run_type,last_schedu#ling_decision) values("'+str(emp[1])+'")')
                cur.execute("insert into dwhops.stg_dag_run_oa (sa_instance_state,state,dag_id,start_date,run_id,creating_job_id,run_type,last_scheduling_decision,id,execution_date,end_date,external_trigger,conf,dag_hash) values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)",row)
                conn.commit()
            except:
                continue
        cur.execute("select count(*) from dwhops.stg_dag_run_oa")
        print ("Total records on DB :"+str(cur.fetchall()[0]))
        # Display employee table records
        # for row in cur:
        #     print (row)
    if conn:
        conn.commit()
