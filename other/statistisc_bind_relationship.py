# -*- coding: UTF-8 -*-
# author: yuanpx

class StatisticsBindRelationship:
    @classmethod
    def statistic_bind_relationship1(self, dict, statistics_dict):
        for key, value in dict.items():
            kv = key.strip() + ':' + value.strip()
            if kv in statistics_dict:
                statistics_dict[kv] = statistics_dict[kv] + 1
            else:
                statistics_dict[kv] = 1

    @classmethod
    def statistic_bind_relationship2(self, statistics_dict):
        statistics_f = {}
        for key, value in statistics_dict.items():
            k = str(value)
            if k in statistics_f:
                statistics_f[k] = statistics_f[k] + ', ' + key
            else:
                statistics_f[k] = '' + key
        return statistics_f


arr = [{'a': 'a', 'b': 'b', 'c': 'c'}, {'a': 'a', 'b': 'b', 'c': 'c'}, {'c': 'c', 'd': 'd', 'e': 'e'},
       {'a': 'a', 'b': 'b', 'c': 'c'}, {'c': 'c', 'd': 'd', 'e': 'e'}]
statistics_dict = {}
for d in arr:
    StatisticsBindRelationship.statistic_bind_relationship1(d, statistics_dict)

sd = StatisticsBindRelationship.statistic_bind_relationship2(statistics_dict)
for key, value in sd.items():
    print(key + ' => ' + value)
