import asyncio
import httpx

from graia.ariadne.app import Ariadne
from graia.saya import Saya, Channel
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain, Image, At, Voice
from graia.ariadne.model import Group, MiraiSession
from graiax import silkcoder
from graia.ariadne.message.parser.twilight import Twilight, FullMatch, WildcardMatch, Sparkle

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
    print("in")
    if tag1.matched or tag2.matched:
        print("match")
        tag = (
            tag1.result.getFirst(Plain).text
            if tag1.matched
            else tag2.result.getFirst(Plain).text
        )
        print("tag:",tag)
        #替代url：https://www.dmoe.cc/random.php
        if "r18" in message:
            san = 6
        else:
            san = 4
        print("san:%d" %san)

        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"http://api.a60.one:404/get/tags/{tag}?num=5&san={san}"
            )
            print(f"http://api.a60.one:404/get/tags/{tag}?num=5&san={san}")
            res = r.json()

        pic = res["data"]["imgs"][0]
        await app.sendGroupMessage(group, MessageChain.create(
            [
                Plain(f"ID：{pic['pic']}\n"),
                Plain(f"NAME：{pic['name']}\n"),
                Plain(f"SAN: {pic['sanity_level']}\n"),
                Image(url=pic["url"]),
            ]
        ))
    
    else:
        print("match2")
        
        #替代url：https://www.dmoe.cc/random.php
        if "r18" in message:
            san = 6
        else:
            san = 4
        print("san:%d" %san)
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"http://api.a60.one:404/get/tags/?num=5&san={san}"
            )
            res = r.json()
        print("http://api.a60.one:404/get/tags/?num=5&san={san}")
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
    else:
        if "不够涩" in message:
            await app.sendGroupMessage(group, MessageChain.create(["最后一滴了",
                Image(url = "https://www.dmoe.cc/random.php")
            ]))
    '''
@bcc.receiver(GroupMessage)        
async def wurusai(app: Ariadne, group: Group, message: MessageChain):        
    if "无路赛" in message:
        audio_bytes = await silkcoder.encode("voice\dinggong.mp3")
        await app.sendGroupMessage(group, MessageChain.create(
            Voice(data_bytes=audio_bytes)
        ))

@bcc.receiver(GroupMessage)
async def setu(app: Ariadne, group: Group, message: MessageChain):
    if "喜欢" in message:
        await app.sendGroupMessage(group, MessageChain.create("日，磕到了"))

@bcc.receiver(NudgeEvent)

async def getup(app: Ariadne, event: NudgeEvent):
    if event.context_type == "group":
        await app.sendGroupMessage(event.group_id, MessageChain.create("别戳我，好痒"))
    else:
        await app.sendFriendMessage(event.friend_id, MessageChain.create("别戳我，好痒"))

app.launch_blocking()