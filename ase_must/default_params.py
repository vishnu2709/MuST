defaults = {
    "default_in_pot": "Default Potential Input File Name",
    "in_pot": "Potential Input File Name",
    "default_out_pot": "Default Potential Output File Name",
    "nscf": "No. Iterations (> 0)",
    "method": "Method of SCF Calculation",
    "out_to_scr": "Output to Screen (y/n)",
    "out_level": "Output Level (>= -1)",
    "out_proc_id": "Output Proc. ID (>= -1)",
    "out_atom_id": "Output Atom ID (>= -1)",
    "generate_movie": "Generate System Movie",
    "stop_rout_name": "Stop-at Routine Name",
    "write_pot_niter": "No. Iter for Each Pot. Write",
    "movie_niter": "No. Iter for Each Movie",
    "calc_harris_energy": "Calc. Harris Energy (H.E.)",
    "ngauss_r": "No. Gauss Pts. along r",
    "ngauss_theta": "No. Gauss Pts. along theta",
    "vband_bot_est": "Valence Band Bottom Est.",
    "temperature": "Temperature Parameter (K)",
    "dos_id": "DOS Run ID",
    "uniform_grid": "Uniform Grid Parameters",
    "visual_grid_type": "Visual Grid Type (0<D<4)",
    "grid_scale": "Grid Scale ",
    "grid_origin": "Origin Grid Vector",
    "grid_1": "Grid Vector 1",
    "grid_2": "Grid Vector 2",
    "grid_3": "Grid Vector 3",
    "grid_pts": "Grid Points",
    "e_density_out_id": "Output Electron Density ID (>= -1)",
    "density_format": "Output Density Format",
    "etol": "Energy (Ryd) Tol (> 0)",
    "ptol": "Potential Tol (> 0)",
    "ftol": "Fermi Energy Tol (> 0)",
    "slu_tol": "SuperLU Tol (> 0)",
    "ktol": "K-space Check Tol (> 0)",
    "rms_tol": "Other RMS Tol (> 0)",
    "val_e_rel": "Val. Electron Rel (>= 0)",
    "core_e_rel": "Core Electron Rel (>= 0)",
    "add_electrons": "Additional Electrons",
    "charge_sym": "Charge Symmetry (>=0)",
    "ss_solver": "Single Site Solver (>= 0)",
    "ss_method": "Single Site Solution Method (>=-1)",
    "irreg_sols": "Irregular Solutions (>=0)",
    "pole_step": "Pole Search Step (>0.0)",
    "sol_lmax_cutoff": "Solutions Lmax Cutoff",
    "compute_phase_shifts": "Compute Phase Shifts (>=0)",
    "lmax_solver": "SS Lmax Potential Solver",
    "potential_type": "Potential Type (>= 0)",
    "xc": "Exch-Corr. LDA Type (>= 0)",
    "lda_improve_scheme": "LDA Improvement Scheme",
    "lda_file_name": "LDA+U Parameter File Name",
    "moment_dir_file": "Moment Direction File Name",
    "spin": "Spin Index Param (>= 1)",
    "int_espin": "Interstitial Electron Spin",
    "canted_torque_coef": "Canted Moment Torque Coef.",
    "calc_j_ij": "Calculate J_ij (y/n)",
    "read_mesh": "Read E-mesh from emeshs.inp",
    "contour_type": "Contour Type (>= 0)",
    "n_contours": "Number of Contours (> 0)",
    "egrid_type": "Energy Grid Type (>= 0)",
    "n_egrids": "No. Energy Grids",
    "extra_energy_pts": "No. Extra Energy Points",
    "offset_energy_pt": "Offset Energy Point",
    "erbot": "Real Axis Bottom erbot",
    "ertop": "Real Axis Top ertop",
    "eibot": "Imag Axis Bottom eibot",
    "eitop": "Imag Axis Top eitop",
    "iterate_fermi_energy": "Iterate Fermi energy",
    "real_axis_method": "SS Real Axis Int. Method",
    "real_axis_points": "SS Real Axis Int. Points",
    "t_inversion": "T-matrix inversion (>= 0)",
    "m_inversion": "M-matrix inversion (>= 0)",
    "n_time_steps": "No. Spin-dynamics Time Steps (>= 0)",
    "time_step": "Spin-dynamics Time Step",
    "mix_quantity": "Mixing quantity type",
    "mix_algo": "Mixing algorithm",
    "lloyd_correction": "Lloyd correction",
    "lloyd_mode": "Lloyd mode",
    "k_solver": "K-space Solver Method",
    "read_kmesh": "Read K-mesh from kmeshs.inp",
    "k_scheme": "Scheme to Generate K (>=0)",
    "n_kmesh": "No. K Meshs in IBZ (> 0)",
    "kpts": "Kx, Ky, Kz Division (> 0)",
    "bzsym": "Symmetrize BZ Integration",
    "large_sphere_radius": "Large sphere radius (a.u.)",
    "pot_in_form": "Default Potential Input File Form",
    "pot_out_form": "Default Potential Output File Form",
    "moment_direction": "Default Moment Direction",
    "constrain_field": "Default Constrain Field",
    "lmax_T": "Default Lmax-T matrix",
    "lmax_wave_func": "Default Lmax-Wave Func",
    "lmax_pot": "Default Lmax-Potential",
    "lmax_trunc_pot": "Default Lmax-Trunc Pot",
    "lmax_charge_den": "Default Lmax-Charge Den",
    "lmax_step_func": "Default Lmax-Step Func",
    "liz_neighbors": "Default LIZ # Neighbors",
    "liz_nn_shells": "Default LIZ # NN Shells",
    "liz_shell_lmax": "Default LIZ Shell Lmax",
    "liz_cutoff": "Default LIZ Cutoff Radius",
    "rho_mix_param": "Default Rho  Mix Param.",
    "pot_mix_param": "Default Pot  Mix Param.",
    "mom_mix_param": "Default Mom  Mix Param.",
    "chg_mix_param": "Default Chg  Mix Param.",
    "evec_mix_param": "Default Evec Mix Param.",
    "max_core_radius": "Default Maximum Core Radius",
    "max_mt_radius": "Default Maximum Muffin-tin Radius",
    "ndivin": "Default No. Rad Points ndivin ",
    "ndivout": "Default No. Rad Points ndivout",
    "nmult": "Default Integer Factor nmult",
    "pseudo_charge_radius": "Default Pseudo Charge Radius",
    "screen_pot": "Default Screen Pot.",
    "lmax_screen": "Default Lmax-Screen",
    "rcut_screen": "Default Rcut-Screen",
    "local_sic": "Local SIC",
    "mix_param": "Default Mixing Parameter",
    "frozen_core_calc": "Frozen-Core Calculation",
    "frozen_core_file": "Frozen-Core File Name",
    "em_iter": "Maximum Effective Medium Iterations",
    "em_scheme": "Effective Medium Mixing Scheme",
    "em_mix_param": "Effective Medium Mixing Parameters",
    "em_eswitch": "Effective Medium Mixing eSwitch Value",
    "em_tmatrix_tol": "Effective Medium T-matrix Tol (> 0)",
    "core_radius": "Default Core Radius",
    "mt_radius": "Default Muffin-tin Radius",
    "radical_plane_ratio": "Default Radical Plane Ratio",
    "ntasks": "Number of Tasks",
    "radial_grid_step": "Default Radial Grid Exponential Step",
    "uniform_grid_origin": "Uniform Grid Origin",
    "core_norm_range": "Core States Normalization Range",
    "renorm_gf": "Renormalize Green function"
}