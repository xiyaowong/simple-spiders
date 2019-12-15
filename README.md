# simple-spyders
一些乱七八糟的简单的爬虫
---
* B站视频封面
* 抖音无水印视频

#### 都返回一个字典，每个字段返回成功获取到的值，否则就是空
---
```python
from utils import *

_ = bilibili_cover.get(url)
_ = douyin.get(share_url)
```
