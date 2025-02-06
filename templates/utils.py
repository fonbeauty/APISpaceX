# import xml.etree.ElementTree as ET
from xml.etree import ElementTree


def check_result_operation(xml_str: str, etalon: str):
    root = ElementTree.fromstring(xml_str)
    return root[0][0][0].text == etalon
