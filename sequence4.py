import random, sys, time, parsing4sensors, winsound

seq1 = [10, 1, 3, 6, 4]
seq2 = []
win = True

beeps = ["beep-01c.wav", "beep-02c.wav", "beep-04c.wav", "beep-06.wav", "beep-01&2.wav", "beep-01&3.wav", "beep-01&4.wav", "beep-02&3.wav", "beep-02&4.wav", "beep-03&4.wav"]

def make_seq():
    if len(seq1) < 3:
        num = random.randrange(1, 5)
    else:
        num = random.randrange(1, 11)
    seq1.append(num)
    for s in seq1:
        time.sleep(1)
        parsing4sensors.arduino_write(s)
        time.sleep(1.3)
        winsound.PlaySound(beeps[s-1], winsound.SND_FILENAME)
        time.sleep(.1)
        parsing4sensors.arduino_write(0)

def manual_seq():
    global seq1
    n = parsing4sensors.sensor_input()
    winsound.PlaySound(beeps[n-1], winsound.SND_FILENAME)
    seq1.append(n)
    for s in seq1:
        time.sleep(1)
        parsing4sensors.arduino_write(s)
        time.sleep(1.2)
        winsound.PlaySound(beeps[s-1], winsound.SND_FILENAME)
        time.sleep(.1)
        parsing4sensors.arduino_write(0)   

def input_seq():
    seq2 = []
    global win
    for i in range(0, len(seq1)):
        n = parsing4sensors.sensor_input()
        seq2.insert(i, n)
        win = compare_seq(seq1, seq2, i)
        if not win:
            print ("You got to level " + str(len(seq1)))
            time.sleep(.5)
            parsing4sensors.arduino_write('e')
            winsound.PlaySound("beep-05.wav", winsound.SND_FILENAME)
            time.sleep(.5)
            break
        

def compare_seq(seq1, seq2, i):
    return seq1[i] == seq2[i]
    

def main():
    time.sleep(2)
    while win:
        #manual_seq()
        make_seq()
        print(seq1)
        input_seq()


main()
 
