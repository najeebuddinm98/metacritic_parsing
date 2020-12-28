# metacritic_parsing

The main aim of this project is to provide a foundational comparison between [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/0) library and [Request-HTML](https://github.com/psf/requests-html) library for parsing websites. 

BS4 has been widely used as the de-facto library for parsing any website or html document. It is known to be very user-friendly and easy to use even for beginners. As an alternative, Requests-HTML was released by the same [people](https://travis-ci.com/github/psf) who made the `requests` library. The  main advantages that it boasts includes full support for JavaScript and Async support.

In this project, we parse the Metacritic webpages containing the ratings of all videogames in their records. There are total 181 pages as of writing this but I have only parsed 100 pages for convenience. The scripts can be easily expanded for all 181 pages. The webpages do not need JavaScript support, so the playing field is level. The data, consisting for the name, score, release date and the platform is stored in a `csv` file after all the parsing is done.

I have also made a small visualization in Jupyter of the data obtained.



### Improvements:

The obvious one is parsing all 181 pages. Also, [ScraPy](https://docs.scrapy.org/en/latest/) is another very commonly used library for such tasks. I does have added functionality for making parsing from multiple webpages easier