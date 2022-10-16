import os


def get_disk_free_space_gb(folder):
    st = os.statvfs(folder)
    return int(st.f_bavail * st.f_frsize / 1024 / 1024 / 1024)


def get_size_mb(path):
    return int(os.path.getsize(path) / 1024 / 1024)
