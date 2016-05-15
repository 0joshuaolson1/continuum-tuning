notesPerSide, middle = 18, "A"

from decimal import Decimal
newLeft = newRight = 60 #MIDI middle C
leftDs = [2, 2, 1, 2, 2, 1, 2]
rightDs = [2, 1, 2, 2, 1, 2, 2]
dOld = 0
for i in range("ABCDEFG".index(middle)):
    leftDs = leftDs[1:] + leftDs[:1]
    rightDs = rightDs[1:] + rightDs[:1]
func = {}
for i in range(notesPerSide + 2):
    func[62 - dOld] = newLeft #the center key of half sizes isn't middle C
    func[62 + dOld] = newRight
    newLeft -= leftDs[0]
    newRight += rightDs[0]
    leftDs = leftDs[-1:] + leftDs[:-1]
    rightDs = rightDs[1:] + rightDs[:1]
    dOld += 23.0 / notesPerSide #there are 23 default keys each side of center
for note in sorted(list(func)):
    formatted = str(Decimal(note).quantize(Decimal("1.000")))
    print(formatted + ", " + str(func[note]) + ".000")
