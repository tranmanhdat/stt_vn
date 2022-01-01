import os
import matplotlib.pyplot as plt
folder = "statistic/log_data"
files = os.listdir(folder)
files = sorted(files, key=lambda x: int(x.split("_")[0]))
print(files)
wer_train = []
wer_test = []
curr_epoch = 0
number_repeat = 0
sum_train_wer = 0
sum_test_wer = 0
for file in files:
    path_file = os.path.join(folder, file)
    data = open(path_file, "r+").readlines()
    for line in data:
        elements = line.split("|")
        epoch = int(elements[0].split()[-1])
        for element in elements:
            if element.__contains__("train-WER"):
                train_wer = float(element.split()[-1])
            elif element.__contains__("test.lst-WER"):
                test_wer = float(element.split()[-1])
        if epoch>curr_epoch:
            if curr_epoch==0:
                curr_epoch=1
                number_repeat=1
                sum_train_wer += train_wer
                sum_test_wer +=test_wer
                continue
            wer_train.append(sum_train_wer/number_repeat)
            wer_test.append(sum_test_wer/number_repeat)
            curr_epoch = epoch
            print(curr_epoch)
            number_repeat = 1
            sum_train_wer = train_wer
            sum_test_wer = test_wer
        else:
            number_repeat += 1
            sum_train_wer += train_wer
            sum_test_wer += test_wer
wer_train.append(sum_train_wer / number_repeat)
wer_test.append(sum_test_wer / number_repeat)
print(wer_train)
print(wer_test)
x = [i for i in range(1,len(wer_test)+1)]
print(x)
import numpy as np
fig, ax = plt.subplots()


ax.plot(x, wer_train, label='train',color='green')
ax.plot(x, wer_test, label='test',color='red')

ax.set_xlabel('Epoch')  # Add an x-label to the axes.
ax.set_ylabel('WER')  # Add a y-label to the axes.
ax.set_xlim(0,35)
ax.set_ylim(0,100)


# ax.set_xticks(major_ticks_top)
# ax.set_yticks(major_ticks_top)
# ax.set_xticks(minor_ticks_top,minor=True)
minor_ticks_x=np.linspace(0,35,36)
ax.set_xticks(minor_ticks_x,minor=True)


minor_ticks_top=np.linspace(0,100,21)
ax.set_yticks(minor_ticks_top,minor=True)

ax.grid(which="minor",alpha=0.3)
ax.grid()
# ax.set_title("WER")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()