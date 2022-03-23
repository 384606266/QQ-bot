from pathlib import Path
from graia.ariadne.app import Ariadne
from graia.saya import Saya, Channel
from graia.ariadne.model import Group
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.broadcast.interrupt import InterruptControl
from graia.ariadne.message.element import Plain, Image
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

channel.name("Message")
channel.description("简单的消息回复")
channel.author("maicha")

HOME = Path(__file__).parent

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
    )
)
async def az(app: Ariadne, group: Group, message: MessageChain):
    saying = message.asDisplay()
    if saying == "草":

        await app.sendGroupMessage(group, MessageChain.create([Plain("一种植物（")]))
    if saying == "喜欢":

        await app.sendGroupMessage(group, MessageChain.create([Plain("喜欢")]))
    if saying == "好耶":

        await app.sendGroupMessage(
            group, MessageChain.create([Image(path=HOME.joinpath("haoye.png"))])
        )
    if saying == "流汗黄豆.jpg":
        await app.sendGroupMessage(
            group, MessageChain.create([Image(path=HOME.joinpath("huangdou.jpg"))])
        )