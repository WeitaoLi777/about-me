import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Tests:

  @pytest.fixture(scope="class")
  def site_settings(self):
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class")
  def web_driver(self):
    """
    Pop open a web browser and make it available to the tests.
    """
    settings = json.load(open('./settings.json', 'r'))
    # print(settings["site_url"])

    # set up the fixture
    driver = webdriver.Chrome('/Users/amos/selenium/chromedriver')
    driver.get(settings["site_url"] + "/about_me.html") # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_two_sections(self, web_driver, site_settings):
    """
    Check that the 2 required sections exist
    """
    # check number of sections
    elems = web_driver.find_elements_by_tag_name("section")
    assert len(elems) >= 2

  def test_two_headings(self, web_driver, site_settings):
    """
    Check that there are headings for the two sections
    """
    # check number of headings
    elems = web_driver.find_elements_by_css_selector("section h2")
    assert len(elems) >= 2

    # check heading text
    found_background = False
    found_interests = False
    for elem in elems:
      heading = elem.text.strip().lower()
      if heading == "my background":
        found_background = True
      elif heading == "my interests":
        found_interests = True
      assert found_background and found_interests

  def test_two_images(self, web_driver, site_settings):
    """
    Check that there are at least two images
    """
    # check number of headings
    elems = web_driver.find_elements_by_tag_name("img")
    assert len(elems) >= 2

  def test_link_href_exists(self, web_driver):
    """
    Check url of links to all required linked pages.
    """
    target_urls = ['index.html', 'more_about_me.html']
    for url in target_urls:
      elem = web_driver.find_element_by_xpath('//a[@href="' + url + '"]')
      assert elem # check that it exists

