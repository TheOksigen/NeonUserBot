import asyncio
import os
import time
from datetime import datetime
from userbot.modules.upload_download import progress
from userbot import TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(pattern=r"^\.c (mp3|ses)(?: |$)(.*)", outgoing=True)
async def _(event):
    if not event.reply_to_msg_id:
        await event.edi("**Mesaja cavab ver.** ❌")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("**Musiqiyə cavab ver.** 🎵")
        return
    input_str = event.pattern_match.group(1)
    event = await event.edit("**Hazırlanır...** ⏳")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await event.client.download_media(
            reply_message, TEMP_DOWNLOAD_DIRECTORY, progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to download")
            ),
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(
            "{} // {}".format(downloaded_file_name, ms)
        )
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "ses":
            new_required_file_caption = "." + str(round(time.time())) + ".ogg"
            new_required_file_name = (
                TEMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name,
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "mp3":
            new_required_file_caption = "." + str(round(time.time())) + ".mp3"
            new_required_file_name = (
                TEMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name,
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("not supported")
            os.remove(downloaded_file_name)
            return
        process = await asyncio.create_subprocess_exec(
            *command_to_run,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            force_document = False
            await event.client.send_file(
                entity=event.chat_id,
                file=new_required_file_name,
                allow_cache=False,
                silent=True,
                force_document=force_document,
                voice_note=voice_note,
                supports_streaming=supports_streaming,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(new_required_file_name)
            await event.delete()

Help = CmdHelp("convert")
Help.add_command("c ses", None, "Mp3/Mp4(Video) və s. səs'ə çevirər.")
Help.add_command("c mp3", None, "Səs/Mp4(Video) Mp3'ə çevirər.")
Help.add()
