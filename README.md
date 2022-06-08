# **Django Rest Framework** 
**Reference Book** [Django For APIS](https://djangoforapis.com/) [William S. Vincent] 





**API replaces the monolithic architechture!**

![monolith_micro_arvh](https://user-images.githubusercontent.com/41924102/172501077-704785b8-f17b-4fc2-a04b-b5d728715a8d.png)

![ms-monolithic](https://user-images.githubusercontent.com/41924102/172501083-3dd29e11-1ad4-4f2e-90f5-bb6d8b5b308e.png)

REpresentational State Transfer (REST) is an architecture first proposed by Roy Fielding in 2000. Every RESTful API:
* is stateless, like HTTP
* supports common HTTP verbs (GET, POST, PUT, DELETE, etc.)
* returns data in either JSON or XML format

Three main steps to transform database mdels into RESTful API:
* urls.py file for the URL routes
* serializers.py file to transform the data into JSON
* views.py file to apply logic to each API endpoint

# Book API [chapter 2]
![book_api](https://user-images.githubusercontent.com/41924102/172057808-775f7190-d5f6-423a-8d6f-c34a3eab7caa.jpg)

# ToDo API [chapter 3, 4]
![To_Do_API](https://user-images.githubusercontent.com/41924102/172057805-deecfbfa-ea2e-4d7d-9520-cfd7dcaf4b6d.jpg)

# Blog API [chapter 5]
![Blog_Api_1](https://user-images.githubusercontent.com/41924102/172057810-aacb3a6d-fc10-4478-9ffe-cd89cf599d2f.jpg)
![Blog_Api_2](https://user-images.githubusercontent.com/41924102/172057809-c687b697-75ed-402e-a423-84dc0d063acd.jpg)

# 6. Permissions

Permissions or restrictions allows authorized user to use the API. Permissions can be applied at a project level, view level and any individual model level.

* **View Level Permissions:** Allows user to have specific permission to view
  
  ![permisions](https://user-images.githubusercontent.com/41924102/172502538-ae97344e-8e07-4e6c-a9e5-aa2d25669b5a.jpg)

* **Project Level Permissions:** Allows strict permission at the project level and loosen it as needed at the view level.
    
    * AllowAny - any user, authenticated or not has full access
    * IsAuthenticated - only authenticated, registered users have access
    * IsAdminUser - only admin/superusers have access
    * IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only authenticated users have write, edit or delete privileges. The following figure shows no edit/delete access for unauthenticated users but have view access.
  
  ![image](https://user-images.githubusercontent.com/41924102/172503650-5f4574b1-3dbc-4aa4-be28-8952b140f7ed.png)
 
 # 7. User Authentication
 Authentication allows identifying the registered users to log in and use the API. Having a Stateless protocol there's no way to remeber if a user is authenticated from one request to the next. Django REST Framework ships with four different built-in authentication options: basic, session, token and default. There have third party packages also like JSON Web Token (JWTs)
 
 * **Basic Authentication:** When a client makes an HTTP request, it is forced to send an approved authentication credential before access is granted.
  
   ![image](https://user-images.githubusercontent.com/41924102/172504359-1465d478-fc8e-4872-8601-e6fea4a94413.png)
    
    * _Advantages:_ 
     1. Simplicity
    * _Drawbacks:_
     1. every single request the server must look up and verify the username and password, which is inefficient 
     2.  user credentials are being passed in clear text—not encrypted at all—over the internet. This is incredibly insecure.
  
  * **Session Authentication:** This is a stateful approach because a record must be kept on both client and server. Here when the user enters their log in credentials the server verifies the credentials and generates a session object which is then stored in the database. Then the server sends a session_ID whic is stored as as cookie. All future request will incude that session_ID as an HTTP header and thus can be verified easily.
    * _Advantages:_
     1. It is more secure since User Credentials are only sent once.
     2. It is also more efficient since the server does not have to verify the user's credentials each time.
    * _Drawbacks:_
     1. session_ID is only valid within the browser so, it will not work across multiple domains.
     2. Session object must kept up-to-date which can be challenging in large sites with multiple servers 
     3. cookie is sent out for every single request, even those that don't require authentication, which is inefficient.
    
  * **Token Authentication:** Token-based authentication is stateless: once a client sends the initial user credentials to the server, a unique token is generated and then stored by the client as either a cookie or in local storage79. This token is then passed in the header of each incoming HTTP request and the server uses it to verify that a user is authenticated
   
    ![image](https://user-images.githubusercontent.com/41924102/172505468-17e0b96b-7663-46a9-9f70-66c7b93a72cf.png)
   
    * Advantages:  
     1.  Since tokens are stored on the client, scaling theservers to maintain up-to-date session objects is no longer an issue.
     2. tokens can be shared amongst multiple front-ends: the same token can represent a user on the website and the same user on a mobile app. The same session ID can not be shared amongst different front-ends, amajor limitation.
   
    * Drawbacks:
     1. tokens can grow quite large. A token contains all user information,not just an id as with a session id/session object set up. Since the token is sent on every request, managing its size can become a performance issue.
     2. Django REST Framework built-in TokenAuthentication is deliberately quite basic. As a result, it does not support setting tokens to expire. It also only generates one token per user. Third party JSON Web Tokens (JWTs) resolves this issues.
     
 * **Default Authentication:** Default Authentication uses both the basic and session authentication in django REST Framework.  Sessions are used to power the Browsable API and the ability to log in and log out of it. BasicAuthentication is used to pass the session ID in the HTTP headers for the API itself.



For adding log-in, log-out and password reset endpoints we've used 3rd party 'dj-rest-package' and for user registration endpoint we use the 'django-allauth' package. 

  ![image](https://user-images.githubusercontent.com/41924102/172506357-38ac7d8d-52a8-4397-aaf3-dc5640d2b3a4.png)

# 8. Viewsets and Routers

A viewset is a way to combine the logic for multiple related views into a single class

  ![image](https://user-images.githubusercontent.com/41924102/172506600-280b59c2-03c9-469f-a8c7-3f92e9bef487.png)

Routers work directly with viewsets to automatically generate URL patterns for us

  ![image](https://user-images.githubusercontent.com/41924102/172506715-7936c716-a99a-4639-8efd-236e69585cfd.png)

# 9. Schemas and Documentation

A schema is a machine-readable document that outlines all available API endpoints, URLs, and the HTTP verbs (GET, POST, PUT, DELETE, etc.) they support. A schema can be static or dynamic

  ![image](https://user-images.githubusercontent.com/41924102/172507107-962f6932-46cd-437a-964b-ee95d404f5c0.png)


Documentation provides the schema in a human readable format for the felloe developerse to understand. Three popular approaches are: SwaggerUI, ReDoc and the third party drf-yasg. 

  ![image](https://user-images.githubusercontent.com/41924102/172507148-801376a7-daa2-4e52-8c46-1cd643301142.png)


 
