#!/usr/bin/python

import os
import re

pattern = re.compile("../style.css")

for filename in os.listdir('.'):
    if filename.endswith(".html"): 
        f = open(filename, 'r')
        lines = list(f)
        index = 0

        for idx, line in enumerate(lines):
            if '../style.css' in line:
                lines[idx] = line.replace('../style.css', 'style.css')
                index = idx

        lines.insert(index, '<script type="text/javascript" src="script.js"/>\n')
        f.close()
        
        f = open(filename, 'w');
        for line in lines:
            f.write(line)
        f.close()

