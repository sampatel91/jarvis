import sys
import os
import tempfile
import constants as const
import subprocess

def get_resample_cmd(src, dest):
    """
    Arguments: source path x destination path
    
    Returns the LAME command to resample the file found at the base of the 
    given source path.
    """
    cmd = '%s --resample 16 -m m -b 16 --silent %s %s' % (const.LAME, src, dest)
    return cmd

def get_decode_cmd(src, dest):
    """
    Arguments: source path x destination path

    Returns the LAME command to decode the file found at the base of the 
    given source path.
    """
    cmd = '%s --decode --silent --mp3input %s %s' % (const.LAME, src, dest)
    return cmd

def get_ogg_conv_cmd(src, dest):
    cmd = 'oggdec --quiet %s -o %s' % (src, dest)
    return cmd

def normalize_wav(filepath):
    """
    Arguments: filepath

    Normalizes and returns a .wav file found at the base of the given
    filepath.
    """
    temp_dir = '/tmp/dan'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    f_type = os.path.splitext(filepath)[1]
    if f_type == '.ogg':
        temp_file, temp_path = tempfile.mkstemp(dir='/tmp/dan')
        cmd = get_ogg_conv_cmd(filepath, temp_path)
        filepath = temp_path
        subprocess.call(cmd, shell=True)

    temp_file1, temp_path1 = tempfile.mkstemp(dir='/tmp/dan')
    command1 = get_resample_cmd(filepath, temp_path1)
    subprocess.call(command1, shell=True)
    
    temp_file2, temp_path2 = tempfile.mkstemp(dir='/tmp/dan')
    command2 = get_decode_cmd(temp_path1, temp_path2)
    subprocess.call(command2, shell=True)

    return temp_path2
