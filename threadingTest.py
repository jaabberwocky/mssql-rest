import multiprocessing
import requests
import numpy as np
import time
import sys

def getRespTime(URL):
	r = requests.get(URL)
	q.put(r.elapsed.total_seconds())
	return None

if __name__=="__main__":

	print("Initiating test...")
	tic = time.time()

	totalThreads = 1000
	URL = "https://www.google.com.sg"

	if len(sys.argv) == 3:
		totalThreads = int(sys.argv[1])
		URL = sys.argv[2]
	elif len(sys.argv) == 2:
		totalThreads = int(sys.argv[1])

	q = multiprocessing.Queue()
	processes = []

	for _ in range(totalThreads):
		if _ % 100 == 0:
			print("Thread %d started"%_)
		p = multiprocessing.Process(target=getRespTime, args=[URL])
		p.start()

	# consume from Queue
	totalSeconds = []
	while q.empty() == False:
		totalSeconds.append(q.get())

	# wait for all processes to finish first
	for p in processes:
		p.join()
	
	toc = time.time()
	
	print("Threads returned: %d/%d" % (len(totalSeconds), totalThreads))
	print("Average response time: %.2fs" % np.mean(totalSeconds))
	print("Load test of %d completed in %.2fs" % (totalThreads, toc-tic))