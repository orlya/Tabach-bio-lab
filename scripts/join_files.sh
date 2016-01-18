#!bin/bash


while read ref_org; do   
	# Make blast db for current org

	sbatch --mem=400m -c40 --wrap="cat ${ref_org}* > $ref_org.blst"
	echo $ref_org
done < {$orgs_list_dir}orgs_list.csv
   
