
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)

class RepositoryAppConfig(AppConfig):
    name = "vorgang.repository"
    label = "repositorty"

    verbose_name = "Vorgang23 :: Repository"

    def ready(self):
        """Application is ready"""
        logger.info("Initializing app: {}".format(self.name))


