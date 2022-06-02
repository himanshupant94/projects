import os
import psycopg2
import psycopg2.extras
import sys
import boto3
import base64
import json
from botocore.exceptions import ClientError




def lambda_handler(event, context):
  schema=os.environ.get('schema')
  secret_id=os.environ.get('secret_id')
  secret=get_secret(secret_id)

  
  REDSHIFT_QUERY = "SELECT TRIM(pgnsp.nspname) AS schema_name,\
       TRIM(pgci.relname) AS table_name,\
       TRIM(pgt.tableowner) AS table_owner,\
       TRUNC(pgci.relcreationtime) AS creation_date,\
       DATEDIFF(day, pgci.relcreationtime, getdate()) AS daysOld\
       FROM pg_class_info pgci\
       LEFT JOIN pg_namespace pgnsp ON pgci.relnamespace = pgnsp.oid\
       JOIN pg_tables pgt ON pgt.tablename = pgci.relname\
       WHERE pgci.reltype != 0\
       AND   TRIM(pgnsp.nspname) = 'scratch'\
       AND DATEDIFF(day, pgci.relcreationtime, getdate()) > '30'\
       ORDER BY 5 DESC"\

  
  try:
    conn = psycopg2.connect(
      dbname=os.environ.get('db'),
      user=secret['username'],
      password=secret['password'],
      port=secret['port'],
      host=secret['host'])
      
  except Exception as ERROR:
    print("Connection Issue: " + str(ERROR))
    sys.exit(1)

  try:
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cursor=conn.cursor()
    cursor.execute(f"truncate {schema}.retention_tables_hist")
    cursor.execute(REDSHIFT_QUERY)
    records = cursor.fetchall()
    for row in records:
      cursor.execute(f"""INSERT INTO {schema}.retention_tables_hist(schema_name,table_name,table_owner,creation_date,daysold) VALUES (%s, %s, %s, %s, %s)""",row)
      conn.commit()
      
    cursor.close()
    conn.commit()
    conn.close()
  except Exception as ERROR:
    print("Execution Issue: " + str(ERROR))
    sys.exit
  
    



def get_secret(secret_id):

    secret_name = secret_id
    region_name = "us-east-1"
    print(secret_name)

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS key.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            print(decoded_binary_secret)
    return json.loads(secret)
    

