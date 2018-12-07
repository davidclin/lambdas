"""
##############################################################################
#
# Author:
#     David Lin 
#
# Description:
#     Create analytics configurations for S3 buckets
#
# Boto3 Docs:
#     https://boto3.amazonaws.com/v1/documentation/api/latest/
#     reference/services/s3.html#S3.Client.put_bucket_analytics_configuration
#
# AWS CLI:
#     aws s3api put-bucket-analytics-configuration --bucket test_bucket
#     --analytics-configuration '{"Id": "report","StorageClassAnalysis":
#     {}}' --id "report"
#
# Variables:
#     bucketname           Source bucket name
#     bucket_location      Source bucket region
#     storage_class_bucket Bucket used to store analytics analysis
#
# Storage Class Buckets:
#     s3-analytics-929292782238-us-east-1
#     s3-analytics-929292782238-us-east-2
#     s3-analytics-929292782238-us-west-1
#     s3-analytics-929292782238-us-west-2
#     s3-analytics-929292782238-ap-northeast-1
#
#############################################################################
"""

import json
import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')

###################################################
# Lambda handler ; This invokes the main() function
###################################################

def lambda_handler(event, context):
    # TODO implement
    main()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
######################################################
# Bucket Analytics Configurations
# 
# This is used to feed in the parameters used by the
# s3 put_bucket_analytics_configuration API utilized
# by the main() function.
######################################################
    
def enable_analytics(bucketname,storage_class_bucket):
    config = {"Id": "report",
              "StorageClassAnalysis": {
                  'DataExport': {
                      'OutputSchemaVersion': 'V_1',
                      'Destination': {
                          'S3BucketDestination': {
                              'Format': 'CSV',
                              'Bucket': 'arn:aws:s3:::' + str(storage_class_bucket),
                              'Prefix': 's3-analysis/' + str(bucketname) + '/' + str(bucketname)}
                        }
                    }
                }
              }

    analytics_config = client.put_bucket_analytics_configuration(
            Bucket=bucketname,
            Id="report",
            AnalyticsConfiguration=config
            )

# Uncomment line below to troubleshoot analytics config
    print analytics_config


'''
################################################################
# The following main() function performs the following tasks:
#   (1) Enables analytics on all buckets
#   (2) Sets storage class bucket in same region as source bucket
#   (3) Sets bucket prefix using bucketname
################################################################
'''

def main():

    for bucket in s3.buckets.all():
    
        bucket_location = client.get_bucket_location(Bucket=bucket.name)
    
        if bucket_location['LocationConstraint'] == None:
            storage_class_bucket = 'toyota-assets-929292782238-us-east-1'
            enable_analytics(bucket.name,storage_class_bucket)            
            print bucket.name , bucket_location['LocationConstraint']
    
        if bucket_location['LocationConstraint'] == 'us-east-1':
            storage_class_bucket = 'toyota-assets-929292782238-us-east-1'
            enable_analytics(bucket.name,storage_class_bucket)            
            print bucket.name , bucket_location['LocationConstraint']
    
        if bucket_location['LocationConstraint'] == 'us-east-2':
            storage_class_bucket = 'toyota-assets-929292782238-us-east-2'
            enable_analytics(bucket.name,storage_class_bucket)
            print bucket.name , bucket_location['LocationConstraint']
    
        if bucket_location['LocationConstraint'] == 'us-west-1':
            storage_class_bucket = 'toyota-assets-929292782238-us-west-1'
            enable_analytics(bucket.name,storage_class_bucket)
            print bucket.name , bucket_location['LocationConstraint']
    
        if bucket_location['LocationConstraint'] == 'us-west-2':
            storage_class_bucket = 'toyota-assets-929292782238-us-west-2'
            enable_analytics(bucket.name,storage_class_bucket)
            print bucket.name , bucket_location['LocationConstraint']
    
        if bucket_location['LocationConstraint'] == 'ap-northeast-1':
            storage_class_bucket = 'toyota-assets-929292782238-ap-northeast-1'
            enable_analytics(bucket.name,storage_class_bucket)
            print bucket.name , bucket_location['LocationConstraint']
