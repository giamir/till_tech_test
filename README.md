Till tech test - Python
=======================

![a till](/images/till.jpg)

We want to sell tills to local hipster coffee shop who are finally embracing the 21st century. We need a new till to replace their vintage machines - unfortunately, hipster staff are too cool to learn a new system, so we need you to build something that they will understand.

Specification
-------------

This is what a sample receipt looks like:

![a receipt](/images/receipt.jpg)


Version 1
---------

Implement a system that contains the business logic to produce receipts similar to this, based on a `json` price list and test orders. A sample `.json` file has been provided with the list of products sold at this particular coffee shop.

Here are some sample orders you can try - whether you use this information is up to you:

> **Jane**  
> 2 x Cafe Latte  
> 1 x Blueberry Muffin  
> 1 x Choc Mudcake  
>
> **John**  
> 4 x Americano  
> 2 x Tiramisu  
> 5 x Blueberry Muffin  

Your receipt must calculate and show the correct amount of tax (in this shop's case, 8.64%), as well as correct line totals and total amount. Do not worry about calculating discounts or change yet. Consider what output formats may be suitable.

##Installation Instructions

Clone the repository then change directory into it.

```
$ git clone git@github.com:giamir/till_tech_test.git
$ cd till_tech_test
```

Install and activate VirtualEnv

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Install required packages using pip and the requirements.txt file

```
$ pip install -r requirements.txt
```

Open the interpreter and import the application files

```python
$ python
>>>
```

Now you can use the till system.


##Contributors

* [Giamir Buoncristiani](https://github.com/giamir)
* [Michael Lennox](https://github.com/michaellennox)
