#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json, argparse, commands

parser = argparse.ArgumentParser(
	description='Generate image text from json file.'
)
parser.add_argument(
	'conf_file',
	nargs='?',
	default='config.json',
	help='config file'
)

args = parser.parse_args()

# Load config file
f = open(args.conf_file, "rU")
loaded = json.load(f)
f.close()

for set in loaded['sets']:
	font = set.get('font', '');
	size = set.get('size', '30');
	label = set.get('label', 'undefined');
	background = set.get('background', 'None');
	color = set.get('color', '#000');
	imgpath = set.get('imgpath', 'undefined.png');
	for convert in set['convert']:
		font = convert.get('font', font);
		size = convert.get('size', size);
		label = convert.get('label', label);
		background = convert.get('background', background);
		color = convert.get('color', color);
		imgpath = convert.get('imgpath', imgpath);
		conv_cmd = u'convert -background %s -fill "%s" -font "%s" -pointsize %s label:"%s" %s' % (background, color, font, size, label, imgpath)
		print conv_cmd
		out = commands.getoutput(conv_cmd.encode('utf_8'))
		print out
print
