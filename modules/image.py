import httpx
import asyncio

from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.twilight import Twilight, FullMatch, WildcardMatch
from graia.ariadne.app import Ariadne
from graia.ariadne.model import Group
from graia.ariadne.message.element import Plain, Image

channel = Channel.current()
port = 8443

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        inline_dispatchers=[
            Twilight(
                {
                    "tag1": WildcardMatch(optional=True),
                    "header": FullMatch("涩图"),
                    "tag2": WildcardMatch(optional=True),
                },
            )
        ],
    )
)

async def main(app: Ariadne, group: Group, message: MessageChain, tag1: WildcardMatch, tag2: WildcardMatch):
    if tag1.matched or tag2.matched:
        tag = (
            tag1.result.getFirst(Plain).text
            if tag1.matched
            else tag2.result.getFirst(Plain).text
        )
        #定义图片内容敏感度
        if "r18" in message:
            san = 6
        elif "r16" in message:
            san = 4
        else:
            san = 2

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
            await app.sendGroupMessage(group, MessageChain.create([
                Plain("慢一点慢一点，别冲辣！"),
                Image(url = "https://www.dmoe.cc/random.php")
            ]))

    
    else:       
        san = 2
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"https://api.a60.one:{port}/?num=5&san={san}"
            )
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
        else:
            await app.sendGroupMessage(group, MessageChain.create([
                Plain("慢一点慢一点，别冲辣！"),
                Image(url = "https://www.dmoe.cc/random.php")
            ]))
'''
#主API修改后改用下面的API
async def Alternative(app: Ariadne, group: Group, message: MessageChain):
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