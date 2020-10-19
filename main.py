import os
import subprocess

input_dir = './input'
output_dir = './output'
video_files = os.listdir(input_dir)

def getInputPath(filename):
  return os.path.join(input_dir, filename)

def getOutputPath(filename):
  return os.path.join(output_dir, filename)

for input_video in video_files:
  input_video_path = getInputPath(input_video)

  if input_video != '.DS_Store' and not os.path.isdir(input_video_path):
    pixel_format_flag = "-pix_fmt yuv420p" if os.path.splitext(input_video_path)[1].lower() == '.avi' else ""
    output_video_path = getOutputPath(os.path.splitext(input_video)[0] + '.mp4')

    command_convert = f"ffmpeg -y -i \"{input_video_path}\" {pixel_format_flag} \"{output_video_path}\""
    subprocess.run(command_convert, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

    command_attributes = f"touch -r \"{input_video_path}\" \"{output_video_path}\""
    subprocess.run(command_attributes, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    print(f"*** Completed encoding of \"{output_video_path}\" ***")

print("Completed export of all videos!")
