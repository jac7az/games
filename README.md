# DS4320 Project 2: Gamers
* Name: Carissa Chen; jac7az
* DOI: 10.5281/zenodo.19874511
* [Press Release](https://github.com/jac7az/games/blob/main/PressRelease.md)
* [Pipeline](https://github.com/jac7az/games/tree/main/code)
* [License](https://github.com/jac7az/games/blob/main/LICENSE)
### Executive Summary
This repository includes a MongoDB nonrelational database containing records for over 4000 video games and analysis designed to evaluate critic score strength by game performance across 10 years, from 2010-2020, including games from a variety of publishers, developers, genres, and consoles. The data was entered as JSON files, with one file per game. This repo also includes metadata explanation and domain exposition, with the structure of the tables, statistical uncertainty for each asset class, and links to resources, press release, and code process.
## Problem Definition
### Problem Statement
The general topic is determining if high production quality directly correlates to higher commercial sales in video games. The specific problem statement is whether a high critic score has a strong influence and serves as a useful predictor for total sales across different console generations.

Video games are a newer, booming industry where new titles require high production costs to implement. Understanding return on investment is critical for anyone who wants to get into this industry. This investigation seeks to analyze whether it would be more accurate to find the highest revenue games based more on score, or if the market is so saturated by similar genre games that it's no longer a factor to focus on.

The initial problem isn't clear on what's considered high quality v. low quality. To narrow this down, quality uses the critic score as the proxy. By shifting the focus to feature importance, the analysis can provide a closer look at how much influence different characteristics hold to predict overall sales and provide a comparison between the actual quality versus other factors like console or who it's made by.

[Headline: Beyond A Score - What Actually Drives Video Game Success?](https://github.com/jac7az/games/blob/main/PressRelease.md)
## Domain Exposition
### Terminology
|Term|Description|
|-----|---------------------------------|
|AAA|High-budget games produced by major publishers|
|Action-Adventure|Game genre combining action game elements like combat with adventure games like exploration and puzzle-solving (eg. Legend of Zelda)|
|Attach Rate|Ratio of games sold to number of consoles in the market|
|FPS|First-person shooter genre game, focusing on weapon-based combat with first-person perspective (eg. Call of Duty)|
|Gacha|Game genre involving spending in-game currency that can also be bought with real money to receive in-game rewards and items, similar to loot boxes (eg. Genshin Impact, Honkai Star Rail)|
|Global Sales|Total units sold across regions like North America, Europe, Japan, etc|
|Live Service|Game design involving a continuous stream of new content over the years to keep players engaged (eg. Fortnite)|
|Metacritic|Weighted average core from different critics|
|Microtransactions|Financial transactions used in purchasing virtual goods|
|MOBA|Multiplayer Online Battle Arena, a game genere focusing on strategy and teamwork competition to destroy enemy structures and towers (eg. League of Legends)|
|Platformer|Game genre where gameplay mainly involves obstacle courses (eg. Super Mario)|
|RPG|Role-Playing Game genre where players control a character in a fictional setting, playing through a story with different characters (eg. Final Fantasy)|
|Sandbox|Genre of games providing a creativity outlet and freedom (eg. Minecraft)|
|Simulation|Game genre simulating real-world activities like flight, city-building, or everyday life (eg. The Sims)|

This project is in the entertainment domain, specifically the video game sector. This area is a unique combination between not only artistic creativity, but also software engineering. Shelf-life and hype goes by incredibly fast, sometimes within a few days, so understanding relationships between customer, vendor and developers is essential to maximize sales and awareness.

[Link to Reading Materials](https://myuva-my.sharepoint.com/:f:/g/personal/jac7az_virginia_edu/IgAUnqDSTWaLRqhAAe5OPsOGAWsVyeiZaIIixJ5oj8ix2t0?e=ClnEaF)

|Title|Publishing Site|Link|Description|
|-----|---------------|------------------------|-------------------|
|6 pillars of game development: a beginner's guide|educative|https://myuva-my.sharepoint.com/:b:/g/personal/jac7az_virginia_edu/IQCo_mXs_BVMQ7rtZv3kzOA2AcmXEoo5_CmndHfHF5DlwNc?e=M7KY48|Beginner's guide to basics of game development, like important skills, processes, mechanics, different parts, advice, etc.|
|A beginner's guide to getting into gaming|npr|https://myuva-my.sharepoint.com/:b:/g/personal/jac7az_virginia_edu/IQAIJLl0Jn2CRJSm7ZLK1eLdASXGRi-EhWmgILFhTFanQYw?e=SCRtsS|Explains different types of games and consoles, what kinds of people and lifestyles they're suited for and examples of each category|
|Game Analytics 101|Number Analytics|https://myuva-my.sharepoint.com/:b:/g/personal/jac7az_virginia_edu/IQBdD5PVY1lBQqvLzNQzWarfAaJrxeGcfn_MCE9n-nyE2_s?e=bzMPxN|Explains what game analytics is, what it's used for, why it's useful, etc.|
|The True Cost of Games: Why Understanding AAA, AA, and Indie Titles Matters Now More Than Ever|LinkedIn|https://myuva-my.sharepoint.com/:b:/g/personal/jac7az_virginia_edu/IQC8gBfHHKKgQZLPYmiLCOd6AdQ8W4Zl_Rpkmnc0i886rVU?e=IzTJ2O|Explains the importance of categories and company hierarchy, what each tier implies, how it's been affecting the industry, etc.|
|How Platforms Are Colliding and Why This Will Spark the Next Era of Growth|BCG|https://myuva-my.sharepoint.com/:b:/g/personal/jac7az_virginia_edu/IQB5qaSS95U6Q7jTJWOSzewKAWGBuDOC2oFy0_Gg1vuM87k?e=DqG5fk|Gaming report for 2026, covering new gaming consoles, advancements in technology, new global updates in marketing, advertisement, and development tactics|
|What is Metacritic and Metascore?|Medium|https://myuva-my.sharepoint.com/:b:/g/personal/jac7az_virginia_edu/IQB3g-fJM_ECQpb4x-L492K5AdtS1U0c1TGYy22rETLIIp4?e=N5I1mv|Basics of Metacritic & metascore, what their importance is and what these measurements imply|
## Data Creation
This data about games was taken from Kaggle 🎮 Video Game Sales & Industry Data from 1980 to 2024. The data contained information about release year, critic rating, total global sales combined across different regions, genre, publisher, and console each game can be played on. This data was aggregated to only include games from 2010-2024, then converted from CSV to JSON documents and downloaded as a zip file. However, the data actually stops at 2020. The JSON documents were created based on each individual row in the CSV. Each game becomes one document, and the document title uses its index number in the CSV with the game name.
|Code File|Description|Link to Code|
|---------|-----------|------------|
|data_creation.py|code file splitting each game in each row of the CSV into a JSON document|https://github.com/jac7az/games/blob/main/code/data_creation.py|
### Bias Identification
First, there is selection bias, since I restricted the data to 2010 onwards only, meaning games from 1980 to 2009 will all be missing. All data will favor more modern trends like live-service models and mobile/PC gaming, ignoring the old trends like renting CDs, DS, Game Boys, etc. Additionally, multiple games can appear as different JSON docs because they were released on different consoles, making them weigh more significantly than other games with fewer releases.

Since restricting the data to 2010 onwards was intentional, the scope of the project is limited to modern-era gaming trends rather than overall. To solve the problem of multiple games having their own JSON document, the game can be aggregated into 1, splitting the data appropriately according to console-level.

### Rationale
We restricted ourselves to post-2009 to avoid computational overload and stay within the MongoDB Free Tier to reduce costs. The year 2016 served as a logical threshold of the modern era, and it has data from more standardized tracking methods that games from older eras, especially pre-2010, won't have the benefit of accurate digital records, which will mitigate uncertainty. Converting the CSV to individual JSON documents allows NoSQL logic and use. Another important decision was encoding the publisher and developer brands to avoid high cardinality and dimensionality after encoding. The average total sales per company was used as a way of converting a qualitative variable to a numerical variable while being able to maintain brand presence between brands. Higher average sales mean a more popular gaming company compared to a different company with a handful of games. This method also accounts for publishers with very few games but all popular hits. Uncertainty is mitigated by nesting similar information into 1 document rather than separating by each row in a CSV. Additionally, to avoid duplication, games with multiple rows because of differences in information, like different consoles, are combined into 1 DOC and split by nesting. 

## Metadata
### Implicit Schema
The top level should contain attributes that remain constant across all versions of 1 game title, including genre, publisher, and developer. At the nested level, it should contain platform-specific information, which is the console machine and total sales associated with it, and what year the game was released on that console and the critic rating. All of these form 1 document.

### Data Summary
|Feature|Count|
|-------|-----|
|Total Docs|7135|
|Unique Game Titles|4522|
|Release Year Range|2010-2020|
|Most Frequent Genre|Action|
|Least Frequent Genre|Sandbox|
|Most Frequent Console|PS3|
|Least Frequent Console|SAT, GBA, WW|
|Most Frequent Publisher|Ubisoft|
|Average Critic Score|7.29|

### Data Dictionary
|Name|Datatype|Description|Example|
|----|--------|-----------|-------|
|title|string|Official game title|"Grand Theft Auto V|
|console|string|platform hardware|"PS3"|
|critic_score|float|average review rating|9.4|
|total_sales|float|global units sold per million|0.24|
|release year|int|year of release|2013|
|genre|string|genre type of the game|shooter|
|publisher|string|company that published the game|Namco Bandai|
|developer|string|studio that created the game|Konami|

|Feature|Mean|Standard Deviation|Min|Max|Interpretation|
|-------|----|------------------|---|---|--------------|
|critic_score|7.287|0.614|1|10|Mostly clustered around mean with low variance, with scores concentrated between 7 and 8
|total_sales|0.353|0.995|0|20.32|Massive spread from the mean, suggesting high volatility
|release_year|2013|2.798|2010|2020|Consistent upward trend from 2010 with relative lack of outliers due to pre-filtering.|
