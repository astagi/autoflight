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
from requests.exceptions import ConnectionError
from optparse import OptionParser

url = 'http://testflightapp.com/api/builds.json'

def main():
    usage = "Usage: %prog [options] my_apk_or_ipa_path"
    parser = OptionParser(usage=usage)
    parser.add_option( "-a", "--api-token", dest="api_token", default="", help="The API token from the testflight website." )
    parser.add_option( "-t", "--team-token", dest="team_token", default="",help="The team token from the testflight website." )
    parser.add_option( "-l", "--distribution-lists", dest="distribution_lists", default="",help="The name of the distribution list in testflight which should have access to this build." )
    parser.add_option( "-n", "--notify", dest="notify", default=False, help="True if the distribution list should be notified for new builds." )
    parser.add_option( "-d", "--notes", dest="notes", default="", help="Your notes for this build." )
    parser.add_option( "-s", "--dsym", dest="dsym", default="", help="iOS ONLY, the zipped .dSYM corresponding to the build.")
    parser.add_option( "-c", "--config-file", dest="config_file", default="", help="Configuration file" )

    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.print_usage()
        exit(0)
    if len(args) == 1:
        build_file = args[0]

    if not os.path.exists(build_file):
        print "Error! %s build file doesn't exist" % build_file
        exit(0)

    if options.dsym and not os.path.exists(options.dsym):
        print "Error! %s dSYM file doesn't exist" % options
        exit(0)

    params = {}
    params['api_token'] = options.api_token
    params['team_token'] = options.team_token
    params['notify'] = options.notify
    params['notes'] = options.notes
    params['distribution_lists'] = options.distribution_lists
    if options.config_file:
        print "Reading configuration..."
        if os.path.exists(options.config_file):
            json_file_content = open(options.config_file, "r").read()
        else:
            print "Error! %s file doesn't exist" % options.config_file
            exit(0)
        params = dict(params.items() + json.loads(json_file_content).items())

    if not 'notes' in params or not params['notes']:
        params['notes'] = raw_input("Release Notes - What's new in this build? \n> ")

    print "Uploading file..."
    files = {'file': open(build_file, 'rb')}
    if options.dsym:
        files['dsym'] = open(options.dsym, 'rb')
    try:
        req = requests.post(url=url, data=params, files=files)
        print req.text
    except ConnectionError:
        print "Connection error. Please try again."

if __name__ == "__main__":
    main()
