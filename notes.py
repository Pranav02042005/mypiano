note='C4 C#4 D4 D#4 E4 F4 F#4 G4 G#4 A4 A#4 B4 C5 C#5 D5 D#5 E5 F5 F#5 G5 G#5 A5 A#5 B5 '
keybord_input ='A W S E D R F T G Y H U J I '
white_input='A S D F G H J'
black_input='W E R T Y U I'
note_list= note.split()
key_input=keybord_input.split()
white_keys='C D E F G A B'.split()
black_keys='C# D# F# G# A#'.split()

def search(k_input,start):
    octave=note_list[start:start+12]
    if k_input in setting(start):
        a=setting(start).index(k_input)
    return octave[a]




def setting(start):
    key_input = keybord_input.split()
    removal = []
    if start==0:
        removal.append(['R','I'])
    elif start==1:
        removal.append(['E','U'])
    elif start==3:
        removal.append(['W','Y'])
    elif start==4:
        removal.append(['I', 'T'])
    elif start == 5:
        removal.append(['U', 'R'])
    elif start == 6:
        removal.append(['Y', 'E'])
    elif start == 7:
        removal.append(['T', 'W'])
    for i in removal[0]:
        key_input.remove(i)
    return key_input



