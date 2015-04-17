#-*- coding: utf-8 -*-
# python 2

myStr = u'α'

# # Bad. This is a error.
print 'Greek alpha: ', myStr

# Good
print 'Greek alpha: ', myStr.encode("utf-8")