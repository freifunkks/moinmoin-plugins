# Font Awesome Icons with headers
# (unfortunately headers in MoinMoin can't contain macros)
def macro_FAHeader(macro, icon, text, level=1):
        return '<h%s><i class="fa fa-%s"></i> %s</h%s>' % (level, icon, text, level)

