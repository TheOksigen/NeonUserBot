# N Σ O N / esebj / Ｗ ｈｉｓｐｅｒ𐂡
# Oğurlayanın anasın sikim
# Əkmə peysər 


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep as t
from asyncio import sleep
from userbot import bot, BOTSAHIBI, SUDO_ID
import os 
@register(incoming=True, from_users=SUDO_ID, pattern="^.bassbost(?: |$)(.*)")
@register(outgoing=True, pattern="^.bass(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        input = event.pattern_match.group(1)
    else:
        await event.client.send_message(event.chat_id, "🔸 __Bass effekti üçün bass səviyyəsi təyin et!__")
        return
    if not event.reply_to_msg_id:
        await event.edit("ℹ️ __Hansı musiqiyə bass vermək lazımdırsa, cavab ver ona.__")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("ℹ️ __Hansı musiqiyə bass vermək lazımdırsa, cavab ver ona.__")
        return
    chat = "@Baasss_bot"
    await event.delete()
    a = await event.client.send_message(event.chat_id, "__Bass effekti gücləndirilir.__ 🔊")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=488701812)
            )
            reply = await event.client.send_message(chat, reply_message)
            t(3)
            strr = await event.client.send_message(chat, input)
            response = await response
        except YouBlockedUserError:
            await event.edit("**@Baasss_bot'u blokdan çıxart. Yenidən yoxla.**")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Gizlilik ayarlarınızdakı ileti qismini düzəldin."
            )
        else:
            await event.client.delete_messages(event.chat_id, [a.id])
            await event.client.send_file(
                event.chat_id,
                response.message.media, caption=f"🔸 **Bass səviyyəsi** [N Σ O N](t.me/neonsup) **ilə gücləndirildi.**\n🔊 **Bass səviyyəsi -** `{input}`\n🀄️ **Mənim Sahibim -** {BOTSAHIBI}")             
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.delete_messages(conv.chat_id,
                                             [reply.id, strr.id, response.id])
        
            
Help = CmdHelp('bass').add_command(
    "bass <Audio faylına cavab> <Bass səviyyəsi>", None,
    "Musiqinin bass səviyyəsini çoxaldar."
    ).add_info("**@Esebj Tərəfindən Yaradılıb.**"
    ).add()
