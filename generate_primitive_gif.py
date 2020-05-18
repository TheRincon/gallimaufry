import sys
import subprocess
import os

def build_command(definition_array, input_file, output_file):
	for index, entry in enumerate(definition_array):
		subprocess.run(["./primitive", "-i", input_file, "-o", output_file[0] + '-' + str(index + 1) + output_file[1], "-n", entry])


if __name__ == '__main__':
	args = sys.argv[1:]
	output_file = args[2] if len(args) > 2 else 'output.png'
	def_array = args[0].split(',')
	input_file = args[1]
	filename, file_extension = os.path.splitext(output_file)
	build_command(def_array, input_file, [filename, file_extension])
	subprocess.run(["convert", f'{filename}-%d{file_extension}[1-{len(def_array)}]', f'{filename}.gif'])