**List Menu**
----
  Returns list of menu as json data.

* **URL**

  /menu/list/

* **Method:**

  `GET`
  
*  **URL Params**

   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** None

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/menu/list/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**Create Menu**
----
  Create a menu using json data.

* **URL**

  /menu/create/

* **Method:**

  `POST`
  
*  **URL Params**

   None

* **Data Params**

  * **name:** 'menu1' <br />
    **code:** 'm001'

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** {'name': 'menu1', 'code': 'm001' }
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** None

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/menu/create/",
      dataType: "json",
      type : "POST",
      data: {'name': 'menu1', 'code': 'm001'},
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
 **Get Menu**
----
  Get details of a menu as json data.

* **URL**

  /menu/1/

* **Method:**

  `GET`
  
*  **URL Params**

   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** {'name': 'menu1', 'code': 'm001' }
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** None

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/menu/1/",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
 **Update Menu**
----
  Update a menu using json data.

* **URL**

  /menu/1/update/

* **Method:**

  `PUT`
  
*  **URL Params**

   None

* **Data Params**

  * **name:** 'menu2' <br />
    **code:** 'm001'

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** {'name': 'menu2', 'code': 'm001' }
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** None

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/menu/1/update/",
      dataType: "json",
      type : "PUT",
      data: {'name': 'menu2', 'code': 'm001'},
      success : function(r) {
        console.log(r);
      }
    });
  ```
  
**Delete Menu**
----
  Delete a menu.

* **URL**

  /menu/1/delete/

* **Method:**

  `DELETE`
  
*  **URL Params**

   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** None

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/menu/1/delete/",
      dataType: "json",
      type : "DELETE",
      success : function(r) {
        console.log(r);
      }
    });
  ```