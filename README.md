#### Project 02
# Webscraping General Conference
- This is a team project. Through GitHub Classroom you should have created a shared GitHub repository with your teammates. As long as you upload your finished code to that team repository, each team member will get credit. You will also need to fill out a peer review survey on Learning Suite to recieve credit (if you're in a team by yourself, you don't need to).
- I do not provide automated tests for projects. You will need to determine yourself whether the code meets the requirements provided in the rubric. It is important for you to be able to determine whether a program you write meets requirements (in the real world there won't be pre-written tests to tell you if you did your job right).
  - The disadvantage is that it takes some time to grade your assignment. After you turn in your code, your code will be manually graded (meaning partial credit may be given for certain requirements). The TAs will update the `RUBRIC.md` file with your grade and any comments that they have. Give us about 2 weeks after the due date to get the grades in.
- For this project you will web scrape the talks from General Conference of The Church of Jesus Christ of Latter-day Saints, which you can find [here](https://www.churchofjesuschrist.org/study/general-conference/2025/10?lang=eng). For those that aren’t members of the church, general conference is when church leaders give talks (speeches) about different topics to the whole world. Talks have a title and a speaker, and typically there are many references to books of scripture (among other things). Your team's task is to scrape the name of the talk, the speaker, as well as the number of references to each book of scripture in each talk. You can watch a video of me walking through what you'll scrape [here](https://www.youtube.com/watch?v=nmkdnwjX_N0).

> **Note:** Currently, the project requires scraping just the **October 2025** general conference. This is because there are a couple of quirks (some talks not making any references to external sources) that make the scraping task a little more complicated, which is great practice for other realistic scraping tasks.

## Libraries Required
- `playwright`
- `pandas`
- `openpyxl`
    - you don't need to import this one, but it needs to be installed on your computer for pandas to export and import Excel files.

## Logical Flow
There are many ways to do this project, and all that matters is that you fulfill the requirements.

After the logical flow section, you’ll find suggestions and hints for completing the project. You don't need to follow those suggestions, but I highly recommend reading through it.

You are only required to scrape the talks from the October 2025 conference, but your code should still work even if you switched the URL to a different conference session date. That means **no hardcoding** things that wouldn’t generally work for different conference sessions. Feel free to ask the professor or the TAs if you aren’t sure about what qualifies as hardcoding.

### Menu
Repeatedly print out:
```
Menu:
1: Scrape October 2025 Conference
2: View summary data
Exit: Exit the program
Enter an option: 
```
If the user enters anything else, just print a message and repeat the menu until `Exit` is entered.
If they enter `1` or `2`, do the following:

### Option 1: Scraping General Conference
1. Using `playwright`, navigate to the October 2025 conference page:
    - `https://www.churchofjesuschrist.org/study/general-conference/2025/10?lang=eng`
    - When you are setting up a browser with `playwright` using the `.launch()` method, please use `slow_mo=2000` as a parameter/argument pair. That will make it pause 2 seconds between each action. That is just so we aren't overloading the church's website, especially if 100s of students are working on this at the same time.
2. Access the pages for **all individual talks**
    - **Ignore** pages that just have video recordings, like “Saturday Morning Session”.
    - **Ignore** “Sustaining of General Authorities, Area Seventies, and General Officers” (it isn’t a talk).
3. For each talk, scrape the following info:
    - Speaker’s name
        - Depending on where you scrape the name from, it might be prefixed with `"By "`. Trim those leading characters. Titles (e.g., “Elder”, “Sister”) can remain.
    - Title of the talk
    - The “kicker” (the quote in different font before the main text)
    - The **number of times each book of scripture** is listed in the references side panel.
        - This is accessed by clicking the "Related Content" button (the one with some dots and lines) near the top right.
        - Every time a book of scripture is mentioned (for example, "1 Nephi") increase the count for that book of scripture.
        - Some talks don't have any "Related Content". Make sure you still grab the speaker's name, title and kicker for those pages though.
4. Store the aformentioned info in a copy of the `std_works` dictionary that is provided to you
    - For each talk, create a copy of the dictionary: `std_works_copy = std_works.copy()`
    - Store all the info in the copy of the dictionary, and then append that dictionary to a list. 
    - If you accidentally delete the dictionary, here it is:
```
std_works = {
    'Speaker_Name': "",
    'Talk_Title': "",
    'Kicker': "",
    'Matthew': 0, 'Mark': 0, 'Luke': 0, 'John': 0, 'Acts': 0, 'Romans': 0,
    '1 Corinthians': 0, '2 Corinthians': 0, 'Galatians': 0, 'Ephesians': 0,
    'Philippians': 0, 'Colossians': 0, '1 Thessalonians': 0, '2 Thessalonians': 0,
    '1 Timothy': 0, '2 Timothy': 0, 'Titus': 0, 'Philemon': 0, 'Hebrews': 0,
    'James': 0, '1 Peter': 0, '2 Peter': 0, '1 John': 0, '2 John': 0, '3 John': 0,
    'Jude': 0, 'Revelation': 0, 'Genesis': 0, 'Exodus': 0, 'Leviticus': 0,
    'Numbers': 0, 'Deuteronomy': 0, 'Joshua': 0, 'Judges': 0, 'Ruth': 0,
    '1 Samuel': 0, '2 Samuel': 0, '1 Kings': 0, '2 Kings': 0, '1 Chronicles': 0,
    '2 Chronicles': 0, 'Ezra': 0, 'Nehemiah': 0, 'Esther': 0, 'Job': 0,
    'Psalm': 0, 'Proverbs': 0, 'Ecclesiastes': 0, 'Song of Solomon': 0,
    'Isaiah': 0, 'Jeremiah': 0, 'Lamentations': 0, 'Ezekiel': 0, 'Daniel': 0,
    'Hosea': 0, 'Joel': 0, 'Amos': 0, 'Obadiah': 0, 'Jonah': 0, 'Micah': 0,
    'Nahum': 0, 'Habakkuk': 0, 'Zephaniah': 0, 'Haggai': 0, 'Zechariah': 0,
    'Malachi': 0, '1 Nephi': 0, '2 Nephi': 0, 'Jacob': 0, 'Enos': 0, 'Jarom': 0,
    'Omni': 0, 'Words of Mormon': 0, 'Mosiah': 0, 'Alma': 0, 'Helaman': 0,
    '3 Nephi': 0, '4 Nephi': 0, 'Mormon': 0, 'Ether': 0, 'Moroni': 0,
    'Doctrine and Covenants': 0, 'Moses': 0, 'Abraham': 0,
    'Joseph Smith—Matthew': 0, 'Joseph Smith—History': 0, 'Articles of Faith': 0
}
```
5. Export the scraped data
    - After you've scraped the page of each talk, turn your list of dictionaries into a pandas DataFrame
    - Then, export your DataFrame to an excel file named `conference_talks_data.xlsx`
    - Feel free to reference `solution_conference_talks_data.xlsx` for an example of what it should look like when you export the data.
6. Print:  
   `You've scraped all the conference data.`

---

## Option 2: View summary data
> I give you basically all the code for this part in the hints/suggestions section. Be sure to check that out if you want help.

1. If this option is chosen before the data has been scraped, meaning the exported excel file can't be found, print out:
    - `"Excel file couldn't be found"`
    - Then go back to the main menu for the user to choose an option again.
2. If the Excel file is successfully loaded, print out:
    1. The 10 most quoted standard works
    2. The talk(s) that quoted the Doctrine and Covenants the most
    - Here's what it should look like:
```
These are the top 10 most quoted standard works in October 2025 conference:

Doctrine and Covenants    108
Alma                       61
John                       56
Matthew                    54
Mosiah                     38
3 Nephi                    33
2 Nephi                    31
Moroni                     30
Luke                       18
Isaiah                     16
dtype: int64


The talk(s) that quoted the Doctrine and Covenants the most:

                 Speaker_Name                     Talk_Title  Doctrine and Covenants
3   Elder Ronald M. Barcellos  The Lord Looketh on the Heart                       9
10       Elder Kevin G. Brown  The Eternal Gift of Testimony                       9 
```

## Hints/Suggestions

### General Hints/Suggestions
- You can do this without AI; everything can be scraped using just the playwright techniques showed to you in the class practice files. I'd recommend looking at the solutions folder of the class practice. But if you do decide to use AI to help you out, just remember it will be WAY more helpful if you paste in the html of the page you are trying to scrape so that it has the proper context. It may provide solutions more complex than what you learned in class, so use at your own risk.

### Option 1 Hints/Suggestions
1. Using `playwright`, navigate to the October 2025 conference page:
    - see the solutions from the class practice for examples on setting this up.
2. Access the pages for **all individual talks**
    - Try right clicking the list of talks on the content page and inspect the elements that contain each talk section. You might find something that makes it easy to tell the talks apart from the other links. There are other potential ways to only grab talks too. Do what makes the most sense.
    - Make sure you aren't just finding every `<a>` element on the whole page. The page has lots of other `<a>` elements that link to things other than the talks.
    - For navigating to each talk's page, you have at least 2 strategies:
        1. Use `playwright`'s `.click()` method to click on an individual talk, then scrape the data your need, and then go back to the contents page. Then click on the next talk and repeat the process until you've clicked on all of the talks. Like file `05` from the class practice
        2. Find and store all the talk URLs from the relevant `<a>` elements, then directly open up each URL one by one until you've gone through them all. Like file `06` from the class practice.
            - If you do option 2, remember that talk links are **relative**. Prepend `https://www.churchofjesuschrist.org` to the `href` attribute in the `<a>` elements.
            - I personally find option 2 easier, but do whatever you want.
    - If you are having trouble isolating the `<a>` elements you need, consider first locating a parent element that encapsulates the section that has all the talk links, but leaves out the other stuff (like the navigation banner at the top of the page, etc.).
    - (Optional) Print something like `trying to scrape url: {url}` before loading a specific page for debugging and visibility. That way if your code crashes, at least you can tell which page it crashed on by checking what last printed in the terminal.
3. & 4. Scraping the info
    - Once you've accessed the page for an individual talk, use `.locator()` liberally. Remember `.text_content()` will get you the actual text from an element.
    - Make a copy of the dictionary I give you using `std_works_copy = std_works.copy()`. That way, you aren't overwriting any data you scraped when you get to a new page. To ensure the data is saved, make sure you append the `std_works_copy` dictionary to a list before going to the next page.
    - **Speaker Name**
        - Store the string as the value to `std_works_copy["Speaker_Name"]`.
        - If you need to trim the `"By "` before the speaker's name, you could use `.replace()` or add `[3:]` to the end of your string.
    - **Talk Title** and **Kicker**
        - Kicker is the quote before the talk’s main text.
        - Store each string to `std_works_copy` using their keys (`Talk_Title` and `Kicker`)
    - **Reference counts per book**
        - To get access to the references, first tell playwright to click the "Related Content" button near the top right corner that has the dots and lines.
        - Once you click it, it should open up a panel on the right side. For a couple of talks, including the first "Introduction" talk, there are no references. Make sure your code doesn't break for those talks. One way to guard against it breaking is to check the `.count()` of an element and see if it is above 0 before trying to scrape data from that element. See class practice file `07` for an example of that.
        - I recommend just grabbing all of the references text in one element and storing it using `.text_content()`
        - For books like `"1 Nephi"` or `"1 Kings"`, HTML often uses non-breaking spaces between the number and the name instead of regular spaces. For example, if you inspect the references of Elder Stevenson's talk "Blessed are the Peacemakers" you'll notice that `"3 Nephi 12:16"` shows up as `"3@nbsp;Nephi 12:16"`. That makes it so that the `3` and `Nephi` never show up on separate lines. But, to make it easier to count the number of references, you should replace those non-breaking spaces with regular spaces. Here's some code to help you:
            - ```
              related_content_references = page.locator('you figure this part out yourself')
              if related_content_references.count() > 0:
                  references_text = related_content_references.text_content()
                  references_text = references_text.replace("\u00A0", " ")
              ```
        - Once you have the text of the references ready, loop over the the `std_works_copy` dictionary. Each key in that dictionary (after the first 3) is a book of scripture. You can use the `.count()` function on the references text you scraped with each key from the dictionary. That will tell you the number of times each key appears in that string. For example, if you wanted to store how often `Luke` appeared in the references section text, you could do:
            - ```
              std_works_copy["Luke"] = references_text.count("Luke")
              ```
            - But instead of hardcoding in "Luke", just use the keys of the dictionary as you loop through it
            - Skip the non-book keys: `"Speaker_Name"`, `"Talk_Name"`, `"Kicker"`. You might find `continue` useful for that, but it depends on how you code it.
        - Once all the data is stored, append the `std_works_copy` to a list (and make sure the list is created outside of the loop going through each page).
        - Then, move on to next talk and repeat.
        - EXTRA STUFF FOR NO EXTRA POINTS:
            - If you are particularly observant, you might notice a problem with some books of scripture: if there is a reference to `John`, we would also count it for `1 John`, `2 John`, etc.
            - Honestly, the best way to count references wouldn't be to use `.count()`, but instead use regular expressions for complex pattern matching. Regular expressions would also help get rid of situations where the references text uses a name like "John" in passing, but not as an actual reference to scripture. But I didn't teach you regular expressions. Feel free to look that up if you want and implement a better solution (for no extra points mind you). But we can still get around the first issue by using just `count()`. You just need to subtract any potential double counts before saving the dictionary. If you want to include that code, here's an example below. But because there are no references to `1 John`, `2 John`, `3 John`, `Words of Mormon`, or `Joseph Smith—Matthew` in October 2025's conference, it actually doesn't make any difference in the results for this assignment. But for those of you that want to make it more accurate on principle, here you go:
            - ```
              std_works_copy["John"] = std_works_copy["John"] - std_works_copy["1 John"] - std_works_copy["2 John"] - std_works_copy["3 John"]
              std_works_copy["Mormon"] = std_works_copy["Mormon"] - std_works_copy["Words of Mormon"]
              std_works_copy["Matthew"] = std_works_copy["Matthew"] - std_works_copy["Joseph Smith—Matthew"] 
              ```
5. Exporting the data
    - Import `pandas` and put the list with all the dictionaries into `df = pd.DataFrame(your_list_here)`
    - Use `.to_excel()` to export the dataframe to an Excel file. Make sure you include `index=False` to leave out the index numbers that pandas always adds to the data.
6. Print:  
   `You've scraped all the conference data.`


### Option 2 Hints/Suggestions
1. Guarding against importing a file you can't find
    - The easiest way to not crash when python can't find a file is to handle a `FileNotFoundError` exception. Here's an example:
    - ```
      try:
          df = pd.read_excel("conference_talks_data.xlsx")
      except FileNotFoundError:
          print("Excel file couldn't be found")
          continue
      ```
2. Summary data
    - The focus of this project is the webscraping. To save you time, here's the code that will get you the summary analysis you need. Read through the comments and try to understand what each piece is doing. Also note that if you forgot to exclude the index column when you exported your DataFrame to an excel file, you'd need to change the `3` in the first part to a `4` to account for the extra column.
    - ```
      # df.columns[3:] gets you the all the column names from index 3 on
      # .sum() will calculate the sum for each of those columns
      # .sort_values(ascending=False) will sort the sums from highest to lowest
      # .head(10) will limit the results to only 10. Since they are sorted, it is the 10 highest
      print(f"\nThese are the top 10 most quoted standard works in October 2025 conference:\n")
      print(df[df.columns[3:]].sum().sort_values(ascending=False).head(10))

      # .max() finds the highest value
      # @ in .query() lets you insert a variable value into the query
      # This .query() is finding the rows that have the highest count for d&c
      # Then, after .query(), we only print out the 3 columns that we want to show
      print(f"\n\nThe talk(s) that quoted the Doctrine and Covenants the most:\n")
      max_dc = df["Doctrine and Covenants"].max()
      print(df.query("`Doctrine and Covenants` == @max_dc")[['Speaker_Name', "Talk_Title", "Doctrine and Covenants"]], "\n")
      ```

## Rubric:
Remember there are no automated tests for projects. See RUBRIC.md. Remember to right click and select "Open Preview" to view the file in a nice format. The TAs will update this file with your grade and any comments they have when they are done grading your submission.

## Example Output
This first shows entering a bad option, then doing option 2 before scraping, then scraping all the data, and then viewing the summary data.

```
Menu:
1: Scrape October 2025 Conference
2: View summary data
Exit: Exit the program
Enter an option: asdf
Invalid option, try again.


Menu:
1: Scrape October 2025 Conference
2: View summary data
Exit: Exit the program
Enter an option: 2
Excel file couldn't be found

Menu:
1: Scrape October 2025 Conference
2: View summary data
Exit: Exit the program
Enter an option: 1
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/19oaks?lang=eng
        No references for this talk
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/12stevenson?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/13browning?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/14barcellos?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/15eyre?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/17johnson?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/16uchtdorf?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/21rasband?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/22webb?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/23jaggi?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/24brown?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/25gong?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/26cziesla?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/27cook?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/31kearon?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/32dennis?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/33barlow?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/34jackson?lang=eng
        No references for this talk
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/35andersen?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/41holland?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/42evanson?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/43soares?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/44johnson?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/45christofferson?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/46spannaus?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/47eyring?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/51bednar?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/52cuvelier?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/53holland?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/54godoy?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/55renlund?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/56amos?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/57farias?lang=eng
trying to go to https://www.churchofjesuschrist.org/study/general-conference/2025/10/58oaks?lang=eng

You've scraped all the conference data.

Menu:
1: Scrape October 2025 Conference
2: View summary data
Exit: Exit the program
Enter an option: 2

These are the top 10 most quoted standard works in October 2025 conference:

Doctrine and Covenants    108
Alma                       61
John                       56
Matthew                    54
Mosiah                     38
3 Nephi                    33
2 Nephi                    31
Moroni                     30
Luke                       18
Isaiah                     16
dtype: int64


The talk(s) that quoted the Doctrine and Covenants the most:

                 Speaker_Name                     Talk_Title  Doctrine and Covenants
3   Elder Ronald M. Barcellos  The Lord Looketh on the Heart                       9
10       Elder Kevin G. Brown  The Eternal Gift of Testimony                       9 


Menu:
1: Scrape October 2025 Conference
2: View summary data
Exit: Exit the program
Enter an option: exit
Thanks for using the program
```