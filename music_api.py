
from urllib import request
from urllib import parse
import random
import time
import math
import json

# QQ音乐API
class MusicAPI(object):
    # 单例
    __instance = None

    # 请求头
    headers = {
        'User-Agent' : r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.30 Safari/537.36',
        'Referer' : r'http://y.qq.com/portal/player.html',
        'Cookie' : r'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30; ts_last=y.qq.com/portal/player.html;',
    }

    # 参数
    GUID = ''
    KEY = ''
    CDN = ''

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(MusicAPI, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def curl_get(self, url):
        req = request.Request(url, headers = self.headers)
        response = request.urlopen(req).read()
        return response

    def search(self, key, limit=10, offset=0):
        url = 'http://c.y.qq.com/soso/fcgi-bin/search_cp?'
        data = {
            'p' : offset + 1, 
            'n' : limit, 
            'w' : key, 
            'aggr' : 1, 
            'lossless' : 1, 
            'cr' : 1, 
        }
        return self.curl_get(url + parse.urlencode(data))[9:-1].decode('utf-8')

    def artist(self, artist_mid, begin=0, limit=10):
        url = 'http://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?'
        data = {
            'singermid' : artist_mid, 
            'order' : 'listen', 
            'begin' : begin, 
            'num' : limit, 
        }
        return self.curl_get(url + parse.urlencode(data))[0:-1].decode('utf-8')

    def album(self, album_mid):
        url = 'http://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?'
        data = {
            'albummid' : album_mid, 
        }
        return self.curl_get(url + parse.urlencode(data))[1:].decode('utf-8')

    def detail(self, song_mid):
        url = 'http://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?'
        data = {
            'songmid' : song_mid, 
            'format' : 'json', 
        }
        return self.curl_get(url + parse.urlencode(data)).decode('utf-8')

    def url(self, song_mid):
        self.getkey()
        url = 'http://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?'
        data = {
            'songmid' : song_mid, 
            'format' : 'json', 
        }
        data = self.curl_get(url + parse.urlencode(data)).decode('utf-8')
        json_data = json.loads(data)['data'][0]['file']
        # print(json_data)
        types = {
            'size_320mp3' : ('M800','mp3'), 
            'size_128mp3' : ('M500','mp3'), 
            'size_96aac' : ('C400','m4a'), 
            'size_48aac' : ('C200','m4a'), 
            'size_flac' : ('F000','flac'), 
        }
        urls = {}
        for k in types:
            if json_data[k]:
                v = types[k]
                urls[k[5:]] = "%s%s%s.%s?vkey=%s&guid=%s&fromtag=30" % (self.CDN, v[0], json_data['media_mid'], v[1], self.KEY, self.GUID)
        return json.dumps(urls)

    def getkey(self):
        self.GUID = random.randint(1, 2147483647) * (self.microtime(True) * 1000) % 10000000000
        data = self.curl_get('https://c.y.qq.com/base/fcgi-bin/fcg_musicexpress.fcg?json=3&guid=' + str(self.GUID)).decode('utf-8')
        json_data = json.loads(data[13:-2])
        self.KEY = json_data['key']
        # self.CDN = json_data['sip'][0]
        self.CDN = 'http://dl.stream.qqmusic.qq.com/'

    def microtime(self, get_as_float=False) :
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())

    def playlist(self, playlist_id):
        url = 'http://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?'
        data = {
            'disstid' : playlist_id, 
            'utf8' : 1, 
            'type' : 1, 
        }
        return self.curl_get(url + parse.urlencode(data))[13:-1].decode('utf-8')

    def lyric(self, song_mid):
        url = 'http://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg?'
        data = {
            'songmid' : song_mid, 
            'nobase64' : 1, 
        }
        return self.curl_get(url + parse.urlencode(data))[18:-1].decode('utf-8')
