from chrplotlib import img

img_plotter = img.ImagePlotter()

for name in img_plotter.get_all_names():
    print(f"name:{name}")
    print(img_plotter.from_name(name=name))
