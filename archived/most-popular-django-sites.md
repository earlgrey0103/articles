# 为什么这些国外大网站都选择了Django？

The first question we ask ourselves when we approach a new project: is Django really the best option here? Even if a client is sure that the answer is confirmative. To be more certain about it, we decided to do a research on that. We wrote a script that would gather all the Django sites on the Internet (yes, we do not choose easy ways:) ) and analyse the list we receive. By this time the script is still processing and the final results will come later.

So we started with 5 popular sites on Django that everyone knows and we had a proof that they are currently working on Django Framework.

Instagram
instagram-logo

Yes, this source of selfies and food photos was developed in Django. 
Why? Instagram developers claim that choosing a technology, they were guided by three principles:

Keep it very simple.

Don’t re-invent the wheel.

Go with proven and solid technologies whenever you can.

It’s perfect for social networks:

Because Django allows working efficiently with a big amount of data, here it has many images, apparently.
It can help to manage a large number of users and provides easy interaction between them.
It works well with other technologies.
Read more what Instagram developers share about their technologies.

2. The Washington Post
washington

Few people know that initially Django was created to develop online editions. No wonder, the most popular newspapers have Django websites. Some of them benefit from certain advantages of Django, like The New York Times, which is mostly built on pure Python and basically uses lots of other technologies. Such newspapers as The Washington Post have their site with Django backend. This is how its developers explain their choice:

sites on Django handle high traffic loads;
providing efficient and fast performance;
ability to contribute to the framework so it meets one’s own specific needs (for instance, one of its first developers Adrian Holovaty (nice to come across Ukrainian surnames so often:) ) was an active contributor to Django).
It also has a lot of various apps on Django, like US Congress Votes Database or Faces of the Fallen, for instance.

3. Disqus
disqus-logo

Disqus also faced the problem of scalability, like Pinterest, but it continued with Django and found another way out of this problem. They’ve managed to achieve 8 billion page views in 2013. And even when they needed to handle 1.5 millions concurrently connected users, 45,000 new connections per second, they also did it with Django.

Again, they point out such benefits of Django:

availability of ready solutions. However, they also stress that one needs to develop within “Django" philosophy to have it function well;
again, a wide community;
and thus easiness to find good specialists.
They’ve also managed to benefit from Django, providing different smaller side services and after they extended on “How they do it when it isn’t Django”, which means how they used different technologies to make them get friends with Django. They moved back to Django, mainly because of its wide community and yes, due to the fact that they’ve already worked with it.

4. Zapier
zapier-logo

Now we’ll move from globally popular sites to rather popular ones in certain circles. For instance, Zapier gained its glory in the business world. This service helps to connect various similar services into one. For instance, one can save G-mail attachments to Dropbox or create a Trello ticket from his calendar.

An interesting fact is that you can also validate that Zapier is running on Django by just opening their admin login page. It shows a default Django interface for the admin panel.

From the development perspective, it’s a really fascinating one:

it connects different sources (via APIs) and enables quick collaboration between different sources of information; 141 APIs have been added to Zapier by January 2014;
what is more, it enables performing different actions by means of the service without switching from one app to another;
it enables work with a big amount of data for thousands of users.
The choice of Django was based on familiarity, according to the article by Bryan Helmig. They just chose the technology they were acquainted with. Thus, they basically chose Python/Django before working for Zapier. It should be mentioned, Bryan states that Ruby, e.g., would not be a worse choice. However, nobody has proved his point in practice:)

By the way, Zapier also turns to ReactJS and even prepared a small tutorial for those who also consider it a good choice. So do we.

5. Bitbucket
bitbucket

Bitbacket also doesn’t hide its roots, you can see Django admin panel on https://bitbucket.org/admin/

This article shows its developer had fallen in love with Django much earlier than the development of Bitbucket started.
However, this love continues till now. Which means it’s a true love and not the love of the kind “I was lazy to find something else, and you’re ok”. Why is that so?

Its developers claim that it wouldn’t be for the Django’s wide community which keeps it fit and up to date.
Moreover, one doesn’t need to pay for all the apps separately, such as URL mapping. 
They’re also grateful for Django’s having so many ready parts for them to use, rather than developing from scratch. That’s why they had such a short turn-around time.
Concerning the drawbacks of Django, they point out its problems with “Group by” (yes, we’ve been there too:) ) expressions and a lack of flexibility in ORM usage.

https://7webpages.com/blog/most-popular-django-sites/