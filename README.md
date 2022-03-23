# 基于Mirai-ariadne的QQ-Bot

#### 目前主要功能：

* 每日闹钟 `9:30` 和 `9:45`
* 图片（支持Tag搜索
  * 搜索格式为：“tag1涩图tag2”
* 语音回复（默认为钉宫语音）
* 简单消息回复
* 对富文本消息进行保存（包括语音、图片）
* 对bot事件的响应 （“戳一戳”） 

#### 部署方法：

1. 安装Mirai 

2. 配置Mirai Http模块

   ```shell
   ./mcl --update-package net.mamoe:mirai-api-http --channel stable-v2 --type plugin
   ```

3. 克隆 bot 到本地

   ```shell
   git clone https://github.com/384606266/QQ-bot.git
   ```

4. 安装poetry模块和相关依赖（poetry能提供依赖模块下载和虚拟环境运行）

   * 安装 `poetry`

   ```shell
   # osx / linux / bashonwindows
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   ```shell
   # windows powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

   * 创建虚拟容器

   ```shell
   poetry env use 3.8
   ```

   * 使用虚拟容器安装依赖

   ```shell
   poetry install
   ```

   * 将 `main.py` 文件中的 `app` 信息改写为自己的信息

5. 运行：`poetry run python main.py` 即可启动Bot


#### 效果展示：

<img src=".\src\imgs\show_img1.png" style="zoom:10%;" />

<img src=".\src\imgs\show_img2.png" style="zoom:10%;" />


#### Todo：

1. 扒谱功能由于 `poetry` 不支持 `libsora` 库暂时搁置
2. 数据库功能
3. 复读，日推，打卡 等日常功能 

#### 参考：

(https://github.com/mamoe/mirai)]:**Mirai库**

(https://github.com/GraiaProject/Ariadne)]: **Ariadne框架**

(https://github.com/djkcyl/ABot-Graia)]: **ABot**



##### To do：

1. 增加数据库服务，记录简单问答和本地图片
2. 抽卡模拟（？）



