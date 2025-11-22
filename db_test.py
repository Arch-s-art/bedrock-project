import psycopg2
import boto3
import json

# Use the Secrets Manager ARN from Terraform output
secret_arn = "arn:aws:secretsmanager:us-west-2:490555583216:secret:my-aurora-serverless-0FroeE"
region_name = "us-west-2"

# Fetch secret
session = boto3.session.Session()
client = session.client(service_name='secretsmanager', region_name=region_name)

get_secret_value_response = client.get_secret_value(SecretId=secret_arn)
secret = json.loads(get_secret_value_response['SecretString'])

host = secret['host']
port = secret['port']
username = secret['username']
password = secret['password']
database = secret['db']

# Connect to Aurora
try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    print("✅ Connected to Aurora Serverless!")

    # Test query
    cursor.execute("SELECT NOW();")
    print("Current DB Time:", cursor.fetchone()[0])

except Exception as e:
    print("❌ Connection failed:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
