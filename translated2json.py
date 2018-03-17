#!/usr/bin/env python3

import json
import io
from pprint import pprint

fh = open('translated.json', 'rb')
orig_list = json.load(fh)

ID_DESC = 'description'
ID_MSG = 'message'

out_dict = {}
for item in orig_list:
    out_dict[item['id']] = {ID_MSG: item[ID_MSG]}
    if (ID_DESC in item) and item[ID_DESC].strip():
        out_dict[item['id']][ID_DESC] = item[ID_DESC]

# https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
#pprint(out_dict)

with io.open('sorted_trans.json', 'w', encoding='utf8') as json_file:
    data = json.dumps(out_dict, ensure_ascii=False, sort_keys=True, indent=2)
    json_file.write(data)
