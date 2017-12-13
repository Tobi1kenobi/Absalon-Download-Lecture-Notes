import DownloadSlides as ds
import UserSpecific as us

LOGIN = ds.fetch_login_details(abs_username=us.ABSALON_USERNAME, abs_password=us.ABSALON_PASSWORD)
DRIVER = ds.launch_browser(us.DOWNLOAD_DIR())
DRIVER = ds.access_absalon(DRIVER, LOGIN)
DOWNLOADED_FILES = ds.access_abs_files_url(DRIVER)
DRIVER.close()
print(DOWNLOADED_FILES)
