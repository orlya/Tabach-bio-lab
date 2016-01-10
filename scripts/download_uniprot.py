__author__ = 'orly'

import os
#from urllib2 import urlopen, URLError, HTTPError
import requests


def dlfile(url, org, outdir):
    # Open the url
    try:
        #f = urlopen(url)
        f = requests.get(url)
        print "downloading " + url

        # Open our local file for writing
        #with open(os.path.basename(url), "wb") as local_file:
        with open(outdir + org + ".fasta", "wb") as local_file:
            local_file.write(f.content)
            local_file.close()


    #handle errors
    except requests.HTTPError, e:
        print "HTTP Error:", e.code, url
    #except requests.URLError, e:
    #    print "URL Error:", e.reason, url


def main():
    orgs_list = open("orgs_list.csv")
    outdir = "/vol/ek/orlya/orgs_db/"

    http_get_str = "http://www.uniprot.org/uniprot/?query=organism:{0}&format=fasta&include=yes"

    # Iterate over organisms list
    for org in orgs_list:
        org = org.rstrip('\n')
        url = http_get_str.format(org)
        dlfile(url, org, outdir)

if __name__ == '__main__':
    main()

