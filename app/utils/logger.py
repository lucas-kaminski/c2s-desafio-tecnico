import logging

from app.utils.enviroment import is_development_environment


def set_logger():
    logging.basicConfig(
        level=logging.DEBUG if is_development_environment() else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s %(filename)s:%(lineno)d %(funcName)s: %(message)s",
        handlers=[logging.StreamHandler()],
    )

    logging.getLogger("urllib3").setLevel(logging.WARNING)
