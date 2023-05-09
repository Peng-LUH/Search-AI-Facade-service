# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    The version of the OpenAPI document: 0.4.2
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class NuggetCreationDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "isTypeOf",
            "language",
            "processingTime",
        }
        
        class properties:
            
            
            class isTypeOf(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "ANALYZE": "ANALYZE",
                                "INTRODUCTION": "INTRODUCTION",
                                "CONTENT": "CONTENT",
                                "EXAMPLE": "EXAMPLE",
                                "EXERCISE": "EXERCISE",
                                "TEST": "TEST",
                            }
                        
                        @schemas.classproperty
                        def ANALYZE(cls):
                            return cls("ANALYZE")
                        
                        @schemas.classproperty
                        def INTRODUCTION(cls):
                            return cls("INTRODUCTION")
                        
                        @schemas.classproperty
                        def CONTENT(cls):
                            return cls("CONTENT")
                        
                        @schemas.classproperty
                        def EXAMPLE(cls):
                            return cls("EXAMPLE")
                        
                        @schemas.classproperty
                        def EXERCISE(cls):
                            return cls("EXERCISE")
                        
                        @schemas.classproperty
                        def TEST(cls):
                            return cls("TEST")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'isTypeOf':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            language = schemas.StrSchema
            processingTime = schemas.StrSchema
            presenter = schemas.StrSchema
            mediatype = schemas.StrSchema
            __annotations__ = {
                "isTypeOf": isTypeOf,
                "language": language,
                "processingTime": processingTime,
                "presenter": presenter,
                "mediatype": mediatype,
            }
    
    isTypeOf: MetaOapg.properties.isTypeOf
    language: MetaOapg.properties.language
    processingTime: MetaOapg.properties.processingTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isTypeOf"]) -> MetaOapg.properties.isTypeOf: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processingTime"]) -> MetaOapg.properties.processingTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["presenter"]) -> MetaOapg.properties.presenter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mediatype"]) -> MetaOapg.properties.mediatype: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isTypeOf", "language", "processingTime", "presenter", "mediatype", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isTypeOf"]) -> MetaOapg.properties.isTypeOf: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processingTime"]) -> MetaOapg.properties.processingTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["presenter"]) -> typing.Union[MetaOapg.properties.presenter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mediatype"]) -> typing.Union[MetaOapg.properties.mediatype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isTypeOf", "language", "processingTime", "presenter", "mediatype", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        isTypeOf: typing.Union[MetaOapg.properties.isTypeOf, list, tuple, ],
        language: typing.Union[MetaOapg.properties.language, str, ],
        processingTime: typing.Union[MetaOapg.properties.processingTime, str, ],
        presenter: typing.Union[MetaOapg.properties.presenter, str, schemas.Unset] = schemas.unset,
        mediatype: typing.Union[MetaOapg.properties.mediatype, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NuggetCreationDto':
        return super().__new__(
            cls,
            *_args,
            isTypeOf=isTypeOf,
            language=language,
            processingTime=processingTime,
            presenter=presenter,
            mediatype=mediatype,
            _configuration=_configuration,
            **kwargs,
        )
