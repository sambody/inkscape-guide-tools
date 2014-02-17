Inkscape guide tools
===================

These are a series of [Inkscape](http://inkscape.org/) extensions related to guides - generating, deleting, moving etc. Work in progress.

### The extensions are:

### 1. Remove guides

Three simple extensions:

- remove all guides (may be part of core inkscape in upcoming version 0.49)
- remove all horizontal guides
- remove all vertical guides

### 2. Add centered guides to the document

With this extension you can 

- add a horizontally centered guide to the document
- or a vertically centered guide
- or both at once.

(add centered guides to selection/bounding box coming soon)

### 3. Add margin guides to document

Add guides at a certain distance (margin) from the borders of the document. Margins can be equal or different for every side.

### How to install the extensions

1. Download the zip archive to your computer;
2. Unzip (extract) the archive on your computer;
3. Open it. In the folder extensions, you will find the extension files (.inx and .py files). You can select them all, or only the ones you need. Copy the chosen files into your Inkscape extensions folder:

- on Windows: "C:\Program Files\Inkscape\share\extensions"
- on Linux: " /home/yourusername/.config/inkscape/extensions" (.config is a hidden folder)
- on OS X: "/Applications/Inkscape.app/Contents/Resources/extensions" 

Restart or open Inkscape.

### Where to find them

The extensions will all be available in the menu under **Extensions > Guide**

### Other extensions

Other guides related extensions for Inkscape:

- The [Inkscape Grid Maker extension](https://github.com/sambody/inkscape-grid-maker), which I made to generate guides in a grid of columns/rows with gutters - useful for web design for example.
- Guides Creator (part of Inkscape by default), by Jonas Termeau - to divide your document into equal parts, or in proportional parts (rule of thirds, golden rule). Limited to 10 divisions, no gutters. I've used that extension as a base to make my extensions, so thanks to Jonas' work.

### Tips

- You can add a keyboard shortcut to any extension. (todo: step by step instructions; for now google it)

### News

- February 17, 2014: added margin guides
- February 16, 2014: initial commit, added delete guides, added centered guides

### Licence

All my extensions are licenced under the GPL v2.

Author: Samuel Dellicour