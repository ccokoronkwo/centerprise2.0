# Centerprise 2.0

Centerprise 2.0 is the next iteration of a web application for handling Centers Business Office Invoices, Expenses and Payroll Allocation Across Facilities

## Getting Started

This documentation is intended to aid with a basic remote pull-down and local spin-up of Centerprise 2.0

## Table of Contents
<details>
<summary>Click to expand</summary>

- [About](#about)
- [Install](#install)
- [TODO](#todo)use
  * [Security](#security)
  * [Invoices](#invoices)
  * [Payroll](#payroll)
  * [ACH](#ach)
  * [Details](#details)
  * [Receivables](#receivables)  
  * [Distribution](#distributions)
  * [Credit Card Data](#credit-data)
  * [Credit Card Allocations](#credit-allocations)
  * [AP Rep Pending Allocations](#pending-allocations)
  * [Facilities](#facilities)
  * [Departments](#departments)
  * [Unit](#unit)
- [🔌 Third Party Plugins](#plugins)
- [Tests](#tests)
- [Version](#version)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

</details>

## About

Centerprise 2.0 is the next iteration of a web application for handling Centers Business Office Invoices, Expenses and Payroll Allocation Across Facilities

## Install

A step by step series of examples that tell you how to get a development env running

Steps to come ...

```

```

## TODO

### Security
	* [X] Security
		* [X] User Login
		* [X] Role Assignment
		* [X] User Management
	    * [] Other Unknowns

<details>
<summary>Security Notes</summary>

- [Authentication](#user-authentication)
<!--
- [Install](#install)
- [TODO](#todo)
  * [Security](#security)
  * [Invoices](#invoices)
  * [Payroll](#payroll)
  * [ACH](#ach)
  * [Details](#details)
  * [Receivables](#receivables)  
  * [Distribution](#distributions)
  * [Credit Card Data](#credit-data)
  * [Credit Card Allocations](#credit-allocations)
  * [AP Rep Pending Allocations](#pending-allocations)
  * [Facilities](#facilities)
  * [Departments](#departments)
  * [Unit](#unit)
- [🔌 Third Party Plugins](#plugins)
- [Tests](#tests)
- [Version](#version)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
-->

## User Authentication

Flask-Security has many native advanced authentication and user login management features - all of whcih can be controlled from the ./app.config.py file.  See [this article]https://pythonhosted.org/Flask-Security/configuration.html) for customization details.

Default templates for security pages (login/logout/reset_password,etc) can be found in the following folder:
```
--centerprise2.0/app/templates/security/
```
</details>

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
    	* [] Filter/Reset Filter
    	* [] Print
    	* [] Excel
    	* [] PDF
    * [] Cash Receipt Batches
    * [] Cash Receipts

### Distributions
    * [] Distributions
    	* [] Lots
    		* [] New Lots
    	* [] Distributions
    		* [] New Distribution

### Credit Data
	* [] Credit Data
		* [] Upload Credit Card Data
    	* [] New Credit Card Data

### Credit Allocations
	* [] Credit Allocations
		* [] Credit Card Allocations
    	* [] New Credit Card Allocation

### Pending Allocations
	* [] Pending Allocations
		* [] AP Rep Pending Allocations
    	* [] Create one instance of this in each blueprint

### Facilities
	* [] Facilities
		* [] New Facility
		* [] New Facility Subgroup
		* [] Email Facility

### Departments
	* [] Departments
		* [] New Department
		* [] New Department Group

### Unit
	* []  Unit Tests


## Deployment

In order to deploy this application on a live system ...
```
Details to come ...
```

### Plugins

Supporting Technology:

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


## Tests

To run the automated tests for this Centerprise 2.0 please execute ...

### Test 1

Explain what these tests test and why

```
Example to come ...
```

### Test 2

Explain what these tests test and why

```
Example to come ...
```

### Test 3

Explain what these tests test and why

```
Example to come ...
```

## Version

Versioning of Centerprise follows Sematic Versioning 2.0.0 [SemVer](http://semver.org/).

## Authors

* **Chinwendu Okoronkwo**

## Acknowledgments

* Charly Jazz [Flask-MVC Template](https://github.com/CharlyJazz/Flask-MVC-Template)