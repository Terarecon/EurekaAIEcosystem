
import Font

def drawPoint(buffer, x, y, value):

    if buffer.shape[0] > y and buffer.shape[1] > x:
        buffer[y,x] = value


def drawLine(buffer, startx, starty, endx, endy, value):

    # 2 points distance
    dx = abs(endx - startx)
    dy = abs(endy - starty)

    # points direction
    sx = 1 if endx >= startx else -1
    sy = 1 if endy >= starty else -1

    # If angle is smaller than 1
    if dx > dy:

        e = -dx

        for i in range(dx + 1):
            drawPoint(buffer, startx, starty, value)
            startx += sx
            e += 2 * dy
            if e < 0:
               continue

            starty += sy
            e -= 2 * dx

    else: # if angle is bigger than 1

        e = -dy
        for i in range(dy + 1):
            drawPoint(buffer, startx, starty, value)
            starty += sy
            e += 2 * dx
            if e < 0:
                continue
            startx += sx
            e -= 2 * dy


def fillBox(buffer, startx, starty, size, value):

    for y in range(starty, starty + size):
        for x in range(startx, startx + size):
            drawPoint(buffer, x, y, value)
   
def drawString(buffer, startx, starty, size, str, value):

    x = startx
    for ch in str:
        if ch == '\n':
            x = startx
            starty += 8
            continue

        drawChar(buffer, x, starty, size, ch, value)
        x += size * 5 # because 5x8 font

def drawChar(buffer, startx, starty, size, c, value):

    if ord(c) < 0x20 or ord(c) > 0x7e:
        return;

    f = Font.Font5X8[ord(c) - 0x20];

    for y in range(len(f)):

        f0 = f[y]

        for b in range(5):
            if f0 & (1 << (7 - b)) != 0:
                fillBox(buffer, startx + b * size, starty + y * size, size, value)
