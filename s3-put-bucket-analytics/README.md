# Lambda Management Console Settings

## Function code
<pre>
Filename: lambda_function.py
Runtime: 2.7
Handler: lambda_function.lambda_handler
</pre>

## Environment variables
<pre>
None set
</pre>

## Tags
<pre>
None set
</pre>

## Execution role
<pre>
Choose an existing role
Existing role: ie-s3-put-bucket-analytics-configuration  (see below for more details of role)
</pre>

## Basic settings
<pre>
Timeout: 5 min
</pre>

## Network
<pre>
No VPC
</pre>

## Debugging and error handling
<pre>
DLQ resource: None
Enable active tracing: not enabled
</pre>

## Concurrency
<pre>
Use unreserved account concurrency
</pre>

## Lambda Trigger
<pre>
CloudWatch Events
Rules name: ie-s3-put-bucket-analytics-configuration
Event Source: Schedule , Fixed rate of 1 Days
</pre>

# Lambda Role and Attached Policy
Policy name: ie-s3-put-bucket-analytics-configuration

ie-s3-put-bucket-analytics-configuration Policy:
<pre>
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "s3:PutAccountPublicAccessBlock",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAllMyBuckets",
                "s3:PutAnalyticsConfiguration",
                "s3:HeadBucket",
                "s3:GetBucketLocation",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::929292782238-us-east-1/*",
                "arn:aws:s3:::929292782238-us-east-2/*",
                "arn:aws:s3:::929292782238-us-west-1/*",
                "arn:aws:s3:::929292782238-us-west-2/*",
                "arn:aws:s3:::929292782238-ap-northeast-1/*",
                "arn:aws:s3:::929292782238-us-east-1",
                "arn:aws:s3:::929292782238-us-east-2",
                "arn:aws:s3:::929292782238-us-west-1",
                "arn:aws:s3:::929292782238-us-west-2",
                "arn:aws:s3:::929292782238-ap-northeast-1"
            ]
        }
    ]
}
</pre>

# Lambda Role Trust relationships 
<pre>
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "s3.amazonaws.com",
          "lambda.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
</pre>

