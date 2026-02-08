# Maya Constrain Locator to Vertex

A PyMEL script for Autodesk Maya that attaches a locator to a specific vertex on a mesh using a follicle, enabling precise vertex tracking for rigging, animation, or technical setups.

This tool is especially useful for workflows that require locators to follow a vertex accurately, such as animation fixes, simulations, or VR/CG research setups.

---

## Features

- Attach a locator to a single vertex on a mesh.
- Automatically creates a follicle to maintain vertex tracking.
- Connects mesh output and world matrix to the follicle for consistent behavior.
- Supports both translation and rotation constraints.
- Ideal for rigging, animation technical fixes, and experimental setups in Maya.

---

## Installation

1. Place `ConstrainLocatorToVertex.py` in your Maya scripts folder.  
   - On Windows: `Documents\maya\scripts\`  
   - On macOS: `~/Library/Preferences/Autodesk/maya/scripts/`  
   - On Linux: `~/maya/scripts/`

2. Start Maya and open the Script Editor.

3. Import the script:
```python
import ConstrainLocatorToVertex
