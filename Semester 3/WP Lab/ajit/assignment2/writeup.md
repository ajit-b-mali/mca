### **Assignment 2: Web Programming (WP)**

**Title: Design external CSS and link it in the HTML file**

---

#### **1. Objective**

To apply external CSS styling to an HTML document to control and enhance the presentation of headings and paragraph text using linked style rules.

---

#### **2. Introduction**

Cascading Style Sheets (CSS) is a stylesheet language used to describe the visual presentation of web documents written in HTML. By separating structure (HTML) from style (CSS), web developers achieve cleaner, reusable, and more manageable code.

There are three main ways to apply CSS: inline, internal (embedded in `<style>` tags), and external (linked through a separate `.css` file). Among these, **external CSS** is the most efficient and maintainable method, especially when working on multi-page websites, as a single CSS file can be applied across all pages.

In this assignment, the focus is on creating an external CSS file to apply specific styling rules—such as setting font size, text color, and heading appearance—and linking this CSS file to an HTML document to observe the effects.

---

#### **3. Materials and Methods**

**Tools/Materials Required:**

* HTML and CSS (basic understanding)
* Text editor (e.g., Notepad, VS Code)
* Web browser (e.g., Chrome, Firefox)

**Methods Used:**

* Create a basic HTML file with headings and a paragraph.
* Create an external CSS file to define the required styles.
* Use the `<link>` element to associate the CSS file with the HTML file.

**Style Rules to Implement:**

* Define a heading section in HTML (e.g., `<h1>`).
* Set the paragraph text font size to 13 pixels.
* Set all text color to blue.
* Override the heading text color to green for distinction.

---

#### **4. Procedure**

**Algorithm / Step-by-step Process:**

1. Open a text editor and create an HTML file.
2. Write a simple structure that includes a heading and a paragraph.
3. Create a separate CSS file with the `.css` extension.
4. Define a CSS rule to style the heading with green text.
5. Define another rule to make the paragraph font size 13 pixels.
6. Set a general rule to apply blue color to all text elements.
7. Use the `<link>` tag in the HTML `<head>` section to connect the external CSS file.
8. Save both files in the same directory.
9. Open the HTML file in a web browser to verify the applied styles.

---

#### **5. Results**

**Observation:**

* The heading text appears in green color, overriding the general blue color rule.
* The paragraph text is displayed with a font size of 13 pixels.
* All other text inherits the blue color as expected from the general styling rule.

**Outcome:**
The CSS rules were successfully applied using an external stylesheet. The layout demonstrates proper styling separation from the HTML content, validating the use of external CSS for scalable and maintainable web design.

---
