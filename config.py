try:
    import configparser as cp
except ImportError:
    import ConfigParser as cp

config = cp.RawConfigParser()

try: #python2
    config.read('config')
except UnicodeDecodeError:
    config.read('config',encoding='utf-8')

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

