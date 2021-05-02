from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**سڵاوو من **{bn}** 🎵

من بۆتی پەخشکردنی گۆرانیم لە چاتە دەنگیەکانی گرووپەکان زیادم بکە و بمکە بەڕێوەبەر  بە یارمەتی  [{bn}](https://t.me/Music_HamaBot).

لەسەر زیادکردنی گرووپ لێدە 🎶**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 ئەژمێری پەرەپێدەر 🛠", url="https://t.me/hhmhhh")
                  ],[
                    InlineKeyboardButton(
                        "💬 کەناڵی ڕوونکردنەوەکانی پەرەپێدەر", url="https://t.me/in_arrray"
                    ),
                    InlineKeyboardButton(
                        "🔊 کەناڵەکەم", url="https://t.me/CQCQQ"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕زیادم بکە بۆ کۆکراوەکەت ➕", url="https://t.me/MusiVchatBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** بۆتەکە بە سەرکەوتوویی چالاک کرا. ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 کەناڵەکەم", url="https://t.me/xawnakam_lm")
                ]
            ]
        )
   )


@Client.on_message(filters.command("panel") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** ئەم بۆتە بەدوادا گەڕان و داگرتن  دەکاتنـ و گۆرانی لەڤۆیس چات لێ ئەداتن✨
ناسنامەی بۆت بنووسە بە ناوی گۆرانییەکە بۆ گەڕان 🔊
نموونە: 
@Music_HamaBot ئاوات بۆکانی

هەروەها دەتوانیت هەر گۆرانییەک دابەزێنیت💞
بەم فەرمانانەی خوارەوە:
- /ytp لینک گۆرانی لە یوتوب
- /song لینکی گۆرانی لە یوتوب

بۆ کۆنترۆڵکردنی گۆرانی ناو ڤۆیس چاتەکە بە پەیوەندی 🔊

- /play بە وەڵامدانەوەی گۆرانیەکە یان لینکی ڤیدیۆی یووتووب بۆ پەخشکردن
- /stop بۆ وەستانی گۆرانیەکە بە شێوەیەکی کاتی لە ناو پەیوەندیەکە
- /resume بۆ تەواوکردنی گۆرانییە ڕاگیراوەکە
- /stop بۆ ئەوەی بۆتەکە لە ژەنینی گۆرانیەکە بوەستێ
-/skip بۆ بازدان لە گۆرانی ئێستا و بڕوا بۆ گۆرانی داهاتوو

#تێبینی : دەتوانیت گۆرانییەکی تر ببەی و زیاد بکەیت بۆ ڕۆڵەکەی دوای گۆرانیەکەی ئێستا بۆیە دەجولێیت لەنێوانی و باقی گۆرانیەکان بە بەکارهێنانی ڕیز /skip 🔖**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 کەناڵی پەرەپێدەر", url="https://t.me/Music_Hama")
                ],[
                    InlineKeyboardButton(
                        "🎶 ئەژمێری یاریدەر", url="https://t.me/MUSIC_VOICEY"
                    )
                ]
            ]
        )
   )
