# -*-coding=utf-8-*-
import logging
import logging.handlers
import datetime

# 获取logger
logger = logging.getLogger()
# 设置logger 默认日志级别
logger.setLevel(logging.DEBUG)

# Handler	                                描述
# logging.StreamHandler	                    将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
# logging.FileHandler	                    将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
# logging.handlers.RotatingFileHandler	    将日志消息发送到磁盘文件，并支持日志文件按大小切割
# logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
# logging.handlers.HTTPHandler	            将日志消息以GET或POST的方式发送给一个HTTP服务器
# logging.handlers.SMTPHandler	            将日志消息发送给一个指定的email地址
# logging.NullHandler	                    该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。


# 创建一个按照时间切割的处理器
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7)
#设置日志格式
rf_handler.setFormatter(logging.Formatter("%(asctime)s--%(levelname)s--%(message)s"))

# 创建处理器
f_handler = logging.FileHandler('error.log')
# 设置日志级别
f_handler.setLevel(logging.ERROR)
#设置日志格式
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

#添加过滤器
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

#log 输出消息
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
