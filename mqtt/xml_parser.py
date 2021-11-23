import xml.etree.ElementTree as et
import my_beautify as mb
message = """<?xml version="1.0" encoding="UTF-8" ?>
<root>
    <cabinetId>CAB0103UK003</cabinetId>
    <testGroup>
        <testGroupName>testGroupName</testGroupName>
        <testSuite>
            <testSuiteName>testSuiteName</testSuiteName>
            <testCase>
                <testCaseName>testCaseName</testCaseName>
                <meterId>meterId</meterId>
                <actions>actions</actions>
            </testCase>
            <testCase>
                <testCaseName></testCaseName>
                <meterId></meterId>
                <actions></actions>
            </testCase>
        </testSuite>
    </testGroup>
</root>"""

root = et.fromstring(message)
mb.log_print(variable_name='root.tag',variable=root.tag)
mb.log_print(variable_name='root.attrib',variable=root.attrib)

print("printing child tag and attrib: ")
for child in root:
    mb.log_print(variable_name='child.tag', variable=child.tag)
    mb.log_print(variable_name='child.attrib', variable=child.attrib)

mb.log_print(variable_name='root[1][0].text',variable=root[1][0].text)
message = {
    'cabinet_id' : root[0].text,
    'testGroupName': root[1][0].text,
    'testSuiteName': root[1][1][0].text,
    'testCaseName': root[1][1][1][0].text,
    'meterId': root[1][1][1][1].text,
    'actions': root[1][1][1][2].text,
}
print(message)
