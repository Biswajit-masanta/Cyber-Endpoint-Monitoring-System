import time

from modules.sys_info import get_system_info
from modules.resource_info import get_resource_info
from modules.sender import send_report

while True:

    data = {}

    data.update(get_system_info())
    data.update(get_resource_info())

    response = send_report(data)

    time.sleep(10)