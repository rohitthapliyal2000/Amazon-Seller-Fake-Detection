import progress_bar as pb
import time

# Fetching reviews for fake detection classifier
def fetching(fake_product_reviews, original_product_reviews):

	print("Phase 1...\n")
	pb.progress(0.0, 100)

	with open("dataset/fake_pro.txt", "r") as file:
		for line in file:
			fake_product_reviews.append(line)

	with open("dataset/original_pro.txt", "r") as file:
		for line in file:
			original_product_reviews.append(line)

	time.sleep(1)
