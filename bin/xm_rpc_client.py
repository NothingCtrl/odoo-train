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
import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'OdooTrain'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/2/' % (HOST, PORT)
url = 'http://localhost:8069'

common = xmlrpclib.ServerProxy(ROOT + 'common'.format(url))
print common.version()

uid = common.authenticate(DB, USER, PASS, {})

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute_kw,
    DB, uid, PASS)

sessions = call('openacademy.session', 'search_read', [], {'fields': ['name', 'seats']})

for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

# 3.create a new session
course_id = call('openacademy.course', 'search', [[['name', 'ilike', 'Course']]])[0]

session_id = call('openacademy.session', 'create', [{
    'name': 'My session 22',
    'course_id': course_id,
}])
