def macro_FFGrafana(macro, days=7, height=300):
	height = int(height)
	if height <= 0:
		return 'Error with stats height'
        return '<iframe src="https://stats.freifunk-kassel.de/dashboard-solo/db/overview?panelId=1&fullscreen&theme=light&from=now-%sd&to=now" width="100%" height="%s" frameborder="0"></iframe>' % (days, height)
