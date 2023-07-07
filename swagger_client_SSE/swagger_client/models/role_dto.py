# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RoleDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'is_type_of': 'object'
    }

    attribute_map = {
        'id': 'id',
        'is_type_of': 'isTypeOf'
    }

    def __init__(self, id=None, is_type_of=None):  # noqa: E501
        """RoleDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._is_type_of = None
        self.discriminator = None
        self.id = id
        self.is_type_of = is_type_of

    @property
    def id(self):
        """Gets the id of this RoleDto.  # noqa: E501


        :return: The id of this RoleDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleDto.


        :param id: The id of this RoleDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_type_of(self):
        """Gets the is_type_of of this RoleDto.  # noqa: E501


        :return: The is_type_of of this RoleDto.  # noqa: E501
        :rtype: object
        """
        return self._is_type_of

    @is_type_of.setter
    def is_type_of(self, is_type_of):
        """Sets the is_type_of of this RoleDto.


        :param is_type_of: The is_type_of of this RoleDto.  # noqa: E501
        :type: object
        """
        if is_type_of is None:
            raise ValueError("Invalid value for `is_type_of`, must not be `None`")  # noqa: E501

        self._is_type_of = is_type_of

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RoleDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RoleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
