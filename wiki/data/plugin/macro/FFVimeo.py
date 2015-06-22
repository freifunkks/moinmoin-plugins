def macro_FFVimeo(macro, width, height, id):
	width = int(width)
	height = int(height)
	id = int(id)
	if width <= 0:
		return 'Error with video width'
	if height <= 0:
		return 'Error with video height'
	return '<iframe src="https://player.vimeo.com/video/%s" width="%s" height="%s" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>' % (id, width, height)

