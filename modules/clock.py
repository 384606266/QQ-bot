import os
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.saya import Channel
from graia.scheduler import timers
from graia.scheduler.saya.schema import SchedulerSchema
from graia.ariadne.message.element import Voice
from graiax import silkcoder

channel = Channel.current()

channel.name("Clock")
channel.description("日常闹钟")
channel.author("maicha")

#每天9:30点起床闹钟
@channel.use(SchedulerSchema(timers.crontabify("30 9 * * *")))  #分钟, 小时, 月, 日, 周, 秒
async def clock(app: Ariadne):
    await app.sendGroupMessage(921709479, MessageChain.create("早上好"))

#每天9:45语音回复
@channel.use(SchedulerSchema(timers.crontabify("45 9 * * *")))  #分钟, 小时, 月, 日, 周, 秒
async def clock2(app: Ariadne):
    dir_path = os.path.join(os.path.abspath('..'),"voice")
    file_path = os.path.join(dir_path,"kugimiya_clock.mp3")
    audio_bytes = await silkcoder.encode(file_path)
    await app.sendGroupMessage(921709479, MessageChain.create(
        Voice(data_bytes=audio_bytes)
    ))

