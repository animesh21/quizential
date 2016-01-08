import feedparser


URLs = {
    "sciencedaily": {
        "all": "http://www.sciencedaily.com/newsfeed.xml",
        "top": "http://www.sciencedaily.com/rss/top.xml",
        "top_science": "http://www.sciencedaily.com/rss/top/science.xml",
        "top_health": "http://www.sciencedaily.com/rss/top/health.xml",
        "top_technology": "http://www.sciencedaily.com/rss/top/technology.xml",
        "top_environment": ("http://www.sciencedaily.com/"
                            "rss/top/environment.xml"),
        "top_society": "http://www.sciencedaily.com/rss/top/society.xml",
        "strange": "http://www.sciencedaily.com/rss/strange_offbeat.xml",
        "most_popular": "http://www.sciencedaily.com/rss/most_popular.xml",
    },

    "phys.org": {
        "rss": "http://phys.org/rss-feed/",
        "featured_stories": "http://phys.org/rss-feed/editorials/",
        "physics": "http://phys.org/rss-feed/physics-news/",
        "mathematics": "http://phys.org/rss-feed/science-news/mathematics/",
    },

    "nature.com": {
        "nature_issue": "http://feeds.nature.com/nature/rss/current",
        "scientificamerican": ("http://feeds.nature.com/scientificam"
                               "erican/rss/current"),
        "biotechnology": "http://feeds.nature.com/nbt/rss/current",
        "nanotechnology": "http://feeds.nature.com/nnano/rss/current",
    },

    "technology.org": {
        "all": "http://feeds.feedburner.com/TechnologyOrg",
        "information_processing": ("http://feeds.feedburner.com/Techno"
                                   "logyOrgInformationProcessingNews"),
        "life_sciences": ("http://feeds.feedburner.com/TechnologyOrg"
                         "LifeSciencesTechnologiesNews"),
        "space_and_astronomy": ("http://feeds.feedburner.com/"
                                "TechnologyOrgSpaceAstronomyNews")
    },

    "sciencenews.org": {
        "all": "https://www.sciencenews.org/feeds/headlines.rss",
    },

    "new.discovery.com": {
        "all": "http://feeds.feedburner.com/DiscoveryNews-Top-Stories",
    },

    "physicsworld.com": {
        "all": "http://feeds.feedburner.com/PhysicsWorld",
        "news": "http://feeds.feedburner.com/PhysicsWorldNews",
        "blog": "http://blog.physicsworld.com/feed/",
        "in_depth": "http://feeds.feedburner.com/PhysicsWorldInDepth",
    },

    "news.sciencemag.org": {
        "all": "http://news.sciencemag.org/rss/weekly_news_email.xml"
    }
}


for name, url_dict in URLs.items():
    print("RSS feeds from %s:" % name)
    for category, url in url_dict.items():
        feeds = feedparser.parse(url)
        # print("Category: %s, feeds: %d" % (category, len(feeds.entries)))
        print(feeds.entries[0])
        print("Timestamp: ", feeds.entries[0]['published_parsed'])
        
RSS_URLs = {"biology": ["http://z.about.com/6/o/m/biology_p2.xml",
                        "http://phys.org/rss-feed/biology-news/",
                        ("http://feeds.feedburner.com/TechnologyO"
                         "rgLifeSciencesTechnologiesNews"),
                        ("http://feeds.sciencedaily.com/sci"
                         "encedaily/plants_animals/biology"),]
           }

