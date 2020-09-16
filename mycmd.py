"""
 Written by Amit Das
 Reference : https://sungju.wordpress.com/2020/09/09/how-to-write-mpykdump-extension/
 Step : Add following file in the ~/.crashrc
	# epython /<home-path>/mypycrash
"""

from crash import register_epython_prog as rprog


help='''
Show kernel boot options
'''

rprog("commandline",
        "show commandline",
        "-h - list available options",
        help)

help='''
SELinux status
'''

rprog("selinuxinfo",
        "show selinux status",
        "-h     list available options",
        help)
