import sys
import subprocess
import os

def build_command(definition_array, input_file, output_file, shapes):
	for index, entry in enumerate(definition_array):
		subprocess.run(["primitive", "-i", input_file, "-o", output_file[0] + '-' + str(index + 1) + output_file[1], "-n", entry, "-m", shapes])


if __name__ == '__main__':
	args = sys.argv[1:]
	output_file = args[2] if len(args) > 2 else 'output.png'
	# mode: 0=combo, 1=triangle, 2=rect, 3=ellipse, 4=circle, 5=rotatedrect, 6=beziers, 7=rotatedellipse, 8=polygon
	shapes = args[3] if len(args) > 3 else '1'
	def_array = args[0].split(',')
	input_file = args[1]
	filename, file_extension = os.path.splitext(output_file)
	build_command(def_array, input_file, [filename, file_extension], shapes)
	subprocess.run(["convert", f'{filename}-%d{file_extension}[1-{len(def_array)}]', f'{filename}.gif'])
