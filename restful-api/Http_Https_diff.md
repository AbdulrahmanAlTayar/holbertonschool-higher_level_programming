# HTTP/HTTPS explanation

## Introduction
The web relies on **HTTP** and **HTTPS** as the backbone of communication between browsers (clients) and servers.  
While both share the same foundation, their **security** is what makes the real difference.

---

## HTTP vs HTTPS

### HTTP (Hypertext Transfer Protocol)
- Basic protocol for data transfer
- Data is sent **as plain text**
- Vulnerable to spying, modification, and interception
- Default port: **80**

### HTTPS (HTTP Secure)
- Secure extension of HTTP using **SSL/TLS encryption**
- Encrypts all transmitted data
- Protects against **man-in-the-middle** attacks
- Default port: **443**
- Used for **sensitive transactions** (banking, logins, payments)

👉 **Summary:** HTTP = open channel, HTTPS = locked channel.

---

## HTTP Request/Response Flow

Here’s how a browser talks to a server:

```text
Client (Browser) ---> [HTTP Request] ---> Server
Client (Browser) <--- [HTTP Response] <--- Server
```

### Example of a Request
```
METHOD /path HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Content-Type: application/json

{request body}
```

### Example of a Response
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123

{response body}
```

---

## Common HTTP Methods

Here are some everyday actions the client can take:

1. **GET** – Ask the server for information  
   - Use case: Load a webpage or fetch user profile  
   - Example: `GET /users/123`

2. **POST** – Send new data to the server  
   - Use case: Submit a form or create a new record  
   - Example: `POST /users` with JSON data

3. **PUT** – Replace an existing resource  
   - Use case: Update a user’s entire profile  
   - Example: `PUT /users/123`

4. **DELETE** – Remove a resource  
   - Use case: Delete a blog post or user account  
   - Example: `DELETE /users/123`

---

## Common HTTP Status Codes

When the server answers, it uses a status code to tell us the result:

1. **200 OK** – Everything worked fine  
   - Example: Page loaded successfully  

2. **401 Unauthorized** – Login required  
   - Example: Accessing a protected API without a token  

3. **403 Forbidden** – You’re logged in, but not allowed  
   - Example: Normal user tries to reach admin panel  

4. **404 Not Found** – Resource doesn’t exist  
   - Example: Visiting a deleted or mistyped URL  

5. **500 Internal Server Error** – Problem on the server side  
   - Example: Database crash or unexpected bug  

