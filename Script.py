class script(object):
    START_TXT = """<b>ʏᴏ.. ʏᴏ.. {}🙋,
ɪ'ᴍ <a href='https://t.me/Marshmello_Robot'>M̶ꪖ𝘳𝘴ꫝꪑꫀꪶꪶꪮ</a>, ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴀs ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ....

ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ; ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ, ᴛʜᴀᴛs ᴀʟʟ, ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ...🤓

©ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙ𝚢
<a href='https://t.me/peace_fighter_TG'>»»»»»»»𝙿𝚎𝙰𝚌𝙴-𝙵𝚒𝙶𝚑𝚃𝚎𝚁-𝚃𝙶</a></b>

     """
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>♡︎ ᴍʏ ɴᴀᴍᴇ:{}
♡︎ ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/peace_fighter_TG'>𝙿ᴇ𝙰ᴄ𝙴-𝙵ɪ𝙶ʜ𝚃ᴇ𝚁-ᴛɢ</a>
♡︎ ᴄʀᴇᴅɪᴛs: ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ
♡︎ ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ</a>
♡︎ ʟᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴᴇ 3</a>
♡︎ ᴅᴀᴛᴀ ʙᴀsᴇ: <a href='https://www.mongodb.com/cloud'>ᴍᴀɴɢᴏ ᴅʙ</a>
♡︎ ʙᴏᴛ sᴇʀᴠᴇʀ: <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a>
♡︎ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: <a href='https://t.me/NOKIERUNNOIPPKITTUM'>ᴄʟɪᴄᴋ ᴍᴇ 👈</a>
♡︎ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: 𝚅7.6 [ ʙᴇᴛᴀ ]</b>"""
    SOURCE_TXT = """<b>എന്തായാലും ഇടുവരെ വന്ന സ്ഥിതിക്ക് ഇന്ന ഈ BUN 🥯 കയിച്ചിട്ട് പോയമദി 💁</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Marshmello should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Marshmello Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. marshmello supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b>"""
    LOG_TEXT_G = """<b>#𝙽𝙴𝚆𝙶𝚁𝙾𝚄𝙿
♡︎ 𝙶𝚁𝙾𝚄𝙿 = {}(<code>{}</code>)
♡︎ 𝚃𝙾𝚃𝙰𝙻 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 = <code>{}</code>
♡︎ 𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 - {}
</b>"""
    LOG_TEXT_P = """<b>#𝙽𝙴𝚆𝚄𝚂𝙴𝚁
♡︎ 𝙸𝙳 - <code>{}</code>
♡︎ 𝙽𝙰𝙼𝙴 - {}
</b>"""
