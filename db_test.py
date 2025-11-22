import psycopg2
import boto3
import json

# --- Secrets Manager ARN from Stack1 ---
secret_arn = "arn:aws:secretsmanager:us-west-2:490555583216:secret:my-aurora-serverless-edgRd4"
region_name = "us-west-2"

# --- Fetch secret from AWS Secrets Manager ---
try:
    client = boto3.client("secretsmanager", region_name=region_name)
    secret_value = client.get_secret_value(SecretId=secret_arn)
    secret_dict = json.loads(secret_value["SecretString"])
except Exception as e:
    print("❌ Failed to retrieve secret:", e)
    exit(1)

# --- Database connection parameters ---
DB_HOST = secret_dict["host"]
DB_NAME = secret_dict["db"]         # your DB name, "myapp"
DB_USER = secret_dict["username"]   # "dbadmin"
DB_PASSWORD = secret_dict["password"]
DB_PORT = secret_dict["port"]       # usually 5432

# --- Connect to Aurora PostgreSQL ---
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    print("✅ Connection successful!")
except Exception as e:
    print("❌ Connection failed:", e)
    exit(1)

# --- Run a test query ---
try:
    cur = conn.cursor()
    cur.execute("""
        SELECT table_schema || '.' || table_name AS show_tables
        FROM information_schema.tables
        WHERE table_schema='bedrock_integration';
    """)
    tables = cur.fetchall()
    print("Tables in 'bedrock_integration' schema:", tables)
finally:
    cur.close()
    conn.close()
