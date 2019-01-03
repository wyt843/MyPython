# -*-coding=utf-8-*-
import logging

# 不设置 默认级别是Warning，所以Debug，Info级别不输出
# filename 文件名称及路径
# filemode 文件模式
# format   日志格式
# datefmt  时间格式
# level    级别
# stream
LOG_FORMAT = "%(asctime)s====%(levelname)s====%(message)s"  #日志格式
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        #时间格式
logging.basicConfig(level=logging.DEBUG,filename="logging.log",
                    format=LOG_FORMAT,datefmt=DATE_FORMAT)
logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")

# 另一种新式
logging.log(logging.DEBUG,"this is a debug log")
logging.log(logging.INFO,"this is a info log")
logging.log(logging.WARNING,"this is a warning log")
logging.log(logging.ERROR,"this is a error log")
logging.log(logging.CRITICAL,"this is a critical log")


