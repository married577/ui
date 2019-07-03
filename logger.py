import logging,time,os
log_path = 'f:\\logs'


class Log:
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' %time.strftime("%y_%m_%d_%H_%M_%S"))
        # 创建一个logger
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __console(self, level, message):
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        # 给日志添加handle
        self.logger.addHandler(fh)
        # 创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 避免日志重复输出
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    log = Log()
    log.info('--测试开始--')
    log.debug('--debug测试--')
    log.warning('--警告测试--')
    log.error('--错误测试--')

