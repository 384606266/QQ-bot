import os
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.ariadne.event.message import GroupMessage
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.parser.twilight import Twilight, FullMatch, WildcardMatch
from graia.ariadne.model import Group
from graiax import silkcoder
from graia.ariadne.message.element import Voice

channel = Channel.current()

channel.name("Reply")
channel.description("语音回复")
channel.author("maicha")

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        inline_dispatchers=[Twilight([FullMatch("无路赛")])],
    ),
)
async def wurusai(app: Ariadne, group: Group, message: MessageChain):        
    if "无路赛" in message:
        dir_path = os.path.join(os.path.abspath('.'),"src","voice")
        file_path = os.path.join(dir_path,"kugimiya_wurusai.mp3")
        audio_bytes = await silkcoder.encode(file_path)
        await app.sendGroupMessage(group, MessageChain.create(
            Voice(data_bytes=audio_bytes)
        ))

