import matplotlib.pyplot as plt

v1_time_elapsed = []
v2_time_elapsed = []
v_data_set = []
def converter(time_elapsed_line):
    curr_time_elapsed = []
    for j in range(len(time_elapsed_line)):
        if (time_elapsed_line[j].isalpha()): break
        curr_time_elapsed.append(time_elapsed_line[j])
    return float("".join(curr_time_elapsed))

def scraper(num: int):
    k = ["{:03d}".format(i) for i in range(1, 101)]
    n = 0
    for i in range(100):
        data_scraped = []

        file_path = f'lab8\\matrix-v{num}-runs\\matrix-v{num}.{k[i]}.txt'

        with open(file_path, 'r') as file:
            line = file.readline()
            while line:
                n+=1
                data_scraped.append(line.strip())
                line = file.readline()

        time_elapsed_line = data_scraped[13]

        arr = f"v{num}_time_elapsed"
        
        globals()[arr].append(converter(time_elapsed_line))


def average(v):
    return sum(v) / 100

def grapher(data_set):
    plt.boxplot(data_set, patch_artist=True, label=True)
    plt.xlabel("Matrix dataset")
    plt.ylabel("Time elapsed (secs)")
    plt.show()

def main():
    scraper(1)
    scraper(2)
    v_data_set.append(v1_time_elapsed)
    # print(v1_time_elapsed)
    v_data_set.append(v2_time_elapsed)

    grapher(v_data_set)
main()
    

