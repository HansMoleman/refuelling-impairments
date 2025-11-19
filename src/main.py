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

import os
import psutil
import time



if __name__ == "__main__":
	wait_time = 0.5
	data_path = "data.csv"
	elapsed = 0
	#fobj = None

	try:
		home_path = os.path.dirname(os.path.abspath(__file__))
		if os.path.isfile(f"{home_path}/{data_path}"):
			os.remove(f"{home_path}/{data_path}")
		fobj = open(data_path, 'a')
		wstr = ""

		while True:
			cpu_usage = psutil.cpu_percent(interval=None)
			ram_usage = psutil.virtual_memory().percent
			elapsed += wait_time

			wstr = f"{elapsed}, {cpu_usage}, {ram_usage}\n"
			fobj.write(wstr)
			print()
			print(f"CPU@{elapsed}:  {cpu_usage}")
			print(f"RAM@{elapsed}:  {ram_usage}")
			time.sleep(wait_time)
	except:
		print()
	finally:
		fobj.close()