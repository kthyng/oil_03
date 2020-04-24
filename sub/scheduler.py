import os

nhiss = [1, 2, 5, 10, 20, 50, 100, 200, 500]
whichadvect = ['U3C4','MPDATA']


for nhis in nhiss:

    ## Update .in file ##
    # input template and output version of .in file
    infile_in = 'oil_03_ss.in'
    infile_out = 'oil_03_ss_nhis%i.in' % nhis

    # Substitute appropriate values in for placeholders in infile_in, then save changes to infile_out.
    outdir = 'output_ss/%s/nhis%i/' % (whichadvect,nhis)
    hisname = '%s/oil_03_his.nc' % outdir
    avgname = '%s/oil_03_avg.nc' % outdir
    strings = (nhis, nhis, hisname, avgname, '../External/'+infile_in, '../External/'+infile_out)
    os.system("sed -e 's/#NHIS#/%s/' -e 's/#NAVG#/%s/' -e 's/#HISNAME#/%s/' -e 's/#AVGNAME#/%s/' %s > %s" % strings)
        
    # make output directory
    os.system('mkdir -p %s' % ('../'+outdir))

    ## Update slurm file ##
    jobfile_in = 'run_oil_ss.slurm'
    jobfile_out  = 'run_oil_ss_nhis%i.slurm' % (nhis)

    logfile = 'ss_%s_nhis%i' % (whichadvect,nhis)
    strings = (logfile, whichadvect, nhis, jobfile_in, jobfile_out)
    os.system("sed -e 's/#LOGNAME#/%s/' -e 's/#WHICHADVECT#/%s/' -e 's/#NHIS#/%s/' %s > %s" % strings)

    os.chdir('../')
    os.system('sbatch sub/%s' % jobfile)
    os.chdir('./sub')

