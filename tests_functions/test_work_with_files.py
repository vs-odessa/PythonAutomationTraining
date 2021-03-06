import sys
sys.path.append('.')
from functions.file_helper import *
import allure
import pytest


current_path = os.getcwd()
abs_xmlfile_path = os.path.join(current_path, "samples", "xml", "test_data.xml")


@pytest.mark.unit
class TestsFileProcessing:

    @allure.tag('unit')
    @allure.title('Check xml file presence')
    def test_check_xmlfile_presence(self):
        assert os.path.isfile(abs_xmlfile_path) is True

    @allure.tag('unit')
    @allure.title('Check xml file structure')
    def test_check_xml_structure(self):
        file_content = read_file_to_string(abs_xmlfile_path)
        _dict = convert_xml_to_dict(file_content)
        first_person_name = _dict['PERSONS']['PERSON'][0]['FIRST_NAME']
        assert first_person_name == 'Lector'

    @allure.tag('unit')
    @allure.title('Check xml file update')
    def test_check_updated_value(self):
        file_content = read_file_to_string(abs_xmlfile_path)
        _dict = convert_xml_to_dict(file_content)
        updated_dict = update_key_values(_dict)
        my_person_name = _dict['PERSONS']['PERSON'][1]['FIRST_NAME']
        assert my_person_name == 'Brian'

    @allure.tag('unit')
    @allure.title('Check export to json')
    def test_export_to_json(self):
        file_content = read_file_to_string(abs_xmlfile_path)
        _dict = convert_xml_to_dict(file_content)
        temp_dir = tempfile.gettempdir()
        json_file_path = os.path.join(temp_dir, 'mydist.json')
        write_dict_to_json_file(_dict, json_file_path)
        assert os.path.isfile(json_file_path) is True #check json file is created

        with open(json_file_path) as _file:
            data = json.load(_file)
        first_person_name = data['PERSONS']['PERSON'][0]['FIRST_NAME']
        assert first_person_name == 'Lector'






