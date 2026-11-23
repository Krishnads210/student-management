import logging


def setup_logger():
    logging.basicConfig(
        filename="student.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("sms")


logger = setup_logger()  # other modules: from sms.logger import logger