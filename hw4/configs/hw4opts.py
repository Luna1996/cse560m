# add options
def addHW4Opts(parser):
  parser.add_option("--pipeline_width", type="int", default=8)
  parser.add_option("--bp-type", type="str", default="LTAGE")


# set parameters taken in from options on command line
def set_config(cpu_list, options):
  for cpu in cpu_list:
    if hasattr(cpu, 'fetchWidth'):
      cpu.fetchWidth = options.pipeline_width
    if hasattr(cpu, 'decodeWidth'):
      cpu.decodeWidth = options.pipeline_width
    if hasattr(cpu, 'renameWidth'):
      cpu.renameWidth = options.pipeline_width
    if hasattr(cpu, 'dispatchWidth'):
      cpu.dispatchWidth = options.pipeline_width
    if hasattr(cpu, 'issueWidth'):
      cpu.issueWidth = options.pipeline_width
    if hasattr(cpu, 'wbWidth'):
      cpu.wbWidth = options.pipeline_width
    if hasattr(cpu, 'commitWidth'):
      cpu.commitWidth = options.pipeline_width
    if hasattr(cpu, 'squashWidth'):
      cpu.squashWidth = options.pipeline_width