## Plugin Example.

### Example - 1.

>```python
>from userbot.events import register
>from userbot.cmdhelp import CmdHelp # <-- Add it.
>
>@register(outgoing=True, pattern="^.test")
>async def neonuserbot(event):
>    await event.edit('Use Neon Userbot, you will benefit.')
>
>Help = CmdHelp('test') # Module name.
>Help.add_command('test', # Command.
>    None, # If you have command parameters, type. If not, type None.
>    'Animation on N Σ O N.', # Command information.
>    '.test' # Use an example.
>    )
>Help.add_info('Developed by @nusrets.') # You can write information.
># or warning. --> Help.add_warning('It is dangerous!')
>Help.add() # this is a must.
>```
### Example - 2.
>```python
>from userbot.events import register
>from userbot.cmdhelp import CmdHelp
>from userbot import NEON_VERSION, bot
>from time import sleep as t
>from telethon import events
>
>@register(
>        pattern="^.test(?: |$)(.*)",
>        outgoing=True
>)
>async def test(event):
>    await event.client.send_message(event.chat_id, "**Hello.**")
>    t(1)
>    await event.client.send_message(event.chat_id, "**You too, use N Σ O N.** 🧘🏻")
>    t(1)
>    await event.delete() # <- it deletes all messages written.
>    await event.client.send_message(event.chat_id, "**AYE N Σ O N 🤟🏻**") # and finally sends this message alone
>    t(1)
>
>Help = CmdHelp('test').add_command(
>  'test',None,'Animation on N Σ O N.' # Explain what the module does
>).add_info(
>  '**Developed by @nusrets.**' # add information.
>).add() # this is a must.
>```
