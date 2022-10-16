from time import sleep

from db import MySQL
from disk import Disk
from event import Event

DISKS = []


def get_disks():
    with MySQL() as db:
        for disk_id, path in db.get(f'select Id, Path from Storage'):
            DISKS.append(Disk(disk_id, path))


def get_oldest_events(disk: Disk):
    events = []
    with MySQL() as db:
        sql = f'select Id, StartTime, monitor_id from Events where StorageId="{disk.id}" order by StartTime limit 10'
        for event_id, time, monitor_id in db.get(sql):
            events.append(Event(event_id, time, monitor_id, disk))
    return events


def clean_disk(disk: Disk):
    oldest = get_oldest_events(disk)
    for event in oldest:
        event.remove()


def main():
    get_disks()
    for disk in DISKS:
        while disk.free_space_gb < 10:
            clean_disk(disk)
    sleep(30)


if __name__ == '__main__':
    main()
