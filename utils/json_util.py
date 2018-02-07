#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

import json

# json.dumps() python object to json string
# json.loads() json string to python object


def data_to_json(p_data):
    json_string = json.dumps(p_data, sort_keys=True,
                             indent=4, separators=(',', ': '))
    return json_string


def json_to_data(json_data):
    data_string = json.loads(json_data)
    return data_string
