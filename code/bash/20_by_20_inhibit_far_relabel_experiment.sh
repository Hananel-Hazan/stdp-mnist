# Grid search over hyperparameters for experiments with new inhibition schemes.

num_train=30000
reduced_dataset="False"
inhib_scheme="strengthen"
conv_features=400

for random_seed in 1 2 3
do
	for inhib_const in 0.5 1.0 1.5 2.0 2.5
	do
		for strengthen_const in 0.05 0.1 0.15 0.2 0.25
		do
			sbatch csnn_pc_inhibit_far_relabel_job.sh none 28 0 $conv_features 4 10 $num_train $reduced_dataset 1000 8 $inhib_scheme $inhib_const $strengthen_const False 0.0 $random_seed
		done
	done
done

exit
