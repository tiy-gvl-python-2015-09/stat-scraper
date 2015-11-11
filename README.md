# Sport Scraper

## Description

Create a django app that does real time scraping of nfl.com to give back player data.

## Objectives

### Learning Objectives

After completing this assignment, you should be able to:

* Proxy requests from your site to an external resource
* Scrape HTML data with Beautiful Soup and parse out important elements
* Explore methods to optimize the performance of your site

## Details

### Deliverables

* A Git repo called sport-scraper containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project

### Requirements

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

NFL.com has a database of current and historical data available for players in their system.  Your task is to
reverse engineer their search functionality so that you can use your own site to search for a particular player's
data. Clean up the individual stats or bring back the entire HTML structure and display it on your page.

## Hard Mode

Create a player model and store their stats in the database so subsequent searches do not hit the NFL.com website.
