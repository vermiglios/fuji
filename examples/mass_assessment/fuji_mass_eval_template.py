#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import json

# That is a request may look like (from the swagger API)
# curl -X POST "http://localhost:1071/fuji/api/v1/evaluate" -H  "accept: application/json" -H  "Authorization: Basic bWFydmVsOndvbmRlcndvbWFu" -H  "Content-Type: application/json" -d "{\"object_identifier\":\"https://archive.materialscloud.org/record/2021.146\",\"test_debug\":true,\"use_datacite\":true}"

results_folder = './results/'
pids = ['https://doi.org/10.1594/PANGAEA.908011']
# pids = ['10.17605/OSF.IO/GHVKN] # DOI of a dataset with EML schema
# pids = ["https://dataportal.lifewatchitaly.eu/view/urn%3Auuid%3A555b4ef6-7783-4aa1-9e0a-ee84e4446c83"] # same dataset as
# the one with the DOI

# or load pids from a file with one pid per line, which you have to generate beforehand
# with open('dois.txt', 'r') as fileo:
#    pids = fileo.readlines()

fuji_api_url = 'http://localhost:1071/fuji/api/v1/evaluate'
# the Authorization key you get from your running swagger API instance
headers = {
    'accept': 'application/json',
    'Authorization': 'Basic bWFydmVsOndvbmRlcndvbWFu',
    'Content-Type': 'application/json'
}
# metrics identifiers for the rules to be skipped are defined in fuji_server/yaml/metrics_v0.5.yaml
base_request_dict = {'object_identifier': None, 'test_debug': True, 'use_datacite': True,
                     "rule_skip_list": ["FsF-I2-01M",
                                        "FsF-R1-01MD"
                                        ], }

# Store one file per pid for later report creation
for pid in pids:
    req_dict = base_request_dict.copy()
    req_dict['object_identifier'] = pid
    req = requests.post(fuji_api_url, json=req_dict, headers=headers)

    rs_json = req.json()
    res_filename = '{}.json'.format(pid.split('/')[-1])  # depending on the pid you may want to change this
    res_filename_path = os.path.join(results_folder, res_filename)

    with open(res_filename_path, 'w', encoding='utf-8') as fileo:
        json.dump(rs_json, fileo, ensure_ascii=False)
