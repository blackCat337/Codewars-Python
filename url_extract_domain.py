import tldextract

def extract_domain(url):
    domain = tldextract.extract(url)
    return domain.domain

print(extract_domain("http://example.com"))
