# Lookup subdomain_finder_research.txt file in asset folder

import requests


class SubDomain:
    def __init__(self, domain):
        self.domain = domain
        self.domain_finder()

    def domain_finder(self):
        domain_finder_text_file = open('subdomain_finder_research.txt', 'r')
        reading_file_content = domain_finder_text_file.read()
        subdomains = reading_file_content.splitlines()

        for subdomain in subdomains:
            url_shaper = f'http://{subdomain}.{self.domain}'

            try:
                requests.get(url_shaper)
            except requests.ConnectionError:
                pass
            else:
                return 'Discovered Subdomain: ', url_shaper

    def __repr__(self):
        return str(self.domain_finder())


if __name__ == '__main__':
    # Do not attempt on any web address unless you're authorised
    print(SubDomain(domain='web address here'))
