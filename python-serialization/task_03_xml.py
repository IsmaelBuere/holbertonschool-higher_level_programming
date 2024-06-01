#!/usr/bin/python3
"""
task 03
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
