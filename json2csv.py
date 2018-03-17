#!/usr/bin/env python

import json
import csv

fh = open('messages.json')
msg = json.load(fh)

DESC = 'description'

with open('messages.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'old_msg', 'message', 'old_desc', DESC]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for k in sorted(msg.keys()):
        newdict = {'id': k, 'old_msg': msg[k]['message'], 'message': ''}
        if DESC in msg[k]:
            newdict['old_desc'] = msg[k][DESC]
        writer.writerow(newdict)
