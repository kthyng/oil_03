[![DOI](https://zenodo.org/badge/250289497.svg)](https://zenodo.org/badge/latestdoi/250289497)

# oil_03
Project files for running online test with oil application

## Overview for running online simulation

- Can compile your COAWST online/offline code (get from https://github.com/kthyng/COAWST-ROMS-OIL) with `python build-coawst.py --clean --mpi  oil_03` (or use your own preferred approach)
- Run your simulation with files starting from templates:
  - `Include/oil_03.h`
    - Choose tracer advection scheme:
      - MPDATA or U3C4 have been tested for offline accuracy and MPDATA performed better
    - double precision for best results
    - ANA_AKTCLIMA should be defined so that necessary variables can be found
  - `External/ocean_oil_03.in`
    - Choose output frequency for your available storage and desired offline accuracy
    - Choose his vs avg file output from online to force offline simulation (doesn't matter much which you choose)
    - Output necessary variables (all currently included)
      - zeta, ubar, vbar, u, v for forcing, dye_01; optional: Aks
    - varinfo file (links to varinfo-online.dat in COAWST-ROMS-OIL)
  - `sbatch sub/run_oil.slurm`: to run on slurm clusters

Then, use output from this simulation to run an offline simulation using the files at https://github.com/kthyng/oil_off.
