import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='Mozilla/5.0',
)
# Uncomment for a more verbose output:
# browser.set_verbose(2)
URL = "https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page"
browser.open(URL)
form = browser.select_form()
browser["wpName"] = ""
browser["wpPassword"] = ""
resp = browser.submit_selected()


page = browser.get_current_page()
