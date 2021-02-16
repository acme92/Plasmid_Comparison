import os
#import compare_plasmids

#Input data relative locations 
HyAsP_results = '../data/ARETE_Efaecalis/HyAsP_17082020/results'
MOBsuite_results = '../data/Plasmid_Contig_IDs'

HyAsP_isolates = set()
MOBsuite_isolates = set()

for file in os.listdir(MOBsuite_results):
    if file.endswith(".fasta"):
        isolate_id = file.split("_")[0]
        if isolate_id not in MOBsuite_isolates:
            MOBsuite_isolates.add(isolate_id)

for folder in os.listdir(HyAsP_results):
    if folder.endswith("assembly"):
        isolate_id = folder.split("_")[0]
        if isolate_id not in HyAsP_isolates:
            HyAsP_isolates.add(isolate_id)

common_isolates = HyAsP_isolates.intersection(MOBsuite_isolates)
#print(len(common_isolates))

for isolate_id in common_isolates:
	os.system("python compare_plasmids.py "+isolate_id)