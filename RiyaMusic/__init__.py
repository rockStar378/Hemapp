from RiyaMusic.core.bot import Sona
from RiyaMusic.core.dir import dirr
from RiyaMusic.core.git import git
from RiyaMusic.core.userbot import Userbot
from RiyaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sona()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
