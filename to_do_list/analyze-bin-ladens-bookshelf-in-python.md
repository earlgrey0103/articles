http://automatingosint.com/blog/2015/05/osint-python-analyze-bin-ladins-bookshelf/

On May 20, 2015 the ODNI released a trove of documents called “Bin Ladin’s Bookshelf“. This included all kinds of materials including letters he had written, books he was reading and other various bits of information. This document released piqued my interest primarily because I was interested to see what the most common thing was that Bin Ladin wrote about. I am fully aware that these documents are only a fraction of the material he had, but it seemed like a good exercise to stretch my Python legs and to learn a new API. This blog post will teach you how to analyze PDF’s (pretty useful all around really), and how to use the Alchemy API which is an extremely powerful data processing API that can do entity extraction, sentiment analysis, keyword extraction and a whole bunch of other stuff. All of this should be some solid additions to your OSINT toolkit. Let’s get started!

Installing Prerequisites
The first thing you are likely going to need is pyPDF. If you have read any of my previous posts you will use pip to install it:


pip install pypdf

Alright, done! Now let’s grab the Alchemy API prerequisites. The first step is to sign up for an API key. This will take 2 minutes and while you wait for it to arrive in your inbox let’s get the code downloaded. You can use their Git instructions or you can download from Github directly. All you have to do is unzip the folder and by now you should have your API key in your inbox, so drop into a terminal or command prompt and run:


