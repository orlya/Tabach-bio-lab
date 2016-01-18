#!/bin/sh
# blast_human_vs_mouse_part.sh

# Getting paramters: scripts_dir, dbs_dir,reference_org from conf file
source /vol/ek/orlya/orgs_db/orgs_config.conf

query_org=$1
reference_org=$2
 
echo "Computing blast for $1 - $2"

#/vol/ek/share/bin/ncbi-blast-2.2.31+/bin/blastp \
#-query ${dbs_dir}${query_org}.fa.00 \
#-db ${dbs_dir}${reference_org} -num_threads $(nproc) \
#-evalue 1e-10 \
#-best_hit_score_edge 0.05 \
#-best_hit_overhang 0.25 \
#-max_target_seqs 1  \
#-outfmt "6 qseqid qlen sseqid slen  evalue bitscore score length" \
#-out ${out_dir}${reference_org}.00.blst


task_id=$(printf "%02d\n" $SLURM_ARRAY_TASK_ID)

/vol/ek/share/bin/ncbi-blast-2.2.31+/bin/blastp \
-query ${dbs_dir}${query_org}.fa.${task_id} \
-db ${dbs_dir}${reference_org} -num_threads $(nproc) \
-evalue 1e-10 \
-best_hit_score_edge 0.05 \
-best_hit_overhang 0.25 \
-max_target_seqs 1  \
-outfmt "6 qseqid qlen sseqid slen  evalue bitscore score length" \
-out ${out_dir}${reference_org}.${task_id}.blst
