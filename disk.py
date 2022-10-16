from tools import get_disk_free_space_gb


class Disk:
    def __init__(self, disk_id, path):
        self.id = disk_id,
        self.path = path

    def free_space_gb(self):
        return get_disk_free_space_gb(self.path) < 10
