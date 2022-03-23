import asyncio
import os
import pkgutil

from graia.ariadne.app import Ariadne
from graia.ariadne.model import MiraiSession
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.broadcast import Broadcast
from graia.scheduler import GraiaScheduler
from graia.scheduler.saya.behaviour import GraiaSchedulerBehaviour
from graia.ariadne.adapter import DefaultAdapter

loop = asyncio.new_event_loop()
bcc = Broadcast(loop=loop)
scheduler = GraiaScheduler(loop=loop, broadcast=bcc)

app = Ariadne(
    broadcast=bcc,
    connect_info=DefaultAdapter(
        bcc,
        MiraiSession(
            host="http://localhost:8080",
            verify_key="ServiceVerifyKey",
            account=2971724391,
            # 此处的内容请按照实际 MAH 配置来填写
        ),
    ),
)
#创建saya实例
saya = app.create(Saya)
saya.install_behaviours(
    BroadcastBehaviour(bcc),
    GraiaSchedulerBehaviour(scheduler),
)

'''
with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        if module_info.name.startswith("_"):
            continue
        saya.require("modules." + module_info.name)
'''
with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        if module_info.name.startswith("_"):
            continue
        saya.require("modules." + module_info.name)

if __name__ == "__main__":
    app.launch_blocking()
