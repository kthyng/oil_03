# oil_03
Project files for running online test with oil application

## Run as online simulation using these types of files

1. As a starting place, use files like:
  - `python build-coawst.py --clean --mpi  oil_03_kmt`: convenient way to compile your simulation, but not necessary
  - `Include/oil_03_kmt.h`: already has flags set up for online simulation.
  - `External/ocean_oil_03_LeftGaussian_1hr.in`: most of what is in here should just be to run your normal online simulation, though a lot of extra variables are set to be output for the offline simulation. (I will be testing to see how much the sets of variables matter for running offline) Note that VARNAME *HAS* to match the location of the file for the offline COAWST oil code or you will get a segfault. Your file locations will need to be updated from this file.
  - `sbatch sub/run_oil_LeftGaussian_1hr.slurm`: for TAMU clusters to run simulation
1. Then, use output from this simulation to run an offline simulation using the files at https://github.com/kthyng/oil_off.
