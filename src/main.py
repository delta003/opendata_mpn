import codecs
import csv
import json
import constants

from cyrtranslit import to_latin
from api.opendata import Region, RegionId, Township, TownshipId, OpenDataId, SchoolType, School


def get_by_type():
    return {
        SchoolType.OSNOVNA: _parse_data(constants.OSNOVNA_FILE),
        SchoolType.SREDNJA: _parse_data(constants.SREDNJA_FILE),
        SchoolType.SPECIJALNA: _parse_data(constants.SPECIJALNA_FILE),
        SchoolType.MUZICKABALETSKA: _parse_data(constants.MUZICKABALETSKA_FILE),
    }


def _parse_data(path):
    content = []
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            new_line = []
            for column in constants.COLUMN_NAMES:
                new_line.append(line[column])
            content.append(new_line)
    print("Parsed %d lines from %s" % (len(content), path))
    return content


def regions(data):
    names = set()
    for content in data.values():
        for entry in content:
            region_name = entry[constants.REGION_COL]
            names.add(region_name)
    name_to_id = {}
    for i, name in enumerate(sorted(names)):
        name_to_id[name] = RegionId(i + 1)
    regions = {}
    for content in data.values():
        for entry in content:
            region_name = entry[constants.REGION_COL]
            region_id = name_to_id[region_name]
            if region_id in regions.keys():
                continue
            regions[region_id] = Region(
                id=region_id,
                name=region_name,
                name_lt=to_latin(region_name))
    print("Found %d regions" % len(regions))
    return regions


def townships(data, reg):
    names = set()
    for content in data.values():
        for entry in content:
            township_name = entry[constants.TOWNSHIP_COL]
            names.add(township_name)
    name_to_id = {}
    for i, name in enumerate(sorted(names)):
        name_to_id[name] = TownshipId(i + 1)
    townships = {}
    for content in data.values():
        for entry in content:
            township_name = entry[constants.TOWNSHIP_COL]
            township_id = name_to_id[township_name]
            region_name = entry[constants.REGION_COL]
            region = _region_for_name(reg, region_name)
            if township_id in townships.keys():
                township = townships[township_id]
                if township.region_id != region.id:
                    raise ValueError("Found same township for different regions: %s -> (%d, %d)"
                                     % (township_name, township.region_id, region.id))
            else:
                townships[township_id] = Township(
                    id=township_id,
                    name=township_name,
                    name_lt=to_latin(township_name),
                    region_id=region.id)
    print("Found %d townships" % len(townships))
    return townships


def schools(data, town):
    schools = {}
    for school_type, content in data.items():
        for entry in content:
            township = _township_for_name(town, entry[constants.TOWNSHIP_COL])
            open_data_id = OpenDataId(entry[constants.OPEN_DATA_ID_COL])
            if open_data_id in schools.keys():
                raise KeyError("Found duplicate open data id: %d", open_data_id)
            school = School(
                id=open_data_id,
                township_id=township.id,
                type=school_type,
                name=entry[constants.NAME_COL],
                name_lt=to_latin(entry[constants.NAME_COL]),
                address=entry[constants.ADDRESS_COL],
                address_lt=to_latin(entry[constants.ADDRESS_COL]),
                place=entry[constants.PLACE_COL],
                place_lt=to_latin(entry[constants.PLACE_COL]),
                postcode=entry[constants.POSTCODE_COL],
                website=entry[constants.WEBSITE_COL],
                phone=entry[constants.PHONE_COL],
                email=entry[constants.EMAIL_COL])
            schools[open_data_id] = school
    print("Found %d schools" % len(schools))
    return schools


def _region_for_name(reg, name):
    for entry in reg.values():
        if entry.name == name:
            return entry
    raise KeyError("Region not found for name %s" % name)


def _township_for_name(town, name):
    for entry in town.values():
        if entry.name == name:
            return entry
    raise KeyError("Township not found for name %s" % name)


def _json(objects):
    values = []
    for obj in objects:
        obj_dict = {}
        for field in obj._fields().keys():
            obj_dict[field] = str(getattr(obj, field))
        values.append(obj_dict)
    return values


def main():
    data = get_by_type()

    reg = regions(data)
    town = townships(data, reg)
    school = schools(data, town)

    output = {
        'regions': _json(reg.values()),
        'townships': _json(town.values()),
        'schools': _json(school.values())
    }

    with codecs.open(constants.JSON_OUTPUT_PATH, 'w', encoding='utf8') as outfile:
        json.dump(output, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
