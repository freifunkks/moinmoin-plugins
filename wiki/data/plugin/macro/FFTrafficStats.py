# -*- coding: utf-8 -*-
import json
import ffcommon

sourceUrl = 'http://api.ffks.de/traffic.json'
monthsDict = {1:'Januar', 2:'Februar', 3:u'März', 4:'April', 5:'Mai', 6:'Juni', 7:'Juli', 8:'August', 9:'September', 10:'Oktober', 11:'November', 12:'Dezember'}

def mag(n):
	sizeDict = {0:'K', 1:'M', 2:'G', 3:'T', 4:'P'}
	div = 1024
	i = 0
	m = n
	while n > div and i <= len(sizeDict):
		i += 1
		n /= float(div)
	ret = "%s %s" % (round(n, 2), sizeDict[i])
	return "%siB" % ret
		

def macro_FFTrafficStats(macro):
	traffic = json.loads(ffcommon.FFCommon().get_file(4))
	#return str(json.dumps(traffic, sort_keys=True, indent=4, separators=(',', ': ')))
	months = traffic['interfaces'][0]['traffic']['months']
	ret = "<table><tbody>"
	ret += "<tr class=\"header\"><td>Jahr</td><td>Monat</td><td>RX</td><td>TX</td></tr>"
	rx = 0
	tx = 0
	for m in months:
		rx += m['rx']
		tx += m['tx']
		ret += "<tr>"
		mon = str(m['date']['month'])
		ret += "<td>%s</td>" % str(m['date']['year'])
		ret += "<td style=\"text-align:right\">%s</td>" % monthsDict[m['date']['month']]
		ret += "<td style=\"text-align:right\">%s</td>" % mag(m['rx'])
		ret += "<td style=\"text-align:right\">%s</td>" % mag(m['tx'])
		ret += "</tr>"
	ret += "<tr class=\"footer\"><td>Gesamt</td><td></td><td style=\"text-align:right\">%s</td><td style=\"text-align:right\">%s</td></tr>" % (mag(rx), mag(tx))
	ret += "</tbody></table>"
	ret += "<p><a href=\"%s\">Quelldaten</a></p>" % sourceUrl
	return ret

