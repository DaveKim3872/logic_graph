import json
import os

a = [{
    'name':'水果',
    'parentId':'0',
    'id':'10',
    'isLeafe':'0'
    },{
    'name':'甜品',
    'parentId':'0',
    'id':'20',
    'isLeafe':'0'
    },{
    'name':'文具',
    'parentId':'0',
    'id':'30',
    'isLeafe':'0'
    },{
    'name':'香蕉',
    'parentId':'10',
    'id':'1010',
    'isLeafe':'1'
    },{
    'name':'菠萝',
    'parentId':'10',
    'id':'1020',
    'isLeafe':'1'
    }
]

for item in a:
    print(item['name'])
