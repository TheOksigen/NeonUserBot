from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import bot
import os


@register(
    pattern=".ttf(?: |$)(.*)",
    outgoing=True,
)
async def TextToFile(e):
    ad = e.text[5:]
    yanit = await e.get_reply_message()
    if yanit.text:
        with open(ad, "w") as fayl:
            fayl.write(yanit.message)
        await e.delete()
        await bot.send_file(e.chat_id,
                            ad,
                            force_document=True)
        os.remove(ad)
        return


# --------------------------------------------------------------


@register(
    pattern=r".ftt",
    outgoing=True,
)
@register(
    pattern=r".oxu",
    outgoing=True,
)
@register(
    pattern=r".open",
    outgoing=True,
)
async def FileToText(e):
    await e.delete()
    cavab = e.get_reply_message()
    download = await e.client.download_media(cavab)
    o = open(download, "r")
    r = o.read()
    o.close()
    if len(r) > 4095:
        await e.edit("<b>Məzmun 4 KiloBaytdan çoxdur.</b>",
                     parse_mode="html"
                     )
    else:
        await bot.send_message(
            e.chat_id,
            f"<code>{r}</code>",
            parse_mode="html"
        )
    os.remove(cavab)

# --------------------------------------------------------------
Help = CmdHelp('doc')
Help.add_command('ttf',
                 '<mətn\'ə cavab>',
                 'Telegram mətnini qoyduğunuz adda fayla çevirər.',
                 'ttf <mətn\'ə cavab> test.py')
Help.add_command(
    'oxu | .ftt | .open',
    '<fayl\'a cavab>',
    'Telegram faylını Telegram mətninə çevirər. (Limit 4 KiloBaytdır.)',
    "oxu <fayl'a cavab>")
Help.add()
