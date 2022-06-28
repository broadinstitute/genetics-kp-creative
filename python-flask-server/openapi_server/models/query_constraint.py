# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
# from openapi_server.models.any_type import AnyType
from openapi_server import util

# from openapi_server.models.any_type import AnyType  # noqa: E501

class QueryConstraint(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, _not=False, operator=None, value=None, unit_id=None, unit_name=None):  # noqa: E501
        """QueryConstraint - a model defined in OpenAPI

        :param id: The id of this QueryConstraint.  # noqa: E501
        :type id: str
        :param name: The name of this QueryConstraint.  # noqa: E501
        :type name: str
        :param _not: The _not of this QueryConstraint.  # noqa: E501
        :type _not: bool
        :param operator: The operator of this QueryConstraint.  # noqa: E501
        :type operator: str
        :param value: The value of this QueryConstraint.  # noqa: E501
        :type value: AnyType
        :param unit_id: The unit_id of this QueryConstraint.  # noqa: E501
        :type unit_id: AnyType
        :param unit_name: The unit_name of this QueryConstraint.  # noqa: E501
        :type unit_name: AnyType
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            '_not': bool,
            'operator': str,
            'value': object,
            'unit_id': object,
            'unit_name': object
            # 'value': AnyType,
            # 'unit_id': AnyType,
            # 'unit_name': AnyType
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            '_not': 'not',
            'operator': 'operator',
            'value': 'value',
            'unit_id': 'unit_id',
            'unit_name': 'unit_name'
        }

        self._id = id
        self._name = name
        self.__not = _not
        self._operator = operator
        self._value = value
        self._unit_id = unit_id
        self._unit_name = unit_name

    @classmethod
    def from_dict(cls, dikt) -> 'QueryConstraint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryConstraint of this QueryConstraint.  # noqa: E501
        :rtype: QueryConstraint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this QueryConstraint.

        CURIE of the concept being constrained. For properties defined by the Biolink model this SHOULD be a biolink CURIE. otherwise, if possible, from the EDAM ontology. If a suitable CURIE does not exist, enter a descriptive phrase here and submit the new type for consideration by the appropriate authority.  # noqa: E501

        :return: The id of this QueryConstraint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryConstraint.

        CURIE of the concept being constrained. For properties defined by the Biolink model this SHOULD be a biolink CURIE. otherwise, if possible, from the EDAM ontology. If a suitable CURIE does not exist, enter a descriptive phrase here and submit the new type for consideration by the appropriate authority.  # noqa: E501

        :param id: The id of this QueryConstraint.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this QueryConstraint.

        Human-readable name or label for the constraint concept. If appropriate, it SHOULD be the term name of the CURIE used as the 'id'. This is redundant but required for human readability.  # noqa: E501

        :return: The name of this QueryConstraint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryConstraint.

        Human-readable name or label for the constraint concept. If appropriate, it SHOULD be the term name of the CURIE used as the 'id'. This is redundant but required for human readability.  # noqa: E501

        :param name: The name of this QueryConstraint.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def _not(self):
        """Gets the _not of this QueryConstraint.


        :return: The _not of this QueryConstraint.
        :rtype: bool
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this QueryConstraint.


        :param _not: The _not of this QueryConstraint.
        :type _not: bool
        """

        self.__not = _not

    @property
    def operator(self):
        """Gets the operator of this QueryConstraint.

        Relationship between the database value and the constraint value for the specified id. The operators ==, >, and < mean is exactly equal to, is greater than, and is less than, respectively. The 'matches' operator indicates that the value is a regular expression to be evaluated. If value is a list type, then at least one evaluation must be true (equivalent to OR). This means that the == operator with a list acts like a SQL 'IN' clause. The 'not' property negates the operator such that not and == means 'not equal to' (or 'not in' for a list), and not > means <=, and not < means >=, and not matches means does not match. The '==' operator SHOULD NOT be used in a manner that describes an \"is a\" subclass relationship for the parent QNode.  # noqa: E501

        :return: The operator of this QueryConstraint.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this QueryConstraint.

        Relationship between the database value and the constraint value for the specified id. The operators ==, >, and < mean is exactly equal to, is greater than, and is less than, respectively. The 'matches' operator indicates that the value is a regular expression to be evaluated. If value is a list type, then at least one evaluation must be true (equivalent to OR). This means that the == operator with a list acts like a SQL 'IN' clause. The 'not' property negates the operator such that not and == means 'not equal to' (or 'not in' for a list), and not > means <=, and not < means >=, and not matches means does not match. The '==' operator SHOULD NOT be used in a manner that describes an \"is a\" subclass relationship for the parent QNode.  # noqa: E501

        :param operator: The operator of this QueryConstraint.
        :type operator: str
        """
        allowed_values = ["==", ">", "<", "matches"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this QueryConstraint.

        Value of the attribute. May be any data type, including a list. If the value is a list and there are multiple items, at least one comparison must be true (equivalent to OR). If 'value' is of data type 'object', the keys of the object MAY be treated as a list. A 'list' data type paired with the '>' or '<' operators will encode extraneous comparisons, but this is permitted as it is in SQL and other languages.  # noqa: E501

        :return: The value of this QueryConstraint.
        :rtype: AnyType
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this QueryConstraint.

        Value of the attribute. May be any data type, including a list. If the value is a list and there are multiple items, at least one comparison must be true (equivalent to OR). If 'value' is of data type 'object', the keys of the object MAY be treated as a list. A 'list' data type paired with the '>' or '<' operators will encode extraneous comparisons, but this is permitted as it is in SQL and other languages.  # noqa: E501

        :param value: The value of this QueryConstraint.
        :type value: AnyType
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def unit_id(self):
        """Gets the unit_id of this QueryConstraint.

        CURIE of the units of the value or list of values in the 'value' property. The Units of Measurement Ontology (UO) should be used if possible. The unit_id MUST be provided for (lists of) numerical values that correspond to a quantity that has units.  # noqa: E501

        :return: The unit_id of this QueryConstraint.
        :rtype: AnyType
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this QueryConstraint.

        CURIE of the units of the value or list of values in the 'value' property. The Units of Measurement Ontology (UO) should be used if possible. The unit_id MUST be provided for (lists of) numerical values that correspond to a quantity that has units.  # noqa: E501

        :param unit_id: The unit_id of this QueryConstraint.
        :type unit_id: AnyType
        """

        self._unit_id = unit_id

    @property
    def unit_name(self):
        """Gets the unit_name of this QueryConstraint.

        Term name that is associated with the CURIE of the units of the value or list of values in the 'value' property. The Units of Measurement Ontology (UO) SHOULD be used if possible. This property SHOULD be provided if a unit_id is provided. This is redundant but recommended for human readability.  # noqa: E501

        :return: The unit_name of this QueryConstraint.
        :rtype: AnyType
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this QueryConstraint.

        Term name that is associated with the CURIE of the units of the value or list of values in the 'value' property. The Units of Measurement Ontology (UO) SHOULD be used if possible. This property SHOULD be provided if a unit_id is provided. This is redundant but recommended for human readability.  # noqa: E501

        :param unit_name: The unit_name of this QueryConstraint.
        :type unit_name: AnyType
        """

        self._unit_name = unit_name
