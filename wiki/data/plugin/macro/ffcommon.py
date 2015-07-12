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
        icon_good = 'caret-up'
        icon_bad= 'caret-down'
        icon_neutral = 'caret-right'
        cls_good = 'stats-good'
        cls_bad = 'stats-bad'
        cls_neutral = 'stats-neutral'
        stats = '<span class="%s">%s <i class="fa fa-%s"></i></span>'
        val = self.read_file(self.files_diff[n])
        pval = str(abs(int(val))) + "%" if n is 1 else abs(int(val))
        if int(val) > 0:
            cls = cls_good
            icon = icon_good
        elif int(val) < 0:
            cls = cls_bad
            icon = icon_bad
        else:
            cls = cls_neutral
            icon = icon_neutral
        html = "asdf"
        html = stats % (cls, pval, icon)
        return html
        # where is the macro imported from? needed for xml output
        #return macro.formatter.text("NODECOUNT: %d" % (val, diff))

