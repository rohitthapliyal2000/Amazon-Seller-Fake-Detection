import sys

def progress(count, total, cond=False):

	bar_len = 100
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)

	if cond == False:
		sys.stdout.write('[%s] %s%s\r' % (bar, percents, '%'))
		sys.stdout.flush()

	else:
		sys.stdout.write('[%s] %s%s' % (bar, percents, '%'))
