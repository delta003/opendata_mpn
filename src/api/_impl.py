import builtins
from conjure_python_client import (
    ConjureBeanType,
    ConjureEnumType,
    ConjureFieldDefinition,
)
from typing import (
    Dict,
    List,
)

class opendata_Region(ConjureBeanType):

    @builtins.classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'id': ConjureFieldDefinition('id', opendata_RegionId),
            'name': ConjureFieldDefinition('name', str),
            'name_lt': ConjureFieldDefinition('nameLt', str)
        }

    __slots__ = ['_id', '_name', '_name_lt'] # type: List[str]

    def __init__(self, id, name, name_lt):
        # type: (int, str, str) -> None
        self._id = id
        self._name = name
        self._name_lt = name_lt

    @builtins.property
    def id(self):
        # type: () -> int
        return self._id

    @builtins.property
    def name(self):
        # type: () -> str
        return self._name

    @builtins.property
    def name_lt(self):
        # type: () -> str
        return self._name_lt


opendata_Region.__name__ = "Region"
opendata_Region.__qualname__ = "Region"
opendata_Region.__module__ = "opendata"


class opendata_School(ConjureBeanType):

    @builtins.classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'id': ConjureFieldDefinition('id', opendata_OpenDataId),
            'township_id': ConjureFieldDefinition('townshipId', opendata_TownshipId),
            'type': ConjureFieldDefinition('type', opendata_SchoolType),
            'name': ConjureFieldDefinition('name', str),
            'name_lt': ConjureFieldDefinition('nameLt', str),
            'address': ConjureFieldDefinition('address', str),
            'address_lt': ConjureFieldDefinition('addressLt', str),
            'place': ConjureFieldDefinition('place', str),
            'place_lt': ConjureFieldDefinition('placeLt', str),
            'postcode': ConjureFieldDefinition('postcode', str),
            'website': ConjureFieldDefinition('website', str),
            'phone': ConjureFieldDefinition('phone', str),
            'email': ConjureFieldDefinition('email', str)
        }

    __slots__ = ['_id', '_township_id', '_type', '_name', '_name_lt', '_address', '_address_lt', '_place', '_place_lt', '_postcode', '_website', '_phone', '_email'] # type: List[str]

    def __init__(self, address, address_lt, email, id, name, name_lt, phone, place, place_lt, postcode, township_id, type, website):
        # type: (str, str, str, int, str, str, str, str, str, str, int, opendata_SchoolType, str) -> None
        self._id = id
        self._township_id = township_id
        self._type = type
        self._name = name
        self._name_lt = name_lt
        self._address = address
        self._address_lt = address_lt
        self._place = place
        self._place_lt = place_lt
        self._postcode = postcode
        self._website = website
        self._phone = phone
        self._email = email

    @builtins.property
    def id(self):
        # type: () -> int
        return self._id

    @builtins.property
    def township_id(self):
        # type: () -> int
        return self._township_id

    @builtins.property
    def type(self):
        # type: () -> opendata_SchoolType
        return self._type

    @builtins.property
    def name(self):
        # type: () -> str
        return self._name

    @builtins.property
    def name_lt(self):
        # type: () -> str
        return self._name_lt

    @builtins.property
    def address(self):
        # type: () -> str
        return self._address

    @builtins.property
    def address_lt(self):
        # type: () -> str
        return self._address_lt

    @builtins.property
    def place(self):
        # type: () -> str
        return self._place

    @builtins.property
    def place_lt(self):
        # type: () -> str
        return self._place_lt

    @builtins.property
    def postcode(self):
        # type: () -> str
        return self._postcode

    @builtins.property
    def website(self):
        # type: () -> str
        return self._website

    @builtins.property
    def phone(self):
        # type: () -> str
        return self._phone

    @builtins.property
    def email(self):
        # type: () -> str
        return self._email


opendata_School.__name__ = "School"
opendata_School.__qualname__ = "School"
opendata_School.__module__ = "opendata"


class opendata_SchoolType(ConjureEnumType):
    """
    As classified in http://opendata.mpn.gov.rs/index.php?page=ustanove
    """

    OSNOVNA = 'OSNOVNA'
    '''OSNOVNA'''
    SREDNJA = 'SREDNJA'
    '''SREDNJA'''
    SPECIJALNA = 'SPECIJALNA'
    '''SPECIJALNA'''
    MUZICKABALETSKA = 'MUZICKABALETSKA'
    '''MUZICKABALETSKA'''
    UNKNOWN = 'UNKNOWN'
    '''UNKNOWN'''

    def __reduce_ex__(self, proto):
        return self.__class__, (self.name,)


opendata_SchoolType.__name__ = "SchoolType"
opendata_SchoolType.__qualname__ = "SchoolType"
opendata_SchoolType.__module__ = "opendata"


class opendata_Township(ConjureBeanType):

    @builtins.classmethod
    def _fields(cls):
        # type: () -> Dict[str, ConjureFieldDefinition]
        return {
            'id': ConjureFieldDefinition('id', opendata_TownshipId),
            'name': ConjureFieldDefinition('name', str),
            'name_lt': ConjureFieldDefinition('nameLt', str),
            'region_id': ConjureFieldDefinition('regionId', opendata_RegionId)
        }

    __slots__ = ['_id', '_name', '_name_lt', '_region_id'] # type: List[str]

    def __init__(self, id, name, name_lt, region_id):
        # type: (int, str, str, int) -> None
        self._id = id
        self._name = name
        self._name_lt = name_lt
        self._region_id = region_id

    @builtins.property
    def id(self):
        # type: () -> int
        return self._id

    @builtins.property
    def name(self):
        # type: () -> str
        return self._name

    @builtins.property
    def name_lt(self):
        # type: () -> str
        return self._name_lt

    @builtins.property
    def region_id(self):
        # type: () -> int
        return self._region_id


opendata_Township.__name__ = "Township"
opendata_Township.__qualname__ = "Township"
opendata_Township.__module__ = "opendata"


opendata_TownshipId = int

opendata_RegionId = int

opendata_OpenDataId = int

