#!/usr/bin/env python

from ..common import *
from ..extractor import VideoExtractor
import json

class SoundCloud(VideoExtractor):
    name = "SoundCloud"

    def prepare(self, **kwargs):
        assert self.url or self.vid

        if self.url and not self.vid:
            metadata = get_html('https://api.soundcloud.com/resolve.json?url=' + self.url + '&client_id=02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea')
            info = json.loads(metadata)
            self.title = info["title"]
            self.vid = str(info["id"])
        else:
            if 'title' in kwargs and kwargs['title']:
                self.title = kwargs['title']
            else:
                self.title = self.name + "-" + self.vid

        url = 'https://api.soundcloud.com/tracks/' + self.vid + '/stream?client_id=02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea'

        type, ext, size = url_info(url)

        self.streams['current'] = {'container': ext, 'src': [url], 'size' : size}
        self.stream_types.append('current')
 
site = SoundCloud()
download = site.download_by_url
download_playlist = playlist_not_supported('soundcloud')
