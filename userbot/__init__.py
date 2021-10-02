# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License

# Neon User Bot #
""" UserBot hazırlanışı """
#from telethon.tl.functions.phone import GetGroupCallRequest as getvc
#from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.events import callbackquery, InlineQuery, NewMessage
from telethon.tl.functions.channels import JoinChannelRequest
from logging import basicConfig, getLogger, INFO, DEBUG
from telethon.sync import TelegramClient, custom
from telethon.sessions import StringSession
from distutils.util import strtobool as sb
from pylast import LastFMNetwork, md5
from dotenv import load_dotenv
from pySmartDL import SmartDL
from sys import version_info
from requests import get
from re import compile
from math import ceil

import os

load_dotenv("config.env")

# Bot gündeliyi
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

ASYNC_POOL = []

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - @Neonsup - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - @Neonsup - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.info("En az Python 3.6 versiyasına sahib olmalısınız."
              "Birden çox xüsusiyyet buna bağlıdır. Bot söndürülür.")
    quit(1)

CONFIG_CHECK = os.environ.get(
    "___________XAIS_______BU_____SETIRI_____SILIN__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Zehmet olmasa ilk setirdeki yazını config.env faylından silin"
    )
    quit(1)

# Modullar siyahısında olan emojini dəyişə bilmək üçündür.
NEON_STIK = os.environ.get(
    "NEON_STIK") or "🈴 "

# Bot Sahibi
BOTSAHIBI = os.environ.get("BOTSAHIBI",".set var BOTSAHIBI <Istədiyiniz ad> yaza bilərsiniz.")

# Səsli üçün
#async def get_call(event):
 #   mm = await event.client(getchat(event.chat_id))
  #  xx = await event.client(getvc(mm.full_chat.call))
   # return xx.call

# Sudo üçündü
try:
    SUDO_ID = set(int(x) for x in os.environ.get("SUDO_ID", "").split())
except ValueError:
    raise Exception("SUDO_ID qeyd etməmisiniz!")

# Sudonun versiyası
SUDO_VERSION = "v0.5"

# Bot'un dili
LANGUAGE = os.environ.get("LANGUAGE", "AZ").upper()

if not LANGUAGE in ["EN", "TR", "AZ", "UZ", "DEFAULT"]:
    LOGS.info("Namelum dil yazıdnız buna göre AZ dil işledilir.")
    LANGUAGE = "AZ"
    
# Neon Version
NEON_VERSION = "v0.7"

# Owners
OWNERS = [1849828581, 1929222125, 1901206758]

# Telegram API KEY ve HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

SILINEN_PLUGIN = {}
# UserBot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Neon
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))

# NEON
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Hey! Bu bir bot. :)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Yenileme üçün
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)


# Yenileme üçün repo linki
UPSTREAM_REPO_URL = "https://github.com/TheOksigen/neon_userbot.git"


# Konsol gündeliy
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL 
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///neon.db")

# OCR API
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API 
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# AVTO PP
AVTO_PP = os.environ.get("AVTO_PP", None)

# Warn 
WARN_LIMIT = int(os.environ.get("WARN_LIMIT", 3))
WARN_MODE = os.environ.get("WARN_MODE", "gmute")

if not WARN_MODE in ["gmute", "gban"]:
    WARN_MODE = "gmute"

# Qaleriya
QALERIYA_VAXT = int(os.environ.get("QALERIYA_VAXT", 60))

# NeonUserBot
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

PLUGINID = os.environ.get("PLUGIN_CHANNEL_ID", None)
# Plugin İçin
if not PLUGINID:
    PLUGIN_CHANNEL_ID = "me"
else:
    PLUGIN_CHANNEL_ID = int(PLUGINID)

# OpenWeatherMap API
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# Anti Spambot
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Saat & Tarix - Ölke Saat dilimi
COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Temiz qarşılama
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm 
BIO_PREFIX = os.environ.get("BIO_PREFIX", "@NeonUserBot | ")
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive 
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")

# Inline bot 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Genius 
GENIUS = os.environ.get("GENIUS", None)
CMD_HELP = {}
CMD_HELP_BOT = {}
PM_AUTO_BAN_LIMIT = int(os.environ.get("PM_AUTO_BAN_LIMIT", 4))

SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)
SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)

PAKET_ISMI = os.environ.get("PAKET_ISMI", "@NeonUserBot Paketi")

# Avto qatılma
AVTO_QATILMA = sb(os.environ.get("AVTO_QATILMA", "True"))

# Patternler
PATTERNS = os.environ.get("PATTERNS", ".;!,")
WHITELIST = get('https://raw.githubusercontent.com/TheOksigen/neon_userbot/main/whitelist.json').json()

# CloudMail.ru ve MEGA.nz 
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' 
if STRING_SESSION:
    # pylint: devre dışı=geçersiz ad
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: devre dışı=geçersiz ad
    bot = TelegramClient("userbot", API_KEY, API_HASH)

# Sesli sohbet
async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call

if os.path.exists("learning-data-root.check"):
    os.remove("learning-data-root.check")
else:
    LOGS.info("Braincheck faylı yoxdur, getirilir...")

URL = 'https://raw.githubusercontent.com/quiec/databasescape/master/learning-data-root.check'
with open('learning-data-root.check', 'wb') as load:
    load.write(get(URL).content)

async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "Xüsusi xeta gündeliyinin işlemesi üçün BOTLOG_CHATID ayarlanmalıdır.")
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "Günlüye qeyd etme xüsusiyyetinin işlemesi üçün BOTLOG_CHATID ayarlanmalıdır.")
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Hesabınızın BOTLOG_CHATID qrupuna mesaj gönderme yetkisi yoxdur. "
            "Qrup ID'sini doğru yazıb yazmadığınızı yoxlayın.")
        quit(1)
        
if not BOT_TOKEN == None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None

def butonlastir(sayfa, moduller):
    Satir = 5
    Kolon = 2
    
    moduller = sorted([modul for modul in moduller if not modul.startswith("_")])
    pairs = list(map(list, zip(moduller[::2], moduller[1::2])))
    if len(moduller) % 2 == 1:
        pairs.append([moduller[-1]])
    max_pages = ceil(len(pairs) / Satir)
    pairs = [pairs[i:i + Satir] for i in range(0, len(pairs), Satir)]
    butonlar = []
    for pairs in pairs[sayfa]:
        butonlar.append([
            custom.Button.inline("🔸 " + pair, data=f"bilgi[{sayfa}]({pair})") for pair in pairs
        ])

    butonlar.append([custom.Button.inline("◀️ Geri", data=f"sayfa({(max_pages - 1) if sayfa == 0 else (sayfa - 1)})"), custom.Button.inline("İreli ▶️", data=f"sayfa({0 if sayfa == (max_pages - 1) else sayfa + 1})")])
    return [max_pages, butonlar]

with bot:
    if AVTO_QATILMA:
        try:
            bot(JoinChannelRequest("@Neonsup"))
            bot(JoinChannelRequest("@NeonUserBot"))
            bot(JoinChannelRequest("@NeonPlugin"))
        except:
            pass

    moduller = CMD_HELP
    me = bot.get_me()
    uid = me.id
    SAHIBIM = uid

    try:
        @tgbot.on(NewMessage(pattern='/start'))
        async def start_bot_handler(event):
            if not event.message.from_id == uid:
                await event.reply(f'`Salam mən` @NeonUserBot`! Mən sahibimə (`@{me.username}`) kömək etmək üçün varam, yəni sənə kömək edə bilmərəm :( Amma səndə [N Σ O N](https://t.me/NeonSup) User Bot qura bilərsən Dəstək qrupumuza gəl` @Neonsup')
            else:
                await event.reply(f'`N Σ O N User Bot İşləyir🔥`')

        @tgbot.on(InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query == "@NeonUserBot":
                rev_text = query[::-1]
                veriler = (butonlastir(0, sorted(CMD_HELP)))
                result = await builder.article(
                    f"Zəhmət olmasa sadəcə .kömek ilə kömək istəyin.",
                    text=f"**N Σ O N Əla İşləyir 🔥** [N Σ O N User Bot](https://t.me/neonuserbot) __İşləyir...__\n\n**Yüklənən Modul Sayı:** `{len(CMD_HELP)}`\n**Sayfa:** 1/{veriler[0]}",
                    buttons=veriler[1],
                    link_preview=False
                )
            elif query.startswith("http"):
                parca = query.split(" ")
                result = builder.article(
                    "Fayl Yükləndi",
                    text=f"**Fayl uğurla {parca[2]} saytına yükləndi!**\n\nYükləmə Zamanı: {parca[1][:3]} saniyə\n[‏‏‎ ‎]({parca[0]})",
                    buttons=[
                        [custom.Button.url('URL', parca[0])]
                    ],
                    link_preview=True
                )
            else:
                result = builder.article(
                    "@NeonUserBot",
                    text="""@NeonUserBot işlədin
Hesabınızı bot'a çevirə bilərsiz və bunları işlədə bilərsiz. Unutmayın, siz başqasının botunu idarə etməssiniz! Altdakı GitHub adresində bütün qurulum detayları var""",
                    buttons=[
                        [custom.Button.url("Kanal", "https://t.me/neonuserbot"), custom.Button.url(
                            "Qrup", "https://t.me/neonsup")],
                        [custom.Button.url(
                            "GitHub", "https://github.com/TheOksigen/neon_userbot")]
                    ],
                    link_preview=False
                )
            await event.answer([result] if result else None)

        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"sayfa\((.+?)\)")))
        async def sayfa(event):
            if not event.query.user_id == uid: 
                return await event.answer("Hey! Mənim mesajlarımı düzəltməyə çalışma! Özünə bir @NeonUserBot qur.", cache_time=0, alert=True)
            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            veriler = butonlastir(sayfa, CMD_HELP)
            await event.edit(
                f"**N Σ O N Əla İşləyir🔥** [N Σ O N User Bot](https://t.me/neonuserbot) __İşləyir...__\n\n**Yüklənən Modul Sayı:** `{len(CMD_HELP)}`\n**Sayfa:** {sayfa + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"bilgi\[(\d*)\]\((.*)\)")))
        async def bilgi(event):
            if not event.query.user_id == uid: 
                return await event.answer("Hey! Mənim mesajlarımı düzəltməyə çalışma! Özünə bir @NeonUserBot qur..", cache_time=0, alert=True)

            sayfa = int(event.data_match.group(1).decode("UTF-8"))
            komut = event.data_match.group(2).decode("UTF-8")
            try:
                butonlar = [custom.Button.inline("🔹 " + cmd[0], data=f"komut[{komut}[{sayfa}]]({cmd[0]})") for cmd in CMD_HELP_BOT[komut]['commands'].items()]
            except KeyError:
                return await event.answer("❌ Bu modula açıqlama yazılmayıb.", cache_time=0, alert=True)

            butonlar = [butonlar[i:i + 2] for i in range(0, len(butonlar), 2)]
            butonlar.append([custom.Button.inline("◀️ Geri", data=f"sayfa({sayfa})")])
            await event.edit(
                f"**📗 Fayl:** `{komut}`\n**🔢 Komanda Sayı:** `{len(CMD_HELP_BOT[komut]['commands'])}`",
                buttons=butonlar,
                link_preview=False
            )
        
        @tgbot.on(callbackquery.CallbackQuery(data=compile(b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))
        async def komut(event):
            if not event.query.user_id == uid: 
                return await event.answer("Hey! Mənim mesajlarımı düzəltməyə çalışma! Özünə bir @NeonUserBot qur.", cache_time=0, alert=True)

            cmd = event.data_match.group(1).decode("UTF-8")
            sayfa = int(event.data_match.group(2).decode("UTF-8"))
            komut = event.data_match.group(3).decode("UTF-8")

            result = f"**📗 Fayl:** `{cmd}`\n"
            if CMD_HELP_BOT[cmd]['info']['info'] == '':
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⬇️ Rəsmi:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                    result += f"**⚠️ Xəbərdarlıq:** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
                else:
                    result += f"**⬇️ Rəsmi:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
            else:
                result += f"**⬇️ Rəsmi:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
                    result += f"**⚠️ Xəbərdarlıq:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
                result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

            command = CMD_HELP_BOT[cmd]['commands'][komut]
            if command['params'] is None:
                result += f"**🛠 Komanda:** `{PATTERNS[:1]}{command['command']}`\n"
            else:
                result += f"**🛠 Komanda:** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
                
            if command['example'] is None:
                result += f"**💬 Açıqlama:** `{command['usage']}`\n\n"
            else:
                result += f"**💬 Açıqlama:** `{command['usage']}`\n"
                result += f"**⌨️ Nümunə:** `{PATTERNS[:1]}{command['example']}`\n\n"

            await event.edit(
                result,
                buttons=[custom.Button.inline("◀️ Geri", data=f"bilgi[{sayfa}]({cmd})")],
                link_preview=False
            )
    except Exception as e:
        print(e)
        LOGS.info(
            "Botunuzda inline modu deaktiv edildi. "
            "Aktivleşdirmek üçün bir bot token yazın ve inline modunu açın. "
            "Eger bunnan başqa probleminiz varsa bize yazın @Neonsup."
        )

    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        LOGS.info(
            "BOTLOG_CHATID ortam deyişkeni keçerli bir varlıq deyildir. "
            "Ortam deyişkenlerinizi / config.env faylını yoxlayın."
        )
        quit(1)


# =====================
SON_GORULME = 0
COUNT_MSG = 0
USERS = {}
# live ucun
#NEONID = uid
BRAIN_CHECKER = []
COUNT_PM = {}
LASTMSG = {}
ENABLE_KILLME = True
ISAFK = False
AFKREASON = None
ZALG_LIST = [[
    "̖",
    " ̗",
    " ̘",
    " ̙",
    " ̜",
    " ̝",
    " ̞",
    " ̟",
    " ̠",
    " ̤",
    " ̥",
    " ̦",
    " ̩",
    " ̪",
    " ̫",
    " ̬",
    " ̭",
    " ̮",
    " ̯",
    " ̰",
    " ̱",
    " ̲",
    " ̳",
    " ̹",
    " ̺",
    " ̻",
    " ̼",
    " ͅ",
    " ͇",
    " ͈",
    " ͉",
    " ͍",
    " ͎",
    " ͓",
    " ͔",
    " ͕",
    " ͖",
    " ͙",
    " ͚",
    " ",
],
    [
    " ̍", " ̎", " ̄", " ̅", " ̿", " ̑", " ̆", " ̐", " ͒", " ͗",
    " ͑", " ̇", " ̈", " ̊", " ͂", " ̓", " ̈́", " ͊", " ͋", " ͌",
    " ̃", " ̂", " ̌", " ͐", " ́", " ̋", " ̏", " ̽", " ̉", " ͣ",
    " ͤ", " ͥ", " ͦ", " ͧ", " ͨ", " ͩ", " ͪ", " ͫ", " ͬ", " ͭ",
    " ͮ", " ͯ", " ̾", " ͛", " ͆", " ̚"
],
    [
    " ̕",
    " ̛",
    " ̀",
    " ́",
    " ͘",
    " ̡",
    " ̢",
    " ̧",
    " ̨",
    " ̴",
    " ̵",
    " ̶",
    " ͜",
    " ͝",
    " ͞",
    " ͟",
    " ͠",
    " ͢",
    " ̸",
    " ̷",
    " ͡",
]]
