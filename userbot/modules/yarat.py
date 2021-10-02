# NeonUserBot #

# ============== IMPORTS =================
from userbot.events import register
from telethon.tl import functions
from telethon import events
import asyncio 
# ============= LANGUAGE =================
from userbot.language import get_value
LANG = get_value("yaratpy")
# ========================================
n=None
# ========================================

@register(outgoing=True, pattern="^.yarat (qrup|kanal)(?: |$)(.*)")
async def telegraphs(grop):
    if grop.fwd_from:
        return
    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@", "!"):
        if grop.fwd_from:
            return
        növ = grop.pattern_match.group(1)
        ad = grop.pattern_match.group(2)

        if növ == f"{LANG['GROUP']}" or növ == f"{LANG['CHANNEL']}":

            try:

                r = await grop.client(
                    functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                        title=ad,
                        bio=f"{LANG['WITH']}",
                        megagroup=False if növ == f"{LANG['CHANNEL']}" else True,
                    )
                )

                created_chat_id = r.chats[0].id
                result = await grop.client(
                    functions.messages.ExportChatInviteRequest(
                        peer=created_chat_id,
                    )
                )
                await grop.edit(
                    f"{LANG['CREATED']}".format(
                        ad, ad, result.link
                    )
                )
            except Exception as e:  
                await grop.edit(str(e))

# ========================== CMDHELP ===================================

Komek = CmdHelp("yarat")
Komek.add_info("**@Nusrets**")
Komek.add_command(LANG['C1'], LANG['C2'], LANG['C3'], LANG['C4'])
Komek.add_commad(LANG['C5'], LANG['C6'], LANG['C7'], LANG['C8'])
Komek.add()
