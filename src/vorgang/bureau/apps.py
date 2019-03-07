
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)

class BureauAppConfig(AppConfig):
    name = "vorgang.bureau"
    label = "bureau"

    verbose_name = "Vorgang23 :: Bureau"

    def ready(self):
        """Application is ready"""
        logger.info("Initializing app: {}".format(self.name))


