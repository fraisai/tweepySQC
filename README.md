# tweepySQC
This is a "Twitter-scraper" I made that calls on the Twitter API and tweepy to scrape Tweets based on the hashtag you would like to search for. This program will export all the Tweets that contain your desired hashtag or text every couple of minutes for a specificed number of times and then export them into a .csv file that you will then be able to filter and sort through.

These are the following information that my code collects and includes in the .csv output file:
1. screen_name: EXAMPLE: "screen_name": "TwitterAPI"
2. followers_count : The number of followers the account has.
3. retweet_count: Number of times this Tweet has been retweeted. 
4. favorite_count: Indicates approximately how many times this Tweet has been liked by Twitter users.
5. text: actual UTF-8 text of the status update aka the actual Tweet containing the hashtag or word you wanted to search for. EXAMPLE: "text":"To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm"
6. created_at: UTC time at which tweet was created. EXAMPLE: "created_at": "Wed Oct 10 20:19:24 +0000 2018"
7. hashtags:
8. verified : Indicates whether the user is verified or not. EXAMPLE: "verified": true
9. url: URL of the Tweet. 
10. description: Description of the Twitter account that the Tweet was posted on. EXAMPLE: "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
