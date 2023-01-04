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

# To run the development server

The development server is used by default when creating Django applications. To do this you will need to install 
requirements.txt, after which you will need to run:
`python manage.py migrate`

Finally, to start the server:
`python manage.py runserver`

Note: it's also recommended that you create a superuser for the app. The default user model has been overloaded
therefore email will be used when logging in to your account. 
`python mange.py createsuperuser`
&nbsp;
&nbsp;
&nbsp;
> This is an ongoing project. Something that I will constantly seek to improve. The default layout of the App
> was created following a tutorial series from Very Academy https://www.youtube.com/@veryacademy . 
> However, now I will seek to improve the design and integrate new features one of which includes PayPal
> integration which is not working from the tutorial series. I will just leave the download link for the
> Redis server for future reference https://github.com/tporadowski/redis/releases . 

Command to run celery on windows.
`celery -A ecommerce.celery worker --pool=solo -l info` 