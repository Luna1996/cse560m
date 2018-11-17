from m5 import fatal
import m5.objects
from textwrap import TextWrapper

#add options for number of ROB entries, IQ entries, and number of physical
#floating point registers
def addHW3Opts(parser):
  parser.add_option("--num-rob-entries",type="int",default=192)
  parser.add_option("--num-iq-entries",type="int",default=64)
  parser.add_option("--num-phys-float-regs",type="int",default=256)

#set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    cpu.numROBEntries = options.num_rob_entries
    cpu.numIQEntries = options.num_iq_entries
    cpu.numPhysFloatRegs = options.num_phys_float_entries
