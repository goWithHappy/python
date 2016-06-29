#将两种配置文件都统一读到config.py中
from heapq import merge

from MyWebsite.www import config_default, config_override

configs=config_default.configs

#先不尝试读取生产环境下的配置文件
# try:
#     configs=merge(configs,config_override.configs)
# except ImportError:
#     pass
