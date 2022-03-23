import asyncio
import httpx
import requests
import os
#import ffmpy
from io import BytesIO

from graia.ariadne.app import Ariadne
from graia.saya import Saya, Channel
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, Image, At, Voice
from graia.ariadne.model import Group, MiraiSession
from graiax import silkcoder
from graia.ariadne.message.parser.twilight import Twilight, FullMatch, WildcardMatch, Sparkle
from graia.scheduler import timers, GraiaScheduler

port = 8443
img_path = "imgs\img1.png"
app = Ariadne(
    MiraiSession(
        host="http://localhost:8080",
        verify_key="ServiceVerifyKey",
        account=2971724391,
        # 此处的内容请按照实际 MAH 配置来填写
    ),
)
bcc = app.broadcast
sche = app.create(GraiaScheduler)

#支持tag查找的setu功能
@bcc.receiver(
    GroupMessage,
    dispatchers=[
        Twilight(Sparkle(
            {
                "tag1": WildcardMatch(optional=True),
                "header": FullMatch("涩图"),
                "tag2": WildcardMatch(optional=True),
            },
        ))
    ],
)
async def setu(app: Ariadne, group: Group, message: MessageChain, tag1: WildcardMatch, tag2: WildcardMatch):
    
    if tag1.matched or tag2.matched:
        print("match")
        tag = (
            tag1.result.getFirst(Plain).text
            if tag1.matched
            else tag2.result.getFirst(Plain).text
        )
        print("tag:",tag)
        if "r18" in message:
            san = 6
        else:
            san = 4
        print("san:%d" %san)

        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"https://api.a60.one:{port}/get/tags/{tag}?num=5&san={san}"
            )
            #print(f"https://api.a60.one:{port}/get/tags/{tag}?num=5&san={san}")
            res = r.json()
        if res.get("code", False) == 200:
            pic = res["data"]["imgs"][0]
            await app.sendGroupMessage(group, MessageChain.create(
                [
                    Plain(f"ID：{pic['pic']}\n"),
                    Plain(f"NAME：{pic['name']}\n"),
                    Plain(f"SAN: {pic['sanity_level']}\n"),
                    Image(url=pic["url"]),
                ]
            ))
        elif res.get("code", False) == 404:
            await app.sendGroupMessage(
                group, MessageChain.create([Plain("未找到相应tag的色图")])
            )
        else:
            await app.sendGroupMessage(
                group, MessageChain.create([Plain("慢一点慢一点，别冲辣！")])
            )

    
    else:       
        if "r18" in message:
            san = 6
        else:
            san = 4
        print("san:%d" %san)
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"https://api.a60.one:{port}/?num=5&san={san}"
            )
            res = r.json()
        #print("https://api.a60.one:{port}/?num=5&san={san}")
        pic = res["data"]["imgs"][0]
        await app.sendGroupMessage(group, MessageChain.create(
            [
                Plain(f"ID：{pic['pic']}\n"),
                Plain(f"NAME：{pic['name']}\n"),
                Plain(f"SAN: {pic['sanity_level']}\n"),
                Image(url=pic["url"]),
            ]
        ))
'''
#不支持tag查找的随机涩图功能
@bcc.receiver(GroupMessage)
async def wurusai(app: Ariadne, group: Group, message: MessageChain):
    if "涩图" in message:
        await app.sendGroupMessage(group, MessageChain.create([
                Image(url = "https://www.dmoe.cc/random.php")
            ]))
    
    else:
        if "不够涩" in message:
            await app.sendGroupMessage(group, MessageChain.create(["最后一滴了",
                Image(url = "https://www.dmoe.cc/random.php")
            ]))
'''
#语音响应
@bcc.receiver(GroupMessage)        
async def wurusai(app: Ariadne, group: Group, message: MessageChain):        
    if "无路赛" in message:
        audio_bytes = await silkcoder.encode("src\voice\kugimiya_clock.mp3")
        await app.sendGroupMessage(group, MessageChain.create(
            Voice(data_bytes=audio_bytes)
        ))

#对plain文字的反应
@bcc.receiver(GroupMessage)
async def setu(app: Ariadne, group: Group, message: MessageChain):
    if "喜欢" in message:
        await app.sendGroupMessage(group, MessageChain.create("磕到了"))

#对戳一戳的反应
@bcc.receiver(NudgeEvent)
async def getup(app: Ariadne, event: NudgeEvent):
    if event.context_type == "group":
        await app.sendGroupMessage(event.group_id, MessageChain.create("别戳我，好痒"))
    else:
        await app.sendFriendMessage(event.friend_id, MessageChain.create("别戳我，好痒"))


#测试消息内多媒体文件下载
@bcc.receiver(GroupMessage)

async def download(app: Ariadne, group: Group, message: MessageChain): 
    
    if message[Image] != []:
        imgs = message[Image]
        print(imgs)
        url = imgs[0].url
        imageId = imgs[0].id
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'download',"imgs")
        file_path = os.path.join(dir_path,"target.img")
        
        r = requests.get(url)
        with open(file_path,'rb+') as f:
            f.write(r.content)
    
    if message[Voice] != []:
        print("get")
        voice = message[Voice]
        print(voice)
        url = voice[0].url
        voiceId = voice[0].id
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'download',"voice")
        file_path = os.path.join(dir_path,"target.wav")
        
        async with httpx.AsyncClient() as client:
            voice_resp = await client.get(url)
        voice = voice_resp.content
        voice = await silkcoder.decode(voice,file_path)

app.launch_blocking()