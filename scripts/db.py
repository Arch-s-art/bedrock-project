import psycopg2
import boto3
import json

# -------------------------
# Config: Secrets Manager ARN
# -------------------------
secret_arn = "arn:aws:secretsmanager:us-west-2:490555583216:secret:my-aurora-serverless-mSKubq"
region_name = "us-west-2"

# -------------------------
# Fetch secret from AWS
# -------------------------
client = boto3.client("secretsmanager", region_name=region_name)
secret_value = client.get_secret_value(SecretId=secret_arn)
secret_dict = json.loads(secret_value["SecretString"])

# -------------------------
# Aurora connection params
# -------------------------
DB_HOST = secret_dict["host"]          # Aurora endpoint
DB_USER = secret_dict["username"]      # Master or created user
DB_PASSWORD = secret_dict["password"]  # Password from secret
DB_PORT = int(secret_dict.get("port", 5432))  # Default PostgreSQL port

# Set DB name: either from secret (rarely present) or default/fixed DB
DB_NAME = secret_dict.get("dbname", "myapp")  # Replace "myapp" with your actual DB name if different

# -------------------------
# Connect to Aurora Serverless
# -------------------------
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

# -------------------------
# Example: list tables in schema
# -------------------------
try:
    cur = conn.cursor()
    cur.execute("""
        SELECT table_schema || '.' || table_name AS show_tables
        FROM information_schema.tables
        WHERE table_schema='bedrock_integration';
    """)
    tables = cur.fetchall()
    print("Tables in bedrock_integration schema:", tables)
finally:
    cur.close()
    conn.close()
