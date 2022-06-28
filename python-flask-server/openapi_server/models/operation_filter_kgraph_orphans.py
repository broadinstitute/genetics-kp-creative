# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
# from openapi_server.models.any_type import AnyType
from openapi_server import util

# from openapi_server.models.any_type import AnyType  # noqa: E501

class OperationFilterKgraphOrphans(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, parameters=None):  # noqa: E501
        """OperationFilterKgraphOrphans - a model defined in OpenAPI

        :param id: The id of this OperationFilterKgraphOrphans.  # noqa: E501
        :type id: str
        :param parameters: The parameters of this OperationFilterKgraphOrphans.  # noqa: E501
        :type parameters: AnyType
        """
        self.openapi_types = {
            'id': str,
            'parameters': object
            # 'parameters': AnyType
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters'
        }

        self._id = id
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'OperationFilterKgraphOrphans':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationFilterKgraphOrphans of this OperationFilterKgraphOrphans.  # noqa: E501
        :rtype: OperationFilterKgraphOrphans
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this OperationFilterKgraphOrphans.


        :return: The id of this OperationFilterKgraphOrphans.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperationFilterKgraphOrphans.


        :param id: The id of this OperationFilterKgraphOrphans.
        :type id: str
        """
        allowed_values = ["filter_kgraph_orphans"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this OperationFilterKgraphOrphans.


        :return: The parameters of this OperationFilterKgraphOrphans.
        :rtype: AnyType
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this OperationFilterKgraphOrphans.


        :param parameters: The parameters of this OperationFilterKgraphOrphans.
        :type parameters: AnyType
        """

        self._parameters = parameters
