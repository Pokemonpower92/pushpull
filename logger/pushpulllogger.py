import logging


class PushPullLogger:
    FORMAT = '%(asctime)s %(module)s %(lineno)d %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT)

    def __init__(self, logger_name: str):
        """
        Initialize the looger.
        :param logger_name: The name of the logger to get.
        :return: the logger.
        """
        self._logger = logging.getLogger(logger_name)

    def info(self, message: str, stacklevel: int) -> None:
        """
        send an info level log.
        :param stacklevel: the stack level the call came from.
        :param message: message to log.
        :return: None
        """
        self._logger.setLevel(logging.INFO)
        self._logger.info(message, stacklevel=stacklevel)

    def error(self, message: str, stacklevel: int) -> None:
        """
        send an error level log.
        :param stacklevel: the stack level the call came from.
        :param message: message to log.
        :return: None
        """
        self._logger.setLevel(logging.ERROR)
        self._logger.error(message, stacklevel=stacklevel)
