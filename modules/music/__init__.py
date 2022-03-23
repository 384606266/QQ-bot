import os
import httpx
#from wave_note.music_transcriber import MusicTranscriber
from graia.ariadne.app import Ariadne
from graia.ariadne.model import Group
from graia.ariadne.message.element import Plain, Image,Voice
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.event.message import GroupMessage
from graiax import silkcoder
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.parser.twilight import Twilight, FullMatch, WildcardMatch

channel = Channel.current()

channel.name("Music")
channel.description("通过语音识别乐谱")
channel.author("maicha")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
    ),
)
async def download(app: Ariadne, group: Group, message: MessageChain): 
    '''
    #保存聊天中图片信息
    if message[Image] != []:
        imgs = message[Image]
        print(imgs)
        url = imgs[0].url
        imageId = imgs[0].id
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'download',"imgs")
        file_path = os.path.join(dir_path,"target.img")

        async with httpx.AsyncClient() as client:
            r = await client.get(url)
        with open(file_path,'rb+') as f:
            f.write(r.content)
    '''
    if message[Voice] != []:
        print("get")
        voice = message[Voice]
        url = voice[0].url
        voiceId = voice[0].id
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'wave_note',"examples")
        file_path = os.path.join(dir_path,"target.wav")
        
        async with httpx.AsyncClient() as client:
            voice_resp = await client.get(url)
        voice = voice_resp.content
        #音频文件将以wav格式保存在目录下
        voice = await silkcoder.decode(voice,file_path)
'''
        #由于poetry不兼容libsora,暂时无法直接使用打谱功能
        transcriber = MusicTranscriber(file_path)
        notes, durations = transcriber.transcribe()
        #乐谱文件保存在 wave_note\example 文件夹下

'''
