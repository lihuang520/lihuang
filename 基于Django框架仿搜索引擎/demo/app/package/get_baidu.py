#codning = utf-8
import urllib2


def get_info(wd):
	req = urllib2.Request('https://www.baidu.com/s?wd=%s' %wd)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')
	html = urllib2.urlopen(req).read()
	return html