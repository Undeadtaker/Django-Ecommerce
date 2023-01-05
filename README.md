# Django Ecommerce Web App
### Live demo https://www.starshop-demo.online

![alt text](https://i.imgur.com/k80Eks9.png) 
## Features

- Account creation (with email token confirmation)
- Browsing through the catalogue and selecting items
- Adding items to basket, proceeding to checkout, payment to be implemented
- Creation of Address of delivery
- Adding items to wishlist

 An ecommerce store is an online platform that allows businesses or individuals to sell their products or services 
 to customers over the internet. Customers can browse and purchase products through the store's website or app, 
 and the store usually handles the payment processing, order fulfillment, and customer service. Ecommerce stores 
 can sell a wide variety of products and services, and they can be used by businesses of all sizes, from small 
 independent sellers to large multinational corporations.

# 1) To run the development server

The development server is used by default when creating Django applications. To do this you will need to install 
requirements.txt, after which you will need to run:
`python manage.py migrate`

Finally, to start the server:
`python manage.py runserver`

Note: it's also recommended that you create a superuser for the app. The default user model has been overloaded
therefore email will be used when logging in to your account. 
`python mange.py createsuperuser`

### 2) To setup redis on Windows 

Redis is not officially supported on Windows. However, there is a workaround. By installing a redis server on windows it 
will take shape of a background process which will be listening on port 6379 passively. Redis is for now used as a messaging
queue for Celery and sending tasks to it. To have redis running in the background simply go to the website 
> https://github.com/tporadowski/redis/releases

and download the latest version ending in .msi
Additionally, there will be a redis package in requirements.txt which will be installed.

### 3) To setup Celery 
From the requirements.txt the python package Celery will be included. Since Celery is also not supported on windows because
the worker cannot spawn additional worker processes, the worker itself will perform all of the background calculations by
specifying --pool=solo. Navigate to root directory and write out the following command:

`celery -A ecommerce.celery worker --pool=solo -l info` 

which will prompt the celery client to be initiated. Any prints to the console or any things of that nature will be printed
in this terminal. 
&nbsp;
&nbsp;
&nbsp;
> This is an ongoing project. Something that I will constantly seek to improve. The default layout of the App
> was created following a tutorial series from Very Academy https://www.youtube.com/@veryacademy . 
> However, now I will seek to improve the design and integrate new features one of which includes a payment gateway
> integration. For now in mind I have the allsecure service provider, but it is open to discussion. 
>