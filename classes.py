from urllib.parse import unquote_plus

import requests
from bs4 import BeautifulSoup

class App:
    '''Creates a software/app/program id, scrapes its website and downloads
    the setup file or archive. Looks for the latest build on 64-bit Windows.'''

    def __init__(self, name, download_page, pattern,
                 page_response=None, content_type=None, links=None,
                 base_url=None,file_name=None, download_url=None):
        self.name = name                    # Name of program
        self.download_page = download_page  # Page with direct link to program
        self.pattern = pattern              # To find correct file to d/l
        self.page_response = page_response  # Response to request (200 = OK)
        self.content_type = content_type    # HTML, JSON or FILE
        self.links = links                  # All links on the page
        self.base_url = base_url            # For absolute url reconstruction
        self.download_url = download_url    # Absolute/direct download url
        self.file_name = file_name          # Name of downloaded file
        
        self.session = requests.Session()   # For multiple requests on one page

        # GitHub needs to be treated as a special case
        # because mismatch between absolute and relative urls 
        if 'github.com' in self.download_page:
            self.base_url = 'https://www.github.com'

    def request_page(self) -> requests.models.Response:
        '''Request download page and check for errors'''
        # try-except syntax source: https://stackoverflow.com/a/47007419
        # Keep headers parameter to avoid ConnectionErrors.
        headers = {'User-Agent': 'Mozilla/5.0 \
                                 (Windows NT 10.0; Win64; x64; rv:90.0) \
                                 Gecko/20100101 Firefox/90.0'}
        try:
            self.page_response = self.session.get(url=self.download_page,
                                                  timeout=10, headers=headers)
            self.page_response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error for {self.download_page}:", errh)
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting for {self.download_page}:", errc)
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error for {self.download_page}:", errt)
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong with  for {self.download_page}:", err)
        return self.page_response

    def get_content_type(self) -> str:
        '''Gets content type of page (i.e. file, html or json)'''
        content_type = self.page_response.headers['Content-Type']
        try:
            if content_type == 'binary/octet-stream' or \
               content_type == 'application/octet-stream' or \
               content_type == 'application/x-msdownload' or \
               content_type == 'application/x-msdos-program':
                self.content_type = 'FILE'
            elif content_type.startswith('text/html'):
                self.content_type = 'HTML'        
            elif content_type.startswith('application/json'):
                self.content_type = 'JSON'
        except Exception as e:
            raise e("Unable to set content_type attribute! Url content type \
                is {self.page_response.headers['Content-Type']}.")
        return self.content_type

    def get_html_links(self) -> list:
        '''Gets all urls from an html page'''
        html = self.page_response.text
        soup = BeautifulSoup(html, 'lxml')
        anchors = soup.select('a')
        # Exclude potential NoneTypes (would keep code from running)
        self.links = [link.get('href') for link in anchors
                      if isinstance(link.get('href'), str)]
        return self.links

    def get_json_links(self) -> list:
        '''Gets all urls from a json page'''
        json = self.page_response.json()
        json_list = json['products']
        self.links = [link['url'] for link in json_list]
        return self.links

    def get_download_url(self) -> str:
        '''Finds download url for latest version'''
        # 'FILE' = download page contains redirection to download url
        if self.content_type == 'FILE':
            self.download_url = self.page_response.url
            return self.download_url
        
        # List all download candidates
        try:
            versions = [version for version in self.links
                        if self.pattern.search(version) != None]
        except IndexError as ie:
            raise ie("No url matches instance's 'pattern' attribute! \
                Check pattern and scraped page's list of hrefs.")        
        
        # Pick first candidate
        latest = versions[0] # Latest version likely to be at the top
        
        if self.name == 'foobar2000':
            # "/getfile/" deleted, replaced by "/files/" from base_url
            latest = latest.split('/')[-1]
        # Simplest way to distinguish between relative and absolute urls;
        # avoids incorrect url reconstruction in most cases
        if self.base_url == None:
            self.download_url = latest
        elif self.base_url != None:
            self.download_url = self.base_url + latest
        return self.download_url

    def get_file_name(self) -> str:
        '''Creates file name from download url'''
        self.file_name = self.download_url.split('/')[-1]
        
        # Restore intended characters (e.g. spaces, parentheses...)
        if '%' in self.file_name or '+' in self.file_name:
            self.file_name = unquote_plus(self.file_name)
        return self.file_name

    def download_installer(self) -> int:
        '''Downloads the installer/archive'''
        file_bytes = self.session.get(self.download_url).content
        # Write in binary ('wb'); only for Windows
        with open(self.file_name, 'wb') as output_file:
            output_file.write(file_bytes)

    def __str__(self):
        instance_info = f"""
        Name:                   {self.name}
        Download page:          {self.download_page}
        Pattern:                {self.pattern}
        Page response:          {self.page_response}
        Content type:           {self.content_type}
        File name:              {self.file_name}
        Base url (optional):    {self.base_url}
        Download url:           {self.download_url}
        """
        return instance_info