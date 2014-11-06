import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

last_digit = 0


def plot(distribution,digit_number,current_digit):
    global last_digit

    y_data,x_data = zip(*distribution)
    y_pos = np.arange(len(y_data))
    plt.clf()
    plt.xlim([0,100])
    plt.ylim([-1,11])
    plt.xlabel('Digit')
    plt.ylabel('%')
    plt.barh(y_pos, x_data, align='center', alpha=0.4)
    plt.yticks(y_pos, y_data)
    plt.text(0,10,'%d%d' % (last_digit,current_digit))
    plt.text(0,10.4,'%09d' % digit_number)

    plt.savefig('images/%09d.png' % digit_number)
    #plt.show()
    last_digit = current_digit
