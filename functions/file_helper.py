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
        write_dict_to_json_file(_dict, out_file_path)


