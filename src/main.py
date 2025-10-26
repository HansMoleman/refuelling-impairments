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

	try:
		while True:
			cpu_usage = psutil.cpu_percent(interval=None)
			print(f"CPU:  {cpu_usage}")
			time.sleep(wait_time)
	except:
		print()