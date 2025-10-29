#!/usr/bin/python3

### main.py
#
# RUN:
# DEP:
#
# ...
#
# ---
#  HansMoleman (c) October 25, 2025.
# ---
##

import psutil
import time



if __name__ == "__main__":
	wait_time = 0.5
	data_path = "data.csv"
	elapsed = 0
	#fobj = None

	try:
		fobj = open(data_path, 'a')
		wstr = ""

		while True:
			cpu_usage = psutil.cpu_percent(interval=None)
			elapsed += wait_time
			wstr = f"{elapsed}, {cpu_usage}\n"
			fobj.write(wstr)
			print(f"CPU@{elapsed}:  {cpu_usage}")
			time.sleep(wait_time)
	except:
		print()
	finally:
		fobj.close()