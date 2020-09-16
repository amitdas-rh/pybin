"""
 Written by Amit Das
 Reference : https://sungju.wordpress.com/2020/09/09/how-to-write-mpykdump-extension/
"""

from pykdump.API import *

#command_line = readSymbol("saved_command_line")
command_line = readSymbol("selinux_enforcing")
print(command_line)
