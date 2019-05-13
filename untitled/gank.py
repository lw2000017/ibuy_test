# coding:utf-8

# import unittest
import hashlib


invitee = '15211111009'
code = '523834'

sign_text = 'APP_SIGN' + '{}{}'.format(invitee, code)

for n in range(2):
    m = hashlib.md5()
    m.update(b'%s' % sign_text.encode())
    sign_result = m.hexdigest()
    sign_text = sign_result
