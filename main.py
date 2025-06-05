#!/bin/env python3
from math import ceil
import sys, os
from PIL import Image
from pathlib import Path
import bpy
import bpy_extras.image_utils

bpy.ops.wm.open_mainfile(filepath="scene.blend")
scene = bpy.context.scene
frame_count = scene.frame_end
framerate = ceil(1000 / scene.render.fps * scene.render.fps_base)

if __name__ == "__main__":
	if len(sys.argv) == 2 and os.path.isfile(filepath := Path(sys.argv[1])):
		new_filename = f"wacp-{filepath.stem}.gif"
		new_image = bpy_extras.image_utils.load_image(os.path.abspath(filepath), dirname=os.path.abspath(filepath))
	else:
		print("No image argument provided")
		input()
		sys.exit(1)

	for node in bpy.data.materials["textureMaterial"].node_tree.nodes:
		if node.type == "TEX_IMAGE":
			node.image = new_image

	bpy.ops.render.render(animation=True)

	frames = [Image.open(f"output/{img}") for img in sorted(os.listdir("output"))]

	frames[0].save(new_filename, "GIF", save_all=True, append_images=frames[1:], duration=framerate, loop=0, disposal=2)
else:
	print("huh")
	input()