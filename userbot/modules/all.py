#Neon UserBot
# CREDİT - EPİCUSERBOT
## 
# ---------------------------------------------------------------------------
from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import bot
from time import sleep
import asyncio
import random

# ---------------------------------------------------------------------------

@register(
	pattern="^.tag(?: |$)(.*)",
	outgoing=True, 
	groups_only=True,
)
async def tagger(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		s = q.pattern_match.group(1)
	else:
		s=""
		#await q.edit("**Bir səbəb yaz...** 👀\n**Nümunə:** `.tag Aktiv olaq millət 😃🗡️`")
		
	c = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(c):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(s, i.first_name, i.id))
		await asyncio.sleep(1.5)

#--------------------------------------------------------------------------------------------------------------------------------
		
@register(
	pattern="^.all(?: |$)(.*)",
	outgoing=True,
	groups_only=True,
)
async def all_tagger(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		s = q.pattern_match.group(1)
	else:
		s = ""
		#await q.edit("**Bir səbəb yaz...** 👀\n**Nümunə:** `.all Salam, Necəsiz?`")
	c = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(c):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(s, 
											      i.first_name, 
											      i.id)
					   						)
		await asyncio.sleep(0.5)

# -----------------------------------------------------------------------------------------------------------------

@register(
	pattern="^.alladmin(?: |$)(.*)", 
	outgoing=True,
	groups_only=True,
)
async def _(q):
	if q.fwd_from:
		return
	

	if q.pattern_match.group(1):
		s = q.pattern_match.group(1)
	else:
		s = ""
		#await q.edit("**Bir səbəb yaz...** 👀\n**Nümunə:** `.alladmin Salam, Necəsiz?`")	
	c = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(c, filter=cp):
		if a_ == 50:
			break
		a_+=1
		await bot.send_message(q.chat_id,"[{}](tg://user?id={}) **{}**".format(i.first_name, i.id ,s))
		await asyncio.sleep(1.5)
		
# ---------------------------------------------------------------------------------------------------------------
		
import re
from telethon.tl import types
from userbot import  bot

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")


@register(
	outgoing=True, 
	ignore_unsafe=True, 
	disable_errors=True
)
async def mention(event):
    newstr = event.text
    if event.entities:
        newstr = nameexp.sub(r'<a href="tg://user?id=\2">\3</a>', newstr, 0)
        for match in usernexp.finditer(newstr):
            user = match.group(1)
            text = match.group(2)
            name, entities = await bot._parse_message_text(text, "md")
            rep = f'<a href="tg://resolve?domain={user}">{name}</a>'
            if entities:
                for e in entities:
                    tag = None
                    if isinstance(e, types.MessageEntityBold):
                        tag = "<b>{}</b>"
                    elif isinstance(e, types.MessageEntityItalic):
                        tag = "<i>{}</i>"
                    elif isinstance(e, types.MessageEntityCode):
                        tag = "<code>{}</code>"
                    elif isinstance(e, types.MessageEntityStrike):
                        tag = "<s>{}</s>"
                    elif isinstance(e, types.MessageEntityPre):
                        tag = "<pre>{}</pre>"
                    elif isinstance(e, types.MessageEntityUnderline):
                        tag = "<u>{}</u>"
                    if tag:
                        rep = tag.format(rep)
            newstr = re.sub(re.escape(match.group(0)), 
			    rep, 
			    newstr
			   )
    if newstr != event.text:
        await event.edit(newstr, 
			 parse_mode="html"
		)

# ------------------------------------------------------------------------------------------

emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


class FlagContainer:
    is_active = False

@register(
	pattern=r"^\.stag(?: |$)(.*)",
	outgoing=True
)
async def b(event):
    if event.fwd_from or FlagContainer.is_active:
        return

    if not event.is_group:
        await event.edit(
"""
**Mənim fikrimcə bura qrup deyil.** ❌
""")
        return

    try:
        FlagContainer.is_active = True

        text = None
        args = event.message.text.split(" ", 1)
        if len(args) > 1:
            text = args[1]

        chat = await event.get_input_chat()
        await event.delete()

        tags = list(map(lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})", await event.client.get_participants(chat),
		),
		   )
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            current_pack.append(participant)

            if len(current_pack) == 5: 
                tags = list(map(lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})", current_pack
			      ),
			   )
                current_pack = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(1.3) 
    finally:
        FlagContainer.is_active = False

# -----------------------------------------------------------------------------
"""
@register(
	pattern=r'^\.tagstop(?: |$)(.*)',
	outgoing=True,
)
async def tagstop(event):
	if event.is_group:
		await event.edit(
			"**Bura qrup deyil. Bu modul qrupda olan tag prosesləri üçün nəzərdə tutulmuşdur.**")
		return
	
	if BOTLOG:
                await event.client.send_message(
			BOTLOG_CHATID, 
			"""#**Tag prosesi dayandırıldı.**"""
		#)
            	#await bot.disconnect()
# ------------------------------ CMDHELP --------------------------------------

Help = CmdHelp("tag")
Help.add_command(
	"tag", "<səbəb>", 
        "Qrupdakı şəxsləri tag edər maksimum 3.000 nəfər flood wait səbəbi ilə.")
Help.add_command(
	"all", 
        "<səbəb>", 
        "Qrupdakı şəxsləri sürətli tağ edər. Flood ola bilərsiniz.")
Help.add_command(
	"alladmin", 
        "<səbəb>", 
        "Qrupdakı adminləri tag edər")
Help.add_command(
	'stag',
	'<səbəb>',
	'Qrupdakı şəxsləri fərqli emojilər ilə tag edər.')
Help.add_command(
        '@tag[istədiyiniz ad/söz]',
        'İnsanlanları istədiyiniz kimi tag edin',
        'Əvvəlində nöqtə qoymadan işlədin. Nümunə: @nusrets[Qağaşşş]')  
#Help.add_command("tagstop", None, "Tag prosesini dayandırar.")
Help.add()
