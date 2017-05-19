
README
=================

its a backup script(Dynamodb to S3)

extend (https://github.com/bchew/dynamodump) lib.

requirement
---------
1. python dependency (python2.7, boto2, boto3)
2. setting aws acccess key, secret in ~/.aws/credentials

Setup
---------------

If you need isolate python environment

You should use (virtualenv)[https://virtualenv.pypa.io/en/stable/userguide/]

Install package dependency by pip

```
pip install boto boto3
```

Backup
---------------

update your s3 aws_region and bucket_name in sync.py and make sure you have created the bucket.

for backup which will generate a dump folder with everything under organized by table name SRCTABLE

```
./run REGION SRCTABLE
```

Restore
---------------

#### Caution!! This will delete DESTTABLE and restore data from the dump folder.

```
python dynamodump/dynamodump.py -m restore -r REGION -s SRCTABLE -d DESTTABLE
```



