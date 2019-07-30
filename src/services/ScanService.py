from common.settings import settings

IP_PORT_LIST_FILE = settings.IP_PORT_LIST_FILE


class ScanService(object):

    def run(self):
        for ip, port in self.get_ip_port_lists():
            self.simple_scan(ip, port)

    def get_ip_port_lists(self):
        with open(IP_PORT_LIST_FILE) as fd:
            l = []
            for lines in fd.readlines():
                l.append(lines.strip())
            return l

    def simple_scan(self, ip, port):
        # call masscan
        print(ip, port)
