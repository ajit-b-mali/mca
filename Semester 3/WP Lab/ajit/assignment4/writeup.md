### **Assignment 4: Web Programming (WP)**

**Title: Create a Bootstrap Grid with 50% Split on Small, Medium, and Large Devices**

---

#### **1. Objective**

To design a responsive grid layout using Bootstrap that evenly splits content into two columns (50% width each) across small, medium, and large screen sizes.

---

#### **2. Introduction**

Bootstrap is a powerful front-end framework widely used for developing responsive and mobile-first websites. One of its core features is a **flexible grid system** based on a 12-column layout, which enables developers to control how content is displayed across various screen sizes.

Responsiveness ensures that websites adapt their layout dynamically depending on the device's screen width—be it a mobile, tablet, or desktop. The grid system uses classes like `.col-sm-*`, `.col-md-*`, and `.col-lg-*` to define how much space an element should occupy at different breakpoints.

In this assignment, we focus on creating a two-column grid layout that divides the screen 50%–50% at **small**, **medium**, and **large** device sizes using Bootstrap’s built-in grid classes.

---

#### **3. Materials and Methods**

**Tools/Technologies Used:**

* Bootstrap CSS framework (version 4 or 5)
* HTML
* Web browser for preview

**Methodology:**

* Use a `<div>` container to define the layout boundaries.
* Inside the container, use Bootstrap’s `.row` class to create a horizontal group.
* Add two columns using `.col-sm-6`, `.col-md-6`, `.col-lg-6` to specify that each column should take 6 of the 12 grid units (50%) on all screen sizes.
* Add content to each column for demonstration.

**Responsive Grid Behavior:**

* **Small Devices (≥576px)**: 2 columns, each 50%
* **Medium Devices (≥768px)**: 2 columns, each 50%
* **Large Devices (≥992px)**: 2 columns, each 50%

---

#### **4. Procedure**

**Step-by-step Algorithm:**

1. Include the Bootstrap CSS via CDN in the `<head>` section of your HTML file.
2. Create a `<div>` element with the class `container` to hold the grid layout.
3. Inside the container, create a `row` using `<div class="row">`.
4. Add two column `<div>`s inside the row:

   * Assign each column the classes `.col-sm-6`, `.col-md-6`, and `.col-lg-6`.
   * This ensures a 50% width split at all target screen sizes.
5. Add content such as text or boxes to visually represent the columns.
6. Save the file and open it in a web browser to test the responsiveness.

---

#### **5. Results**

**Observation:**

* The two columns appear side by side with equal width across small, medium, and large screen sizes.
* On extra small screens (less than 576px), the columns automatically stack vertically as Bootstrap defaults to 100% width when no specific class is applied.

**Outcome:**
A fully responsive 50%-50% split layout has been successfully created using Bootstrap’s grid system. It adapts seamlessly to various screen widths, fulfilling the requirements of modern responsive web design.