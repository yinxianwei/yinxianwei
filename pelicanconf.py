AUTHOR = "yinxianwei"
SITENAME = "一枝红杏出墙来"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Shanghai"

DEFAULT_LANG = "zh-CN"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Pelican", "https://getpelican.com/"),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["media", "extra"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
ANALYTICS = """
    <script>
        var link = document.createElement('a')
        link.style.marginRight = "10px"
        link.href = "https://beian.miit.gov.cn"
        link.target = "_blank"
        link.textContent = "豫ICP备16018939号-2"
        document.querySelector('#contentinfo > p').prepend(link)
    </script>
"""
GITHUB_URL = "https://github.com/yinxianwei"
DEFAULT_CATEGORY = "随笔"
THEME_TEMPLATES_OVERRIDES = ["templates"]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
