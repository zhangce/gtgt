#! /usr/bin/python

import json

for l in open('/lfs/madmax/0/czhang/gtgt/fs_test_top10k'):
	ss = l.rstrip().split('\t')
	print json.dumps({"feature": " ".join(ss[1:])})