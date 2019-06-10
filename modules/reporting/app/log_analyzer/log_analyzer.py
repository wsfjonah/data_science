import re


class LogAnalyzer:
    output = {}

    def process_line(self, line):
        # print(re.search(re.compile("[^ ]*"), line).group(0))  # before the first space, the ip address
        # print(re.search(re.compile("(?<=\[)[^\]]*(?=\])"), line).group(0))  # between the first [], the timestamp
        # print(re.search(re.compile("(?<=\")[^\"]*(?=\")"), line).group(0))  # between the first "", the api url
        try:
            ip_address = re.search(re.compile("[^ ]*"), line).group(0)
        except Exception:
            pass
        else:
            self.__record__(ip_address)

    def __record__(self, key):
        count = 0
        if key in self.output:
            count = self.output[key]
        count = count+1
        self.output[key] = count
