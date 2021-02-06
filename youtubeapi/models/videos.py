from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Optional

from dataclasses_json import DataClassJsonMixin
from dataclasses_json import LetterCase
from dataclasses_json import dataclass_json

from .common import BaseApiResponse
from .common import BaseResource
from .common import Thumbnails


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoSnippet(DataClassJsonMixin):
    channel_id: Optional[str] = field(default=None)
    channel_title: Optional[str] = field(default=None)
    category_id: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None)
    tags: Optional[List[str]] = field(default=None)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoStatistics(BaseResource):
    view_count: Optional[int] = field(default=None)
    like_count: Optional[int] = field(default=None)
    dislike_count: Optional[int] = field(default=None, repr=False)
    comment_count: Optional[int] = field(default=None, repr=False)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Video(BaseResource):
    snippet: Optional[VideoSnippet] = field(default=None, repr=False)
    statistics: Optional[VideoStatistics] = field(default=None, repr=False)


@dataclass
class VideoListResponse(BaseApiResponse):
    items: Optional[List[Video]] = field(default=None, repr=False)
