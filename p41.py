from colored import fg, bg, attr
print ('%s Hello World !!! %s' % (fg(2), attr(1)))
print ('%s%s Hello World !!! %s' % (fg(1), bg(15), attr(1)))