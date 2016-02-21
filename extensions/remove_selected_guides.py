#!/usr/bin/env python
'''
Copyright 2014 Samuel Dellicour,
This is actually a modified version of
Copyright (C) 2009 Richard Querin, screencasters@heathenx.org
Copyright (C) 2009 heathenx, screencasters@heathenx.org
Modified from an extension distributed with JessyInk (code.google.com/p/jessyink).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
'''

# These lines are only needed if you don't put the script directly into
# the installation directory
import sys
# Unix
sys.path.append('/usr/share/inkscape/extensions')
# OS X
sys.path.append('/Applications/Inkscape.app/Contents/Resources/extensions')
# Windows
sys.path.append('C:\Program Files\Inkscape\share\extensions')

import inkex

class remove_selected_guides(inkex.Effect):

	def __init__(self):

		# Call the base class constructor.
		inkex.Effect.__init__(self)

		self.OptionParser.add_option('--remove_hor_guide',
			action = 'store', type = 'inkbool',
			dest = 'remove_hor_guide', default = False,
			help = 'Remove all horizontal guides')

		self.OptionParser.add_option('--remove_vert_guide',
			action = 'store', type = 'inkbool',
			dest = 'remove_vert_guide', default = False,
			help = 'Remove all vertical guides')

		self.OptionParser.add_option('--remove_ang_guide',
			action = 'store', type = 'inkbool',
			dest = 'remove_ang_guide', default = False,
			help = 'Remove all angled guides')


	def effect(self):

		# get options
		remove_hor_guide = self.options.remove_hor_guide
		remove_vert_guide = self.options.remove_vert_guide
		remove_ang_guide = self.options.remove_ang_guide

		# Find and delete guide node.
		for node in self.document.xpath("//sodipodi:guide", namespaces=inkex.NSS):
			if remove_hor_guide and (node.get('orientation') == '0,1'):
				node.getparent().remove(node)
			if remove_vert_guide and (node.get('orientation') == '1,0'):
				node.getparent().remove(node)
			if remove_ang_guide and (node.get('orientation') != '0,1') and (node.get('orientation') != '1,0'):
				node.getparent().remove(node)


# Create effect instance.
effect = remove_selected_guides()
effect.affect()
