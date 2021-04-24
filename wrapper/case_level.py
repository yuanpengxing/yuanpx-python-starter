# -*- coding: UTF-8 -*-

"""
不同等级case运行总开关，例如：如果 Medium = False 表示所有被标注成Medium等级的case将不会运行，这样做的目的是：如果时间紧急，
可以只跑caselevel为high的case，caselevel为Medium、Low的case置为false以后再跑
"""
class CaseLevel:

    HIGH = True
    Medium = False
    Low = True