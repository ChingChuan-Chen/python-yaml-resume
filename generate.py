# -*- coding: utf-8 -*-
# Copyright (C) 2018-2019 Jamal Chen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os, yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from shutil import copyfile
import pdfkit

if __name__ == '__main__':
  if len(sys.argv) < 2:
      print("Usage: python generate.py <yaml file>")
      sys.exit(1)

  # sys.argv = ["generate.py", "resume.yaml"]
  # load yaml file
  with open(sys.argv[1], encoding="utf8") as f:
    data = yaml.safe_load(f)

  # render html by jinja2
  env = Environment(
      loader=FileSystemLoader('./'),
      autoescape=select_autoescape(['html', 'xml']),
      trim_blocks=True,
      lstrip_blocks=True
	)
  template = env.get_template(data["conf"]["template"])
  html_output = template.render(data)
  with open(data["conf"]["html"], 'w', encoding="utf8") as f:
    f.write(html_output)

  # convert generated html to pdf
  ## !! Don't use opacity CSS which makes words blur in pdf !!
  options = {
    'page-size': 'Letter',
    'encoding': "UTF-8"
  }
  tempFolder = "C:\\Users\\Jamal\\AppData\\Local\\Temp"

  copyfile(data["conf"]["css"], tempFolder + "\\" + os.path.basename(data["conf"]["css"]))
  if "picture" in data["info"].keys():
    copyfile(data["info"]["picture"], tempFolder + "\\" + data["info"]["picture"])
  pdfkit.from_string(html_output, data["conf"]["pdf"], options=options)
