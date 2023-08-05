from NOOBMUSIC.core.bot import NOOBMUSICBot
from NOOBMUSIC.core.dir import dirr
from NOOBMUSIC.core.git import git
from NOOBMUSIC.core.userbot import Userbot
from NOOBMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = NOOBMUSICBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
