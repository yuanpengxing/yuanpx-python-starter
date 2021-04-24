# -*- coding: UTF-8 -*-
# author: yuanpx
import requests


def assertHttpGetResponseTextContains(url, expect):
    def wrapper(fun):
        def _wrapper(*args, **kwargs):
            fun(*args, **kwargs)
            actual = requests.get(url).text
            assert expect in actual

        return _wrapper

    return wrapper


def assertHttpGetResponseJsonEqual(url, jsonpath, expect):
    def wrapper(fun):
        def _wrapper(*args, **kwargs):
            fun(*args, **kwargs)
            json = requests.get(url).json()
            actual = json["a"]  # 此处后续完善
            assert expect == actual
            pass

        return _wrapper

    return wrapper
