from dataclasses import dataclass, field
from typing import Optional, List

from dataclasses_json import dataclass_json, LetterCase, DataClassJsonMixin

from .common import BaseApiResponse, BaseResource, Thumbnails


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ChannelSnippet(DataClassJsonMixin):
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    custom_url: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None)


@dataclass_json
@dataclass
class Channel(BaseResource):
    snippet: Optional[ChannelSnippet] = field(default=None, repr=False)


@dataclass_json
@dataclass
class ChannelListResponse(BaseApiResponse):
    items: Optional[List[Channel]] = field(default=None, repr=False)
