import jsonschema
import json

schema=json.load(open('../schema/siglist-01.json'))
test_data=json.load(open('../data/siglist-01.json'))

result=jsonschema.validate(test_data,schema)

if result==None:
	print "Valid test data and schema"
else:
	print result

