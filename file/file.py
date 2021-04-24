# -*- coding: UTF-8 -*-

# 方式一
f = open('test', 'r')
for line in f.readlines():
    print(line)
f.close()

# 方式二，该方式的好处是自动关流
with open('test', 'r') as f:
    for line in f.readlines():
        print(line)