from m5 import fatal
import m5.objects
from textwrap import TextWrapper
from m5.util import addToPath
gem5_path = os.environ["GEM5"]
addToPath(gem5_path + '/configs')
from common import BPConfig

# add options
def addHW4Opts(parser):
  parser.add_option("--pipeline_width", type="int", default=8)
  parser.add_option("--bp-type", type="choice", default=None,
                      choices=BPConfig.bp_names(),
                      help = """
                      type of branch predictor to run with
                      (if not set, use the default branch predictor of
                      the selected CPU)""")

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
    cpu.branchPred = BPConfig.get(options.bp_type)