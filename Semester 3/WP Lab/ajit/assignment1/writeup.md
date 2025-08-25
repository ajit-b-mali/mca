
---

### **Assignment 1: Web Programming (WP)**

**Title: Create a static HTML page that displays the following output using frame**

---

#### **1. Objective**

To design a simple static web page layout using HTML frames for organizing content in a structured and navigable format.

---

#### **2. Introduction**

Web development involves creating web pages using various technologies such as HTML, CSS, JavaScript, and others. HTML (HyperText Markup Language) is the foundational language used to structure content on the web. An older but once widely used feature in HTML was the use of frames, which allowed developers to divide the browser window into multiple sections, each capable of loading separate HTML documents.

Frames help in building interfaces where persistent elements (like navigation menus) remain in place while other sections of the page change content dynamically. Although frames are now deprecated in modern HTML5 standards due to issues with usability, SEO, and responsiveness, understanding them is essential for maintaining legacy systems and grasping the evolution of web design.

This assignment focuses on constructing a static personal profile layout using HTML frames. The layout includes a header, a side navigation bar, and a content area that allows user input, mimicking a basic profile management interface.

---

#### **3. Materials and Methods**

**Materials/Tools Required:**

* HTML (Basic knowledge)
* A text editor (Notepad, VS Code, Sublime Text)
* A web browser (Chrome, Firefox, Edge)

**Methodology:**

* Plan the layout with three sections: Header, Navigation (Sidebar), and Content Area.
* Use the `<frameset>` and `<frame>` elements to split the browser window.
* Link each section to separate HTML files.
* Structure the content logically to reflect a typical profile layout.

**Flowchart of Execution:**

```
Main Webpage (index.html)
│
├── Header Frame: Displays Title (MY WEBSITE & MY PROFILE)
│
├── Sidebar Frame: Navigation links (Home, My Profile)
│
└── Main Content Frame: Profile Input Form (Name, Contact No.)
```

---

#### **4. Procedure**

**Algorithm / Step-by-step Process:**

1. Start by creating a main HTML file to define the frameset layout.
2. Divide the browser window horizontally into two parts: header and body.
3. Further split the body into two vertical frames: left for navigation, right for content.
4. Create a separate HTML file for the header to display the title.
5. Create another HTML file for the navigation menu with links.
6. Create a third HTML file for the main content area with input fields for Name and Contact No.
7. Link all the files correctly within the main frameset.
8. Save all HTML files in the same directory and open the main file in a browser to view the result.

---

#### **5. Results**

**Observation:**

* The page layout successfully divides the screen into three sections.
* The header frame displays "MY WEBSITE" and "MY PROFILE" in a bold format.
* The left frame contains navigable links to "Home" and "My Profile".
* The right frame shows input fields where users can type their Name and Contact No.

**Outcome:**
The desired layout has been accurately implemented using HTML frames. The structure matches the provided reference image and allows basic user interaction through input fields in the profile section.

---