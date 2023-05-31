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

class NuggetDto(object):
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
        'is_type_of': 'list[str]',
        'language': 'str',
        'processing_time': 'str',
        'presenter': 'str',
        'mediatype': 'str',
        'id': 'float'
    }

    attribute_map = {
        'is_type_of': 'isTypeOf',
        'language': 'language',
        'processing_time': 'processingTime',
        'presenter': 'presenter',
        'mediatype': 'mediatype',
        'id': 'id'
    }

    def __init__(self, is_type_of=None, language=None, processing_time=None, presenter=None, mediatype=None, id=None):  # noqa: E501
        """NuggetDto - a model defined in Swagger"""  # noqa: E501
        self._is_type_of = None
        self._language = None
        self._processing_time = None
        self._presenter = None
        self._mediatype = None
        self._id = None
        self.discriminator = None
        self.is_type_of = is_type_of
        self.language = language
        self.processing_time = processing_time
        if presenter is not None:
            self.presenter = presenter
        if mediatype is not None:
            self.mediatype = mediatype
        self.id = id

    @property
    def is_type_of(self):
        """Gets the is_type_of of this NuggetDto.  # noqa: E501


        :return: The is_type_of of this NuggetDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._is_type_of

    @is_type_of.setter
    def is_type_of(self, is_type_of):
        """Sets the is_type_of of this NuggetDto.


        :param is_type_of: The is_type_of of this NuggetDto.  # noqa: E501
        :type: list[str]
        """
        if is_type_of is None:
            raise ValueError("Invalid value for `is_type_of`, must not be `None`")  # noqa: E501
        allowed_values = ["ANALYZE", "INTRODUCTION", "CONTENT", "EXAMPLE", "EXERCISE", "TEST"]  # noqa: E501
        if not set(is_type_of).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `is_type_of` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(is_type_of) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._is_type_of = is_type_of

    @property
    def language(self):
        """Gets the language of this NuggetDto.  # noqa: E501


        :return: The language of this NuggetDto.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this NuggetDto.


        :param language: The language of this NuggetDto.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def processing_time(self):
        """Gets the processing_time of this NuggetDto.  # noqa: E501


        :return: The processing_time of this NuggetDto.  # noqa: E501
        :rtype: str
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, processing_time):
        """Sets the processing_time of this NuggetDto.


        :param processing_time: The processing_time of this NuggetDto.  # noqa: E501
        :type: str
        """
        if processing_time is None:
            raise ValueError("Invalid value for `processing_time`, must not be `None`")  # noqa: E501

        self._processing_time = processing_time

    @property
    def presenter(self):
        """Gets the presenter of this NuggetDto.  # noqa: E501


        :return: The presenter of this NuggetDto.  # noqa: E501
        :rtype: str
        """
        return self._presenter

    @presenter.setter
    def presenter(self, presenter):
        """Sets the presenter of this NuggetDto.


        :param presenter: The presenter of this NuggetDto.  # noqa: E501
        :type: str
        """

        self._presenter = presenter

    @property
    def mediatype(self):
        """Gets the mediatype of this NuggetDto.  # noqa: E501


        :return: The mediatype of this NuggetDto.  # noqa: E501
        :rtype: str
        """
        return self._mediatype

    @mediatype.setter
    def mediatype(self, mediatype):
        """Sets the mediatype of this NuggetDto.


        :param mediatype: The mediatype of this NuggetDto.  # noqa: E501
        :type: str
        """

        self._mediatype = mediatype

    @property
    def id(self):
        """Gets the id of this NuggetDto.  # noqa: E501


        :return: The id of this NuggetDto.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NuggetDto.


        :param id: The id of this NuggetDto.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(NuggetDto, dict):
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
        if not isinstance(other, NuggetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
