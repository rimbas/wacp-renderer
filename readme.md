# whack ass crystal prison renderer

![](wacp-zczLApC.gif)

Needs Python 3.11 because Blender Python module (currently 4.4.0) is on Python 3.11. Make a virtualenv if not on 3.11.
```bash
pip install bpy pillow
```

# how to run
1. On Windows - drag and drop an image onto the `render.bat`

OR 
```bash
py -3.11 main.py IMAGE_FILENAME
```
OR if python is 3.11
```bash
python3 main.py IMAGE_FILENAME
```

# customisation
1. Open `scene.blend` (preferably also in Blender 4.4.0 for compatibility)
2. Change things in scene
	- Script expects `textureMaterial` blender material to exist
	- Script expects animation render operation to output to `//output/image`
	- Anything else goes
3. Save scene
4. Re-render
