from dataclasses import dataclass, field
from typing import Optional, List

from dataclasses_json import dataclass_json, LetterCase, DataClassJsonMixin

from .common import Thumbnails, BaseResource, BaseApiResponse


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlaylistSnippet(DataClassJsonMixin):
    channel_id: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    channel_title: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Playlist(BaseResource):
    snippet: Optional[PlaylistSnippet] = field(default=None, repr=False)


@dataclass
class PlaylistResponse(BaseApiResponse):
    items: Optional[List[Playlist]] = field(default=None, repr=False)
