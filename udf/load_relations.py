#! /usr/bin/python

import json

rels = {
"_per_children":0,
"_per_parents":1,
"_per_city_of_death":2,
"_org_founded_by":3,
"_per_spouse":4,
"_org_top_members_employees":5,
"_per_member_of":6,
"_org_subsidaries":7,
"_org_parents":8,
"_org_city_of_headquarters":9,
"_per_siblings":10,
"_per_city_of_birth":11,
"_per_stateorprovinces_of_residence":12,
"_per_employee_of":13,
"_per_cities_of_residence":14,
"_per_countries_of_residence":15,
"_per_title":16,
"_per_schools_attended":17}

for l in open('/lfs/madmax/0/czhang/gtgt/data/alldata.tsv'):
	ss = l.rstrip().split('\t')
	if len(ss) < 3:
		ss.append("EMPTY")

	rs = {}
	rs["feature1"] = ss[1]
	rs["feature2"] = ss[2]

	for r in rels:
		if r == ss[0]:
			rs[r] = True
		else:
			rs[r] = False

	print json.dumps(rs)
