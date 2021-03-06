import snep.utils
# import utils
import matplotlib as mpl

mpl.use('Agg')
# import plotting
from . import animating
# import matplotlib.pyplot as plt
import time
import general_utils.arrays
import general_utils.misc
import general_utils.snep_plotting
import numpy as np
import string
import os

# import IPython

# Set font sizes in general and for all legends
# Use fontsize 42 for firing rate maps and correlograms, then change their
# height to 164pt to have the rate map of the same size as the examples
# mpl.rc('font', size=18)
mpl.rc('font', size=12)


# mpl.rc('legend', fontsize=18)
# If you comment this out, then everything works, but in matplotlib fonts
# mpl.rc('font', **{'family': 'serif', 'serif': ['Helvetica']})
# mpl.rc('text', usetex=True)


def animate_psps(tables, paramspace_points,
                 animation_function, start_time, end_time, step_factor=1,
                 save_path=False, interval=50, take_weight_steps=False):
    """
    Animate (several) paramspace points

    _________
    Arguments:
    See also definition of plot_psps
    - animation_function: string with the name of animation defined in animating.py
    """
    for n, psp in enumerate(psps):
        print(n)
        print(psp)
        params = tables.as_dictionary(psp, True)
        try:
            rawdata = tables.get_raw_data(psp)
        except:
            continue
        animation = animating.Animation(params, rawdata, start_time=start_time,
                                        end_time=end_time,
                                        step_factor=step_factor,
                                        take_weight_steps=take_weight_steps)
        ani = getattr(animation, animation_function)
        if save_path:
            # remove the uno string
            save_path_full = os.path.join(save_path,
                                          string.replace(str(psp), ' uno',
                                                         '') + '.mp4')
        else:
            save_path_full = False
        ani(save_path=save_path_full, interval=interval)


def get_path_tables_psps(date_dir):
    path = general_utils.snep_plotting.get_path_to_hdf_file(date_dir)
    tables = snep.utils.make_tables_from_path(path)
    tables.open_file(False)
    tables.initialize()
    print(tables)
    psps = tables.paramspace_pts()
    return path, tables, psps


######################################################
##########	Decide what should be plotted	##########
######################################################
# function_kwargs is a list of tuples of strings (the function names)
# and dictionaries (the function parameters as keys and values)
t0 = 0.
t1 = 1e7
t2 = 2e7
# t2 = 2e7
# t3 = 1e8
t3 = -1
t_hm = 5e4
# t = 16e7
t = 18e5 * 5
t_switch_experiments = 36e5
# t4 = 24e6
# t2 = 40e5
# t1 = 120e6
# t1 = 80e6
# t1 = 100e6
# t=10e7
method = None
type = 'exc'
# t2 = 1e7
# Neurons for conjunctive and grid cells
# neurons = [23223, 51203, 35316, 23233]
# Neurons for head direction cell
# neurons =[5212, 9845, 9885, 6212]
plot_individual = False
gridscore_norm = 'all_neighbor_pairs'
colorbar_range = np.array([0, 1])
# gridscore_norm = None
t_reference = 4.9 * 36e4
t_compare = 8 * 36e4
conversion_factor = 36e3
time_l = 18e5 / 4
time_r = 18e5 / 2
time_all = 18e5
function_kwargs = [
    ##########################################################################
    ##############################   New Plots  ##############################
    ##########################################################################

    # ('output_rates_left_and_right', dict(time_l=time_l, time_r=time_r,
    # 									 show_colorbar=True)),
    # ('spikemap_from_ratemap', dict(n=2000, time_l=time_l, time_r=time_r)),
    # ('gridscore_vs_location', dict(n=2000, time_l=time_l, time_r=time_r)),
    # ('spikemap_from_ratemap', dict(n=2000, time=time_all)),
    # ('gridscore_vs_location', dict(n=2000, time=time_all)),

    # ('distance_histogram_for_spikemap_from_ratemap', dict(frame=-1, n=2000)),
    # ('distance_histogram_for_ratemap', dict(frame=-1)),

    # ('plot_correlogram', dict(time=time_l, from_file=True, mode='same',
    # 						  method='langston')),
    # ('plot_scorrelogram', dict(time=time_r, from_file=True, mode='same',
    # 						  method='langston')),
    # ('plot_correlogram', dict(time=0, from_file=True,
    # 						  mode='same', method='langston',
    # 						  time_l=time_l, time_r=time_r, left_right=True)),
    # ('plot_output_rates_from_equation', dict(time=-1,
    # 										 from_file=False,
    # 										 show_colorbar=True)),
    # ('plot_correlogram', dict(time=01, from_file=True, mode='same',
    # 						  method='langston')),
    # # ('weight_evolution', dict(syn_type='exc', weight_sparsification=1))
    # ('correlation_in_regions', dict(region_size=(60, 12))),
    ('grid_score_histogram', {})
    # ('correlation_of_final_grid_from_left_to_right_all', dict(region_size=(
    # 	60, 12))),
    # ('correlation_of_final_grid_from_left_to_right_all', dict(region_size=(
    # 	60, 10))),
    # ('correlation_of_final_grid_from_left_to_right_all', dict(region_size=(
    # 	60, 6))),
    # ('correlation_of_final_grid_from_left_to_right_all', dict(region_size=(
    # 	60, 4))),

    # ('trajectory_with_firing',
    # 		dict(start_frame=0, end_frame=4e5)),

    # ('input_tuning', dict(populations=['exc'], neuron=0)),
    # ('input_tuning', dict(populations=['inh'], neuron=0)),
    # ('input_tuning', dict(populations=['exc'], neuron=1)),
    # ('input_tuning', dict(populations=['inh'], neuron=1)),
    # ('input_tuning', dict(populations=['exc'], neuron=2)),
    # ('input_tuning', dict(populations=['inh'], neuron=2)),

]

if __name__ == '__main__':
    t1 = time.time()

    # for date_dir in ['2016-07-27-17h22m04s_1d_grf_grid_cell']:
    for date_dir in [
                    # '2016-12-07-13h59m36s_different_centers_different_trajectories',
                    # '2016-06-29-17h09m25s_10_conjunctive_cells',
                    # '2017-04-28-12h36m43s_20_conjunctive_cells',
                    # '2017-05-02-11h20m28s_20_conjunctive_cells_less_angular_noise',
            # '2017-09-01-11h38m37s_room_switch',
        # '2017-09-01-12h56m41s_room_switch',
        # '2017-09-01-14h52m33s_test',
        # '2017-09-05-14h41m29s_room_switch_1fps',
        # '2017-09-05-16h03m34s_room_switch_2fps',
        # '2017-09-05-16h04m15s_room_switch_4fps',
        # '2017-10-16-16h17m50s_wernle_10_seeds',
        # '2017-10-17-11h24m06s_wernle_start_left',
        # '2017-10-17-11h45m12s_start_right',
        # '2017-10-17-11h46m00s_start_left',
        # '2017-10-23-15h44m22s_wernle_independent_normalization',
        # '2017-10-23-18h00m15s_wernle_independent_norm_start_right_100',
        # '2017-10-24-11h10m34s_wernle_independent_norm_start_left_100',
        # '2017-10-24-11h11m39s_wernle_single_norm_left_100',
        # '2017-10-24-11h27m12s_wernle_single_norm_right_100',
        # '2017-11-09-18h37m32s_wernle_seed_55_with_trajectory'
        # '2018-01-25-11h50m52s_exc_1fps_inh_50fps_mixed_statistics',
        # '2018-01-25-11h50m52s_exc_1fps_inh_50fps_mixed_statistics',
        # '2018-01-25-12h14m36s_exc_1fps_inh_50fps_faster',
        # '2018-01-25-12h48m18s_faster',
        # '2018-01-25-12h50m08s_faster_2',
        # '2018-01-25-13h01m42s_80_simulations',
        # '2018-01-25-13h02m38s_80_simulations_larger_weight_spreading',
        # '2018-01-25-13h04m48s_80_simulations_larger_init_weight',
        # '2018-01-25-14h44m00s_both_higher',
        # '2018-01-25-14h59m11s_exc_1fps_inh_50fps_higher_initi_weight_and_noise_500sims',
        # '2018-01-25-16h56m09s_500sims_init_weight_2',
        # '2018-01-25-17h27m14s_faster_inhibition',
        # # '2018-01-25-17h33m12s_exc_gaussian_height_2_results_in_all_place_cells',
        # '2018-01-25-17h39m33s_smaller_sigmas',
        # '2018-01-25-17h45m46s_init_weight_4',
        # '2018-01-25-18h01m06s_init_weight_4_faster',
        # '2018-01-25-18h20m38s_slower_inhibition',
        # '2018-01-26-10h36m34s_500sims_only_larger_weight_spread',
        # '2018-01-26-10h39m46s_500sims_init_weight_4_and_larger_spread'
        '2018-01-26-13h02m03s_mixed_statistics'
            ]:
        path, tables, psps = get_path_tables_psps(date_dir)
        save_path = False
        save_path = os.path.join(os.path.dirname(path), 'visuals')
        try:
            os.mkdir(save_path)
        except OSError:
            pass

        all_psps = psps
        # for seed in [0,1,2,3]:
        # for eta_factor in [0.2, 0.5, 1.0]:
        # 	for sigma_inh in [0.25, 0.20]:
        # for sigma in sigmaI_range:
        psps = [p for p in all_psps
                # if p[('sim', 'seed_centers')].quantity == 55
                # and  p[('sim', 'alpha_room2')].quantity == 1
                # and p[('exc', 'fields_per_synapse')].quantity == 1
                # if not (p[('sim', 'seed_centers')].quantity == 1 and p[('sim', 					'room_coherence_after_switch')].quantity == 0.25 and p[('exc', 					'fields_per_synapse')].quantity == 2)
                #
                # if p[('inh', 'weight_factor')].quantity < 1.025
                # if p[('sim', 'gaussian_process_rescale')].quantity == 'fixed_mean'
                # if general_utils.misc.approx_equal(p[('exc', 'eta')].quantity,
                # 								  eta_factor * 3e-5 / (2* 0.5 * 10. * 22),
                # 								   3e-5 / (2* 0.5 * 10. * 22) / 100.)
                ]

        prefix = general_utils.plotting.get_prefix(function_kwargs)
        # prefix = 'eta_factor_{0}_sigma_inh_{1}'.format(eta_factor, sigma_inh)
        # prefix = 'seed_{0}'.format(seed)
        # prefix = 'extrema_distribution_sigma_{0}'.format(sigma)
        general_utils.snep_plotting.plot_psps(
            tables, psps, project_name='learning_grids', save_path=save_path,
            psps_in_same_figure=True, function_kwargs=function_kwargs,
            prefix=prefix, automatic_arrangement=True, file_type='png',
            dpi=300, figsize=(7, 4), transparent=False)

    # Note: interval should be <= 300, otherwise the videos are green
    # animate_psps(tables, psps, 'animate_positions', 0.0, 3e2, interval=50, save_path=save_path)
    # animate_psps(tables, psps, 'animate_output_rates', 0.0, 1e6, interval=50, save_path=save_path, take_weight_steps=True)

t2 = time.time()
# tables.close_file()
# plt.show()
print('Plotting took % seconds' % (t2 - t1))
