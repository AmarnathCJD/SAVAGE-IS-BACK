# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import os
import time
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, StartTime, topfunc
from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd, edit_or_reply, sudo_cmd

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
    PM_iMG = "https://telegra.ph/file/96e24977e0e11d7a0f9af.mp4"
else:
    PM_iMG = ALIVE_PIC


HELL_PIC = os.environ.get("HELL_PIC", None)
if HELL_PIC is None:
    HELL_IMG = "https://telegra.ph/file/96e24977e0e11d7a0f9af.mp4"
else:
    HELL_IMG = HELL_PIC

CAT_IMGE = os.environ.get("CAT_IMGE", None)
if CAT_IMGE is None:
    CAT_IMG = "https://telegra.ph/file/96e24977e0e11d7a0f9af.mp4"
else:
    CAT_IMG = CAT_IMGE

version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "✮ MY BOT IS RUNNING SUCCESFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "
hellversion = "7.0"
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(lightning_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(salive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "🔥🔥𝐒𝐀𝐕𝐀𝐆𝐄 𝐎𝐍 𝐅𝐈𝐑𝐄🔥🔥\n"
        pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
        pm_caption += "𝐎𝐖𝐍𝐄𝐑             : [⚡丂卂爪乇乇尺⚡](@sameer_795)\n" 
        pm_caption += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 1.17.5\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  : [ᴊᴏɪɴ](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏    : [ᴊᴏɪɴ](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏       : [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[ꀷꏂᖘ꒒ꂦꌩ ꌩꂦꀎꋪ ꂦꅐꈤ ꌚꍏ꒦ꍏꁅꏂ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"
        await salive.get_chat()
        await salive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            salive.chat_id, ALIVE_PHOTTO, caption=pm_caption, link_preview=False
        )
        await sallive.delete()
        return
    req = requests.get("")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(salive.chat_id, file=sticker)
        await borg.send_message(
            salive.chat_id,
            pm_caption = "🔥🔥𝐒𝐀𝐕𝐀𝐆𝐄 𝐎𝐍 𝐅𝐈𝐑𝐄🔥🔥\n"
        pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
        pm_caption += "𝐎𝐖𝐍𝐄𝐑             : [⚡丂卂爪乇乇尺⚡](@sameer_795)\n" 
        pm_caption += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 1.17.5\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  : [ᴊᴏɪɴ](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏    : [ᴊᴏɪɴ](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏       : [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[ꀷꏂᖘ꒒ꂦꌩ ꌩꂦꀎꋪ ꂦꅐꈤ ꌚꍏ꒦ꍏꁅꏂ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"
            link_preview=False,
        )
        await salive.delete()


# Hellbot's Alive Message
# Credits to Hellboy Op


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid


pm_caption = "🔥🔥𝐒𝐀𝐕𝐀𝐆𝐄 𝐎𝐍 𝐅𝐈𝐑𝐄🔥🔥\n"
        pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
        pm_caption += "𝐎𝐖𝐍𝐄𝐑             : [⚡丂卂爪乇乇尺⚡](@sameer_795)\n" 
        pm_caption += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 1.17.5\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  : [ᴊᴏɪɴ](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏    : [ᴊᴏɪɴ](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏       : [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[ꀷꏂᖘ꒒ꂦꌩ ꌩꂦꀎꋪ ꂦꅐꈤ ꌚꍏ꒦ꍏꁅꏂ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"
@borg.on(lightning_cmd(outgoing=True, pattern="halive$"))
@borg.on(sudo_cmd(pattern="halive$", allow_sudo=True))
async def amireallyalive(halive):
    await halive.get_chat()
    await halive.delete()
    """ For .halive command, check if the bot is running.  """
    await borg.send_file(halive.chat_id, HELL_IMG, caption=pm_caption)
    await halive.delete()


# catuserbot's Alive
# Credits To catbot And Sandi


@borg.on(lightning_cmd(outgoing=True, pattern="calive$"))
@borg.on(sudo_cmd(pattern="calive$", allow_sudo=True))
async def amireallyalive(calive):
    if calive.fwd_from:
        return
    reply_to_id = await reply_id(calive)
    uptime = await topfunc.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if PM_IMG:
        pm_caption = "🔥🔥𝐒𝐀𝐕𝐀𝐆𝐄 𝐎𝐍 𝐅𝐈𝐑𝐄🔥🔥\n"
        pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
        pm_caption += "𝐎𝐖𝐍𝐄𝐑             : [⚡丂卂爪乇乇尺⚡](@sameer_795)\n" 
        pm_caption += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 1.17.5\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  : [ᴊᴏɪɴ](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏    : [ᴊᴏɪɴ](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏       : [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[ꀷꏂᖘ꒒ꂦꌩ ꌩꂦꀎꋪ ꂦꅐꈤ ꌚꍏ꒦ꍏꁅꏂ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"
        await calive.client.send_file(
            calive.chat_id, CAT_IMG, caption=pm_caption, reply_to=reply_to_id
        )
        await calive.delete()
    else:
        await edit_or_reply(
            calive,
            pm_caption = "🔥🔥𝐒𝐀𝐕𝐀𝐆𝐄 𝐎𝐍 𝐅𝐈𝐑𝐄🔥🔥\n"
        pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
        pm_caption += "𝐎𝐖𝐍𝐄𝐑             : [⚡丂卂爪乇乇尺⚡](@sameer_795)\n" 
        pm_caption += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 : 1.17.5\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  : [ᴊᴏɪɴ](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏    : [ᴊᴏɪɴ](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏       : [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[ꀷꏂᖘ꒒ꂦꌩ ꌩꂦꀎꋪ ꂦꅐꈤ ꌚꍏ꒦ꍏꁅꏂ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


# Telebot's Alive
# Credits To Telbot And xditya
from userbot.Config import Var
from userbot.thunderconfig import Config

CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)


telemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✵**"


if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@lightningsupport"


CMD_HELP.update(
    {
        "alive": "**alive**\
        \n\n**Syntax : **`.halive For Hellbot's Alive`\
        \n**Function : **__ Hellbot's Alive__\
        \nFor above two commands use `.bigspam` instead of spam for spamming more than 50 messages\
        \n\n**Syntax : **`.falive`\
        \n**Function : **__ Fridays's Alive.__\
        \n\n**Syntax : **`.calive `\
        \n**Function : **__ .CatUSerbot's Alive.__\
        \n\n**Syntax : **`.dalive `\
        \n**Function : **__ .DC Uerbot's Alive.__\
        \n\n**Syntax : **`.alive `\
        \n**Function : **__ .Lightning Uerbot's Alive.__\
        \n\n**Syntax : **`.awake `\
        \n**Function : **__ .Awake.__\
        \n\n**Syntax : **`.salive `\
        \n**Function : **__ .Lightning Uerbot's Alive.__\
        \n\n\n**NOTE : All Credits To Thier Respective !!**"
    }
)
