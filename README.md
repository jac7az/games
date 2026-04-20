# DS4320 Project 2: Gamers
* Executive Summary:
* Name: Carissa Chen; jac7az
* DOI:
* Press Release
* Pipeline
* [License](https://github.com/jac7az/games/blob/main/LICENSE)
## Problem Definition
### Problem Statement
The general topic is determining if high production quality directly correlates to higher commercial sales in video games. The specific problem statement is whether a high critic score has a stronger influence and serves as a better predictor for total sales across different console generations, or whether brand loyalty is a stronger predictor.

Video games are a newer, booming industry where new titles require high production costs to implement. Understanding return on investment is critical for anyone who wants to get into this industry. This investigation seeks to analyze whether it would be more accurate to find the highest revenue games based more on score or if the market is so saturated by similar genre games that brand recognition is becoming a better factor

The initial problem isn't clear on what's considered high quality v. low quality. To narrow this down, predicting and modeling sales is used as the proxy to determine what's high v. low quality, using different characteristics and inputs like console, critic score, publisher, developer, etc. to analyze how consumers now make decisions about what games to try and buy.

[Headline]()
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

[Link to Reading Materials](https://myuva-my.sharepoint.com/:f:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials?csf=1&web=1&e=zRSVjV)

|Title|Publishing Site|Link|Description|
|-----|---------------|------------------------|-------------------|
|6 pillars of game development: a beginner's guide|educative|https://myuva-my.sharepoint.com/:b:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials/6%20pillars%20of%20game%20development_%20a%20beginner_s%20guide.pdf?csf=1&web=1&e=SXzPrD|Beginner's guide to basics of game development, like important skills, processes, mechanics, different parts, advice, etc.|
|A beginner's guide to getting into gaming|npr|https://myuva-my.sharepoint.com/:b:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials/Best%20video%20games%20and%20consoles%20for%20beginners%20_%20NPR.pdf?csf=1&web=1&e=XVBQ6X|Explains different types of games and consoles, what kinds of people and lifestyles they're suited for and examples of each category|
|Game Analytics 101|Number Analytics|https://myuva-my.sharepoint.com/:b:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials/Game%20Analytics%20101.pdf?csf=1&web=1&e=20LKJh|Explains what game analytics is, what it's used for, why it's useful, etc.|
|The True Cost of Games: Why Understanding AAA, AA, and Indie Titles Matters Now More Than Ever|LinkedIn|https://myuva-my.sharepoint.com/:b:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials/The%20True%20Cost%20of%20Games_%20Why%20Understanding%20AAA,%20AA,%20and%20Indie%20Titles%20Matters%20Now%20More%20Than%20Ever.pdf?csf=1&web=1&e=L7Iytp|Explains the importance of categories and company hierarchy, what each tier implies, how it's been affecting the industry, etc.|
|How Platforms Are Colliding and Why This Will Spark the Next Era of Growth|BCG|https://myuva-my.sharepoint.com/:b:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials/The%20True%20Cost%20of%20Games_%20Why%20Understanding%20AAA,%20AA,%20and%20Indie%20Titles%20Matters%20Now%20More%20Than%20Ever.pdf?csf=1&web=1&e=L7Iytp|Gaming report for 2026, covering new gaming consoles, advancements in technology, new global updates in marketing, advertisement and development tactics|
|What is Metacritic and Metascore?|Medium|https://myuva-my.sharepoint.com/:b:/r/personal/jac7az_virginia_edu/Documents/DS4320%20Project%202/Reading%20Materials/What%20is%20Metacritic%20and%20Metascore_%20_%20by%20Sunghee%20Cho%20_%20minimap.net%20_%20Medium.pdf?csf=1&web=1&e=t0N6Ac|Basics of metacritic & metascore, what their importance is and what these measurements imply|
## Data Creation
This data about games was taken from Kaggle 🎮 Video Game Sales & Industry Data from 1980 till 2024. The data contained information about release year, critic rating, total global sales combined across different regions, genre, publisher and console each game can be played on. This data was aggregated to only include games from 2010-2024, then converted from CSV to json documents and downloaded as a zip file. However, the data actually stops at 2020. The json documents were created based on each individual row in the CSV. Each game becomes one document, and the document title uses its index number in the CSV with the game name.
|Code File|Description|Link to Code|
|---------|-----------|------------|
|data_creation.py|code file splitting each game in each row of the csv into a json document|https://github.com/jac7az/games/blob/main/code/data_creation.py|



## Metadata
