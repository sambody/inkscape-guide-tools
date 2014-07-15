Inkscape guide tools
===================

These are a series of [Inkscape](http://inkscape.org/) extensions related to guides.

### The current extensions are:

### 1. Add centered guides to the document

With this extension you can quickly add a horizontal and/or a vertical guide through the center of the document.

![Add centered guides](img/centered.png)

### 2. Add margin guides to document

Inkscape already allows you to add guides exactly on the borders of the page, with **Edit > Guides around page**. With this extension however, you can add guides at a certain distance (margin) from the borders of the document. Add them all at once (for equal margins) or separately. Margins can be negative for guides outside the page borders. Zero margin guides are not drawn - use the mentioned Guides around Page for that.

![Add margin guides](img/margins.png)

### 3. Remove all or selected guides

- **Remove All Guides** (no user interface) - actually made by heathenx, bundled here with his permission. See [this blog post](http://screencasters.heathenx.org/blog/2009/06/09/inkscape-extension-remove-guides/) and [this forum topic](https://www.ruby-forum.com/topic/188929). I've just moved the menu item to Extensions > Guides; this functionality may become part of inkscape in upcoming version 0.49
- **Remove Selected Guides**: remove all horizontal and/or vertical and/or angled (diagonal) guides. Based on heathenx's extension. Useful for example when you need to change to different grid columns (vertical guides), but want to keep your existing horizontal guides.

![Remove selected guides](img/remove.png)

### How to install the extensions

1. Download the zip archive to your computer;
2. Unzip (extract) the archive on your computer;
3. Open it. In the folder "extensions", you will find the extension files - they come in pairs, an .inx and .py file for each extension. You can select them all, or only the ones you need. Copy the chosen files into your Inkscape extensions folder:

- on Windows: "C:\Program Files\Inkscape\share\extensions"
- on Linux: " /home/yourusername/.config/inkscape/extensions" (.config is a hidden folder)
- on OS X: "/Applications/Inkscape.app/Contents/Resources/extensions" 

Restart or open Inkscape.

### Where to find them

The extensions will all be available in the menu under **Extensions > Guide**.

### Guides in a grid - columns and rows with gutters

Need to create guides in a grid of columns (or rows) with gutters? See the [Inkscape Grid Maker extension](https://github.com/sambody/inkscape-grid-maker), which I made for that purpose - useful for web design for example. 

### Tips

- To add guides on the borders of your page, go to *Edit > Guides Around the Page*
- To divide your document into equal parts (with no gutters), you could use [Guides Creator](http://code.google.com/p/inkscape-guides-creator/) (part of Inkscape by default, located under Extensions > Render > Guides Creator), by Jonas Termeau. With option for proportional divisions (rule of thirds, golden rule). Limited to maximum 10 divisions, no gutters, no margins. 
- You can add a keyboard shortcut to an inkscape extension (manually, by editing an xml file with user keyboard shortcuts)

### Licence

These guide extensions are licenced under the GPL v2.

Author: Samuel Dellicour