# Tests for purchases of elastic data

## Project structure:

* **fixtures** (top-level fixtures with purchases/products data and its groups)
* **models** (entities that are used within current task)
* **tests** (validation checks)
* **resources** (folder where the test data is stored)
* **utils** (additional toolset)

## Project requirements:

* `python` (used version - 3.7)
* `pip` (for python3)
* `virtualenv` (for install use: *pip install virtualenv*)
* modules from `requirements.txt`

## Notes:

I used the pydantic library in this assignment.  
Honestly, I couldn't figure out how to turn smart casting on/off quickly.

I could use validation inside the model, but I didn't want to mix the model
and checks to it, so I had to write my own bycycle to make an analogue of
soft assertion with readable trace.

It was difficult to work with this data set:

* Data schema is not described, without some unique
  values you could use _int_ instead of _float_ and don't know about it
* Unclear logic to write auto-tests for price calculation
* I wanted to use a grouping of data by time (year plus month)
  but sampling didn't allow this, so products was grouped on usual chunks