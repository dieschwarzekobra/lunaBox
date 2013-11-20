lunaBox
=======

# lunaBox ♡

## Project Purpose and Vision

The lunaBox aims to be an easily navigable collection of all of the original Sailor Moon episodes! The 1990s series is amazing and can be, at times, impossibly difficult to access. It’s super expensive, and it is also really hard to keep track of all of the episodes with so many different companies that have played a part in delivering this series to so many different parts of the world. While I certainly encourage everyone to invest in purchasing the series, the lunaBox can be a great way for those of us who are saving up to buy the series to access the episodes that are already on the web.

The lunaBox is a Raspberry Pi enabled interface for easily accessing and streaming high quality Sailor Moon videos. While this technology could prove incredibly useful with customization capabilities, the scope of this particular project is to create something special for Sailor Moon lovers. The most customization that will be intended for this project is the ability to edit video URLS just in case there are broken links or better quality videos. The scope of this project also restricts the video sources to dailymotion and youtube, as the video player for this project is omxplayer. Of course, this is an open source project so if someone wants to make these customizations they are more than welcome to. It just won’t be something that this project aims to make easier by including it in the user interface and overall software packaging.


## Milestones

**Program connects to hyperlink database.** If this works, episode titles will be able to print onto the console.

**User can paginate through the results, yielding six results at a time.** Meeting this milestone requires python SQL commands into SQLite3. Six titles will be printed, while the six corresponding URLS will be shoved into an array. These URLS will be passed to the video player. More research has to be done in order to figure out how to pass this parameter to the linux operating system with Python. This parameter passing will simply be based on key entry and mapping by the user for this particular milestone. More research will be done to decide whether or not using dictionaries or simple SQL querying would be best for this program.

**Program is displayed in a window.** The steps to achieve this milestone need to be further researched. At this stage, selection and pagination are not as important as rendering the text onto the window in tiles.

**User can paginate through results in windowed version of program.** The user should be able to press forward and backward arrows to get through all of the pages. Selection is limited to “right and left arrows” at this milestone. The SQL selection process has to be connected to the windowed display process. The windowed process also needs a listening protocol to accept user input.

**User can select videos and have that content printed onto the window.** This is just to make sure the parameter is getting stored. Passing it will be measured by whether or not the video is displayed. The video will be displayed once the parameter is passed and the command is issued to the operating system.

**Program is prettyfied :).** You can’t have a Sailor Moon product without making it look pretty. Besides, the original title of the show is Pretty Soldier Sailor Moon :).

**The software runs on the Raspberry Pi.** The Raspberry Pi must be configured to display on the television screen. The software display needs to be formatted in a way that is useful for the user on a television screen.

**The software can be controlled by a remote control.** Though the Pi is a computer and could probably be navigated using a keyboard and/or a mouse, it would make more sense to be able to use a remote that also works with the television so that the user “work flow” when watching television is not interrupted. More research needs to be done to understand how this will work as well.

**User can update the pointers.** The program can issue update commands to the SQLite3 database to update any broken links. This can be tested by seeing if the video works once the update has been performed.

**The software is well-documented.** Once the software is functioning at a level that is useful for the intended user group, Getting Started documentation and an example website will be set up. 

## Collaboration

I will work together with some friends to configure our hardware for the tasks that we have. I think we could learn a lot from configuring the devices for each other. Perhaps it would enable us to think outside of our own focus and understanding of the functionality of the Raspberry Pi, which could give us some further ideas on more efficient ways to solve roadblocks when we run into them. Even if we do not perform the configurations for one another, we could try our hand at writing one another’s Getting Started documentation for the Raspberry Pi portion of the project. This collaboration could be done on either Google Docs, Github, or both. The Getting Started documentations could actually end up being merged into one document, depending on how helpful the learning experience is for both of us.

It could also benefit us to work on a project site together. The site could just be a collective space for sharing and further developing unique and interesting Raspberry Pi projects. Then, we could divide up the work and lighten the workload that may come with trying to come up with a product as well as useful documentation.

## Technologies Used 

A Raspberry Pi will be used to connect the guide to the television, and a remote control will be used to control the Pi. Python will be used to accept and apply the filters, as well as communicate between the GUI and the operating system. The OS/Sys libraries will likely come in handy for this project since a command to the Linux computer to run omxplayer will need to happen. SQLite3 will also be used.


## Enabling Re-use

Anyone who loves Sailor Moon should be able to use this project. Also, anyone who wants to use Python to communicate between a GUI and an operating system could also find this project useful, as it can serve either as an example or a platform upon which they can build their own project. Someone who wants to use a windowed program with a similar functionality that is not necessarily game-related could also find this project useful if they are just starting to understand how windowed programming works. Overall, I hope for this project to be useful as more than just its main intended functionality. I want it to be a learning tool and maybe even a foundation for other work, which is a major characteristic of Open Source work as a concept. Therefore, a Github repository will definitely be used and hopefully well-documented. An example site is another goal, just in case someone who is less familiar with github wants to learn more about the project, or to use it for their own television watching needs. Selecting a license is also important.
