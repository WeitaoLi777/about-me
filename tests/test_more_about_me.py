"""
Tests for the basic content of a more_about_me.html file of a web site with a particular set of content.

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
  def settings(self):
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class")
  def driver(self):
    """
    Pop open a web browser and make it available to the tests.
    """
    settings = json.load(open('./settings.json', 'r'))
    # print(settings["site_url"])

    # set up the fixture
    driver = webdriver.Chrome()
    driver.get(settings["site_url"] + "/more_about_me.html") # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_h1_exists(self, driver, settings):
    """
    Check that the heading exists
    """
    target_element = "h1" # check the ol tag
    elem = driver.find_element_by_tag_name(target_element) # find the h1 tag
    assert elem

  def test_one_section(self, driver, settings):
    """
    Check that the required section exists
    """
    # check number of sections
    elems = driver.find_elements_by_tag_name("section")
    assert len(elems) >= 1

  def test_paragraph_in_section(self, driver, settings):
    """
    Check that the required section has a paragraph in it
    """
    # check number of sections
    elems = driver.find_elements_by_css_selector("section p")
    assert len(elems) >= 1

  def test_two_images(self, driver, settings):
    """
    Check that there are at least two images
    """
    # check number of headings
    elems = driver.find_elements_by_tag_name("img")
    assert len(elems) >= 2

  def test_link_href_exists(self, driver):
    """
    Check url of links to all required linked pages.
    """
    target_urls = ['index.html', 'about_me.html']
    for url in target_urls:
      elem = driver.find_element_by_xpath('//a[@href="' + url + '"]')
      assert elem # check that it exists

