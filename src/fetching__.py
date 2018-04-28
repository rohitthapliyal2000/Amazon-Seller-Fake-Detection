import progress_bar as pb
import time

# Fetching reviews for sentiment analysing classifier
def fetching(neg_rev, pos_rev):

	time.sleep(1)
	pb.progress(20.0, 100.0)

	with open("dataset/neg.txt") as file:
		for line in file:
			neg_rev.append(line.lower())

	time.sleep(1)
	pb.progress(40.0, 100.0)

	with open("dataset/pos.txt") as file:
		for line in file:
			pos_rev.append(line.lower())

	time.sleep(1)
	pb.progress(60.0, 100.0)
