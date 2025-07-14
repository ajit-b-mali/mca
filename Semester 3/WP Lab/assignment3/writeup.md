### **Assignment 3: Web Programming (WP)**

**Title: JavaScript Form Validation for Patient Master Form**

---

#### **1. Objective**

To create and validate a Patient Master form using JavaScript, ensuring user input follows proper data entry rules for accurate and reliable data collection.

---

#### **2. Introduction**

JavaScript is a powerful client-side scripting language used to add interactivity and logic to web pages. One of its most common uses is **form validation**—checking user input before it is submitted to the server.

Proper form validation enhances user experience, improves data quality, reduces server-side errors, and prevents security vulnerabilities. This assignment focuses on building a Patient Master form and validating each field using JavaScript based on predefined rules.

The form includes fields such as Patient ID, Name, Address, City, Contact Number, and Date of Birth. Each field must follow specific constraints (e.g., required format, character limits, data types). JavaScript allows real-time validation, giving immediate feedback to users.

---

#### **3. Materials and Methods**

**Tools/Technologies Used:**

* HTML (for form structure)
* JavaScript (for validation logic)
* Web browser (for testing)

**Methods:**

* Create an HTML form with labeled input fields.
* Use JavaScript functions to check the validity of each field.
* Display error messages for incorrect inputs.
* Use event handling (`onsubmit`, `onblur`, etc.) to trigger validation.

**Validation Criteria:**

* **Patient ID**: Must be alphanumeric and non-empty.
* **Patient Name**: Must contain only letters and be non-empty.
* **Address**: Cannot be empty.
* **City**: Must contain only letters and be selected/entered.
* **Contact Number**: Must be exactly 10 digits.
* **Date of Birth**: Must not be empty and must be a valid past date.

---

#### **4. Procedure**

**Step-by-step Algorithm:**

1. Start by creating an HTML form with appropriate labels and input fields for:

   * Patient ID
   * Patient Name
   * Address
   * City
   * Contact Number
   * Date of Birth

2. Write JavaScript functions to:

   * Check for empty fields.
   * Use regular expressions to match valid patterns (e.g., digits for phone numbers, letters for names).
   * Ensure the date of birth is not in the future.
   * Display alerts or inline error messages if validation fails.

3. Link the validation functions to form events (e.g., `onsubmit`, `onblur`).

4. Test each field by providing both valid and invalid input.

---

#### **5. Results**

**Observation:**

* The form prevents submission until all fields are correctly filled.
* Users are notified of specific input errors through custom messages.
* Real-time feedback improves user experience.

**Outcome:**
The Patient Master form functions correctly with JavaScript-based validation. All fields enforce the required rules and enhance data reliability before submission.

