AUTOFLIGHT
==========
A simple script to upload a given .apk or .ipa to testflight.

USAGE
-----
Create your config.json file in your working directory

{
    "api_token": "0000F4K30000",
    "team_token": "0000F4K30000",
    "notify": true,
    "distribution_lists": "Internal,QA"
}

Then launch

$ ./autoflight.py my_apk_or_ipa_path

LICENSE
-------
Relased under MIT license, Copyright (c) 2013 Andrea Stagi <stagi.andrea@gmail.com>