#########################################################################
# A README file for scripts for creating phylogenetic profiles matrix 	#
# Author: Orly Amsalem, orly.amsalem@gmail.com			      	#	
# Created: 18/01/2016 							#
# Last updated: 18/01/2016						#
#									#	
#########################################################################

List of scripts and files to run human-vs-orgs blast:
-----------------------------------------------------
- orgs_list.csv: 
list of organisms (names) to be processed.

- orgs_config.conf: 
configuration file with all relevant parameters to be shared accorss all scripts.

-download_uniprot.py:
python script for downloading proteins of the orgs listed in orgs_list.csv

- run_blast_par.sh
This is the main file for running blast (human vs all). 
The scripts splits the query file into as many files as number of cores, then, creates a blast db for each organims, then, runs blast_human_vs_all.sh

- blast_human_vs_all.sh
Runs the blast command in parallel (using SLURM_ARRAY_ID)

- join_files.sh
Joins the outputs created by the parallel run.


After all data is ready - you should run:
run_blast_par.sh with no parameters.









