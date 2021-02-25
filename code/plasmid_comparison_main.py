__author__ = 'amane'

from sys import argv
import os
import networkx as nx
import itertools
import copy

import get_data
import compare_plasmids

#USAGE: python plasmid_comparison_main.py isolate_id

isolate_id = argv[1]

	


#Reading data and saving it to a dictionary with plasmids as keys and a nested dictionary of contigs as values
MOBsuite_plasmids = {}
HyAsP_plasmids = {}
MOBsuite_plasmids = get_data.get_MOBsuite_data(MOBsuite_plasmids, isolate_id)
HyAsP_plasmids = get_data.get_HyAsP_data(HyAsP_plasmids, isolate_id)

score_db = compare_plasmids.run_compare_plasmids(HyAsP_plasmids, MOBsuite_plasmids)		


#####################################################
#	SORTING SCORES AND SAVING RESULTS TO LOG FILE   #
#####################################################

#Sorting the combinations in ascending order of the scores
def sort_by_score(tup):
	tup.sort(key = lambda x: x[1])
	return tup

score_list = []
for count in score_db:
	score = score_db[count]['score']
	score_list.append((count, score))

score_list = sort_by_score(score_list)	

#Saving results to log file with labeling corresponding to best score noted first
results_file = open("../results/"+isolate_id+"_comparison.log", "w")
results_file.close()
for tup in score_list:
	results_file = open("../results/"+isolate_id+"_comparison.log", "a")
	count = tup[0]

	results_file.write("Combination "+str(count)+"\n")

	results_file.write("Score:\t\t"+str(score_db[count]['score'])+"\n\n")

	results_file.write("Decomposition of weighted lengths HyAsP|MOBsuite|Common:\t\t")
	for x in score_db[count]['decomposition']:
		results_file.write(str(float(x))+"|")
	results_file.write("\n\n")

	results_file.write("HyAsP plasmids:\n")
	for x in score_db[count]['left_dict']:
		results_file.write(str(x)+":\t")
		for y in list(score_db[count]['left_dict'][x].keys()):
			results_file.write(str(y)+",")
		results_file.write("\n")
	results_file.write("\n")	

	results_file.write("MOBsuite plasmids:\n")
	for x in score_db[count]['right_dict']:
		results_file.write(str(x)+":\t")
		for y in list(score_db[count]['right_dict'][x].keys()):
			results_file.write(str(y)+",")
		results_file.write("\n")		
	results_file.write("\n")	

	results_file.write("HyAsP splits:\n")
	for x in score_db[count]['left_splits']:
		for y in x:
			if y != set():
				results_file.write(str(y))
		results_file.write("\n")	
	results_file.write("\n")
	
	results_file.write("MOBsuite splits:\n")
	for x in score_db[count]['right_splits']:
		for y in x:
			if y != set():			
				results_file.write(str(y))
		results_file.write("\n")	

	results_file.write("#-------------------------\n\n\n\n")	
	results_file.close()


