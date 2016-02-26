# 20行代码自动获取Udemy网站免费课程

Udemy is a teaching and learning platform with loads of courses in various categories. Now very often different coupon codes are available for purchasing courses in minimal amount or with a 100% discount. Various websites serve these coupon codes. One of those websites which I rely on is GrowthCoupon.com

Now, I am not writing a review of 100% off coupon providers. Through this post I will explain my code which I am using to extract the 100% off coupon codes from growthcoupon.com and then get those courses automatically. I have automated my code so that I do not need to worry about new coupon codes available and can save my time. The below code enrolls you in 10 latest 100% off courses available at growthcoupon.com when run a single time. You may wish to automate the script every hour or so.

Get 100%off Udemy courses automatically using python

    from json import loads
    from bs4 import BeautifulSoup
    import mechanize
    api_key = "8def4868-509c-4f34-8667-f28684483810%3AS7obmNY1SsOfHLhP%2Fft6Z%2Fwc46x8B2W3BaHpa5aK2vJwy8VSTHvaPVuUpSLimHkn%2BLqSjT6NERzxqdvQ%2BpQfYA%3D%3D"
    growth_coupon_url = "https://api.import.io/store/data/a5ef05a9-784e-410c-9f84-51e1e8ff413c/_query?input/webpage/url=http%3A%2F%2Fgrowthcoupon.com%2Fcoupon-category%2F100-discount%2F&_user=8def4868-509c-4f34-8667-f28684483810&_apikey=" + api_key
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
    sign_in = br.open("https://www.udemy.com/join/login-popup/")
    br.select_form(nr=3)
    br["email"] = "email@domain.com"
    br["password"] = "password"
    logged_in = br.submit()

    growth_coupon = br.open(growth_coupon_url)
    json_obj = loads(growth_coupon.read())

    for course_link in json_obj["results"]:
        try:
            course_page = br.open(str(course_link["couponcode_link"]))
            soup = BeautifulSoup(course_page)
            for link in soup.find_all("a"):
                req_link = link.get('href')
                if 'https://www.udemy.com/payment/checkout' in str(req_link):
                    print req_link
                    br.open(str(req_link))
                    print "success"
                    break
        except (mechanize.HTTPError,mechanize.URLError) as e:
            print e.code

The above program is a pure python code that extracts 10 latest 100% off coupon codes from GrowthCoupon.com and then enrolls you in those courses automatically.

1. Line 1 to 3

The first three lines are the import statements. In our program, we are using three python libraries. Amongst them, mechanize is used to login to the udemy account. BeautifulSoup is used to get the data on the basis of tags. Here in our program we use BeautifulSoup to get the links in certain page. Json’s loads is used to load the json response.

2. Line 4 and 5

We are using import.io API in order to extract data from growthcoupon. I got to know about this very cool resource in my Programming Synthesis class at my college. Here’s How to get and use import.io API. We store the API in a variable api_key. Then concatenate to the growth_coupon_url which is the standard post request url to get data in json format from growthcoupon.

3. Line 6 to 13

From line 6 to 13 is the procedure to login to a website (udemy in our case). Line 6 initializes a browser. Line 7 says ignore the robots.txt file. Line 8 adds a user agent to the browser. Line 9 opens the login url in the browser we initiated earlier.

The next thing you will need is the form you want to work with. By this I mean this is the login form. All you need to do is go to the username box ->> right click on it->> go to the inspect elements option. Now scroll up until you find the first form tag. In most cases you will find the form name attribute but some of the websites do not have this. If there exists then the value given to the name attribute under the form tag is the thing you need to access the form. Another way to access forms is by their index. The first form is indexed 0. Now in case the form name is not available, you will need to find how many forms are present in the login url(basically most of the websites have only one form because all you want the login page to do is login if authenticated). In this case the form index is 3.

Now you need to know the variable name that is assigned to take the value you enter to the email/username and password section. To get these values inspect element when you are inside the fields email/username and password. Below is a snapshot to give you insights of the variables you want to take care of.

udemyloginform

4. Line 15 and 16

Here on line 15, we are opening the url that gives us the data from growthcoupon in json format. Line 16 loads the url as a json object.

5. Line 18

Our json object is stored in json_obj variable. But the data we need is stored inside an array which is the value for the key “results” Hence we are iterating through this array.

6. Line 20

Now we open the couponcode link which is the value of the key “couponcode_link”. This url is present in each index of the array. On each loop the particular index’s url’s response is stored in variable course_page.

7. Line 21

We then convert the page response to a soup element by invoking the BeautifulSoup method over course_page.

8. Line 22 to 27

Now we want to iterate through each links found in the soup element. The url for enrolling in the udemy course starts with the string “https://www.udemy.com/payment/checkout”. Hence we check if the string is a substring of the link at each iteration. If the condition satisfies, we open that link to enroll ourselves in that course. Well that’s the end of the code that works.