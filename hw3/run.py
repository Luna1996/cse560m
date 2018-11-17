import subprocess

d1 = [256, 512, 1024, 2048, 4096]
d2 = [4, 8, 16, 32, 64, 128, 256]

for a1 in d1:
  for a2 in d2:
    for a3 in d2:
      savedir = 'd%dx%dx%d'%(a1,a2,a3)
      print(savedir,'start')
      subprocess.check_call('$GEM5/build/ARM/gem5.opt',\
      '--outdir="%s"'%(savedir)\
      'hw3config.py',\
      '-c','$GEM5/../test_progs/daxpy/daxpy_arm_big',\
      '--cpu-type="DerivO3CPU"',\
      '--caches','--l2cache',\
      '--num-phys-float-regs=%d'%(a1),\
      '--num-rob-entries=%d'%(a2),\
      '--num-iq-entries=%d'%(a3))
      print(savedir,'done')