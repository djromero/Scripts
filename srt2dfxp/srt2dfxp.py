#!/usr/bin/python

# Convert SubRip (SRT) files to the W3 Timed Text (DFXP) format.
# Original PowerShell script by Josh Erickson:
#   http://josherickson.org/2010/07/28/822/netflix-subtitles/
# Ported to Python by Cody "codeman38" Boisclair
# for the benefit of other Mac-using Netflix users
# (but mainly for my auditory-processing-disordered self!)

# Version 1.1:
#   Ignore UTF-8 BOM if it is present.
#   (Still quick-and-dirty, assumes that SRT is encoded in UTF-8.)
# Version 1.2:
#   Convert & to &amp; in Netflix output - else it chokes
# Version 1.3:
#   Allow for non-integer time offsets

import sys, getopt, datetime, codecs, xml.dom.minidom

def usage():
	print 'SubRip to W3 Timed Text (DFXP) Converter v1.3'
	print 'Original PowerShell version by Josh Erickson'
	print 'Python port by Cody "codeman38" Boisclair'
	print
	print 'Usage:'
	print sys.argv[0] + ' [-n] [-t OFFSET] INFILE [OUTFILE]'
	print '    -n       use Netflix-compatible format'
	print '    -t       add OFFSET seconds to timestamps of ' + \
	      'original SubRip file'
	print '    INFILE   input file name'
	print '    OUTFILE  output file name; will output to STDOUT if omitted'

def srt2delta(stamp):
	timesplit = stamp.split(':')
	secsplit = timesplit[2].split(',')
	delta = datetime.timedelta(hours = int(timesplit[0]), \
	  minutes = int(timesplit[1]), seconds = int(secsplit[0]), \
	  milliseconds = int(secsplit[1]))
	return delta
	
def delta2tick(delta, offset):
	if not isinstance(delta, datetime.timedelta):
		return 0
	else:
		return int((delta.seconds*1000000+delta.microseconds)*10 + (offset*10000000))

def dfxp_out(subdata, offset):
	xmlt = """<tt xml:lang="" xmlns="http://www.w3.org/ns/ttml"><head><metadata/><styling/><layout/></head><body region="subtitleArea"><div></div></body></tt>"""
	dom = xml.dom.minidom.parseString(xmlt)
	div = dom.getElementsByTagName('tt')[0].getElementsByTagName('body')[0].getElementsByTagName('div')[0]
	for sub in subdata:
		p = dom.createElement('p')
		p.setAttribute('xml:id', 'subtitle%d'%(sub[0]-1))
		p.setAttribute('begin', '%dt'%delta2tick(sub[1],offset))
		p.setAttribute('end', '%dt'%delta2tick(sub[2],offset))
		lines = sub[3].split('\n')
		for line in lines:
			if line != lines[0]:
				br = dom.createElement('br')
				p.appendChild(br)			
			txt = dom.createTextNode(line.decode('utf-8'))
			p.appendChild(txt)
		div.appendChild(p)
	return dom.toprettyxml(indent='    ',encoding='utf-8')
	
def nflx_out(subdata, offset):
	str = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<tt xmlns:tt="http://www.w3.org/2006/10/ttaf1" xmlns:ttp="http://www.w3.org/2006/10/ttaf1#parameter" xmlns:tts="http://www.w3.org/2006/10/ttaf1#styling" ttp:tickRate="10000000" xml:lang="en" xmlns="http://www.w3.org/2006/10/ttaf1">
<head>
<ttp:profile use="dfxp-simplesdh"/>
<styling>
<style xml:id="style0"/>
</styling>
</head>
<body>
<div>
"""
	for sub in subdata:
		s = '<p begin="%dt" end="%dt" xml:id="subtitle%s"><span style="style0">%s</span></p>\n' % \
		(delta2tick(sub[1],offset), delta2tick(sub[2],offset), sub[0]-1, sub[3].replace('\n','<br />').replace('&','&amp;'))
		str += s
	str += """</div>
</body>
</tt>
""";
	return str


nflx_compat = False
offset = 0

opts, args = getopt.getopt(sys.argv[1:], 'nt:')
for (o,a) in opts:
	if o == '-n':
		nflx_compat = True
	elif o == '-t':
		offset = float(a)

if len(args) == 0:
	usage()
	sys.exit()

infilename = args[0]
outfilename = None
if len(args) > 1:
	outfilename = args[1]

infile = file(infilename, 'r')
if outfilename is None:
	outfile = sys.stdout
else:
	outfile = file(outfilename, 'w')

inlines = infile.readlines()
infile.close()

# Discard UTF-8 BOM if it is present
if inlines[0].startswith('\xef\xbb\xbf'):
	inlines[0] = inlines[0][3:]

i = 0
subdata = []
while i < len(inlines):
	try:
		id = int(inlines[i])
	except:
		break
	
	j = i + 1
	while j < len(inlines):
		try:
			nid = int(inlines[j])
			break
		except:
			j += 1
	
	timing = inlines[i+1].split('-->')
	start = srt2delta(timing[0].strip(' \r\n'))
	end = srt2delta(timing[1].strip(' \r\n'))
	text = ''.join(inlines[i+2:j-1]).strip(' \r\n')
	
	subdata += [[id, start, end, text]]
	i = j
	
if nflx_compat:
	outfile.write(nflx_out(subdata, offset))
else:
	outfile.write(dfxp_out(subdata, offset))

outfile.close()