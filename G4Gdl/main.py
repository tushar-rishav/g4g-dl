from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from setproctitle import setproctitle
import os
import urllib2
import subprocess
import argparse
import sys
import re

__author__ = 'tushar-rishav'
__version__ = "0.0.1"


class Geeks4Geeks:

    def __init__(self):
        self.base_url = "http://www.geeksforgeeks.org/"
        self.target_dir = "g4gPdf"
        self.flag = False
        self.ds = False
        self.algo = True
        self.limit = 0
        setproctitle('topcoderdl')

    def fetch(self):
        try:
            if not os.path.exists(self.target_dir):
                os.mkdir(self.target_dir)
        except Exception as e:
            print(e)
        try:
            self.page = urllib2.urlopen(self.base_url)
        except Exception as e:
            print(e)
            sys.exit(1)
        self.data = BeautifulSoup(self.page.read(), "lxml")
        if not self.flag:
            content = self.data.find(id="content")
            if self.ds:
                all_a = content.find_all("a")[12:]      # reject list of data structures (first 12 links)
                heading_a = content.findAll("a", href="")   # reject useless headings
                quiz_a = content.findAll("a", href=re.compile("http://geeksquiz.com/*"))    # remove quizes
                all_set = set(all_a)
                heading_set = set(heading_a)
                quiz_set = set(quiz_a)
                post = list(set(all_set).difference(heading_set).difference(quiz_set))
            elif self.algo:
                all_a = content.find_all("a")[15:]      # reject list of algos (first 15 links)
                heading_a = content.findAll("a", href="")   # reject useless headings
                quiz_a = content.findAll("a", href=re.compile("http://geeksquiz.com/*"))    # remove quizes
                all_set = set(all_a)
                heading_set = set(heading_a)
                quiz_set = set(quiz_a)
                post = list(set(all_set).difference(heading_set).difference(quiz_set))
        else:
            post = [self.base_url]

        with ThreadPoolExecutor(max_workers=4) as executor:
            if self.limit:
                future_to_url = {
                    executor.submit(self.download, url): url for url in post[:self.limit]}
            else:
                future_to_url = {
                    executor.submit(self.download, url): url for url in post}
            for future in as_completed(future_to_url):
                url = future_to_url[future]

    def download(self, url):

        if not self.flag:
            post_name = os.path.join(self.target_dir, url.get_text()[:20])  # Limit the name size
            post_url = url['href']
        else:
            post_name = os.path.join(
                self.target_dir, self.data.title.getText())
            post_url = url
        print("Downloading " + post_name + "....")
        args = ['wkhtmltopdf', post_url, post_name+".pdf"]
        subprocess.Popen(args)


class Smarty(Geeks4Geeks):

    def __init__(self, _):
        pass

    def __call__(self, func):
        def read(obj):
            args = func()
            if args.target:
                obj.target_dir = args.target
            if args.limit:
                obj.limit = args.limit
            if args.post:
                obj.base_url = args.post
                obj.flag = True
            elif args.ds:
                obj.base_url += "data-structures/"
                obj.ds = True
            elif args.algo:
                obj.base_url += "fundamentals-of-algorithms/"
                obj.algo = True
            else:
                print("Mention -d or -a for data structure and algo respectively and then try again! See -h for more")
                sys.exit(1)

        return read


@Smarty(None)
def parse():
    parser = argparse.ArgumentParser(description=" \
             Downloads Geeks for Geeks DS and Algorithm tutorials and save as PDF", epilog="\
             Author:https://github.com/tushar-rishav")
    group = parser.add_argument_group('group')
    parser.add_argument("-t", "--target", help="absolute path of target directory to save all PDFs. Default is g4gPdf in current dir",
                        type=str)
    parser.add_argument("-p", "--post", help="link for single post",
                        type=str)
    parser.add_argument("-l", "--limit", help="limit the number of downloads. Count begins from top",
                        type=int)
    group.add_argument("-d", "--ds", help="Fetch all Data Structures",
                        action="store_true")
    group.add_argument("-a", "--algo", help="Fetch all Algorithms",
                        action="store_true")
    args = parser.parse_args()
    return args


def main():
    location_f = subprocess.Popen("whereis \
        wkhtmltopdf", shell=True, stdout=subprocess.PIPE).stdout.read()
    assert "wkhtmltopdf" in location_f, "wkhtmltopdf is not installed. Download from www.wkhtmltopdf.org/downloads.html and try again "

    obj = Geeks4Geeks()
    parse(obj)
    obj.fetch()

if __name__ == "__main__":
    main()