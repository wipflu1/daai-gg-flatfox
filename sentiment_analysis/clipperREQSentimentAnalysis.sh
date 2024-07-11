#!/bin/bash
#SBATCH --nodes=1
#SBATCH --mem=4G
#SBATCH --time=04:00:00
#SBATCH --partition=all
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --job-name=sentimentAnalysis
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=ggmain777@gmail.com


USERNAME=gordongr
EXPERIMENT_ID=sentimentAnalysis
PROJECT_ID=sentimentAnalysis
OUTPUT_DIR=/mnt/home/gordongr/projects/sentimentAnalysis

cd /mnt/home/gordongr/projects/sentimentAnalysis

EXECUTE="python3 pkDescription-csvGenerator.py"
echo ${EXECUTE} > cmd.log
${EXECUTE} > run.log

