from dataclasses import dataclass, field
from typing import Optional, List

from dataclasses_json import dataclass_json, LetterCase, DataClassJsonMixin

from .common import Thumbnails, BaseResource, BaseApiResponse, ResourceId


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PlaylistItemSnippet(DataClassJsonMixin):
    channel_id: Optional[str] = field(default=None)
    channel_title: Optional[str] = field(default=None)
    playlist_id: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None)
    position: Optional[int] = field(default=None)
    resourceId: Optional[ResourceId] = field(default=None, repr=False)


@dataclass_json
@dataclass
class PlaylistItem(BaseResource):
    snippet: Optional[PlaylistItemSnippet] = field(default=None, repr=False)


@dataclass
class PlaylistItemListResponse(BaseApiResponse):
    items: Optional[List[PlaylistItem]] = field(default=None, repr=False)
