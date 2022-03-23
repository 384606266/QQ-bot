from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.ariadne.event.mirai import NudgeEvent
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

channel.name("Nudge")
channel.description("对戳一戳的反应")
channel.author("maicha")

@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def nudged(app: Ariadne, event: NudgeEvent):
    if event.context_type == "group":
        await app.sendGroupMessage(event.group_id, MessageChain.create("别戳我，好痒"))

