from m5 import fatal
import m5.objects
from textwrap import TextWrapper

# add options
def addHW4Opts(parser):
  parser.add_option("--l1i_size", type="str", default="64KB")
  parser.add_option("--l1d_size", type="str", default="64KB")
  parser.add_option("--pipeline_width", type="int", default=8)
  parser.add_option("--branch_pred", type="str", default="LTAGE")

# set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    cpu.fetchWidth = Param.Unsigned(options.pipeline_width, "Fetch width")
    cpu.decodeWidth = Param.Unsigned(options.pipeline_width, "Decode width")
    cpu.renameWidth = Param.Unsigned(options.pipeline_width, "Rename width")
    cpu.dispatchWidth = Param.Unsigned(options.pipeline_width, "Dispatch width")
    cpu.issueWidth = Param.Unsigned(options.pipeline_width, "Issue width")
    cpu.wbWidth = Param.Unsigned(options.pipeline_width, "Writeback width")
    cpu.commitWidth = Param.Unsigned(options.pipeline_width, "Commit width")
    cpu.squashWidth = Param.Unsigned(options.pipeline_width, "Squash width")
    cpu.branchPred = options.branch_pred