from PIL import Image

img = Image.open('uilands-map.png')
UILANDS_AREA = 134.7
W, H = img.size
OCEAN = (144, 218, 238)

def distance(col1, col2):
    return abs(col1[0] - col2[0]) + abs(col1[1] - col2[1]) + abs(col1[2] - col2[2])

DISTANCE = 108

pxcount = 0
for x in range(W):
    for y in range(H):
        r, g, b, a = img.getpixel((x, y))
        if distance((r, g, b), OCEAN) > DISTANCE:
            pxcount += 1
px_to_area = lambda px: UILANDS_AREA / pxcount * px

def city_area(search_color):
    citypx = 0
    for x in range(W):
        for y in range(H):
            r, g, b, a = img.getpixel((x, y))
            if distance((r, g, b), search_color) < DISTANCE:
                citypx += 1

    return round(px_to_area(citypx), 2)

COLOR_CODES = {
    (236, 28, 36): 'Sim City',
    (6, 40, 6): 'Fist Province',
    (255, 127, 39): 'Finger Province',
    (184, 61, 186): 'Thalès Province',
    (14, 209, 69): 'Dininisour Province',
    (63, 72, 204): 'T7 City',
    (255, 174, 200): 'Xitray City',
    (185, 122, 86): 'Euler City',
    (88, 88, 88): 'Tapeworms City',
    (136, 0, 27): 'Will Wood City',
    (0, 169, 243): 'Copycat Province',
    (255, 242, 0): 'Copybetch Province',
    (255, 0, 119): 'SpeedyMcTrash Province'
}

f = open('cities.txt', 'a')

s = 0 
for k, v in COLOR_CODES.items():
    area = city_area(k)
    print(f'{v}: {area}km2')
    f.write(f'{k};{v};{area}\n')
    s += area
f.close()
print(f'Total area: {s}km2')