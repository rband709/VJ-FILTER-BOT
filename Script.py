# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
#<a href=https://t.me/{}>{}</a>

class script(object):
    START_TXT = """<b>👋 سلام {} |🥰😉 \n\n• به ربات یوتیوب دانلودر خوش آمدید ❤️\n\n🎬جهت دانلود ویدیو مورد علاقه خود\nابتدا دستور /youtube را نوشته سپس \nدر ادامه لینک ویدیو مورنظر را قرار دهید مثال:\n➡️ /youtube ---لینک ویدیو موردنظر---\n➡️ /youtube http://www.youtube.com/watch?v=BieOHTC_7dY\n\n🖍️ سازنده ربات : <a href=https://t.me/farshidband >FﾑRSみɨの-BﾑŊの</a></b>"""

    HELP_TXT = """<b>Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""

    ABOUT_TXT = """<b>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/ir_ahangdLBot>ᵗʰᵃˡᵃᵖᵃᵗʰʸ ᶠⁱˡᵗᵉʳ ᵇᵒᵗ 🇮🇷</a> 
 ‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/farshidband'>ⁱᵗᶻ ᵐᵉ ᵗᵍ 🇮🇷</a> 
 ‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
 ‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
 ‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
 ‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>"""

    SOURCE_TXT = """
<b>Hᴇʏ, Tʜɪs ɪs ᴀ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.

Tʜɪs Bᴏᴛ ʜᴀs Lᴀᴛᴇsᴛ ᴀɴᴅ Aᴅᴠᴀɴᴄᴇᴅ Fᴇᴀᴛᴜʀᴇs⚡️</b>


Developer - <a href='https://t.me/farshidband'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""


    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """<b><u>✅ کاربر جدیدی به ربات پیوست 😍 </u>
🔺 نام کاربر  : {}
🔺 آیدی عددی کاربر : <code>{}</code>
🤖 آیدی ربات : @IR_YoutubeDLbot</b>"""


    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""
    

    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

IMDb Data:

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : <code>{languages}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>


⏰Result Shown in: {remaining_seconds} <i>seconds</i> 🔥

Requested by : {message.from_user.mention}</b>"""
    
  
    ABOOK_TXT = """<b>ʜᴇʟᴩ : ᴀᴜᴅɪᴏʙᴏᴏᴋ 
  
 yᴏᴜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴀ ᴩᴅꜰ ꜰɪʟᴇ ᴛᴏ ᴀ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴡɪᴛʜ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ✯ 
  
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ: 
 /audiobook: ʀᴇᴩʟy ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀɴy ᴩᴅꜰ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ᴀᴜᴅɪᴏ 
</b>"""     
 
    RESTART_TXT = """
<b>ربات با موفقیت ران شد. 😍
📅 تاریخ : <code>{}</code>
⏰ زمان : <code>{}</code>
🌐 منطقه زمانی : <code>Asia/Kolkata</code>
🛠️ ورژن کد : <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>
🤖 ربات : @IR_YouTubeDLBot</b>"""
    LOGO = """

BOT WORKING PROPERLY"""
