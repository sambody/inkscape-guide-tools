#!/usr/bin/env python 
'''
Library functions for Guide Tools (grid guides, center guides, margin guides)
'''

import inkex
import gettext
_ = gettext.gettext

# To show error to user (or for debugging)
def show(string):
	inkex.errormsg(_(str(string)))

# Draw single guide
# parameters: position (single length), orientation ("horizontal/vertical"), parent (namedview)
def drawGuide(position, orientation, parent):

	if (orientation == "vertical"):
		orientationString = "1,0"
		positionString = str(position) + ",0"
	else:
		orientationString = "0,1"
		positionString = "0," + str(position)

	# Create a sodipodi:guide node
	inkex.etree.SubElement(parent,'{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}guide',{'position':positionString,'orientation':orientationString})

	# Adding color to guide is not working in 0.91, as Inkscape doesn't read the value in the xml, due to a bug.
	# Let's wait for 0.92 to implement this then. Here is the code to use:
	# inkex.etree.SubElement(parent,'{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}guide',{'position':positionString,'orientation':orientationString, '{http://www.inkscape.org/namespaces/inkscape}color':"rgb(255,0,0)"})

# Delete all/vertical/horizontal guides
def deleteGuidesByOrientation(document, orientation):

	# getting the parent's tag of the guides
	namedview = document.xpath('/svg:svg/sodipodi:namedview',namespaces=inkex.NSS)[0]

	# getting all the guides
	children = document.xpath('/svg:svg/sodipodi:namedview/sodipodi:guide',namespaces=inkex.NSS)

	# depending on which type of guide to remove, remove them
	if (orientation == 'all'):
		for element in children:
			namedview.remove(element)
	elif (orientation == 'horizontal'):
		for element in children:
			if (element.get('orientation') == '0,1'):
				namedview.remove(element)
	elif (orientation == 'vertical'):
		for element in children:
			if (element.get('orientation') == '1,0'):
				namedview.remove(element)



# Draw series of guides with or without gutter - same function called for columns and rows
def drawDoubleGuides(colsRows, width, gutter, start_pos, has_outer_gutter, orientation, parent):

	# position of guide
	position = start_pos

	# Draw series of double guides (or single guides when no gutter)
	for i in range(0, colsRows+1):

		# if first or last gutter
		if ( i == 0 or i == colsRows ):

			# if no gutter, draw single guide; if gutter, draw single or double guide
			if gutter == 0:
				drawGuide(position, orientation, parent)
				position += width
			else:
				if has_outer_gutter == False:
					drawGuide(position, orientation, parent)
					position += width
				else:
					drawGuide(position, orientation, parent)
					position += gutter
					drawGuide(position, orientation, parent)
					position += width

		# other gutter (not first/last)
		else:
			if gutter == 0:
				drawGuide(position, orientation, parent)
				position += width
			else:
				drawGuide(position, orientation, parent)
				position += gutter
				drawGuide(position, orientation, parent)
				position += width

