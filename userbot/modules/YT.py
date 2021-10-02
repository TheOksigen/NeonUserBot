# N Σ O N / Ｗ ｈｉｓｐｅｒ𐂡 / esebj
# ƏKMƏ BLƏT

import asyncio
from userbot.events import register as neon 
import os
from userbot import bot
from youtube_dl import YoutubeDL

@neon(outgoing=True, pattern="^.ytv (.*)")
async def inf(event):
  try:
    await event.edit("🔸 __Video məlumatları hazırlanır...__")
  except:
    pass
  os.system("pip install pytube")
  from pytube import YouTube
  url = event.pattern_match.group(1)
  axtar = YouTube(f"{url}")
  ad = axtar.title
  await event.edit(f"🔸 __{ad}'ı video kimi yükləyirəm...__")
  video = YouTube(f"{url}").streams.get_highest_resolution().download()
  await event.edit(f"🔸 __{ad} video kimi göndərirəm..__")
  await event.client.send_file(event.chat_id, video)
  await event.delete()
  os.remove(video)
  
@neon(outgoing=True, pattern="^.yta (.*)")
async def audio(e):
  try:
    await e.edit("🔸 __Musiqi hazırlanır. Gözləyin..__")
  except:
    pass
  os.system("pip install pytube")
  from pytube import YouTube
  os.system("pip install moviepy")
  import moviepy.editor as mp
  inputstr = e.pattern_match.group(1)
  axtar = YouTube(f"{inputstr}")
  videoad = axtar.title
  await e.edit(f"🔸 __{videoad}__ __yüklənir...__")
  hmm = YouTube(f"{inputstr}").streams.filter(file_extension='mp4').first().download()
  await e.edit(f"🔸 __{videoad} musiqi olaraq hazırlanır...__")
  name = axtar.title + ".mp3"
  my_clip = mp.VideoFileClip(hmm)
  my_clip.audio.write_audiofile(name)
  await e.edit(f"🔸 __{videoad}__ __mp3 olaraq göndərilir...__")
  await e.client.send_file(e.chat_id, name)
  os.remove(hmm)
  os.remove(name)
  my_clip.close()
  await e.delete()



@neon(outgoing=True, pattern="^.yt(?: |$)(.*)")
async def _(event):
    try:
      from youtube_search import YoutubeSearch
    except:
      os.system("pip install youtube_search")
    from youtube_search import YoutubeSearch
    if event.fwd_from:
        return
    fin = event.pattern_match.group(1)
    stark_result = await event.edit("`Axtarılır...`")
    results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
    noob = "<b>N Σ O N YOUTUBE AXTARIŞI</b> \n\n"
    for moon in results:
      ytsorgusu = moon["id"]
      kek = f"https://www.youtube.com/watch?v={ytsorgusu}"
      stark_name = moon["title"]
      stark_chnnl = moon["channel"]
      total_stark = moon["duration"]
      stark_views = moon["views"]
      noob += (
        f"<b><u>Ad</u></b> ➠ <code>{stark_name}</code> \n"
        f"<b><u>Link</u></b> ➠  {kek} \n"
        f"<b><u>Kanal</u></b> ➠ <code>{stark_chnnl}</code> \n"
        f"<b><u>Video Uzunluğu</u></b> ➠ <code>{total_stark}</code> \n"
        f"<b><u>Görüntülənmə</u></b> ➠ <code>{stark_views}</code> \n\n"
        )
      await stark_result.edit(noob, parse_mode="HTML")

from userbot.cmdhelp import CmdHelp
Help = CmdHelp('yt').add_command(
    'yt <Musiqi Adı>',None,'YouTube üzərindən verdiyiniz mətn üzrə axtarış edər.'
    ).add_command(
    'yta <Link 🔗>',None,'Yazdığınız linki YouTube üzərindən musiqi olaraq yükləyər.'
    ).add_command('ytv <Link 🔗>',None," Yazdığınız linki YouTube üzərindən video kimi endirər."
    ).add_info(
      '**@Esebj / @NeonUserBot**'
    ).add()
