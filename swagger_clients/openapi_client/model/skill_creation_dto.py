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


class SkillCreationDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "parentSkills",
            "level",
            "nestedSkills",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            level = schemas.NumberSchema
            
            
            class parentSkills(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SkillCreationDto']:
                        return SkillCreationDto
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SkillCreationDto'], typing.List['SkillCreationDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'parentSkills':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SkillCreationDto':
                    return super().__getitem__(i)
            
            
            class nestedSkills(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SkillCreationDto']:
                        return SkillCreationDto
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SkillCreationDto'], typing.List['SkillCreationDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nestedSkills':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SkillCreationDto':
                    return super().__getitem__(i)
            description = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "level": level,
                "parentSkills": parentSkills,
                "nestedSkills": nestedSkills,
                "description": description,
            }
    
    parentSkills: MetaOapg.properties.parentSkills
    level: MetaOapg.properties.level
    nestedSkills: MetaOapg.properties.nestedSkills
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentSkills"]) -> MetaOapg.properties.parentSkills: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nestedSkills"]) -> MetaOapg.properties.nestedSkills: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "level", "parentSkills", "nestedSkills", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentSkills"]) -> MetaOapg.properties.parentSkills: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nestedSkills"]) -> MetaOapg.properties.nestedSkills: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "level", "parentSkills", "nestedSkills", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        parentSkills: typing.Union[MetaOapg.properties.parentSkills, list, tuple, ],
        level: typing.Union[MetaOapg.properties.level, decimal.Decimal, int, float, ],
        nestedSkills: typing.Union[MetaOapg.properties.nestedSkills, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SkillCreationDto':
        return super().__new__(
            cls,
            *_args,
            parentSkills=parentSkills,
            level=level,
            nestedSkills=nestedSkills,
            name=name,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )
