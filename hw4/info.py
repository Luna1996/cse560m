from m5 import inspect
from m5.defines import buildEnv
from importlib import import_module
for package in ["generic", buildEnv['TARGET_ISA']]:
  try:
    package = import_module(".cores." + package, package=__package__)
  except ImportError:
    # No timing models for this ISA
    continue

  for mod_name, module in inspect.getmembers(package, inspect.ismodule):
    for name, cls in inspect.getmembers(module, is_cpu_class):
      print(name)
