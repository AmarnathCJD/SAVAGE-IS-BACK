"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import os
import time

from userbot import ALIVE_NAME, Lastupdate
from userbot.plugins import currentversion
from userbot.utils import lightning_cmd, sudo_cmd

FRI_IMAGE = os.environ.get("FRI_IMAGE", None)
if FRI_IMAGE is None:
    FRI_IMG = "https://telegra.ph/file/00f60d92a8e02db2a9877.mp4"
else:
    FRI_IMG = FRI_IMAGE


# Functions
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


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

        pm_caption = "π₯π₯ππππππ ππ πππππ₯π₯\n"
        pm_caption += f"               __βΌπΌπ°πππ΄πβ__\n**      γ{DEFAULTUSER}γ**\n\n"
        pm_caption += "πππππ             : [β‘δΈεηͺδΉδΉε°Ίβ‘](@sameer_795)\n" 
        pm_caption += "ππππππππ πππππππ : 1.17.5\n"
        pm_caption += "πππππππ πππππππ  : [α΄α΄ΙͺΙ΄](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "πππππππ πππππ    : [α΄α΄ΙͺΙ΄](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "ππππ πππππ       : [ππππππ](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[κ·κακκ¦κ© κ©κ¦κκͺ κ¦κκ€ κκκ¦κκκ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"


@borg.on(lightning_cmd(pattern=r"falive"))
@borg.on(sudo_cmd(pattern=r"falive", allow_sudo=True))
async def friday(falive):
    await falive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(falive.chat_id, FRI_IMG, caption=pm_caption)
    await falive.delete()
