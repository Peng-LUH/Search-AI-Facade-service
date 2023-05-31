# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 0.4.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LearningPathCreationDto(object):
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
        'title': 'str',
        'description': 'str',
        'goals': 'list[PathGoalCreationDto]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'goals': 'goals'
    }

    def __init__(self, title=None, description=None, goals=None):  # noqa: E501
        """LearningPathCreationDto - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._description = None
        self._goals = None
        self.discriminator = None
        self.title = title
        if description is not None:
            self.description = description
        self.goals = goals

    @property
    def title(self):
        """Gets the title of this LearningPathCreationDto.  # noqa: E501


        :return: The title of this LearningPathCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LearningPathCreationDto.


        :param title: The title of this LearningPathCreationDto.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this LearningPathCreationDto.  # noqa: E501


        :return: The description of this LearningPathCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LearningPathCreationDto.


        :param description: The description of this LearningPathCreationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def goals(self):
        """Gets the goals of this LearningPathCreationDto.  # noqa: E501


        :return: The goals of this LearningPathCreationDto.  # noqa: E501
        :rtype: list[PathGoalCreationDto]
        """
        return self._goals

    @goals.setter
    def goals(self, goals):
        """Sets the goals of this LearningPathCreationDto.


        :param goals: The goals of this LearningPathCreationDto.  # noqa: E501
        :type: list[PathGoalCreationDto]
        """
        if goals is None:
            raise ValueError("Invalid value for `goals`, must not be `None`")  # noqa: E501

        self._goals = goals

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
        if issubclass(LearningPathCreationDto, dict):
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
        if not isinstance(other, LearningPathCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
