# pnav; a python package
## by Zander

hello! thank you for choosing the pnav package.
This outlines how to use the pnav package and what can be done with it.
There are many use cases and it is constantly being updated.
For more information on a certain function run pnav.help.functionname or pnav.help.help(functionname)

        class:
                function

        random:
                messyCheck
                inputOwn
                checkDate
                isPalindrome
                info
        timer:
                base
                candy
        stockScraper:
                select


#### help. this contains help on what each specific function and class does without having to read the documentation. It provides what is similar to a quick-start guide.
it is very useful for a refresher on a certain function and will be updated in the future.

        pnav.help.help()
        this will print a general guide and overview.

        pnav.help.help('random')

or

        pnav.help.random()

both of these will do the same thing and each will give you more detailed information about the class or function.

        pnav.help.info()

this will display more information about what this function does. as of right now it does not show how to use it but may in the future.



random. this class contains misc projects, functions and items that I did not think needed a entire class dedicated to them.

        pnav.random.messyCheck()

this takes a array or string usually read from a input file and iterates it and checks for the alphabet.

        pnav.random.inputOwn()

this lets you input your own items to search for when running the above function.

        pnav.random.isPalindrome()

this takes a string and returns a boolean on its status as a palindrome.

        pnav.random.info()

this returns a dictionary of values including time, date, ipv4, hostname, date in year/month/day format, and all data returned when you run ipconfig/all in a command prompt.

        pnav.random.info(valuesOnly = True)

this returns the same thing but in a value only format which is harder for humans to read, but much easier to manipulate and use in other functions and projects.



#### timer. uses a gui to get user data.

        pnav.timer.candy()

this creates a gui that takes 3 inputs, the first being the amount of time, the second the amount of candy you want to make last that time. there is also a checkbox that when checked will not generate a windows notification. 
this is a great function to run to get a deeper understanding of how to use the following, much more customizable version.

        pnav.timer.base()

this is the base for a extremely customizable timer gui.
the optional parameters are: 

                title: string,
                        title of the timer.
                label1text: string,
                        label for the first input box will be.
                row1: boolean,
                        toggle the existence of the first row.
                label2text: string,
                        label for the second input box will be.
                row2: boolean,
                        toggle the existence of the second row.
                checkboxtext: string,
                        text for the checkbox.
                checkbox: boolean,
                        toggle the existence of the checkbox.
                enterbuttontext: string,
                        text for enter button
                exitbuttontext: string,
                        text for enter button
                returnOnly: boolean,
                        when left to true it will return all values of each input field. if set to false it will take the data and attempt to do the same thing as the candy timer. there are few scenarios when I would change it to false.

#### stockScraper. uses beautifulSoup4 to get html data from a webpage and then returns information on a certain stock.
this is very basic and uses bs4 to scrape the data from Robinhood for market information, it was one of my early projects. 
this will soon likely be archived and depreciated, at this time I do not see a need to replace it with something better, but neither a need to keep it.

        pnav.stockScraper.select()
        
this is the only function that needs called, it will take user input from the console and display related stock information.

#### pcs. used to setup a makeshift server and communicate between multiple computers.
needs called on both server and client side to open communication between the two, very useful for running commands on others machines.

        pnav.pcs.server()

this is the basic server side command and has many optional arguments for customization and improved usability, they are:
        
        host: string
                the hostname / ip address.
        port: int
                the port you will be opening.
        actions: dict
                a dictionary of possible actions to take.
        serverMessage: string
                the message that prints to let the user know it is starting, you can also input a empty string to print nothing.
        waitTime: int
                the time it waits between checking for new requests.
        connectionString: string
                prints when there is a client side connection to the server, you can also input a empty string to print nothing.

there are many options to play around with and more to come.

        pnav.pcs.client(host)

this is for connecting to a pnav.pcs server, it requires a host name and usually a port as well unless both ports are the default '12345', this also has a very customizable framework with quite a few optional parameters, they are: 

        host: string
                the ip address of the server you are trying to connect to.
        port: int
                the port you are connecting to.
        inputStyle: string
                the style of the cli input: 
        connectionMessage: string
                the message that displays when you successfully connect to the server.

check out my github at https://github.com/ZNav

check out this package at https://pypi.org/project/pnav/