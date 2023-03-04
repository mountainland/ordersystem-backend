try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


try:
    import cPickle as pickle
except ImportError:
    import pickle


# Handle the case where the requests module has been patched to not have
# urllib3 bundled as part of its source.
try:
    from libs.pip._vendor.requests import HTTPResponse
except ImportError:
    from libs.pip import HTTPResponse

try:
    from libs.pip._vendor.requests import is_fp_closed
except ImportError:
    from libs.pip import is_fp_closed

# Replicate some six behaviour
try:
    text_type = unicode
except NameError:
    text_type = str
