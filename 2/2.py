from m import connect, test

import m

print(dir())
settings = {
    'host': '127.0.0.1',
    'port': 123,
    'dbname': 'ad',
    'dbuser': 'ad',
    'passwd': 'ad'
}
z = m.connect(
    **settings
)

z = m.test(
    1,
    2,
    3,
    **{'host': '127.0.0.1',
     'port': 123,
     'dbname': 'ad',
     'dbuser': 'ad',
     'passwd': 'ad'}
)
print(z)
