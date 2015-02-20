#!/usr/bin/env python
'''
Add centered guides,
extension by Samuel Dellicour,

This extension creates horizontal and vertical guides through 
the center of the document or the selected object

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
import guidetools
try:
	from subprocess import Popen, PIPE
except ImportError:
	inkex.errormsg(_(
		"Failed to import the subprocess module."
		))
	inkex.errormsg(
		"Python version is : " + str(inkex.sys.version_info)
		)
	exit(1)


# To show debugging output, error messages, use
#	inkex.debug( _(str(string)) )



class addCenteredGuides(inkex.Effect):

	def __init__(self):
		"""
		Constructor.
		Defines options of the script.
		"""
		# Call the base class constructor.
		inkex.Effect.__init__(self)

		# Define string option "--target"
		self.OptionParser.add_option('--target',
				action="store", type="string", 
				dest="target", default="document",
				help="Target: document or selection")


	def effect(self):

		# document or selection
		target = self.options.target

		# getting parent tag of the guides
		namedview = self.document.xpath('/svg:svg/sodipodi:namedview',namespaces=inkex.NSS)[0]

		# getting the main SVG document element (canvas)
		svg = self.document.getroot()

		# getting the width and height attributes of the canvas
		canvas_width  = self.unittouu(svg.get('width'))
		canvas_height = self.unittouu(svg.attrib['height'])

		# If a selected object exists, set guides to that object. 
		# Otherwise, use document center guides		
		if (target == "selection"):

			# check if there is any selection
			if not self.options.ids:
				inkex.errormsg(_("Please select an object first"))
				exit()

			# query bounding box, UPPER LEFT corner (?)
			q = {'x':0, 'y':0, 'width':0, 'height':0}
			for query in q.keys():
				p = Popen(
					'inkscape --query-%s --query-id=%s "%s"' % (query, self.options.ids[0], self.args[-1], ),
					shell=True,
					stdout=PIPE,
					stderr=PIPE,
					)
				p.wait()
				q[query] = p.stdout.read()

			# get width, height, center of bounding box 
			obj_width = float(q['width'])
			obj_height = float(q['height'])
			center_x = float(q['x']) + obj_width/2
			center_y = ( canvas_height - float(q['y']) - obj_height ) + obj_height/2

		else:

			# Pick document center 
			center_x = canvas_width/2 
			center_y = canvas_height/2

		# call the function. Output.
		guidetools.drawGuide(center_x, "vertical", namedview)
		guidetools.drawGuide(center_y, "horizontal", namedview)


# APPLY
# Create effect instance and apply it. Taking in SVG, changing it, and then outputing SVG
effect = addCenteredGuides()
effect.affect()
