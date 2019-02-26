# QQMusicApi
QQMusicAPI(Python & PHP), do not abuse and support genuine please.
- Python 3.0+
- PHP 5.6+

### Function
 - [x] search
 - [x] artist info
 - [x] song info
 - [x] album info
 - [x] playlist
 - [x] source
 - [x] lyric

### Get Started

#### python
```python
# just download the music_api into directory, require it with the correct path.

from music_api import MusicAPI

# Initialize
api = MusicAPI()

# Get data
result = api.search('baby')
# result = api.artist('003CoxJh1zFPpx')
# result = api.detail('001icUif3vTGcO')
# result = api.album('002rBshp4WPAut')
# result = api.playlist('801491460')
# result = api.url('001icUif3vTGcO')
# result = api.lyric('001icUif3vTGcO')

# return JSON, just use it
print(json.loads(result))
```

#### php, fork from [metowolf/TencentMusicApi](https://github.com/metowolf/TencentMusicApi)
```php
# just download the TencentMusicAPI.php into directory, require it with the correct path.

require_once 'TencentMusicAPI.php';

# Initialize
$api = new TencentMusicAPI();

# Get data
$result = $api->search('hello');
// $result = $api->artist('003CoxJh1zFPpx');
// $result = $api->detail('001icUif3vTGcO');
// $result = $api->album('002rBshp4WPAut');
// $result = $api->playlist('801491460');
// $result = $api->url('001icUif3vTGcO');
// $result = $api->lyric('001icUif3vTGcO');

# return JSON, just use it
var_dump(json_decode($result));

```

### TODO
#### album list
```
# headers
Origin: https://y.qq.com
Referer: https://y.qq.com/portal/album_lib.html

# api
https://u.y.qq.com/cgi-bin/musicu.fcg?
format=json
data={
    "albumlib":
    {
        "method":"get_album_by_tags",
        "param":
        {
            "area":1,
            "company":-1,
            "genre":-1,
            "type":-1,
            "year":-1,
            "sort":2,
            "get_tags":1,
            "sin":0,
            "num":20,
            "click_albumid":0
        },
        "module":"music.web_album_library"
    },
    "comm":
    {
        "ct":24,
        "cv":0
    }
}
# album area
data.albumlib.param.area
values: 1:内地 0:港台 3:欧美 15:韩国 14:日本 4:其他

# offset
data.albumlib.param.sin

# limit
data.albumlib.param.num

# whether reture album tags
data.albumlib.param.get_tags
values: 0:disable 1:enable
```

### License
TencentMusicApi is under the MIT license.
