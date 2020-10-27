# AoSBattleManager

1. What was the goal and what were the requirements?

The goal of the project was to make something to consolidate information spread between multiple books used for playing a miniature war gaming board game called Warhammer:Age   of Sigmar. I wanted a single page that could present the information in a simple way that was easy to refer to.

2. How does the work meet (or not meet) the goal and requirements?

I believe the project meets those requirements well- though 2 weeks into it's design there was new volume of the game released that made it's function largely unnecessary by consolidating multiple books in the 2020 release. It was obsolete before it was finished- but it did meet the goals it originally set out to.
 
3. How does it work? (big picture: think about how you would describe this to someone who was going to review the code or add functionality, to get them started)

It's a relatively simple project. It's build in Django and utilized a Postgres database.
It has 3 main views:
 -a landing with a general information news feed
 -a generation page where the different parameters of a specific "battle" can be set, with filtering columns to ensure legality per the game rules
 -a paginated "battle" view that fetches the information from the database and displays it neatly

4. Who did you work on this with, and which parts were you responsible for? (If there is no commit or ticket history to review, please be very explicit here)

I worked alone on this project.

5. If you could spend more time, what would you add/improve? 

Well, I would like to find a way to put it to use now, though largely the issue it was trying to solve was solved organically. If I were to try and improve it I think a lot could be done with the file structure, and the organization of the individual files for readability. 
 
How do I run this code on my own web server so I can try it out?
Honestly, at the moment you can't. I had every intention to get it deployed before I sent it you to view, but I have ran into hurdles with that. Currently it's pulling form a local Postgres server. If you'd like to see it in action, I would be happy to show you. Unfortunately this project fell by the wayside a bit, though it was a labor of love at the time I created it.
