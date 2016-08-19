# import functools
# import xmlrpclib
#
# HOST = 'localhost'
# PORT = 8069
# DB = 'OdooTrain'
# USER = 'admin'
# PASS = 'admin'
# ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
#
# # 1. Login
# uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
# print "Logged in as %s (uid:%d)" % (USER, uid)
#
# call = functools.partial(xmlrpclib.ServerProxy(ROOT + 'object').execute, DB, uid, PASS)
#
# # 2. Read the sessions
# sessions = call('openacademy.session', 'search_read', [], ['name', 'seats'])
# for session in sessions:
#     print "Session %s (%s seats)" % (session['name'], session['seats'])
# # 3.create a new session
# session_id = call('openacademy.session', 'create', {
#     'name': 'My session',
#     'course_id': 2,
# })

import xmlrpclib
url = 'http://localhost:8069'
db = 'OdooTrain'
username = 'admin'
password = 'admin'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
sessions = models.execute_kw(db, uid, password, 'openacademy.session', 'search', [])

for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

