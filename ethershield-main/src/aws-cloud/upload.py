import os
import time
import boto3
from botocore.exceptions import NoCredentialsError

# === USER CONFIGURATION ===
local_log_folder = "/var/log/"              # Log folder to watch
bucket_name = "whiteguardbucket1"           # S3 bucket name
s3_folder_prefix = "logs/"                  # S3 folder prefix
poll_interval = 60                          # How often to check (in seconds)

# Keep track of already uploaded files
uploaded_files = set()

# Initialize S3 client
s3_client = boto3.client('s3')

def upload_logs_to_s3(local_folder, bucket, s3_prefix):
    for root, _, files in os.walk(local_folder):
        for filename in files:
            if not filename.endswith(".log"):
                continue  # Only upload .log files

            local_path = os.path.join(root, filename)

            # Skip if already uploaded
            if local_path in uploaded_files:
                continue

            relative_path = os.path.relpath(local_path, local_folder)
            s3_key = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            try:
                print(f"Uploading {local_path} to s3://{bucket}/{s3_key}...")
                s3_client.upload_file(local_path, bucket, s3_key)
                uploaded_files.add(local_path)
            except NoCredentialsError:
                print("AWS credentials not found. Run 'aws configure' first.")
                return
            except Exception as e:
                print(f"❌ Failed to upload {filename}: {e}")

if __name__ == "__main__":
    print(f"📡 Watching '{local_log_folder}' for .log files every {poll_interval} seconds...")
    while True:
        upload_logs_to_s3(local_log_folder, bucket_name, s3_folder_prefix)
        time.sleep(poll_interval)
