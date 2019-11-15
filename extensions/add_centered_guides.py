#!/usr/bin/env python
'''
Add centered guides,
extension by Samuel Dellicour,

This extension creates horizontal and/or vertical guides through the center of the document

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

# IMPORT


import inkex
import gettext
_ = gettext.gettext


# FUNCTIONS


# To show debugging output, error messages
def printDebug(string):
	inkex.debug( _(str(string)) )

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

def drawCenteredGuides(positionX, positionY, include_hor, include_vert, parent):

	if include_hor: drawGuide(positionY, "horizontal", parent)
	if include_vert: drawGuide(positionX, "vertical", parent)


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
		self.OptionParser.add_option('--include_hor_guide',
			action = 'store', type = 'inkbool',
			dest = 'include_hor_guide', default = False,
			help = 'Include centered horizontal guide')

		# Define boolean option "--include_vert_guide"
		self.OptionParser.add_option('--include_vert_guide',
			action = 'store', type = 'inkbool',
			dest = 'include_vert_guide', default = False,
			help = 'Include centered vertical guide')

	def effect(self):

		# Get script's options values. Input.

		include_hor = self.options.include_hor_guide
		include_vert = self.options.include_vert_guide

		# getting parent tag of the guides
		namedview = self.document.xpath('/svg:svg/sodipodi:namedview',namespaces=inkex.NSS)[0]

		# getting the main SVG document element (canvas)
		svg = self.document.getroot()

		# getting the width and height attributes of the canvas
		canvas_width  = self.unittouu(svg.get('width'))
		canvas_height = self.unittouu(svg.attrib['height'])

		# calculate center of document
		center_pos_x = canvas_width/2
		center_pos_y = canvas_height/2

		# call the function. Output.
		drawCenteredGuides(center_pos_x, center_pos_y, include_hor, include_vert, namedview)


# APPLY


# Create effect instance and apply it. Taking in SVG, changing it, and then outputing SVG
effect = addCenteredGuides()
effect.affect()
