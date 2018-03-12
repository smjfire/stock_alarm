import urllib

#req = urllib.urlopen('http://www.webhard.co.kr')

req = urllib.urlopen('http://files.cloud.naver.com/file/checkupload.api')

if req == req.err :
	print "denied"
	
	

s=req.read()

#print s




'''
if (s.find("mailto:sgh_policy@smilegate.com")) > 0 :
	print "Denied"
		
else :
	print "Open"

req.close()
'''


for 