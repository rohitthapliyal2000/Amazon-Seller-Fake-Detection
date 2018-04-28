# Handling negation: "not good", "not worth it"

def hack(rev):

	for i in range(0, len(rev)):

		line = rev[i].split()

		for it in range(0, len(line)):

			if line[it] == 'no' or line[it] == 'not' or line[it] == 'nope' or line[it] == 'never' or line[it] == "isn't" or line[it] == "don't" or line[it] == "dont" or line[it] == "wasn't":

				j = it

				while j < len(line) and j < it + 4:
					line[j] = "!" + line[j]
					j += 1


		line = ' '.join(line)
		rev[i] = line
