import tldextract
import re

def extract_domain_tldextract(url):
    domain = tldextract.extract(url)
    return domain.domain

def extract_domain_regex(url):
    domain = re.match(r'^(?:https?://)?(?:www\.)?([^./]+)', url)
    return domain.group(1)

print(extract_domain_tldextract("http://example.com"))
print(extract_domain_regex("http://example.com"))
