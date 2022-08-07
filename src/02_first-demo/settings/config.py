import os 

from emoji import emojize


TOKEN = ''
NAME_DB = 'products.sqlite'
VERSION = '0.0.1'
AUTHOR = 'Satipoff'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# boshqarish tugmalari
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Maxsulot tanlash'),
    'INFO': emojize(':speech_balloon: Do\'kon haqida'),
    'SETTINGS': emojize('⚙️ Sozlamalar'),
    'SEMIPRODUCT': emojize(':pizza: Yarim tayyor mahsulotlar'),
    'GROCERY': emojize(':bread: Oziq-ovqat'),
    'ICE_CREAM': emojize(':shaved_ice: Muzqaymoq'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ Buyurtma'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Buyurtma berish',
    'COPY': '©️'
}

# maxsulot id katalogi
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# buyruq nomlari
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
