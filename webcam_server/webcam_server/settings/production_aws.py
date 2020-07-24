from .production import *
import os


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'django-static-assets-prospect'
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_CUSTOM_DOMAIN = '{}.s3.{}.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME,)

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

#this is where collectstatic will look to store files
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
