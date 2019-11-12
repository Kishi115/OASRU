# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:48:05 2019

@author: hamza
"""

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)
    
