import xmltodict, json, os, tempfile

def read_file_to_string(file_path):
    with open(file_path) as _file:
        file_content=_file.read()
        return file_content


def convert_xml_to_dict(xml_content):
    out = xmltodict.parse(xml_content)
    return out


def write_dict_to_json_file(dict, json_file_path):
    data = json.dumps(dict)
    with open(json_file_path, 'w') as f:
        f.write(data)


def update_key_values(_dict):
    persons_list = _dict['PERSONS']['PERSON']
    index = 0
    for person in persons_list:
        person_dict = dict(person)
        for key in person_dict:
            if person_dict[key].upper() == "YOUR_FIRST_NAME":
                person_dict[key] = "Brian"
            if person_dict[key].upper() == "YOUR_LAST_NAME":
                person_dict[key] = "May"
            if person_dict[key].upper() == "YOUR_YYYY":
                person_dict[key] = "1947"
            if person_dict[key].upper() == "YOUR_MONTH":
                person_dict[key] = "07"
            if person_dict[key].upper() == "YOUR_DD":
                person_dict[key] = "19"
            if person_dict[key].upper() == "YOUR_COMPANY":
                person_dict[key] = "Queen"
            if person_dict[key].upper() == "YOUR_PROJECT":
                person_dict[key] = "Concert"
            if person_dict[key].upper() == "YOUR_ROLE":
                person_dict[key] = "Guitarist"
            if person_dict[key].upper() == "YOUR_ROOM":
                person_dict[key] = "London"
            if person_dict[key].upper() == "YOUR_HOBBY":
                person_dict[key] = "Music"
        persons_list[index] = person_dict
        index +=1
    _dict['PERSONS']['PERSON'] = persons_list
    
    print (persons_list)


if __name__ == "__main__":

    current_path = os.getcwd()
    abs_file_path = os.path.join(current_path, "..", "samples", "xml", "test_data.xml")
    exists = os.path.isfile(abs_file_path)
    temp_dir = tempfile.gettempdir()
    out_file_path = os.path.join(temp_dir, 'mydist.json')
    if not exists:
        print('File doesn\'t exist')
    else:
        file_content = read_file_to_string(abs_file_path)
        _dict = convert_xml_to_dict(file_content)
        updated_dict = update_key_values(_dict)
        write_dict_to_json_file(_dict, out_file_path)


