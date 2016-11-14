
README
=================

its a backup script(Dynamodb to S3)

extend (https://github.com/bchew/dynamodump) lib.

requirement
---------

1. python dependency (python2.7, boto2, boto3)
2. setting aws acccess key, secret in ~/.boto

Usage
---------------
suggest use python virtualenv

update your s3 info in sync.py

update your table name in run script


for backup
exec : ./run 

for restore
exec : python dynamodump/dynamodump.py -m restore -r us-west-1 -s testTable



