# Font Awesome Button
#def macro_FAButton(macro, icon, text, color="blue", width=0, height=0):
# kwargs:
#  color: magenta, blue, yellow
#  width: n, n%
#  height: n, n%
#  fontsize: n (px)
from cgi import escape

def macro_FAButton(macro, icon, text, link, _kwargs={}):
	#if _kwargs is not None:
	#	for key, value in _kwargs.iteritems():
	#		test += "%s = %s" % (key, value)
	color = _kwargs.pop('color', 'blue')
	width = _kwargs.pop('width', 'auto')
	height = _kwargs.pop('height', 'auto')
	fontsize = _kwargs.pop('fontsize', 'auto')

	style = 'width:%spx;height:%spx;font-size:%spx' % (width, height, fontsize)
	cls_btn = color if color in ['magenta', 'blue', 'yellow'] else 'blue'

	escape(style)
	escape(icon)
	escape(text)

	return '<form action="%s"><button class="%s" style="%s"><i class="fa fa-%s"></i> %s</button></form>' % (link, cls_btn, style, icon, text)

