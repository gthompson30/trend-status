# trend-status
This was my final project for IntroCS in the 2020-21 school year. I worked on this project with:
- [Anthony Chen](https://github.com/AnthonyChen0818)
- [Maggie Huang](https://github.com/Mags-012705)

For submission to ...
- [Topher Mykolyk](https://github.com/tofr)

This project is accessible at:
- http://moe.stuy.edu/~gthompson30/fp/

**NOTE**: This project runs on Python CGI, as opposed to a Flask server or any other type of server, so if you plan on downloading and running this yourself, you do not need to run and server and can just load the file `index.html` in your browser to access the website.

Also, if you're running this locally on your computer, you will likely not need the folder `pytrends` if you just run `pip3 install pytrends`. The folder is only there because -- on the Apache web server the website is run on -- the module is unable to import for clients loading the website, so we had to put the module in the same folder as the website to avoid import errors.
