import configparser
import os

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
config_file_path = base_dir + "/../setting.ini"

cf = configparser.ConfigParser()
cf.read(config_file_path)


def get_config(section, setting):
    return cf.get(section, setting)


def get_config_default(section, setting, default):
    cfg_value = default
    try:
        cfg_value = cf.get(section, setting)
    except:
        print("no configuration found for [%s]-[%s]," % (section, setting), "use default: '%s'" % default)

    return cfg_value


if __name__ == "__main__":
    print(get_config('Database', 'mongodb.base'))
    print(get_config('File_Storage', 'fs.import'))
    print(get_config('Logging', 'log.dir'))
    print(get_config_default('Logging', 'log.format', '%(asctime)15s - %(name)8s - %(levelname)8s: %(message)s'))
