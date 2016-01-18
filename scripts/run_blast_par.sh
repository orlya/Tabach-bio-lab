#!/bin/sh
n=680

# Getting paramters: scripts_dir, dbs_dir,query_org,out_dir,orgs_list_dir, init_query, blsat_dir , orgs_list_file from conf file
source /vol/ek/orlya/orgs_db/orgs_config.conf

# Changing all file names to have _ instead of spaces:
#for FILENAME in ${dbs_dir}*; do 
#	fixed_name=$(echo $FILENAME | tr " " "_")
#	#echo $fixed_name
#	mv "${FILENAME}" ${fixed_name}
#done 

# Replacing spaces in query_org name
query_org_fixed=$(echo $query_org | tr " " "_")

if [ "$init_query" == "0" ]; then
	echo "Creating files for ${query_org_fixed}"
	#Create blast db for query org
	##zcat ${query_org}.fa.gz | /vol/ek/share/bin/ncbi-blast-2.2.31+/bin/makeblastdb -in -  -dbtype prot -out $query_org -title $query_org
	${blast_dir}makeblastdb -in "${dbs_dir}${query_org_fixed}.fasta" -input_type fasta -dbtype prot -out "${dbs_dir}${query_org_fixed}"  -title "$query_org_fixed"

	#Converting reference sequences files to lines, in order to split it
	${scripts_dir}fasta2line.sh < "${dbs_dir}${query_org_fixed}.fasta" > "${dbs_dir}${query_org_fixed}.fa.lines"

	#Splitting reference org to as many files as number of processors.
	split --number=l/$(nproc) --numeric-suffixes \
	--filter='line2fasta.sh > $FILE' ${dbs_dir}${query_org_fixed}.fa.lines ${dbs_dir}${query_org_fixed}.fa

else
	echo "Query files are already created"
fi
n=40   
while read ref_org; do
	ref_org_fixed=$(echo $ref_org | tr " " "_")
	# Make blast db for current org
	#echo "Making blast db for {$ref_org_fixed}"
	#${blast_dir}makeblastdb -in "${dbs_dir}${ref_org_fixed}.fasta" \
	# -input_type fasta -dbtype prot -out "${dbs_dir}${ref_org_fixed}"  -title "$ref_org_fixed"

	# Run blast human vs current org
	echo "Running blast for human vs {$ref_org_fixed}"
	sbatch -c40 --array=01-${n} -o /vol/ek/orlya/slurm_out.out ${cur_scripts_dir}blast_human_vs_all.sh ${query_org_fixed} ${ref_org_fixed}

done < ${orgs_list_dir}${orgs_list_file}
   
   

