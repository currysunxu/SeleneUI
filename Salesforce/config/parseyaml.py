import os


def read_yaml_file(current_path):
    print("current directory -> %s" % os.getcwd())
    yml_file = os.path.abspath(current_path + "/config.yaml")
    yml = open(yml_file, 'r', encoding='utf-8')
    if os.path.isfile(yml_file):
        return yml.read()
    else:
        print(yml_file + 'file not exist')
