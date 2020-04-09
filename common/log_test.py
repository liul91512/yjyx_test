'''
   日志收集方法
'''
# coding:utf-8
import logging

#handdler 输出日志的渠道---指定文件还是控制台

#日志级别:DEBUG、INFO、WARNING、ERROE、CRITICAL(从左到右越来越严重)

def get_logger(nr):
    # 定义一个日志收集器
    logger = logging.getLogger("test_log")
    # 设置级别
    logger.setLevel('INFO')
    # 输出到指定的txt文件
    handler = logging.FileHandler(r"F:\Pyth\YJYX_web_test\result\log_test\log.txt",encoding="utf-8")
    handler.setLevel('INFO')
    # 设置输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # 两者对接
    logger.addHandler(handler)
    logger.info(nr)
    #移除句柄
    logger.removeHandler(handler)

if __name__ == '__main__':
    get_logger("12334")


