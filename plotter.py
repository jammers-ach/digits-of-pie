import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


last_digits = [0,0,0,0]

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
    for i in range(len(last_digits)-1):
        last_digits[i] = last_digits[i+1]
    last_digits[3] = current_digit
    plt.text(0,10,'%d%d%d%d' % (last_digits[0],last_digits[1],last_digits[2],last_digits[3]))
    plt.text(0,10.4,'digit: %09d' % digit_number)

    plt.savefig('images/%09d.png' % digit_number)
    #plt.show()

