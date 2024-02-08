# read version from installed package
from importlib.metadata import version
__version__ = version("site_level")
from site_level import SiteLevelApp


app = SiteLevelApp()
app.run()
