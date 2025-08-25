### **Assignment 9: Web Programming (WP)**

**Title: Retrieve the Value of a Textbox Using jQuery**

---

#### **1. Objective**

To demonstrate how to access and retrieve the value entered in a textbox using the jQuery library.

---

#### **2. Introduction**

jQuery is a fast, small, and feature-rich JavaScript library that simplifies HTML DOM tree traversal, event handling, animation, and Ajax interactions. One common use of jQuery is interacting with form elements to gather input values without writing verbose JavaScript code.

Textbox elements (`<input type="text">`) are widely used in web forms to collect user input such as names, emails, and other data. Using jQuery, developers can easily retrieve these values by targeting the element and calling the `.val()` method.

This assignment focuses on how to retrieve and display the value of a textbox using a jQuery function triggered by a button click.

---

#### **3. Materials and Methods**

**Tools/Technologies Required:**

* HTML
* jQuery Library (linked via CDN)
* Text Editor (e.g., VS Code, Notepad++)
* Web Browser (e.g., Chrome, Firefox)

**Methodology:**

* Create a simple HTML form with a textbox and a button.
* Include the jQuery library via CDN in the HTML file.
* Write a jQuery function that captures the click event of the button.
* Use the `.val()` method to get the value from the textbox and display it.

**Key Concepts:**

* DOM manipulation using jQuery
* Event handling with `click()`
* Value retrieval using `.val()`

---

#### **4. Procedure**

**Step-by-step Algorithm:**

1. Create a basic HTML structure with:

   * A textbox for user input
   * A button labeled "Get Value"
   * A paragraph or `div` to display the result

2. Link the jQuery library in the `<head>` section using a CDN.

3. Write a jQuery function that:

   * Listens for the `click` event on the button
   * Retrieves the value from the textbox using `.val()`
   * Displays the value in the result area using `.text()` or `.html()`

4. Save and open the HTML file in a web browser.

5. Enter text into the textbox and click the button to see the retrieved value.

---

#### **5. Results**

**Observation:**

* When the user enters text and clicks the button, the typed value is successfully displayed on the web page.
* The textbox value is accessed in real-time without refreshing the page.

**Outcome:**
The program demonstrates the use of jQuery to retrieve input from a textbox, fulfilling the objective of dynamic user interaction through simple and effective DOM manipulation.
