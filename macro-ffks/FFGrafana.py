def macro_FFGrafana(macro, days=7, width=600, height=400):
	width  = int(width)
	height = int(height)
	if height <= 0:
		return 'Error with stats height'
	if width <= 0:
		return 'Error with stats width'

	return '<img src="https://stats.freifunk-kassel.de/render/dashboard-solo/file/overview.json?panelId=1&fullscreen&theme=light&from=now-{0}d&to=now&width={1}&height={2}" alt="Statistik-Graph" />'.format(days, width, height)
