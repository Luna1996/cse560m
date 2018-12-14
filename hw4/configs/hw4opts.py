from m5 import fatal
import m5.objects
from textwrap import TextWrapper


# add options
def addHW4Opts(parser):
  parser.add_option("--branch-pred", type="str", default="LTAGE")

# set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    pass
