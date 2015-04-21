#!/usr/bin/python3

import jsonschema
import json
import os
import unittest


class TestJsonSchemaS(unittest.TestCase):

    def testSchemas(self):
        here = os.path.dirname(__file__)
        schemas = [
            ('addressid', '01'),
            ('outbailmentid', '01'),
            ('outputlist', '01'),
            ('seriesid', '01'),
            ('siglist', '01'),
            ('withdrawalstatus', '01')]
        for name, version in schemas:
            schema_file = os.path.join(
                here, '../schema/' + name + '-' + version + '.json')
            data_file = os.path.join(
                here, '../data/' + name + '-' + version + '.json')
            with open(schema_file) as fd:
                schema = json.load(fd)
            with open(data_file) as fd:
                test_data = json.load(fd)
            error = None
            try:
                jsonschema.validate(test_data, schema)
            except Exception as exc:
                error = exc

            self.assertIsNone(
                error, "Error validating %s against %s: %s" % (schema_file,
                    data_file, error))
