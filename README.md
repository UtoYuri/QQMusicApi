# QQMusicApi
QQ音乐API(Python & PHP), 请支持正版音乐，勿滥用
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

### License
TencentMusicApi is under the MIT license.
