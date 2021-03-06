'''
A simple script that makes an animated version of the digits of pi

'''
from __future__ import division
import operator
from plotter import plot

digit_count = 0 # counting our digits
digit_distribution = dict([ (x,0) for x in range(0,10)]) #distribution of digits


filename = 'million_pi.txt' #filename with the digits
limit = 9000 #when do we stop

def dominant_digit():
    '''which digit so far has appeared the most'''
    sorted_distribution = sorted(digit_distribution.items(), key=operator.itemgetter(1))
    dominant = sorted_distribution[-1]
    return dominant

def progress_print(digit):
    '''Does a simple console print of our progress'''
    print "Digit %11s %d"% (digit_count,dominant_digit()[0])
    #print digit_distribution_percentage(),dominant_digit()
    plot(digit_distribution_percentage(),digit_count,digit)

def digit_distribution_percentage():
    '''Digit distribution but as a %'''
    dominant_percent = [(k,(v/ digit_count)  * 100) for k,v in digit_distribution.items()]
    return dominant_percent


#Read in the file
f = open(filename,'r')

for line in f:
    for c in line:
        if(c.isdigit()):
            digit_count += 1
            digit_distribution[int(c)] += 1
            progress_print(int(c))

        if(digit_count >= limit):
            print "END"
            break
    if(digit_count >= limit):
        print "END"
        break
f.close()
