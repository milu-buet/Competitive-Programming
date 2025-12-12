#!/bin/bash
SBATCH --cpus-per-task 1
SBATCH --time 7-00:00:00
SBATCH --mem-per-cpu 10G
SBATCH --partition computeq

# The above will submit a job:
# 1. In the computeq partition.
# 2. With 10 GB of memory per CPU.
# 3. For up to 7 days of run time.
# 4. With 1 CPU per node.

# Use the 'gpuq' partition and gpu resources if you need Tesla V100 GPUs (remove the first # below)
##SBATCH --partition gpuq
##SBATCH --gres gpu:1


# Load a python module.
# There are 4 versions available: 
# 2.7.15 and 3.6.6 and 3.6.7 and 3.7.0 
module load python/3.7.0

# To use tensorflow, just load the tensorflow module:
#module load tensorflow


# Run a script in the submission directory
# Change test.py to any python script you submit to the cluster.
python3 ./test.py

# Exit
