import inspect
import json
import os
from typing import Any

from django.contrib.postgres.fields import JSONField
from django.core import exceptions
from django.db import models
from jsonschema import exceptions as jsonschema_exceptions
from jsonschema import validate

from weirdlywired.helpers.secrets_helper import get_random_key


class BaseModel(models.Model):
    key = models.CharField(max_length=32, unique=True, default=get_random_key)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class JSONSchemaField(JSONField):
    def __init__(self, *args, **kwargs) -> None:
        self.schema = kwargs.pop("schema", None)
        super().__init__(*args, **kwargs)

    @property
    def _schema_data(self):
        model_file = inspect.getfile(self.model)
        dirname = os.path.dirname(model_file)
        p = os.path.join(dirname, self.schema)
        with open(p, "r") as file:
            return json.loads(file.read())

    def _validate_schema(self, value):

        # Disable validaton on fake migration
        if self.model.__module__ == "__fake__":
            return True

        try:
            status = validate(value, self._schema_data)
        except jsonschema_exceptions.ValidationError as e:
            raise exceptions.ValidationError(e.message, code="invalid")

        return status

    def validate(self, value: Any, model_instance: models.Model) -> None:
        super().validate(value, model_instance)
        self._validate_schema(value)

    def pre_save(self, model_instance: models.Model, add: bool) -> Any:
        value = super().pre_save(model_instance, add)
        if value and not self.null:
            self._validate_schema(value)

        return value
