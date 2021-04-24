# -*- coding: UTF-8 -*-
# author: yuanpx
from wrapper.case_level import CaseLevel


def caselevel(level=CaseLevel.HIGH):
    def warpper(fun):
        def _warpper(*args, **kwargs):
            if level:
                fun(*args, **kwargs)

        return _warpper

    return warpper