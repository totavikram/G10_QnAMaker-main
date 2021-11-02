import logging
import logging.config


class LOGGER:
    root_logger = None

    @staticmethod
    def config():
        FORMATE = '%(asctime)-15s | %(name)s | %(levelname)s | %(message)s'
        formatter = logging.Formatter(FORMATE)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        LOGGER.root_logger = logging.getLogger()
        LOGGER.root_logger.addHandler(stream_handler)
        LOGGER.root_logger.addHandler(file_handler)
        LOGGER.root_logger.setLevel(logging.INFO)
        return LOGGER.root_logger

    @staticmethod
    def get_logger():
        return LOGGER.config() if LOGGER.root_logger is None else LOGGER.root_logger
