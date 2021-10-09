# nusrets // nusrte
# N Σ O N / ekme peyserrrrrrrrrr

import os

from userbot import bot, CMD_HELP
from userbot.events import register as esebj
from userbot.cmdhelp import CmdHelp 
os.system("pip install moviepy")
import moviepy.editor as m

@esebj(outgoing=True, pattern="^.getaudio(?: |$)(.*)", disable_errors=True)
async def _(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await event.edit("**Səs'ə** `cavab verməlisən.`")
    if "audio" in ureply.document.mime_type:
        await event.edit("`Proses Hazırlanır...`")
        d = os.path.join("resources/extras", "ul.mp3")
        await event.edit("`Yüklənir, Zəhmət Olmasa Gözləyin!`")
        await event.client.download_media(ureply, d)
        await event.edit("`İndi Audio əlavə etmək istədiyiniz videoya cavab verin`")


@esebj(outgoing=True, pattern="^.addaudio(?: |$)(.*)", disable_errors=True)
async def _(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await event.edit("**GİF/Video'ya** `cavab verməlisən.`")
        return
    xx = await event.edit("`Proses Hazırlanır...`")
    ultt = await ureply.download_media()
    ls = os.listdir("resources/extras")
    z = "ul.mp3"
    x = "resources/extras/ul.mp3"
    if z not in ls:
        await event.edit("`Əvvəlcə bir səsə cavab verin`")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("ok.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="ok.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id)

Help = CmdHelp('audiotool').add_info(
    '[N Σ O N](t.me/neonuserbot)\n**Öz adınla yayma! - @esebj**'
).add_command(
    'getaudio',None,'UserBot Audio Faylını Daxilinə Yükləyər.'
).add_command(
    'addaudio',None,"Hər Hansısa Gif / Video Cavablayın Və UserBot Daxilinə Yüklədiyi Musiqi İlə Cavab Verdiyiniz Videonu Editləyib Hazırlayar."
).add()
