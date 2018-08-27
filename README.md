# Centerprise 2.0

Centerprise 2.0 is the next iteration of a web application for handling Centers Business Office Invoices, Expenses and Payroll Allocation Across Facilities

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Table of Contents
<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText=Click to expand) -->


<!-- AUTO-GENERATED-CONTENT:END -->

## About
Centerprise 2.0
------------------
Centerprise 2.0 is the next iteration of a web application for handling Centers Business Office Invoices, Expenses and Payroll Allocation Across Facilities

## Install

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

## TODO
TODO:
-----
### Security
* [] Security
    * [] User Login
    * [] Role Assignment
    * [] User Management
    * [] Other Unknowns
* [] Main Application

### Invoices
	* [] Invoices
		* [] New Invoice
		* [] Preview/Process ACH
		* [] New Vendor
	    * [] Advanced Search
	    * [] View/Adjust Old Invoices
	    * [] Export Invoices
	    * [] Import Invoices
	    * [] Compare Invoices
	    * [] Allocate Incomplete Invoices
	    * [] Delete Selected
	    * [] Delete All

### Payroll
    * [] Payroll
    	* [] New Payroll Invoice
    	* [] New Period
    	* [] View/Adjust Old Invoices
    	* [] Export Invoices
    	* [] Update Totals
    	* [] Delete Selected

### ACH
    * [] Pre-Scheduled ACH
    	* [] New Pre-scheduled ACH

### Details
    * [] Monthly Invoice Details
    	* [] Print/View
    	* [] Email
    	* [] Summary PDF
    	* [] Summary Excel
    	* [] Monthly Facility GL Summary

### Receivables
* [] Receivables
    * [] Receivables
    	* [] Filter/Reset Filter
    	* [] Print
    	* [] Excel
    	* [] PDF
    * [] Cash Receipt Batches
    * [] Cash Receipts

### Distributions
* [] Distributions
    * [] Lots
    	* [] New Lot
    * [] Distributions
    	* [] New Distribution

### Credit Data
* [] Upload Credit Card Data
    * [] New Credit Card Data

### Credit Allocations
* [] Credit Card Allocations
    * [] New Credit Card Allocation

### Pending Allocations
* [] AP Rep Pending Allocations
    * [] Create one instance of this in each blueprint

### Facilities
* [] Facilities
	* [] New Facility
	* [] New Facility Subgroup
	* [] Email Facility

### Deployment
* [] Department
	* [] New Department
	* [] New Department Group

### Unit Tests
* []  Unit Tests


## Deployment
In order to deploy this application on a live system ...

### Prerequisites
Supporting Technology:
--------
[Flask-Via](http://flask-via.soon.build/en/latest/):
For create routes like a [Django Rest Framework](http://www.django-rest-framework.org) style using Blueprints!

[Flask-Security](https://pythonhosted.org/Flask-Security/):
To easily have login, logout, recovery password and to keep administrator views restricted.

[Flask-Admin](https://flask-admin.readthedocs.io/en/latest/):
An admin interface customizable for models and assets recources.

**Add yours models in the file admin.py**

[Flask-Upload](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/):
Enables flask-upload in different blueprints and the ability to save the url of file in the database

[Flask-Script](https://flask-script.readthedocs.io/en/latest/):
Awesome commands for your projects, including the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) commands:
- `createadmin`: Create admin user
- `createapp`: Scaffold new  blueprint folder and register in the file app/routes.py

[Rauth](https://rauth.readthedocs.io/en/latest/)
Social Login with facebook, google and twitter

[Flask-Testing](https://pythonhosted.org/Flask-Testing/)
Simple test unit with [Faker](https://github.com/joke2k/faker) for generate forget data and unittest
And Selenium webdriver for front end testing
- `python -m unittest discover -p <file.py>`: Test the specific file


## Testing

To run the automated tests for this Centerprise 2.0 please execute ...

### Test 1

Explain what these tests test and why

```
Give an example
```

### Test 2

Explain what these tests test and why

```
Give an example
```

### Test 3

Explain what these tests test and why

```
Give an example
```

## Versioning

Versioning of Centerprise follows Sematic Versioning 2.0.0 [SemVer](http://semver.org/).

## Authors

* **Chinwendu Okoronkwo**

## Acknowledgments

* Charly Jazz [Flask-MVC Template](https://github.com/CharlyJazz/Flask-MVC-Template)
* David Wells [MarkDown Magic](https://github.com/DavidWells/markdown-magic)