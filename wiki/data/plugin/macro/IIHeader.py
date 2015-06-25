# ionicons with headers
# (unfortunately headers in MoinMoin can't contain macros)
def macro_IIHeader(macro, icon, text, level=1):
        return '<h%s><i class="icon ion-%s"></i> %s</h%s>' % (level, icon, text, level)

