
import os

for i in range(1,101):
    dest = "matrix-v2.{:03d}.txt".format(i)
    source = "/home/cs21FWX1/Desktop/lab8/part2/matrix-v2-runs/matrix-v2.{:03d}c".format(i)
    dest = "/home/cs21FWX1/Desktop/lab8/part2/matrix-v2-runs/{dest}"

    os.rename(source, dest)