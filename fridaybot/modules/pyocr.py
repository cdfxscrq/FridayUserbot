try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
from fridaybot.utils import friday_on_cmd, sudo_cmd
from fridaybot.Configs import Config
import html
@friday.on(friday_on_cmd(pattern="read$"))
async def _(event):
    global images
    if event.fwd_from:
        return
    await event.edit('`Reading..`')
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        imagez = await borg.download_media(
            await event.get_reply_message(), Config.TMP_DOWNLOAD_DIRECTORY
        )
    pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
    results = (pytesseract.image_to_string(Image.open(imagez)))
    mk = f"<b><u> OCR </u></b> \n<b></u>Here is What I Can Read From This.</u></b> \n<code>{results}</code>"
    await event.edit(mk, parse_mode="HTML")
    if os.path.exists(results):
        os.remove(results)
