#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Black = 0,
#Red = 1,
#Green = 2,
#Yellow = 3,
#Blue = 4,
#Magenta = 5,
#Cyan = 6,
#White = 7
DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3

_log_level = 0
def debug(*arg):
    if(_log_level > DEBUG):
        return
    print("%c[%d;%dm" % (0x1B, 0, 32), end='')
    print(*arg)
    print("%c[0;m" % (0x1B), end='')
def info(*arg):
    if(_log_level > INFO):
        return
    print("%c[%d;%dm" % (0x1B, 0, 36), end='')
    print(*arg)
    print("%c[0;m" % (0x1B), end='')
def warn(*arg):
    if(_log_level > WARN):
        return
    print("%c[%d;%dm" % (0x1B, 0, 33), end='')
    print(*arg)
    print("%c[0;m" % (0x1B), end='')
def error(*arg):
    if(_log_level > ERROR):
        return
    print("%c[%d;%dm" % (0x1B, 0, 31), end='')
    print(*arg)
    print("%c[0;m" % (0x1B), end='')
def set_log_level(log_level):
    global _log_level 
    _log_level = log_level
def get_log_level():
    global _log_level
    return _log_level

if __name__ == "__main__":
    debug("debug msg")
    info("info msg")
    warn("warn msg")
    error("error msg")
    print(get_log_level())
    set_log_level(WARN)
    print(get_log_level())
    debug("debug msg")
    info("info msg")
    warn("warn msg")
    error("error msg")

