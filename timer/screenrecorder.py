# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from utils.commandlineutils import CommandLineUtils
from utils.screenshot import take

import sys


def main():
    command_line_params = CommandLineUtils.parser(sys.argv[1:])
    if 'period' not in command_line_params:
        raise Exception('period cant null')
    scheduler = BlockingScheduler()
    scheduler.add_job(take, 'interval', seconds=int(command_line_params.get('period')), id='screenshots')
    scheduler.start()


main()
