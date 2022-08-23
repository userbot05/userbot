import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "11460437"))
API_HASH = getenv("API_HASH", "ad621a42842ee0c86b4d51189ce4343e")
BOT_TOKEN = getenv("BOT_TOKEN", "5740442023:AAHuRoHi5UO-bXpARyQQ0PgQxrKH_iuoUQU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQCHdB2GZksmZkdjtVYPzYXJP_dfW2wVrlExOMMaIbZVj4XRDcfi-RwnWcn4ERwT2mSKwJud2iluiqerXPYIYiVR0pIuw0O-KCeCYExrK8AsYpZsIslUf0SqQj9xbJHgVpaP94VzzLm_WyCkNdUqpgoezgG33jpHBlZngA7a5pC_nMxHv22ojCUCq_CmcFN506LnaTbA2hGWNFk9w4HsBdtul_MMfKG8Zj--SOg1j5Iay7nu9xzcAtn7G5XDIffIvNwpQLH8MXLdmHr4nDY4CgSNu7Fe2aRhjzaDE65Gnb00DTx57JTM4BJ7hA8kcmD5L71Z02a2P_rarToi588U32mQAAAAAUapjgsA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
