from m5 import fatal
import m5.objects
from textwrap import TextWrapper

# add options
def addHW4Opts(parser):
  parser.add_option("--pipeline_width", type="int", default=8)

# set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    cpu.fetchWidth = options.pipeline_width
    cpu.decodeWidth = options.pipeline_width
    cpu.renameWidth = options.pipeline_width
    cpu.dispatchWidth = options.pipeline_width
    cpu.issueWidth = options.pipeline_width
    cpu.wbWidth = options.pipeline_width
    cpu.commitWidth = options.pipeline_width
    cpu.squashWidth = options.pipeline_width