
import os

for i in range(1,101):
    dest = "matrix-v1.{:03d}.txt".format(i)
    src = "matrix-v1.{:03d}c".format(i)
    source = f"/home/cs21FWX1/Desktop/lab8/part2/matrix-v1-runs/{src}"
    dest = f"/home/cs21FWX1/Desktop/lab8/part2/matrix-v1-runs/{dest}"

    os.rename(source, dest)