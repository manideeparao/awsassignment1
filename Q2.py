import sys
import boto3


bucket_name = sys.argv[0]
path = sys.argv[1]
file_name = path.split('/')[-1]



s3 = boto3.client('s3')

dict = {}
for obj in s3.objects.all():
    subsrc = obj.Object()
    if( obj.key not in dict.keys()):
        dict[obj.key] = []
    dict[obj.key].append(subsrc.version_id)

s3.download_file(bucket_name, file_name, '/' + path, ExtraArgs={'VersionId':dict[file_name][1] })
