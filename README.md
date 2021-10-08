
<div align="center">
  <img src="photo/neonub.jpg" width="400" height="400">
  <h1>N Σ O N</h1>
</div>
<p align="center">
    N Σ O N Userbot'u Telegram'ı daha asan və əyləncəli şəkildə istifadə etmək üçün sizlər üçün hazırlayıb təhvil vermişik. Siz bu botla istədiyiniz bir çox şeyləri daha asan yerinə yetirə biləcəksiniz.
    <br>
        <a href="https://t.me/NeonUserBot">Güncəlləmələr</a> |
        <a href="https://t.me/NeonSUP">Kömək Qrupu</a>
    <br>
</p>

----
</div>
<div align="center">
        <h1>Qurulum</h1>
</div>
<div align="left">

*** 
  
### _Asan Üsul_
**Android:** [Termuxu](https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US) açın və bu kodu yapışdırın: 
`bash <(curl -L t.ly/SimZ)`

**Alternativ kod:**
`bash <(curl -L t.ly/YASn)`
  
**iOS:** [ISH](https://apps.apple.com/us/app/ish-shell/id1436902243) və ya [TestFlight'ı](https://apps.apple.com/ru/app/testflight/id899247664) açın və bu kodu yapışdırın: ```apk update && apk add bash && apk add curl && curl -L -o neon_installer.sh https://t.ly/yPtl && chmod +x neon_installer.sh && bash neon_installer.sh```

**Alternativ kod:** ```apk update && apk add bash && apk add curl && curl -L -o neon_installer.sh https://t.ly/RFEj && chmod +x neon_installer.sh && bash neon_installer.sh```

*** 

### _Heroku ilə deploy_
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nusrte/NeonUserBot)

*** 

### _Çətin Üsul_
>```python
>git clone https://github.com/nusrte/NeonUserBot.git
>cd NeonUserBot
>pip install -r requirements.txt
># Config.env yaradıb düzənləyin. #
>python3 main.py
>```

## Plugin Örnəkləri
### Örnək - 1

>```python
>from userbot.events import register
>from userbot.cmdhelp import CmdHelp # <-- Bunu Əlavə edin.
>
>@register(outgoing=True, pattern="^.test")
>async def neonuserbot(event):
>    await event.edit('Neon Userbot istifadə et, xeyir tapacaqsan.')
>
>Help = CmdHelp('test') # Modul adı.
>Help.add_command('test', # Əmr
>    None, # Əmr parametrləri varsa, yazın. Yoxdursa, None yazın.
>    'NeonUserbot haqqında animasiya.', # Əmr açıqlaması
>    '.test' # Örnək istifadə 
>    )
>Help.add_info('@nusrets tərəfindən hazırlanmışdır.') # Məlumat yaza bilərsiniz
># və ya xəbərdarlıq --> Help.add_warning('Təhlükəlidir!')
>Help.add() # bunu mütləq yazın.
>```

### Örnək - 2
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
>    await event.client.send_message(event.chat_id, "**Salam.**")
>    t(1)
>    await event.client.send_message(event.chat_id, "**Sən də N Σ O N işlət..** 🧘🏻")
>    t(1)
>    await event.delete() # <- bu yazılan bütün mesajları silər.
>    await event.client.send_message(event.chat_id, "**AuYeS N Σ O N 🤟🏻**") # və sonda tək bu mesajı göndərər
>    t(1)
>
>Help = CmdHelp('test').add_command(
>  'test',None,'N Σ O N haqqında animasiya.' # modulun ne işə yaradığını deyin
>).add_info(
>  '**@nusrets tərəfindən hazırlanmışdır.**' # məlumat əlavə edin
>).add() # bu mütləqdir.
>```
## İnformasiya

* ***Hər hansısa bir istək & şikayət & önəriləriniz olarsa, [dəstək qrupumuza](https://t.me/NeonSup) müraciət edə bilərsiniz.***

>**Diqqət: [N Σ O N](t.me/neonuserbot) kanalında paylaşılmadığı halda botunuzu yeniləməyin. 
>Əgər botu yeniləsəniz, bot işləməyəcək.
>UserBotumuzu işlətməniz Telegram hesabınızı banlada bilər..
>Bu, açıq mənbəli bir layihədir, etdiyiniz hər şey üçün cavabdehsiniz.
>Buna görə N Σ O N Userbot adminləri məsuliyyət daşımır
>N Σ O N quraraq bunları qəbul etdiyiniz hesab olunur.**

## *Credits;*
**To [Yusuf Usta](github.com/yusufusta) for [AsenaUserBot](https://yusufusta/asenauserbot)
To [NaytSeyd](https://github.com/NaytSeyd) for [SedenUserBot](https://github.com/TeamDerUntergang/Telegram-SedenUserBot)
And thanks to [LunamiWeb](https://github.com/Lonami) for the [Telethon library](https://github.com/LonamiWebs/Telethon).**
