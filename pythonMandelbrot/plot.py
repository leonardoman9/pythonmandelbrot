from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER
from tqdm import tqdm
from itertools import product

# Image size (pixels)
WIDTH = 1800
HEIGHT = 1200

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x, y in tqdm(product(range(WIDTH), range(HEIGHT)), total = WIDTH * HEIGHT):
    # Convert pixel coordinate to complex number
    c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                IM_START + (y / HEIGHT) * (IM_END - IM_START))
    # Compute the number of iterations
    m = mandelbrot(c)
    # The color depends on the number of iterations
    color = 255 - int(m * 255 / MAX_ITER)
    # Plot the point
    draw.point([x, y], (color, color, color))

im.save('output.png', 'PNG')