from pathlib import Path
import boto3
import json

# AWS Access Key and Secret
AWS_ACCESS_KEY = ''
AWS_ACCESS_SECRET = ''
dest = input('Date of collection (%MM-%DD-%YYYY): ')
target_dir = "./data/"+dest

# Open json file to populate access key and secret
with open('env/aws_secrets.json','r') as f:
    data = json.load(f)
    
    # Get access key and secret
    AWS_ACCESS_KEY = data['AWS_ACCESS_KEY']
    AWS_ACCESS_SECRET = data['AWS_ACCESS_SECRET']
    
# Authenticate to AWS
s3 = boto3.client('s3', aws_access_key_id = AWS_ACCESS_KEY, 
                  aws_secret_access_key = AWS_ACCESS_SECRET)

bucket_name = 'tbuiailab'

dataPath = [target_dir+f"/{file.stem}.csv" for file in Path(target_dir).glob('*.csv')]

for path in dataPath:
    print("⬆️Uploading %s to AWS S3 bucket\n" % path)
    try:
        s3.upload_file(Filename=path, Bucket=bucket_name, Key=path)
        print("✅Success!\n")
    except:
        print("❌Unsuccessful attempt!\n")
    
    