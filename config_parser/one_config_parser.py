import configparser
dictionary = {}

config = configparser.ConfigParser()
config.read("file.ini")
for section in config.sections():
    print("@@@@",section)
    dictionary[section] = {}
    for option in config.options(section):
        dictionary[section][option] = config.get(section, option)


print(f"read dictionary is: {dictionary}")