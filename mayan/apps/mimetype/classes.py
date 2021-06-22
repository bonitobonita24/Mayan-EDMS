import logging

from django.utils.module_loading import import_string

from .settings import setting_backend, setting_backend_arguments

logger = logging.getLogger(name=__name__)


class MIMETypeBackend:
    @staticmethod
    def get_backend_instance():
        return import_string(dotted_path=setting_backend.value)(
            **setting_backend_arguments.value
        )

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        return self._init(**kwargs)

    def _init(self, **kwargs):
        """Option method for subclasses to overload."""

    def get_mimetype(self, file_object, mimetype_only=False):
        return self._get_mimetype(
            file_object=file_object, mimetype_only=mimetype_only
        )
