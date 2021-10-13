
<h1 align="center">N Σ O N</h1>
<i>Here you will be informed about NeonUserBot.
You can contact us with all the buttons for questions you do not understand or have in mind.</i>

***

[![Chat on Telegram](https://img.shields.io/badge/Official%20Channel-Telegram-silver.svg?style=flat&logo=Telegram)](http://t.me/neonuserbot) [![Chat on Telegram](https://img.shields.io/badge/Official%20Support-Telegram-red.svg?style=flat&logo=Telegram)](http://t.me/neonsup) [![Chat on Telegram](https://img.shields.io/badge/Plugins-Telegram-gold.svg?style=flat&logo=Telegram)](http://t.me/neonplugin) [![Chat on Telegram](https://img.shields.io/badge/Neon%20Devs-Telegram-succes.svg?style=flat&logo=Telegram)](http://t.me/neondevs) 

[![GitHub language count](https://img.shields.io/github/languages/count/nusrte/NeonUserBot?color=red)](https://github.com/nusrte/NeonUserBot) [![DeepSource](https://deepsource.io/gh/nusrte/NeonUserBot.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/nusrte/NeonUserBot/?ref=repository-badge) [![CodeFactor](https://www.codefactor.io/repository/github/nusrte/neonuserbot/badge)](https://www.codefactor.io/repository/github/nusrte/neonuserbot) ![Repo's Size](https://img.shields.io/github/repo-size/nusrte/neonuserbot?color=blue) ![](https://img.shields.io/github/forks/nusrte/neonuserbot?color=silver&logo=neon) ![Repo's Stars.](https://img.shields.io/github/stars/nusrte/neonuserbot?color=red)


<div align="center">
  <img src="photo/neonub.jpg" width="600" height="600">
</div>
<p align="center">
    <b>N Σ O N Userbot is designed for you to use Telegram in an easier and more entertaining way.
      You can easily do many things you want with this bot.</b>
</p>

*** 

</div>
<div align="center">
        <h2>Deploy Methods.</h2>
</div>


  
### _Easy Method._
**For Android:** Open the [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US) and paste this code:
`bash <(curl -L t.ly/SimZ)`

**Alternative code:**
`bash <(curl -L t.ly/YASn)`
  
**For iOS:** Open [ISH](https://apps.apple.com/us/app/ish-shell/id1436902243) or [TestFlight](https://apps.apple.com/ru/app/testflight/id899247664) and paste this code: ```apk update && apk add bash && apk add curl && curl -L -o neon_installer.sh https://t.ly/yPtl && chmod +x neon_installer.sh && bash neon_installer.sh```

**Alternative code:** ```apk update && apk add bash && apk add curl && curl -L -o neon_installer.sh https://t.ly/RFEj && chmod +x neon_installer.sh && bash neon_installer.sh```

*** 

### _Deploy with Heroku._
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nusrte/NeonUserBot)

*** 

### _Difficult Method._
>```python
>git clone https://github.com/nusrte/NeonUserBot.git
>cd NeonUserBot
>pip install -r requirements.txt
># Create and edit Config.env. #
>python3 main.py
>```
## _Plugin Examples._
### _Example - 1._

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
### _Example - 2._
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

## *Attention!* 📢
*Do not update your bot unless it is shared on the [N Σ O N](t.me/neonuserbot) channel. If you update the bot, the bot will not work.*


## *Attention! 📢 - 2*
*Using our User Bot may block your Telegram account. This is an open source project, you are responsible for everything you do. Therefore, the N Σ O N Userbot staff is not responsible. When using neon, you are considered to be accepting them.*  

## *Additional.* 🎴
*If you have any requests & complaints & suggestions, you can contact [our support team.](https://t.me/NeonSup)*

## *Credits.* 
**Thanks to [Yusuf Usta](github.com/yusufusta) for [AsenaUserBot](https://yusufusta/asenauserbot)
to [NaytSeyd](https://github.com/NaytSeyd) for [SedenUserBot](https://github.com/TeamDerUntergang/Telegram-SedenUserBot)
and to [LunamiWeb](https://github.com/Lonami) for the [Telethon library](https://github.com/LonamiWebs/Telethon).**
