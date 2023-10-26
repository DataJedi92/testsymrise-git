from testsymrise.common import getData as gd
from testsymrise.common import buildBarAbsolute as bba
from testsymrise.common import buildBarRelative as bbr


def run():
    fetched_data = gd.getData()
    print('res : ', fetched_data)

    bba.buildBarAbsolute(fetched_data)
    bbr.buildBarRelative(fetched_data)
    print('__-- END OF SCRIPT --__')