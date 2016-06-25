from collections import deque


class Categories(object):
    def __init__(self, config_file):
        try:
            fdata = open(config_file)
        except:
            print "Wrong filename!"
            return

        categories = dict()
        data = dict()

        with fdata:
            for line in fdata:
                lline = line.rstrip('\n').strip().split(';')
                data[lline[0]] = int(lline[1])
                for c in lline[2:]:
                    if c in categories:
                        categories[c].append(lline[0])
                    else:
                        categories[c] = deque([lline[0]])

        self.count = data
        self.categories = categories

    def get_category(self, category):
        if category in self.categories:
            url = None
            while not url:
                try:
                    url = self.categories[category].popleft()
                except:
                    return
                if self.count[url] > 0:
                    self.count[url] -= 1
                    self.categories[category].append(url)
                    return url
                else:
                    url = None

    def get_categories(self, categories):
        for c in categories:
            url = self.get_category(c)
            if url:
                return url
