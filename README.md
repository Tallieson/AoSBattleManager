# AoSBattleManager

<h1>AoS Battle Manager</h1>


<h2>Project Overview</h2>
Age of Sigmar is a miniature table top war game produced by Games Workshop. To play efficently, you need access to rules speread across half a dozen books, AoS Battle Manager will condense nearly all of those into 1 source. Using Python, Django, HTML/CSS, and MySQL we'll allow users to acess that content without the books, as well as create custom content for other users to use in thier own games. 


<h2>Functionality</h2>
User experience should be streamlined as possible. I want to minimized steps users need to take to find the information they need. When beginning a game of Age of Sigmar multiple things need to be determined such as:
 - Open Play/Matched Play/Narrative Play
 - Which "Realm of Battle" is it taking place on
 - What Battle Plan are you using which dictates:
    - Deployment
    - Scoring
    - Potential additonal rules/strategies
 - Terrain Features (which can be dictated by realm of battle)
 
 Upon logining in the option to create a new battle will be presented. Users starting a game will be able to randomize these options, or select them individually. these options will be drop down, and on hover will generate a modal with a description of the selection. We should only need to take selections, and shouldn't need other input from the user. All of this should function in a standard MVC loop.
 
 Once selections are made the information will be rendered in an easy to read view with collapsable divs to provide an easy user experience. This will be considered my minimum viable product.
 
 Other potential features to implement:
  - User management system
  - A submission process for incorrect rules or typos
  - Allow users to upload custom content

<h2>Data Model</h2>
Organizing and populating the database will be the lionshare of the work on this project. As it's mocked up now, I believe it wil consider of 3 main tables, realms, deployment, and battleplan, with probably a dozen tersiary and through tables. I have a rough mock up, but haven't nailed down specifics. I expect to find edge cases that may require reevaluting the model structure.

<h2>Schedule</h2

 Precapstone weeks:
  - Experiment with, and nail down pdf scraping method
  - Collect high res PDF copies of books
 Week 1: 
  - Construct basic views for testing
  - Populate Database
 Week 2:
  - Achieve minimum viable functionality
  - Work on styling, logos, all around presentation
 Week 3:
  - Work through additional wish list features
 Post Class:
  - Finish any unfinished desired features
  - Contact similiar webapp managers about collaborating
  - Deploy(?)
