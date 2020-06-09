"""
Tests for the basic content of an index.html file of a web site with a particular set of content.

Selenium webdriver for Chrome (a.k.a. the file named chromedriver) must be installed in either:
- in the same directory as chrome.exe on Windows (e.g. C:\Program Files\Google\Chrome\Application)
- in a directory that is included in the PATH on Mac OS X (e.g. /usr/local/bin)
"""

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
    print(settings["site_url"])

    # set up the fixture
    driver = webdriver.Chrome()
    driver.get(settings["site_url"]) # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_title(self, web_driver, site_settings):
    """
    Check the title tag for the correct text
    """
    assert site_settings["name"] in web_driver.title

  def test_h1(self, web_driver, site_settings):
    """
    Check the h1 tag for the correct text
    """
    elem = web_driver.find_element_by_tag_name("h1")
    assert site_settings["name"] in elem.text

  def test_ol_exists(self, web_driver, site_settings):
    """
    Check that the order list items exists
    """
    elems = web_driver.find_elements_by_css_selector("ol li") # find the h1 tag
    assert len(elems) >= 2

  def test_link_href_exists(self, web_driver):
    """
    Check url of links to all assignment pages.
    """
    target_urls = ['index.html', 'about_me.html', 'topic_of_interest.html', 'user_experience_design.html', 'professional_site.html', 'animated_gif.html', 'video.html']
    for url in target_urls:
      # check for hrefs with either single or double quotes
      elem_option1 = web_driver.find_element_by_xpath('//a[@href="' + url + '"]')
      elem_option2 = web_driver.find_element_by_xpath("//a[@href='" + url + "']")
      assert elem_option1 or elem_option2 # check that it exists

  def test_link_text_exists(self, web_driver):
    """
    Check text of links to all assignment pages.
    """
    target_terms = ['UNIX', 'HTML', 'CSS', 'JQuery', 'User Experience', 'Responsive Design', 'Bootstrap', 'Animated GIF', 'Digital Video']
    for term in target_terms:
      elem = web_driver.find_element_by_partial_link_text(term)
      assert elem # check that a matching element exists

