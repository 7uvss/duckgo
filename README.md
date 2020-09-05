# 走鸭 Duck Go Safely 项目介绍

----------

## 开发环境
### 前端
前端部分需要在本地安装 node.js, npm 包管理器以及 yarn 包管理器，在根目录下 ： 

    #安装
    yarn install
    #启动
    yarn serve


### 后端

后端部分需要python3.7以上版本支持，须在本地安装 pip 包管理器，推荐安装 pipenv 作为虚拟环境

```
#安装
cd api
pip install -r requirements.txt
#创建数据库及表（仅首次运行需要）
python manage.py db_create
#启动服务器
python run.py
```

### 接口说明

    '/api/register' 注册
    '/api/login' 登录
    '/api/logout' 登出
    '/api/getlikelist' 获取用户收藏
    '/api/getcommentlist' 获取用户评论
    '/api/geteventlist' 获取活动
    '/api/geteventcomment' 获取活动评论
    '/api/createcomment' 创建评论
    '/api/getusercomment' 获取用户评论


### 数据来源与数据清洗

#### 数据来源：

[大麦网](https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.758523e1NU00KE&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E6%88%90%E9%83%BD)

[摩天轮-票务](https://www.moretickets.com/?utm_source=baidupz-pc&utm_medium=cpt&utm_campaign=logo)

[哔哩哔哩会员购](https://www.baidu.com/link?url=qXjQAUjazBWlV2ZAUemCfoxQd5reyYBE7XH9bvatGSYRkyQDCBvwru7gKDoExY1s&wd=&eqid=f0b3924f000da65c000000025de366a0)

由\api\scrapydata.py程序爬取，导出csv文件\api\damaiwang.csv

#### 数据清洗：

通过[Notepad++](https://www.baidu.com/link?url=3HyDgeJ2tJPpGZXycPKYiF_zPtulwp-xODASJ2Rvuwf1cDYErT50KxmW9BR5aRae&wd=&eqid=e90a0b3c000b25da000000025de367d9)对csv文件进行读取

对不规整的数据采用[正则表达式](https://www.baidu.com/link?url=zg4x5MylyXJOpwzHAev2S9QfeczGnITIwgRFxbCN9DlGfQ8eAWgG7DZNudSZTtdNyZxrLp33JyKdPT8heet6RK&wd=&eqid=b208ff1c0003ff9d000000025de367ac)进行过滤

如对"https://" 或 "http://"等等为开头的url地址

使用正则表达式"/http[s]{0,1}:\/\/([\w.]+\/?)\S*/"即可过滤出想要的内容

数据之间以"|"为分隔，便于后续将csv文件导出为sqlite数据库

#### 导入sqlite数据库

使用sqlitespy.exe运行

```SQL
select * from 表名
into outfile '导出路径\\test.csv'
fields terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n';
```

* 需要注意的是，csv文件的编码方式应为utf-8 with BOM，否则会出现乱码情况



-----------

## 使用
应用根目录即为应用主程序，例如本地环境 http://localhost:8080/ 下，可在未登录的情况下使用部分功能。


### 注册及登录

计划使用手机验证码登录，但因为时间不足没有申请云短信服务，本 demo 暂时取消账号功能，但可以在 http://localhost:8080/register 中查看注册页面，登录可以前往 http://localhost:8080/login 进行登录，提供以下试用账号  

    95432177 888888
    13622737922 888888
    13924336422 888888



### 用户操作与功能备注：

1. 用户进入web端主页，可直接查看附近的活动，通过颜色进行区分
2. 左上角的两个下拉框可进行类别和时间的筛选
3. 用户还可通过搜索功能进行活动的搜索，搜索结果将展示在列表和地图上
   - 上方搜索可正常搜索，但未实装实时弹出
4. 用户点击地图上的标记，可查看活动的具体信息，在登录后可进行收藏、评论和分享等操作
   - 未能填充大量测试评论，地图中间部分紫色标记（筛选选择科技）中 Hackthon 活动内填充了部分评论
   - 评论功能可以实时更新
5. 右上角的头像是用户系统的入口，点击最后一个按钮用户可以查看自己的评论
