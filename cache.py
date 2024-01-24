import json

import redis

red = redis.Redis(
    host='redis-11660.c323.us-east-1-2.ec2.cloud.redislabs.com',
    port=11660,
    password='2rsRkyLQCBTB9beK5BYeSyRh8MrvmcjB'
)

# dict1 = {'Vasja': 54643, 'Petja': 684351}

# red.set('fintil', 'fff')


# red.set('dict1', json.dumps(dict1))
# converted_dict = json.loads(red.get('dict1'))
#
# print(red.get('var1'))
# print(type(converted_dict))
# print(converted_dict)

# dicttotest = {'key1': 'value1', 'key2': 'value2'}
# red.set('vovakey', json.dumps(dicttotest))
#
# getback = json.loads(red.get('vovakey'))
#
# print(getback)
# print(red.get('vovakey'))

# red.delete('fintil')
print(red.get('Vova'))
print(red.keys())