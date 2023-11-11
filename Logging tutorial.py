import logging

logging.basicConfig(level=logging.DEBUG, filename="logging", filemode="w",
                    format= "%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")