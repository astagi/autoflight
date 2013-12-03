Autoflight
==========
A simple script to upload a given .apk or .ipa to testflight.

Usage
-----
Create your config file in your working directory using json format
```
{
    "api_token": "0000F4K30000",
    "team_token": "0000F4K30000",
    "notify": true,
    "distribution_lists": "Internal,QA"
}
```
Then launch
```
$ autoflight my_apk_or_ipa_path --config-file config.json
```
Instead of using a config file, you can specify your parameters from the command line, launch the helper to see all the available options
```
$ autoflight --help
```
-------
Relased under MIT license, Copyright (c) 2013 Andrea Stagi <stagi.andrea@gmail.com>