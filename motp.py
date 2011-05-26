#!/usr/bin/env python
## based from:
## http://motp.sourceforge.net
## http://motp.sourceforge.net/motp_in_php.inc

import time, sys
from hashlib import md5

otp=sys.argv[1]
pin='5555'
secret='6377e84e4cc814b7'
offset=1 # in minute

__author__='Edelberto S. Mania <sierra2@gmail.com>'
__date__='20110526'

def isValidOTP(pin,otp,secret):
	"""
	check validty of the supplied OTP
	"""
	max_period=offset*60 # in seconds = +/- $offset minutes
	t_time=int(time.time())
	i=t_time-max_period
	while i<=t_time+max_period:
		m=str(i)[:-1]+secret+pin
		h=md5(m).hexdigest()[:6]
		if otp==h:return True
		i+=1
	return False


## test
print isValidOTP(pin,otp,secret)


