import os

from db import MySQL
from disk import Disk


class Event:
    def __init__(self, event_id, time, monitor_id, disk: Disk):
        self.id = event_id
        self.time = time
        self.monitor_id = monitor_id
        self.disk = disk

    def remove(self):
        path = os.path.join(self.disk.path, self.monitor_id, self.time.strftime('%Y-%m-%d'), self.id)
        with MySQL() as db:
            db.set(f'delete from Events where id="{self.id}"')
        os.remove(path)
