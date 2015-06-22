from MoinMoin import wikiutil
import os

class FFCommon:

	def __init__(self):
		#dir = os.getenv('HOME') + '/tmp/ffks_network_stats/'
		self.dir = '/home/ffks/tmp/ffks_network_stats/'
		self.values = ('clients', 'link_percentage', 'links', 'nodes')
		self.suffix = '_diff'
		self.files = []
		self.files_diff = []

		# disable caching to display recent changes
		#Dependencies = []

		# give lists absolute paths
		for i in range(len(self.values)):
			self.files.append(self.dir + self.values[i])
			self.files_diff.append(self.dir + self.values[i] + '_diff')

	def read_file(self, path):
		f = open(path)
		ret = f.read()
		f.close()
		return ret

	def print_val(self, n):
		val = self.read_file(self.files[n])
		return val + "%" if n is 1 else val

	def print_diff(self, n):
		col_pre_good = '<span style="padding:4px;color:white;background-color:green">'
		col_pre_bad = '<span style="padding:4px;color:white;background-color:red">'
		col_suf = "</span>"
		val = self.read_file(self.files_diff[n])
		pval = val + "%" if n is 1 else val
		if int(val) > 0:
			pval = col_pre_good + pval + col_suf
		elif int(val) < 0:
			pval = col_pre_bad + pval + col_suf
		else:
			pval = "-"
		return pval
		# where is the macro imported from? needed for xml output
		#return macro.formatter.text("NODECOUNT: %d" % (val, diff))

