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