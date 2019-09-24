# Penn Labs Server Challenge
Remember to **document your work** in this `README.md` file! Feel free to delete these installation instructions in your fork of this repository.

## Installation
1. Fork + clone this repository. 
2. `cd` into the cloned repository.
3. Install `pipenv`
  * `brew install pipenv` if you're on a Mac.
  * `pip install --user --upgrade pipenv` for most other machines.
4. Install packages using `pipenv install`.

## Developing
1. Use `pipenv run index.py` to run the project.
2. Follow the instructions [here](https://www.notion.so/pennlabs/Server-Challenge-Fall-19-480abf1871fc4a8d9600154816726343).
3. Document your work in the `README.md` file.

## Submitting
Submit a link to your git repository to [this form](https://airtable.com/shrqdIzlLgiRFzEWh) by 11:59pm on Monday, September 23rd.

## Installing Additional Packages
To install additional packages run `pipenv install <package_name>` within the cloned repository.

Applicant-defined Features:
<ul>
    <li>
        Routes now have HTTP codes and messages.
    </li>
    <li>
        Users have a list of favorite clubs.
    </li>
    <li>
        Users can now un-favorite clubs.
    </li>
    <li>
        /api/clubs/similar is a route that takes a mandatory club_name: string and an optional n: int in the form data.
        It returns a list of similar clubs to the one specified by club_name. This similarity is currently defined by shared tags,
        but in the future it could have other metrics like shared favorites among users.
    </li>
</ul>
