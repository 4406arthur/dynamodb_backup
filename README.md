
README
=================

its a backup script(Dynamodb to S3).

requirement
---------
1. dump tool (https://github.com/bchew/dynamodump)
2. s3 python sdk (boto3)
3. python dependency (python2.7,boto2, boto3)
4. setting aws acccess key, secret in ~/.boto

Usage
---------------

for backup
exec : ./run 

for restore
exec : python dynamodump/dynamodump.py -m restore -r us-west-1 -s testTable



