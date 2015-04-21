#!/usr/bin/python2

import jsonschema
import json

l = [
    ('addressid', '01'),
    ('outbailmentid', '01'),
    ('outputlist', '01'),
    ('seriesid', '01'),
    ('siglist', '01'),
    ('withdrawalstatus', '01')
    ]

for schema_name, schema_version in l:

    schema_file = '../schema/' + schema_name + '-' + schema_version + '.json'
    data_file = '../data/' + schema_name + '-' + schema_version + '.json'

    schema = json.load(open(schema_file))
    test_data = json.load(open(data_file))

    result = jsonschema.validate(test_data,schema)

    if result is not None:
        print "Error validating %s against %s: %s" % (schema_file, data_file, result)
    else:
        print "Schema %s version %s valid." % (schema_name, schema_version)
