
import os

dir="/home/cs21FWX1/Desktop/lab8/part3/16k-runs-0"

for i in range(1,101):
    dst = "transpose-0.{:03d}.txt".format(i)
    src = "transpose-0.{:03d}".format(i)
    source = f"{dir}/{src}"
    dest = f"{dir}/{dst}"

    os.rename(source, dest)