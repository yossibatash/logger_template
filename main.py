import yaml
import logging.config
import logging
from datetime import datetime
import datetime



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Initialize the logger once as the application starts up.
    with open(f"./logger_config.yaml", 'rt') as f:
        logging_config = yaml.safe_load(f.read())
    logging.config.dictConfig(logging_config)

    # Get an instance of the logger and use it to write a log!
    # Note: Do this AFTER the config is loaded above or it won't use the config.
    logger = logging.getLogger()

    try:
        logger.info(f"Start - Application")
        assert 1==0, "Failed"
        logger.info(f"End - Application")
    except Exception as exception_obj:
        logger.error(str(exception_obj), exc_info=True)

