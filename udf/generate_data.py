
featureid_2_content = {}
for l in open('../data/dptraining.small.featumapping'):
	(fname, fid) = l.rstrip().split('\t')
	featureid_2_content[fid] = fname

labels = []
features = []

labelid_2_content = {}
for l in open('../data/dptraining.small.labelmapping'):
	(fname, fid) = l.rstrip().split('\t')
	labelid_2_content[fid] = fname

for l in open('../data/dptraining.small.label'):
	labels.append(l.rstrip())
for l in open('../data/dptraining.small.featu'):
	features.append(l.rstrip())

for ct in range(0, len(labels)):
	fs = []
	for f in features[ct].split(' '):
		fs.append(featureid_2_content[f])
	print labelid_2_content[labels[ct]] + "\t" + "\t".join(fs)