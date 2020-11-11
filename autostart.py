print("IMPORTED ME!")
def who_imports(studied_module):
	for loaded_module in sys.modules.values():
		for module_attribute in dir(loaded_module):
				if getattr(loaded_module, module_attribute) is studied_module:
						yield loaded_module

import sys
import os
for m in who_imports(os):
  print (m.__name__)

from flask import Flask, render_template, request, redirect  # add

print ('I am being imported by', sys._getframe(1).f_globals.get('__name__'))

app = Flask("__main__")

if __name__ == "__main__":
  app.run(debug=True)
else:
  print(__package__)
