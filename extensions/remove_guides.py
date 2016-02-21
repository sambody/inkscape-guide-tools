#!/usr/bin/env python
'''
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

class remove_guides(inkex.Effect):

	def __init__(self):

		# Call the base class constructor.
		inkex.Effect.__init__(self)

	def effect(self):

		# Find and delete guide node.
		for node in self.document.xpath("//sodipodi:guide", namespaces=inkex.NSS):
			node.getparent().remove(node)

# Create effect instance.
effect = remove_guides()
effect.affect()
