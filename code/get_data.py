import os

def read_file(filename):
        string = open(filename, "r").read()
        string_list = string.split("\n")
        string_list = [line for line in string_list if line and line[0] != '#'] #Read line only if it is nonempty and not a comment.
        return string_list

#Reading MOBsuite data to form a dictionary of plasmids. 
def get_MOBsuite_data(MOBsuite_plasmids, isolate_id):
	MOBsuite_results = '../data/Plasmid_Contig_IDs'
	for file in os.listdir(MOBsuite_results):
		if file.startswith(isolate_id):
			if file.endswith('.fasta'):
				plasmid_id = file.split(".")[0].split("_")[-1]
				#print(plasmid_id)
				MOBsuite_plasmids[plasmid_id] = {}
				filename = os.path.join(MOBsuite_results, file)
				str_list = read_file(filename)
				for string in str_list:
					if string[0] == '>':
						contig_id = string[1:].split(" ")[0]
						contig_len = int(string[1:].split(" ")[1].split('=')[1])
						if contig_id not in MOBsuite_plasmids[plasmid_id]:
							MOBsuite_plasmids[plasmid_id][contig_id] = {}
							MOBsuite_plasmids[plasmid_id][contig_id]['length'] = contig_len
							#MOBsuite_plasmids[plasmid_id][contig_id]['sequence'] = ''
					#else:
						#MOBsuite_plasmids[plasmid_id][contig_id]['sequence'] += string
	return MOBsuite_plasmids

#Reading HyAsP data to form a dictionary of plasmids.
def get_HyAsP_data(HyAsP_plasmids, isolate_id):
	#HyAsP_results = '../data/ARETE_Efaecalis/HyAsP_17082020/results/'+isolate_id+'_assembly/putative_plasmid_contigs.fasta'
	HyAsP_results = '../data/ARETE_Efaecalis/HyAsP_17082020/results'
	for folder in os.listdir(HyAsP_results):
		if folder.startswith(isolate_id):
			if folder.endswith('_assembly'):
				str_list = read_file(HyAsP_results+'/'+isolate_id+'_assembly/putative_plasmid_contigs.fasta')
				for string in str_list:
					if string[0] == '>':
					    contig_id = string[1:].split("|")[0]
					    plasmid_num = string[1:].split("|")[1].split("_")[-1]
					    #print(isolate_id, contig_id, plasmid_num)
					    if plasmid_num not in HyAsP_plasmids:
					        HyAsP_plasmids[plasmid_num] = {}
					    HyAsP_plasmids[plasmid_num][contig_id] = {}
					else:
						contig_seq = string  
						contig_len = len(string)
						HyAsP_plasmids[plasmid_num][contig_id]['length'] = contig_len
						#HyAsP_plasmids[plasmid_num][contig_id]['sequence'] = contig_seq
	return HyAsP_plasmids							       