# add options
def addHW4Opts(parser):
  parser.add_option("--pipeline_width", type="int", default=8)
  parser.add_option("--bp-type", type="str", default="LTAGE")

# set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    if cpu.fetchWidth:
      cpu.fetchWidth = options.pipeline_width
    if cpu.decodeWidth:
      cpu.decodeWidth = options.pipeline_width
    if cpu.renameWidth:
      cpu.renameWidth = options.pipeline_width
    if cpu.dispatchWidth:
      cpu.dispatchWidth = options.pipeline_width
    if cpu.issueWidth:
      cpu.issueWidth = options.pipeline_width
    if cpu.wbWidth:
      cpu.wbWidth = options.pipeline_width
    if cpu.commitWidth:
      cpu.commitWidth = options.pipeline_width
    if cpu.squashWidth:
      cpu.squashWidth = options.pipeline_width