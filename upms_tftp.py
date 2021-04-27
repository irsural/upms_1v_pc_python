from typing import Optional, List
import logging
import os

import tftpy

from text import Text


__files_list_filename = "files_list.txt"
__exclude_words = ["ls", "check", "copy", "System"]


def get_files_list(a_ip: str) -> Optional[List[str]]:
    tftp_client = tftpy.TftpClient(a_ip, 69)
    try:
        tftp_client.download("ls.txt", __files_list_filename, timeout=1)
    except tftpy.TftpTimeout:
        logging.error(Text.get("get_files_list_err"))
        if os.path.isfile(__files_list_filename):
            tftp_client.context.end()
            os.remove(__files_list_filename)
        return None
    except Exception:
        if os.path.isfile(__files_list_filename):
            tftp_client.context.end()
            os.remove(__files_list_filename)
        raise
    else:
        with open(__files_list_filename, encoding='cp1251') as files_list_file:
            files_list = []
            for filename in files_list_file:
                for word in __exclude_words:
                    if word in filename:
                        break
                else:
                    files_list.append(filename.strip())
        os.remove(__files_list_filename)

    return files_list


def download_file_by_tftp(a_ip: str, a_filename: str, a_dst_filepath: str, a_tries_count=1) -> bool:
    tftp_client = tftpy.TftpClient(a_ip, 69)
    try_number = 0
    while try_number < a_tries_count:
        try:
            tftp_client.download(a_filename, a_dst_filepath, timeout=1)
            return True
        except tftpy.TftpTimeout:
            try_number += 1
            logging.error(Text.get("download_file_by_tftp_err").format(a_filename, try_number, a_tries_count))
    return False


if __name__ == '__main__':
    ip = '192.168.0.174'
    print(get_files_list(ip))
    print(download_file_by_tftp(ip, "main_table.csv", "", 3))
