import sys
import os
import argparse
import glob
import re
import shutil


def enum_output_dirs(output_dir):
    dirs = []
    for file in glob.glob(output_dir + os.sep + "*"):
        if os.path.isdir(file):
            dir_name = os.path.basename(os.path.normpath(file))
            dirs.append({'dir_name': dir_name,'dir_path': file})
    return dirs


def process_file(file,output_dirs):
    print("File found: {}".format(file))
    file_name = os.path.basename(os.path.normpath(file))

    for item in output_dirs:
        dir_path = item['dir_path']
        target_file = os.path.join(dir_path, file_name)
        try:
            shutil.copyfile(file, target_file)
        except Exception as e:
            print("Copy failed. {}".format(str(e)))

        if os.path.exists(target_file):
            print("Copy done to {}".format(dir_path))


def get_subfolder_name(path):
    parts = path.split(os.sep)
    if len(parts) <= 2:
        return None
    return parts[-2]

def main():
    parser = argparse.ArgumentParser('Batch copy files from source folder to target folder\'s subfolders')
    parser.add_argument('--input', dest='input', type=str, help='path to root directory with files to copy')
    parser.add_argument('--output', dest='output', type=str, help='path to directory where target subfolders reside')
    args = parser.parse_args()
    subfolder = get_subfolder_name(args.output)
    if subfolder:
        print("Magazine title extracted: {}".format(subfolder))
    else:
        print("Magazine title cannot be extracted from output path")
        return

    input_dir = args.input + os.sep + subfolder
    output_dirs = enum_output_dirs(args.output)
    print("Processing files in {} directory...".format(input_dir))
    counter = 0
    for file in glob.glob(input_dir + os.sep + "*.*"):
        process_file(file, output_dirs)
        counter += 1
        # break
    print("Done. {} files were processed".format(counter))

main()

