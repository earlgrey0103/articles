# Python乐园之一：解析iTunes播放列表（1）

Our Python expedition begins with a simple project that  nds duplicate music
tracks in iTunes playlist  les and plots vari- ous statistics such as track lengths and ratings.
You’ll start by taking a look at the iTunes playlist for- mat and then learn how to extract information from these  les using Python. To plot this data, you’ll use the matplotlib library.
In this project, you will learn the about the following topics:
• XML and property list (p-list) files
• Python lists and dictionaries
• Using Python set objects
• Using numpy arrays
• Histograms and scatter plots
Making simple plots with the matplotlib library
• Creating and saving data  files

anatomy of the itunes Playlist file

The information in an iTunes library can be exported into playlist  les. (Choose File4Library4Export Playlist in iTunes.) The playlist  les are written in Extensible Markup Language (XML), a text-based language designed to represent text-based information hierarchically. It consists of a tree-like collection of user-de ned tags in the form <myTag>, each of which can have attribute and child tags with additional information.
When you open a playlist  le in a text editor, you’ll see something like this abbreviated version:

<?xml version="1.0" encoding="UTF-8"?> u
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www
.apple.com/DTDs/PropertyList-1.0.dtd"> v
<plist version="1.0">
    <dict>
        x
        <key>Major Version</key>
        <integer>1</integer>
        <key>Minor Version</key>
        <integer>1</integer>
        --snip--
        <key>Tracks</key>
        <dict>
            <key>2438</key>
            <dict>
                <key>Track ID</key>
                <integer>2438</integer>
                <key>Name</key>
                <string>Yesterday</string>
                <key>Artist</key>
                <string>The Beatles</string>
                <key>Composer</key>
                <string>Lennon [John], McCartney [Paul]</string>
                <key>Album</key>
                <string>Help!</string>
            </dict>
            --snip--
        </dict>
        <key>Playlists</key>
        <array>
            <dict>
                <key>Name</key>
                <string>Now</string>
                <key>Playlist ID</key>
                <integer>21348</integer> --snip--
                <array>
                    <dict>
                        <key>Track ID</key>
                        <integer>6382</integer>
                    </dict>
                    --snip--
                </array>
            </dict>
        </array>
    </dict>
</plist>

The <dict> and <key> tags relate to the way a property list (p-list)
 le represents objects as dictionaries, which are data structures that link
a key with a value to make it easy to  nd a corresponding value. P-list  les use dictionaries of dictionaries, where values associated with a key in one dictionary are often themselves yet another dictionary (or even a list of dictionaries).

The <xml> tag identi es the  le as XML. Following this opening tag,
a document type declaration (DTD) de nes the structure of the XML docu- mentu. As you can see, Apple de nes this structure at a uniform resource locator (URL) visible in the tag.

Atv, the  le declares the top-level <plist> tag whose only child element is the dictionary <dict>w. This dictionary contains various keys including, atx, Major Version, Minor Version, and so on, but you’re interested in the Tracks key aty. Notice that the value corresponding to this key is also a dictionary, which maps an integer track ID to another dictionary containing elements such as Name, Artist, and so on. Each track in a music collection has a unique track ID key.

The playlist order is de ned atzby Playlists, a child of the top-level dictionary.

requirements

In this project, we’ll use the built-in module plistlib to read the playlist  les. We’ll also use the matplotlib library for plotting and numpy arrays to store data.

the code
The goals in this project are to  nd duplicates in your music collection, identify tracks shared between playlists, plot the distribution of track dura- tions, and graph the relationship between song ratings and length.
As your music collection grows, you’ll invariably end up with dupli- cate songs. To identify duplicates, search the names in the dictionary associ- ated with the Tracks key (discussed earlier) for duplicates and use track length as an additional criterion to detect duplicates, since a track with the same name but a different length is likely unique.

To  nd tracks shared between two or more playlists, you’ll export the collections as playlist  les, gather the track names for each playlist, and compare them as sets to discover common tracks by  nding the intersection between sets.

While gathering data from your music collection, you’ll create a couple of plots with the powerful matplotlib (http://matplotlib.org/) plotting pack- age developed by the late John Hunter. You’ll draw a histogram to show the distribution of track durations and a scatter plot to compare song rat- ings with song length.

To see the full project code, skip ahead to “The Complete Code” on page 11.

Finding Duplicates
You’ll start by  nding duplicate tracks with the findDuplicates() method, as shown here:

def findDuplicates(fileName):
    """
    Find duplicate tracks in given playlist.
    """
    print('Finding duplicate tracks in %s...' % fileName)
    # read in playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks
    tracks = plist['Tracks']
    # create a track name dict
    trackNames = {}
    # iterate through tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # is there an entry already?
            if name in trackNames:
                # if name and duration matches, increment count
                # duration rounded to nearest second
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
            else:
                # add entry - duration and count
                trackNames[name] = (duration, 1)
        except:
            # ignore
            pass

Atu, the readPlist() method takes a p-list  le as input and returns the top-level dictionary. You access the Tracks dictionary atv, and atw, you create an empty dictionary to keep track of duplicates. Atx, you begin iterating through the Tracks dictionary using the items() method, which is commonly used in Python to retrieve both the key and the value of a dic- tionary as you iterate through it.
Aty, you retrieve the name and duration of each track in the diction- ary. You check to see whether the current track name already exists in the dictionary being built by using the in keywordz. If so, the program checks whether the track lengths of the existing and newly found tracks are identi- cal{by dividing the track length of each by 1,000 with the // operator to convert milliseconds to seconds and then rounding to the nearest second. (Of course, this means that two tracks that differ in length only by milli- seconds are considered to be the same length.) If you determine that the two track lengths are equal, you get the value associated with name, which
is the tuple (duration, count), and increment count at|. If this is the  rst time the program has come across the track name, it creates a new entry for it, with a count of 1}.


