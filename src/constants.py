DATE = '2020-11-14'

_path = '/Volumes/git/opendata_mpn/data'

JSON_OUTPUT_PATH = _path + '/output-' + DATE + '.json'


def _for(file):
    return _path + '/' + DATE + '/' + file + '.csv'


OSNOVNA_FILE = _for('osnovne')
SREDNJA_FILE = _for('srednje')
SPECIJALNA_FILE = _for('specijalne')
MUZICKABALETSKA_FILE = _for('muzickebaletske')

COLUMN_NAMES = [
    "#", "ИД установе", "Школска управа", "Округ", "Општина", "Насеље", "Назив установе", "Адреса", "Поштански број",
    "Адреса електронске поште", "Телефон", "Сајт"
]

# Zero based
OPEN_DATA_ID_COL = 1
REGION_COL = 3
TOWNSHIP_COL = 4
PLACE_COL = 5
NAME_COL = 6
ADDRESS_COL = 7
POSTCODE_COL = 8
EMAIL_COL = 9
PHONE_COL = 10
WEBSITE_COL = 11
