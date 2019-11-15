#!/usr/bin/env python
'''
Grid Maker by Samuel Dellicour - www.samplify.be,
heavily based on Guides creator - Copyright (C) 2008 Jonas Termeau - jonas.termeau **AT** gmail.com


## This extension allows you to automatically draw column and row guides in inkscape (including gutters - spacing between columns).

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

import sys
sys.path.append('/usr/share/inkscape/extensions')
import inkex
from simplestyle import *
import gettext
_ = gettext.gettext

# FUNCTIONS

# To show debugging output
def printDebug(string):
	inkex.debug(_(str(string)))

# To show error to user
def printError(string):
	inkex.errormsg(_(str(string)))

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

# Draw single guide
# based on position (length), orientation ("horizontal/vertical"), parent
def drawGuide(position, orientation, parent):

		if orientation == "vertical":
				orientationString = "1,0"
				positionString = str(position) + ",0"

		if orientation == "horizontal":
				orientationString = "0,1"
				positionString = "0," + str(position)

		# Create a sodipodi:guide node
		inkex.etree.SubElement(parent,'{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}guide',{'position':positionString,'orientation':orientationString})


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
				position = position + width
			else:
				if has_outer_gutter == False:
					drawGuide(position, orientation, parent)
					position = position + width
				else:
					drawGuide(position, orientation, parent)
					position = position + gutter
					drawGuide(position, orientation, parent)
					position = position + width

		# other gutter (not first/last)
		else:
			if gutter == 0:
				drawGuide(position, orientation, parent)
				position = position + width
			else:
				drawGuide(position, orientation, parent)
				position = position + gutter
				drawGuide(position, orientation, parent)
				position = position + width


# CLASS

class Grid_Guides(inkex.Effect):

	def __init__(self):
		"""
		Constructor.
		Defines options of the script.
		"""
		# Call the base class constructor.
		inkex.Effect.__init__(self)

		# Parse options and store them in self.options.[destination]

		self.OptionParser.add_option("--tab",
				action="store", type="string",
				dest="tab", default="columns",
				help="")

		# COLUMNS (vertical guides)

		self.OptionParser.add_option('--column_unit',
				action="store", type="string", 
				dest="column_unit", default="mm",
				help="The unit of the values")

		self.OptionParser.add_option('--column_alignment',
				action = 'store', type = 'string',
				dest = 'column_alignment', default = 'centered',
				help = 'Alignment of the columns in relation to the document')

		self.OptionParser.add_option('--column_offset',
				action = 'store', type = 'string',
				dest = 'column_offset', default = '0',
				help = 'Offset distance from the left')

		self.OptionParser.add_option('--columns',
				action = 'store', type = 'string',
				dest = 'columns', default = 0,
				help = 'Number of columns')

		self.OptionParser.add_option('--column_width',
				action = 'store', type = 'string',
				dest = 'column_width', default = 0,
				help = 'Width of each column')

		self.OptionParser.add_option('--column_gutter',
				action = 'store', type = 'string',
				dest = 'column_gutter', default = 0,
				help = 'Spacing between columns')

		self.OptionParser.add_option('--include_outer_col_gutter',
				action = 'store', type = 'inkbool',
				dest = 'include_outer_col_gutter', default = True,
				help = 'Include outer gutters (double guides)')

		self.OptionParser.add_option('--delete_vert_guides',
				action = 'store', type = 'inkbool',
				dest = 'delete_vert_guides', default = False,
				help = 'Delete existing vertical guides')

		self.OptionParser.add_option('--show_total_width',
				action = 'store', type = 'inkbool',
				dest = 'show_total_width', default = False,
				help = 'Show total width')

		# ROWS (horizontal guides)

		self.OptionParser.add_option('--row_unit',
				action="store", type="string", 
				dest="row_unit", default="mm",
				help="The unit of the values")

		self.OptionParser.add_option('--row_alignment',
				action = 'store', type = 'string',
				dest = 'row_alignment', default = 'centered',
				help = 'Alignment of rows in relation to the document')

		self.OptionParser.add_option('--row_offset',
				action = 'store', type = 'string',
				dest = 'row_offset', default = '0',
				help = 'Offset distance from the top')

		self.OptionParser.add_option('--rows',
				action = 'store', type = 'string',
				dest = 'rows', default = 0,
				help = 'Number of rows')

		self.OptionParser.add_option('--row_height',
				action = 'store', type = 'string',
				dest = 'row_height', default = 0,
				help = 'Width of each row')

		self.OptionParser.add_option('--row_gutter',
				action = 'store', type = 'string',
				dest = 'row_gutter', default = 0,
				help = 'Spacing between rows')

		self.OptionParser.add_option('--include_outer_row_gutter',
				action = 'store', type = 'inkbool',
				dest = 'include_outer_row_gutter', default = True,
				help = 'Include outer gutters (double guides)')

		self.OptionParser.add_option('--delete_hor_guides',
				action = 'store', type = 'inkbool',
				dest = 'delete_hor_guides', default = False,
				help = 'Delete existing horizontal guides')

		self.OptionParser.add_option('--show_total_height',
				action = 'store', type = 'inkbool',
				dest = 'show_total_height', default = False,
				help = 'Show total height')

	def effect(self):

		# Get script's option values from self.options

		tab = self.options.tab

		# columns

		# Factor to multiply in order to get value in user units (pixels)
		col_factor = self.unittouu('1' + self.options.column_unit)
		col_alignment = self.options.column_alignment
		col_offset = float(self.options.column_offset) * col_factor
		cols = int(self.options.columns)
		col_width = float(self.options.column_width) * col_factor
		col_gut = float(self.options.column_gutter) * col_factor
		has_outer_col_gutter = self.options.include_outer_col_gutter
		delete_hor = self.options.delete_hor_guides
		show_total_width = self.options.show_total_width

		# rows
		row_factor = self.unittouu('1' + self.options.row_unit)
		row_alignment = self.options.row_alignment
		row_offset = float(self.options.row_offset) * row_factor
		rows = int(self.options.rows)
		row_height = float(self.options.row_height) * row_factor
		row_gut = float(self.options.row_gutter) * row_factor
		has_outer_row_gutter = self.options.include_outer_row_gutter
		delete_vert = self.options.delete_vert_guides
		show_total_height = self.options.show_total_height

		# parent tag of the guides
		namedview = self.document.xpath('/svg:svg/sodipodi:namedview',namespaces=inkex.NSS)[0]

		# main SVG document element (canvas)
		svg = self.document.getroot()
		canvas_width  = self.unittouu(svg.get('width'))
		canvas_height = self.unittouu(svg.attrib['height'])

		# total width  (columns and gutters)
		if has_outer_col_gutter:
			total_col_width = cols*col_width + (cols+1)*col_gut
		else:
			total_col_width = cols*col_width + (cols-1)*col_gut

		# total height (rows and gutters)
		if has_outer_row_gutter:
			total_row_height = rows*row_height + (rows+1)*row_gut
		else:
			total_row_height = rows*row_height + (rows-1)*row_gut

		if (tab == "\"columns\""):

			# Delete existing vertical guides
			if (delete_vert):
				deleteGuidesByOrientation(self.document, 'vertical')

			# Set horizontal starting position, depending on grid alignment
			if (col_alignment == 'left'):
				hor_start = col_offset

			if (col_alignment == 'centered'):
				hor_start = round(canvas_width/2) - round(total_col_width/2) + col_offset

			if (col_alignment == 'right'):
				hor_start = canvas_width - total_col_width + col_offset

			# Create column guides with column_spacings
			drawDoubleGuides(cols, col_width, col_gut, hor_start, has_outer_col_gutter, "vertical", namedview)

			# Give total width in original units
			if (show_total_width == True):
				printDebug("Total width of grid will be: " + str(total_col_width/col_factor) + " " + self.options.column_unit)

		elif (tab == "\"rows\""):

			# Delete existing horizontal guides
			if (delete_hor): deleteGuidesByOrientation(self.document, 'horizontal')

			# Set vertical starting position, depending on grid alignment
			# 0,0 is at BOTTOM left of document, guides will be drawn bottom up
			if (row_alignment == 'top'):
				vert_start = round(canvas_height) - total_row_height - row_offset

			if (row_alignment == 'centered'):
				vert_start = round(canvas_height/2) - round(total_row_height/2) - row_offset

			if (row_alignment == 'bottom'):
				vert_start =  -row_offset

			# Create row guides
			drawDoubleGuides(rows, row_height, row_gut, vert_start, has_outer_row_gutter, "horizontal", namedview)

			# Give total height in original units
			if (show_total_height == True):
				printDebug("Total height of grid will be: " + str(total_row_height/row_factor) + " " + self.options.row_unit)


# Create effect instance and apply it.
effect = Grid_Guides()
effect.affect()
