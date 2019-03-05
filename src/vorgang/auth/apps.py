
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)

class AuthAppConfig(AppConfig):
    name = "vorgang.auth"
    label = "vorgang_auth"

    verbose_name = "Vorgang23 :: Authentication"

    def ready(self):
        """Application is ready"""
        logger.info("Initializing app: {}".format(self.name))


