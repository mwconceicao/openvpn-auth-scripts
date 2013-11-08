#!/usr/local/bin/python

import ldap
import sys
import os

##
# Config parameters
LDAP_URI                = 'ldap://ldap.company.net:389'
LDAP_BASE_DN            = 'dc=company,dc=net'
LDAP_USER_DN_SUFFIX     = 'ou=Users,' + LDAP_BASE_DN
LDAP_ALLOWED_GROUP_DN   = 'cn=vpn,ou=Groups,' + LDAP_BASE_DN
LDAP_ALLOWED_GROUP_ATTR = 'memberUid'
##

pw_username = 'cn=' + os.environ['username'] + ',' + LDAP_USER_DN_SUFFIX
pw_password =         os.environ['password']

# Try to connect to LDAP base using the given username and password
l = ldap.initialize(LDAP_URI)
try:
	l.simple_bind_s(pw_username, pw_password)
	if l.compare_s(LDAP_ALLOWED_GROUP_DN, LDAP_ALLOWED_GROUP_ATTR, pw_username) == 1:
		exit(0)
except Exception, e:
	print('Authentication error: ' + str(e))

exit(1)