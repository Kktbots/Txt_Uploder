import os

API_ID = API_ID = 29540156

API_HASH = os.environ.get("API_HASH", "775d47859519f34f01549344a392280b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6514569486:AAHwv8mkQKSULTUmNdVjrWfvn9Q9tpucpG4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5943972790))

LOG = -1813698654

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5943972790").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


