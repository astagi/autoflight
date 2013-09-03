#! /usr/bin/env python
#
# autoflight.py
#
# Created by Andrea Stagi (stagi.andrea at gmail dot com)
#
# A simple script to upload a given .apk or .ipa to testflight.
#
# -------------------------------------------------------------------------

import requests, json, sys, os.path

url = 'http://testflightapp.com/api/builds.json'

print ""
print "+++++++++++++++++++++++++++"
print "+      =.4UTOFLIGHT=      +"
print "+++++++++++++++++++++++++++"
print ""

if len(sys.argv) == 1:
    print "Usage: ./autoflight.py my_apk_or_ipa_path"
    exit(0)
if len(sys.argv) == 2:
    build_file = sys.argv[1]

if not os.path.exists(build_file):
    print "Error! %s file doesn't exist" % build_file
    exit(0)
config_file = "config.json"

print "Reading configuration..."
if os.path.exists(config_file):
    json_file_content = open(config_file, "r").read()
else:
    print "Error! config.json file doesn't exist"
    exit(0)
params = json.loads(json_file_content)
if not 'notes' in params:
    params['notes'] = raw_input("Release Notes - What's new in this build? \n> ")
print "Uploading file..."
files = {'file': open(build_file, 'rb')}
req = requests.post(url=url, data=params, files=files)
print req.text