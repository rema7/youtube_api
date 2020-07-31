from typing import Union, List

from apiclient.discovery import build

from .models.channel import ChannelListResponse
from .models.playlist import PlaylistResponse
from .models.playlist_item import PlaylistItemListResponse
from .models.videos import VideoListResponse


class Api:
    def __init__(self, api_key):
        self.client = build(
            'youtube',
            'v3',
            developerKey=api_key
        )

    def get_channel_by_id(self, channel_id) -> Union[ChannelListResponse, None]:
        request = self.client.channels().list(
            part="snippet",
            id=channel_id,
        )
        response = request.execute()
        return ChannelListResponse.from_dict(response)

    def get_channel_by_username(self, username) -> Union[ChannelListResponse, None]:
        request = self.client.channels().list(
            part="snippet",
            username=username,
        )
        response = request.execute()
        return ChannelListResponse.from_dict(response)

    def get_channel_playlists(
            self, channel_id, limit: int = 50,
            next_page_token=None,
            prep_page_token=None
    ) -> Union[PlaylistResponse, None]:
        request = self.client.playlists().list(
            part="snippet",
            channelId=channel_id,
            maxResults=limit,
            nextPageToken=next_page_token,
            prepPageToken=prep_page_token
        )
        response = request.execute()
        return PlaylistResponse.from_dict(response)

    def get_playlist_items(
            self, playlist_id: str, limit: int = 50,
            next_page_token=None,
            prep_page_token=None
    ) -> Union[PlaylistItemListResponse, None]:
        request = self.client.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=limit,
            nextPageToken=next_page_token,
            prepPageToken=prep_page_token
        )
        response = request.execute()
        return PlaylistItemListResponse.from_dict(response)

    def get_videos(
            self,
            video_ids: Union[List[str], str],
            limit: int = 50,
            part: Union[List[str], str] = 'snippet'
    ) -> Union[VideoListResponse, None]:
        request = self.client.videos().list(
            part=','.join(part) if isinstance(part, list) else part,
            id=','.join(video_ids) if isinstance(video_ids, list) else video_ids,
            maxResults=limit
        )
        response = request.execute()
        return VideoListResponse.from_dict(response)
