__author__ = 'Orly Ovadia Amsalem'

import os
import sys


def download_data(dbs_dir="/vol/ek/orlya/orgs_db/"):

#Download human
    os.system("wget 'ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000005640_9606.fasta.gz'")
    os.system("mv UP000005640_9606.fasta.gz {0}human.fa.gz".format(dbs_dir))
    os.system("gunzip {0}human.fa.gz")

# Download mouse
    os.system("wget 'ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000000589_10090.fasta.gz'")
    os.system("mv UP000000589_10090.fasta.gz {0}Mus_musculus.fa.gz".format(dbs_dir))
    os.system("gunzip {0}Mus_musculus.fa.gz")

# Download Rat
    os.system("wget 'ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000002494_10116.fasta.gz'")
    os.system("mv UP000002494_10116.fasta.gz {0}Rattus_norvegicus.fa.gz".format(dbs_dir))
    os.system("gunzip {0}Rattus_norvegicus.fa.gz")

def create_blastdb(orgs_list, dbs_dir="/vol/ek/orlya/orgs_db/", blastdb_path="/vol/ek/share/bin/ncbi-blast-2.2.31+/bin/"):
    # Making a blast db out of each of the files
    for org in orgs_list:
        os.system("zcat {0}{1}.fa.gz | {2}makeblastdb -in -  -dbtype prot -out {3}{4} -title {5}".format(dbs_dir,org,blastdb_path,dbs_dir,org,org))
        print("zcat {0}{1}.fa.gz | {2}makeblastdb -in -  -dbtype prot -out {3}{4} -title {5}".format(dbs_dir,org,blastdb_path,dbs_dir,org,org))

def run_parallel_blast(orgs_list, reference_org="human",
                       dbs_dir="/vol/ek/orlya/orgs_db/",blast_path="/vol/ek/share/bin/ncbi-blast-2.2.31+/bin/", scripts_dir="/vol/ek/share/labscripts/"):

   #Converting reference sequences files to lines, in order to split it
   #os.system("{0}fasta2line.sh < {2}{1}.fa > {2}{3}.fa.lines".format(scripts_dir,reference_org,dbs_dir, reference_org))

   #Splitting reference org to as many files as number of processors.
   #os.system("split --number=l/$(nproc) --numeric-suffixes --filter='{0}line2fasta.sh > $FILE' {1}{2}.fa.lines {3}{4}.fa".format(scripts_dir,dbs_dir,reference_org,dbs_dir,reference_org))

   for query_org in orgs_list:
	command = "{0}blastp -query {1}{2}.fa01 -db {3} -num_threads $(nproc) -evalue 1e-10 " \
                 "-best_hit_score_edge 0.05 -best_hit_overhang 0.25 -max_target_seqs 1  " \
                 "-outfmt \"6 qseqid qlen sseqid slen  evalue bitscore score length\" " \
                 "-out {1}{3}.blst".format(blast_path,dbs_dir,reference_org,query_org)

	#"-outfmt \"6 qseqid qlen sseqid slen qstart qend sstart send evalue bitscore score length pident nident mismatch qcovs\" " \
	os.system(command)
	print command


   #Delete orgs splitted files:
   #os.system("rm ")


def main():
    #orgs_list = ("human","Mus_musculus", "Rattus_norvegicus")
    orgs_list = ["Mus_musculus"]
    #download_data()
    #create_blastdb(orgs_list)
    run_parallel_blast(orgs_list)



if __name__ == "__main__":
    main(*sys.argv[1:])


