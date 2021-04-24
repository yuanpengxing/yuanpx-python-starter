# -*- coding: UTF-8 -*-
import getopt
import sys


class CommandLineUtils:
    @classmethod
    def parser(cls, argv):
        command_line_params = {}
        try:
            # h后面没有冒号，表示后面不带参数; help后面没有等号，表示后面不带参数
            options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])
        except getopt.GetoptError:
            sys.exit()

        for option, value in options:
            if option in ("-h", "--help"):
                print("usage example: I don't want to tell you, hahaha!!!!")
            if option in ("-p", "--period"):
                command_line_params["period"] = value
        return command_line_params
