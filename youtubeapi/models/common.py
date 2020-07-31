from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json
@dataclass
class Thumbnail:
    url: Optional[str] = field(default=None)
    width: Optional[int] = field(default=None, repr=False)
    height: Optional[int] = field(default=None, repr=False)


@dataclass_json
@dataclass
class Thumbnails:
    default: Optional[Thumbnail] = field(default=None)
    medium: Optional[Thumbnail] = field(default=None, repr=False)
    high: Optional[Thumbnail] = field(default=None, repr=False)
    standard: Optional[Thumbnail] = field(default=None, repr=False)
    maxres: Optional[Thumbnail] = field(default=None, repr=False)


@dataclass_json
@dataclass
class BaseResource:
    kind: Optional[str] = field(default=None)
    etag: Optional[str] = field(default=None, repr=False)
    id: Optional[str] = field(default=None)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PageInfo:
    total_results: Optional[int] = field(default=None)
    results_per_page: Optional[int] = field(default=None)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BaseApiResponse:
    kind: Optional[str] = field(default=None)
    etag: Optional[str] = field(default=None, repr=False)
    next_page_token: Optional[str] = field(default=None, repr=False)
    prev_page_token: Optional[str] = field(default=None, repr=False)
    page_info: Optional[PageInfo] = field(default=None, repr=False)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceId:
    kind: Optional[str] = field(default=None)
    video_id: Optional[str] = field(default=None)
    channel_id: Optional[str] = field(default=None)
    playlist_id: Optional[str] = field(default=None)
