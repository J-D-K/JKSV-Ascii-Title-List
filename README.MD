# JKSV ASCII Title List
The Nintendo Switch does not support anything other than ASCII characters when working with the SD card filesystem. This is a major limitation when working with game titles. This list ensures that JKSV can use path safe, ASCII titles for any title instead of just falling back to a mixture of sanitized titles and application IDs. Even the smallest, innocent looking characters can make JKSV reject the title and fallback to application IDs to prevent corrupt file and folder names.

## Usage:
When using JKSV, simply go to the `Extras`(or `Toolbox Icon`) on the main menu screen and select `Fetch Game Titles`. JKSV will pull the master list from this repo and automatically fetch, rename, and replace the titles of the games in question with their ASCII-safe counterparts.

## How to contribute:
Since there are thousands of games for the Switch, I can't possibly do this all by myself. It would take forever. If you would like to contribute and help make this list as complete as possible, please take the following steps:

1. In JKSV, select the user with the game(s) in question, select/highlight said game and press X to open the options menu. Select **Change Output Folder**.
    <img src="https://i.imgur.com/Ku2ldUJ.png">

2. Enter a new, **path-safe ASCII name** for the game. Be neat and proper too. Other users will be using this too!

3. Make sure Python is installed. Fork this repo and clone it to your PC.

4. Locate your `Paths.json` file in JKSV's configuration folder (`sdmc:/config/JKSV`) and copy to the cloned repo on your PC.

5. Run the merging script:
    ```bash
    python merge_paths.py
    ```
6. Push the changes to your fork and submit a pull request.

### Notes:
Corrections for titles affected by JKSV's string sanitation are welcome. For example, `FINAL FANTASY X-X-2 HD Remaster` will be converted to `FINAL FANTASY XX-2 HD Remaster` because Square-Enix used a unicode hyphen character instead of a standard ASCII hyphen. The goal of this is to standardize JKSV's output to whatever the user would like (Application IDs or Easily Readable Titles).

If you would like to change or correct a path already in the master list, explain why you feel your interpretation is better in your pull request. I will consider all recommendations.
