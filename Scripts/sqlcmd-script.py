#!e:\01_SOFT\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlcmd==0.7.1','console_scripts','sqlcmd'
__requires__ = 'sqlcmd==0.7.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('sqlcmd==0.7.1', 'console_scripts', 'sqlcmd')()
    )
