#!/usr/bin/env python
'''
Add margin guides,
extension by Samuel Dellicour,

The extension adds document margin guides: guides at a certain distance from the borders of the document.

# Licence
Licence GPL v2
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

# # # extension's begining # # #

# IMPORT

## These two lines are only needed if you don't put the script directly into
## the installation directory
# import sys
# sys.path.append('/usr/share/inkscape/extensions')

## We will use the inkex module with the predefined Effect base class.
import inkex, os

# Allow translation
import gettext
_ = gettext.gettext
## Probable change for 0.49. Allow translation with this instead
# import inkex
# inkex.localize()

from simplestyle import *

# from xml.etree import ElementTree as ET

# FUNCTIONS

# To show debugging output
def printDebug(string):
        inkex.debug( _(str(string)) )

# To show error to user
def printError(string):
        inkex.errormsg( _(str(string)) )

# Draw single guide
# parameters: position (single length), orientation ("horizontal/vertical"), parent
def drawGuide(position, orientation, parent):

        if orientation == "vertical":
                orientationString = "1,0"
                positionString = str(position) + ",0"
        if orientation == "horizontal":
                orientationString = "0,1"
                positionString = "0," + str(position)
        # Create a sodipodi:guide node
        inkex.etree.SubElement(parent,'{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}guide',{'position':positionString,'orientation':orientationString})


# CLASS

class addCenteredGuides(inkex.Effect):

	def __init__(self):
		"""
		Constructor.
		Defines options of the script.
		"""
		# Call the base class constructor.
		inkex.Effect.__init__(self)

		# Define boolean option "--include_hor_guide"
		self.OptionParser.add_option('--same_margins',
		        action = 'store', type = 'inkbool',
		        dest = 'same_margins', default = False,
		        help = 'Same margins on all four sides')

		# Define string option "--top_margin"
		self.OptionParser.add_option('--top_margin',
		        action = 'store',type = 'string',
		        dest = 'top_margin',default = 'centered',
		        help = 'Top margin, distance from top border')

		# Define string option "--right_margin"
		self.OptionParser.add_option('--right_margin',
		        action = 'store',type = 'string',
		        dest = 'right_margin',default = 'centered',
		        help = 'Right margin, distance from right border')

		# Define string option "--top_margin"
		self.OptionParser.add_option('--bottom_margin',
		        action = 'store',type = 'string',
		        dest = 'bottom_margin',default = 'centered',
		        help = 'Bottom margin, distance from bottom border')

		# Define string option "--left_margin"
		self.OptionParser.add_option('--left_margin',
		        action = 'store',type = 'string',
		        dest = 'left_margin',default = 'centered',
		        help = 'Left margin, distance from left border')

		# Define boolean option "--add_border_guides"
		self.OptionParser.add_option('--add_border_guides',
		        action = 'store', type = 'inkbool',
		        dest = 'add_border_guides', default = False,
		        help = 'Add guides around page')

	def effect(self):

		# Get script's options values. Input.

		# boolean
		same_margins = self.options.same_margins
		add_border_guides = self.options.add_border_guides
		# convert string to integer
		top_margin = int(self.options.top_margin)
		right_margin = int(self.options.right_margin)
		bottom_margin = int(self.options.bottom_margin)
		left_margin = int(self.options.left_margin)

		# getting parent tag of the guides
		namedview = self.document.xpath('/svg:svg/sodipodi:namedview',namespaces=inkex.NSS)[0]

		# getting the main SVG document element (canvas)
		svg = self.document.getroot()

		# getting the width and height attributes of the canvas
		canvas_width  = inkex.unittouu(svg.get('width'))
		canvas_height = inkex.unittouu(svg.attrib['height'])

		# Get selection bouding box - TODO

		# now let's use the input:

		# draw margin guides (if not zero)
		if same_margins == True and top_margin == 0:
			printError (_("Zero margin guides are not drawn. To draw guides on the all borders, use Edit > Guides around page."))
		else:
			if same_margins:
				right_margin = top_margin
				bottom_margin = top_margin
				left_margin = top_margin

			# start position of guides
			top_pos = canvas_height - top_margin
			right_pos = canvas_width - right_margin
			bottom_pos = bottom_margin
			left_pos = left_margin

			# Draw the four margin guides (if margin exists)
			if top_pos != canvas_height:
				drawGuide(top_pos, "horizontal", namedview)
			if right_pos != canvas_width:
				drawGuide(right_pos, "vertical", namedview)
			if bottom_pos != 0:
				drawGuide(bottom_pos, "horizontal", namedview)
			if left_pos != 0:
				drawGuide(left_pos, "vertical", namedview)

		# draw guides around page, if checked
		if add_border_guides:
			drawGuide(canvas_height, "horizontal", namedview)
			drawGuide(canvas_width, "vertical", namedview)
			drawGuide(0, "horizontal", namedview)
			drawGuide(0, "vertical", namedview)

# APPLY

# Create effect instance and apply it. Taking in SVG, changing it, and then outputing SVG
effect = addCenteredGuides()
effect.affect()

## end of file extensions_bootstrap.py ##
