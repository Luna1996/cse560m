import subprocess

d1 = ['8kB', '16kB', '32kB', '64kB']
d2 = [4,8]
d3 = [
    'O3_ARM_v7a_3', 'AtomicSimpleCPU', 'ex5_big', 'DerivO3CPU', 'MinorCPU',
    'HPI', 'ex5_LITTLE', 'NonCachingSimpleCPU', 'TimingSimpleCPU'
]
d4 = ['LocalBP', 'TournamentBP', 'BiModeBP', 'TAGE', 'LTAGE']

for a in range(2):
  savedir = 'd2x%d' % (a)
  print(savedir, 'start')
  subprocess.check_call(['/project/linuxlab/gem5/gem5/build/ARM/gem5.opt',\
  '--outdir=%s'%(savedir),\
  'hw4config.py',\
  '--l1d_size=64kB',\
  '--l1i_size=64kB',\
  '--pipeline_width=%d'%(d2[a]),\
  '--cpu-type=DerivO3CPU',\
  '--bp-type=LTAGE',\
  '--caches','--l2cache',\
  '--cmd=/project/linuxlab/gem5/test_progs/dibs/opt_to_tiff'])
  print(savedir, 'done')

for a in range(9):
  savedir = 'd3x%d' % (a)
  print(savedir, 'start')
  subprocess.check_call(['/project/linuxlab/gem5/gem5/build/ARM/gem5.opt',\
  '--outdir=%s'%(savedir),\
  'hw4config.py',\
  '--l1d_size=64kB',\
  '--l1i_size=64kB',\
  '--pipeline_width=8',\
  '--cpu-type=%s'%(d3[a]),\
  '--bp-type=LTAGE',\
  '--caches','--l2cache',\
  '--cmd=/project/linuxlab/gem5/test_progs/dibs/opt_to_tiff'])
  print(savedir, 'done')

for a in range(5):
  savedir = 'd4x%d' % (a)
  print(savedir, 'start')
  subprocess.check_call(['/project/linuxlab/gem5/gem5/build/ARM/gem5.opt',\
  '--outdir=%s'%(savedir),\
  'hw4config.py',\
  '--l1d_size=64kB',\
  '--l1i_size=64kB',\
  '--pipeline_width=8',\
  '--cpu-type=DerivO3CPU',\
  '--bp-type=%s'%(d4[a]),\
  '--caches','--l2cache',\
  '--cmd=/project/linuxlab/gem5/test_progs/dibs/opt_to_tiff'])
  print(savedir, 'done')
