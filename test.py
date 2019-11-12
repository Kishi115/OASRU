# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:43:35 2019

@author: hamza
"""
'''
# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'my-new-bucket'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print('Bucket {} created.'.format(bucket.name))
'''
import os

print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))