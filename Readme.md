# Background Remover
This Python script uses the rembg library to remove the background from an image. The script allows you to select an image file using a file dialog and then processes the image, saving the output with the background removed as "output.png".

## Prerequisites
Ensure you have the required modules installed before running the script. You can install them using the following command:

## How to run the project

1. Clone the repository

```bash
git clone 

```

2. Install the rembg pillow library

```python

pip install rembg pillow

```

3. Run the main file using python main.py

```python

python3 main.py

```

A file dialog will appear, prompting you to select an image file.

## Choose the image file you want to process.

The script will remove the background from the selected image and save the result as "output.png" in the same directory as the script.

```
import rembg
from PIL import Image
from tkinter import filedialog
from tkinter import Tk
```

Import the necessary modules: rembg for background removal, Image from the PIL library for image processing, and filedialog along with Tk from the tkinter library for file selection.

```
root = Tk()
root.withdraw()
```