import json
# serialization

data={
    "Name" : 'Max',
    'Age': 16,
    'IsOnline': True
}
# python-->json
# json convert
json_format=json.dumps(data,indent=4)
print(json_format)


#json-->python
# deserialization

json_data='{"Name": "Max","Age": 16,"IsOnline": true}'

python_format=json.loads(json_data)
print(python_format)