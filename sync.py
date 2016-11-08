import boto3
import os

def sync_to_s3(target_dir, aws_region, bucket_name):
    if not os.path.isdir(target_dir):
        raise ValueError('target_dir %r not found.' % target_dir)

    s3 = boto3.resource('s3', region_name=aws_region)

    for dirName, subdirList, fileList in os.walk(target_dir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            s3.Object(bucket_name,dirName+'/'+fname).put(Body=open(os.path.join(dirName, fname), 'rb'))

target_dir = 'dump/'
aws_region = 'YOUR S3 INFO'
bucket_name = 'YOUT S3 INFO'

sync_to_s3(target_dir,aws_region,bucket_name )
