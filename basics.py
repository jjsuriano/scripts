import sys
import os
import boto3

# SYS MODULE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\nSYS Module", "="*50)

print("\nVERSION", "-"*53)
print(sys.version)

print("\nARGV", "-"*56)
print(sys.argv)

print()

# OS MODULE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\nOS Module", "="*51)

print("\nCWD", "-"*57)
print(os.getcwd())

os.chdir("../")
print("\nCWD", "-"*57)
print(os.getcwd())

"""
Other useful methods:

.remove("path of file") -> removes a file
.mkdir("path where dir will be created") -> makes a directory in the path
.rmdir("path of dir") -> removes the dictionary
.path.join("path1", "path2") -> path2 will be joined to path1
.path.split("path") -> splits the path
.path.exists("path") -> determine if the path exists
"""
print()

# AWS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\nAWS", "="*57)

"""
Run "aws configure" and it will ask for the AWS Access ID and the AWS Secret
Access Key
"""

# # EC2
# ec2 = boto3.resource('ec2')

# # CREATE AN INSTANCE
# instance = ec2.create_instance(
#     ImageId="",
#     MinCount=1,
#     MaxCount=1,
#     InstanceType="",
# )

# print(instance[0].id)

# # DELETE AN INSTANCE
# # instance_id = ""
# instance = ec2.Instance(instance_id)
# response = instance.terminate()

# print(response)

# # S3
# s3 = boto3.resource('s3')

# # CREATE A BUCKET
# name = ""
# try:
#     response = s3.create_bucket(
#         Bucket=name,
#         CreateBucketConfiguration={'LocationContraint': 'us-east-2'},
#     )

#     print(response)
# except Exception as error:
#     print(error)

print()

