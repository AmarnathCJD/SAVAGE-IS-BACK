import time

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
from userbot.Config import Var
from userbot.plugins import telever
from userbot.utils import lightning_cmd, sudo_cmd


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
PM_IMG = Var.ALIVE_IMAGE

        pm_caption = "π₯π₯ππππππ ππ πππππ₯π₯\n"
        pm_caption += f"               __βΌπΌπ°πππ΄πβ__\n**      γ{DEFAULTUSER}γ**\n\n"
        pm_caption += "πππππ             : [β‘δΈεηͺδΉδΉε°Ίβ‘](@sameer_795)\n" 
        pm_caption += "ππππππππ πππππππ : 1.17.5\n"
        pm_caption += "πππππππ πππππππ  : [α΄α΄ΙͺΙ΄](https://t.me/SAVAGE_TECHY)\n"
        pm_caption += "πππππππ πππππ    : [α΄α΄ΙͺΙ΄](https://t.me/SAVAGE_TEAM_BOT)\n"
        pm_caption += "ππππ πππππ       : [ππππππ](https://t.me/SAVAGE_TEAM_BOLTE)\n\n"
        pm_caption += "[κ·κακκ¦κ© κ©κ¦κκͺ κ¦κκ€ κκκ¦κκκ](https://github.com/sameerpanthi/SAVAGE-IS-BACK)\n"

@borg.on(lightning_cmd(pattern=r"fralive"))
@borg.on(sudo_cmd(pattern=r"fralive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .salive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "salive": "**sLive**\
\n\n**Syntax : **`.salive`\
\n**Usage :** Check if UserBot is salive"
    }
)
