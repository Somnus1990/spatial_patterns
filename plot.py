# open the tablefile
from snep.configuration import config
config['network_type'] = 'empty'
import snep.utils
import utils
import matplotlib as mpl
mpl.use('Agg')
import plotting
import animating
import matplotlib.pyplot as plt
import time
import general_utils.arrays
import general_utils.snep_plotting
import numpy as np
import string
import os
# import IPython

# Set font sizes in general and for all legends
# Use fontsize 42 for firing rate maps and correlograms, then change their
# height to 164pt to have the rate map of the same size as the examples
# mpl.rc('font', size=18)
mpl.rc('font', size=10)
# mpl.rc('legend', fontsize=18)
# If you comment this out, then everything works, but in matplotlib fonts
# mpl.rc('font', **{'family': 'serif', 'serif': ['Helvetica']})
# mpl.rc('text', usetex=True)


def animate_psps(tables, paramspace_points,
	animation_function, start_time, end_time, step_factor=1, save_path=False, interval=50, take_weight_steps=False):
	"""
	Animate (several) paramspace points

	_________
	Arguments:
	See also definition of plot_psps
	- animation_function: string with the name of animation defined in animating.py
	""" 
	for n, psp in enumerate(psps):
		print n
		print psp
		params = tables.as_dictionary(psp, True)
		try:
			rawdata = tables.get_raw_data(psp)
		except:
			continue
		animation = animating.Animation(params, rawdata, start_time=start_time, end_time=end_time, step_factor=step_factor, take_weight_steps=take_weight_steps)
		ani = getattr(animation, animation_function)
		if save_path:
			# remove the uno string
			save_path_full = os.path.join(save_path, string.replace(str(psp), ' uno', '') + '.mp4')
		else:
			save_path_full = False
		ani(save_path=save_path_full, interval=interval)


def get_path_tables_psps(date_dir):
	path = os.path.join(
		os.path.expanduser('~/localfiles/itb_experiments/learning_grids/'),
		date_dir, 'experiment.h5')
	tables = snep.utils.make_tables_from_path(path)
	tables.open_file(True)
	print tables
	psps = tables.paramspace_pts()
	return path, tables, psps

######################################################
##########	Decide what should be plotted	##########
######################################################
# function_kwargs is a list of tuples of strings (the function names)
# and dictionaries (the function parameters as keys and values)
# t0 = 80e5
t1 = 24e5
# t1 = 120e6
# t1 = 80e6
# t1 = 100e6
# t=10e7
method = None
# t2 = 1e7
function_kwargs = [
	# ('plot_output_rates_from_equation',
	# 	{'time': 0, 'from_file': True}),
	# ('plot_output_rates_from_equation',
	# 	{'time': -1, 'from_file': True}),
	# ('weights_vs_centers',
	# 	{'time': 0}),
	# ('weights_vs_centers',
	# 	{'time': 0, 'syn_type': 'inh'}),d

	# ('weights_vs_centers',
	# 	{'time': -1}),
	# ('weights_vs_centers',
	# 	{'time': -1, 'syn_ type': 'inh'}),
	# # ('plot_output_rates_from_equation', {'time': 1e3, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 0e6, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 7.5e7, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 8e7, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 8.5e7, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 9e7, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 9.5e7, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 1e6, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 2e6, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 3e6, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 40e4, 'from_file': False, 'spacing': 501}),
	# ('plot_output_rates_from_equation', {'time': 2e6 , 'from_file': True}),


	# ('plot_output_rates_from_equation', {'time': 0e6, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 1e6, 'from_file': True}),
	# ('weight_evolution', {'syn_type': 'exc'}),
	# ('weight_evolution', {'syn_type': 'inh'}),

	# ('spike_map', {'small_dt': 1e-10, 'start_frame': 0, 'end_frame': 5e3})
	# ('fields_times_weights', {'time': 150e4, 'syn_type': 'inh'}),
	# ('plot_output_rates_from_equation', {'time': t1, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 0, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 4e6, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 8e6, 'from_file': True, 'maximal_rate': False}),
	
	# ('plot_output_rates_from_equation', {'time': t1, 'from_file': True, 'maximal_rate': False}),
	# ('plot_output_rates_from_equation', {'time': t1, 'from_file': True, 'maximal_rate': False, 
	# 									'subdimension': None}),	
	# ('plot_correlogram', {'time': 0, 'from_file': True, 'mode': 'same', 'method': method}),	
	# ('plot_correlogram', {'time': t/4., 'from_file': True, 'mode': 'same', 'method': method}),	
	# ('plot_correlogram', {'time': t/2., 'from_file': True, 'mode': 'same', 'method': method}),	
	# ('plot_correlogram', {'time': t, 'from_file': True, 'mode': 'same', 'method': method}),	
	
	# ('plot_output_rates_from_equation', {'time': t0, 'from_file': False, 'spacing': 301}),
	# ('plot_correlogram', {'time': 24e5, 'from_file': True, 'mode': 'same'}),
	# ('plot_output_rates_from_equation', {'time': t1, 'from_file': True}),
	# ('plot_time_evolution', {'observable': 'grid_score', 't_start': 0}),
	# ('plot_correlogram', {'time': 0, 'from_file': True, 'mode': 'same', 'method': 'Weber'}),
	# ('plot_grids_linear', {'time': t1, 'from_file': True}),	
	# ('plot_correlogram', {'time': t1, 'from_file': True, 'mode': 'same', 'method': 'Weber', 'subdimension': 'space'}),


	# ('plot_head_direction_polar', {'time':t1, 'from_file': True, 'show_watson_U2': True}),
	# ('plot_output_rates_from_equation', {'time': t1, 'from_file': True, 'subdimension': 'space'})

	# ('watsonU2_vs_grid_score', {'time': t1-10.*24e4, 'precomputed': True}),
	# ('watsonU2_vs_grid_score', {'time': t1-24e4, 'precomputed': True}),
	# ('watsonU2_vs_grid_score', {'time': t1, 'precomputed': False}),

	('watsonU2_vs_grid_score_with_examples', {'time': t1}),


	# ('input_current', {'time': t0, 'spacing': 301}),
	# ('weight_statistics', {'time': t0, 'syn_type': 'exc'}),
	# ('weight_statistics', {'time': t0, 'syn_type': 'inh'}), 


	# ('sigma_histogram', {'populations': ['exc', 'inh'], 'bins': 30})

	# ('plot_head_direction_polar', {'time': 0*t1, 'from_file': True}),
	# ('plot_head_direction_polar', {'time': 0.125*t1, 'from_file': True}),
	# ('plot_output_rates_from_equation', {'time': 0.25*t1, 'from_file': True, 'maximal_rate': False}),
	# ('plot_output_rates_from_equation', {'time':  0.5*t1, 'from_file': True, 'maximal_rate': False}),
	# ('plot_output_rates_from_equation', {'time':  0.75*t1, 'from_file': True, 'maximal_rate': False}),
	# ('plot_output_rates_from_equation', {'time': t1, 'from_file': True, 'maximal_rate': False}),


	# ('plot_head_direction_polar', {'time': t1, 'from_file': True}),

	# ('fields', {'neuron': 5, 'show_each_field': False, 'show_sum': True}),
	# ('fields', {'neuron': 19, 'show_each_field': False, 'show_sum': True}),
	# ('fields', {'neuron': 211, 'show_each_field': False, 'show_sum': True}),
	# ('fields', {'neuron': 375, 'show_each_field': False, 'show_sum': True}),

	# ('fields', {'neuron': 341, 'show_each_field': False, 'show_sum': True}),
	# ('fields', {'neuron': 1567, 'show_each_field': False, 'show_sum': True}),
	# ('fields', {'neuron': 2312, 'show_each_field': False, 'show_sum': True}),
	# ('fields', {'neuron': 4211, 'show_each_field': False, 'show_sum': True}),

	# ('plot_polar', {'time': 9e6, 'from_file': True}),
	# ('plot_polar', {'time': 10e6, 'from_file': True}),
	# ('plot_grid_spacing_vs_parameter',
	# 		{	'from_file': True,
	# 			'parameter_name': 'sigma_exc',
	# 			'parameter_range': np.linspace(0.012, 0.047, 200),
	# 			# 'parameter_range': np.linspace(0.015, 0.055, 200),
	# 			'plot_mean_inter_peak_distance': True})
	# ('plot_grid_spacing_vs_parameter',
	# 		{	'from_file': True,
	# 			'parameter_name': 'sigma_inh',
	# 			'parameter_range': np.linspace(0.08, 0.36, 201),
	# 			# 'parameter_range': np.linspace(0.015, 0.055, 200),
	# 			'plot_mean_inter_peak_distance': True})
	# ('output_rate_heat_map', {'from_file': True, 'end_time': 40e4})
	# ('output_rate_heat_map', {'from_file': False, 'spacing': 201, 'start_time': 0, 'end_time': 12e4})
	# ('weights_vs_centers', {'time': 0.}),v
	# ('weights_vs_centers', {'time': 0., 'syn_type': 'inh'}), 
	# ('weights_vs_centers', {'time': 12e4}),
	# ('weights_vs_centers', {'time': 40e5, 'syn_type': 'exc'}),
	# ('weights_vs_centers', {'time': 40e5, 'syn_type': 'inh'}),
	]

if __name__ == '__main__':
	path, tables, psps = get_path_tables_psps( 
		'2014-10-27-15h51m20s') 
	save_path = False
	save_path = os.path.join(os.path.dirname(path), 'visuals')
	try:
		os.mkdir(save_path)
	except OSError:
		pass

	all_psps = psps
	# fields_per_synapse = [1, 2, 4, 8, 16, 32]
	# for fps in fields_per_synapse:
	# sigma_exc_x = [0.08, 0.11, 0.15]
	# sigma_exc_x = [0.1]
	# sigma_inh_y = [0.7]
	# for se, si in zip(sigma_exc_x, sigma_inh_y):
	# psps = [p for p in all_psps
	# # # 		# if p[('sim', 'output_neurons')].quantity == 2
	# # # 		# and p[('sim', 'weight_lateral')].quantity == 4.0
	# # # 		# and p[('sim', 'output_neurons')].quantity == 8
	# # # 		# and p[('sim', 'dt')].quantity == 0.01
	# 			# if p[('sim', 'seed_centers')].quantity == 0
	# 			# and p[('sim', 'symmetric_centers')].quantity == True
	# 			# if np.array_equal(p[('exc', 'sigma')].quantity, [0.05, 0.05])
	# 			# if p[('exc', 'sigma')].quantity[0] == se
	# 			# and p[('inh', 'sigma')].quantity[1] == si
	# # # 		# and p[('sim', 'symmetric_centers')].quantity == False
	# # # 		# or p[('inh', 'sigma')].quantity == 0.08
	# # # 		# and p[('exc', 'sigma')].quantity < 0.059
	# # # 		# if p[('inh', 'sigma')].quantity <= 0.2
	# # # 		# and  p[('exc', 'sigma')].quantity <= 0.055
	# # 		# and p[('sim', 'boxtype')].quantity == 'linear'
	# 		 	if p[('sim', 'seed_sigmas')].quantity <= 4
	# 		# and p[('sim', 'initial_x')].quantity > 0
	# 		]	
	general_utils.snep_plotting.plot_psps(
			tables, psps, project_name='learning_grids', save_path=save_path,
			 psps_in_same_figure=True, function_kwargs=function_kwargs, prefix='Sargolini')

	# Note: interval should be <= 300, otherwise the videos are green
	# animate_psps(tables, psps, 'animate_positions', 0.0, 3e2, interval=50, save_path=save_path)
	# animate_psps(tables, psps, 'animate_output_rates', 0.0, 1e6, interval=50, save_path=save_path, take_weight_steps=True)

	# # # t2 = time.time()
	# tables.close_file()
	# plt.show()
	# print 'Plotting took %f seconds' % (t2 - t1)