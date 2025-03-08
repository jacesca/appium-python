from loggingPy import CustomLogger as cl


class CustomLoggerDemo:
    LOG = cl.CustomLogger()

    def method_one(self):
        self.LOG.critical("This is a critical msg!")
        self.LOG.error('This is an error msg!')
        self.LOG.warning('This is a warning msg!')
        self.LOG.info('This is an info msg!')
        self.LOG.debug('This is a debug msg')

    def method_two(self):
        m2 = cl.CustomLogger()
        m2.critical('Critical msg!')
        m2.error('Error msg!')
        m2.warning('Warning msg!')
        m2.info('Info msg!')
        m2.debug('Debug msg')


cld = CustomLoggerDemo()
cld.method_one()
cld.method_two()
