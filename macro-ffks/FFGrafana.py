def macro_FFGrafana(macro, days=7, height=300):
	height = int(height)
	if height <= 0:
		return 'Error with stats height'
	return '<iframe src="https://stats.freifunk-kassel.de/dashboard-solo/db/overview?panelId=1&fullscreen&theme=light&from=now-{0}d&to=now" width="100%" height="{1}" frameborder="0"></iframe>'.format(days, height)
