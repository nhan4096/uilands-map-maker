from PIL import Image

POPULATIONS = {
    'SpeedyMcTrash Province': 40,
    'Dininisour Province': 40,
    'Copycat Province': 40,
    'Copybetch Province': 25,
    'Will Wood City': 80,
    'Tapeworms City': 75,
    'Sim City': 150,
    'T7 City': 75,
    'Xitray City': 60,
    'Fist Province': 20,
    'Finger Province': 20,
    'Euler City': 60,
    'Thalès Province': 40,
}

def distance(col1, col2):
    return abs(col1[0] - col2[0]) + abs(col1[1] - col2[1]) + abs(col1[2] - col2[2])

def to_color(density):
    density /= 9.2
    density = max(0, min(1, density))
    red = 255
    green = int(255 * (1 - density))
    blue = int(255 * (1 - density))
    return (red, green, blue)

img = Image.open('uilands-map.png')
f = open('cities.txt', 'r')
lines = f.readlines()
lines = [l[:-1].split(';') for l in lines]
lines = [(tuple(map(int, [a.replace('(', '').replace(')', '') for a in l[0].split(',')])), l[1], float(l[2])) for l in lines]
f.close()

W, H = img.size
MAXDISTANCE = 2 # with outlines, for no outlines, use 175-180
for x in range(W):
    for y in range(H):
        r, g, b, a = img.getpixel((x, y))
        for k, v, area in lines:
            if distance((r, g, b), k) < MAXDISTANCE:
                img.putpixel((x, y), to_color(POPULATIONS[v]/area))

img.show()
img.save('uilands-map-density.png')