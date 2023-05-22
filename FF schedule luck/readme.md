# Overview
This project analyzes data from my fantasy football league's last season. The motivation behind this project was to look into the role that the randomness of the scheule played into our final standings. In the end, I wanted to know how teams performed based on weekly points alone, and how that corresponds to the probability of ending with a given record,playoff berth, etc.

# Data
The data was acquired from ESPN's API. From there, you can download many different statistics about your league, team, and players.

# Methods
My first step was to create a data frame with containing each teams record, and performance each week. From there, I was able to look at statitical quantities like average points scored. In the end, I computed season records based on a "randomized" schedule many times, to get a distribution of records for each team. The distribution is the final illustation of how many games a team "should have" won, and how "lucky" they were with respect to that distribution. Anyone that uses ESPN for fantasy football should be able to run this with their credentials to replicate this analysis with their own team. 
