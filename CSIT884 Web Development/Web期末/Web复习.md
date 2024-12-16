Web考试重点
 重点可以参考作业/练习 训练的多的
 四次作业里出现的是重点
 主要考 html css js xml json ajax（练得多的）
 不重点考察只将了一两次课 convas / 

8道题
 3道概念简答题
 5道编程题
 总分60分

 

Web Development

HTML、css、JavaScript 的基础不用说，必须得会

ajax 考的是 display(obj)，不要求完整ajax 代码

animation 考了，在例题难度的基础上加了个暂停按钮和对应操作

xml，dtd，xslt 这次考的简答，不排除下次考代码

html+css 考的巨细无比，常见的那些 style 的名称最好都记住

考了一道类似 ppt 中实现加减乘除运算的题，改成了坐标运算，其中还要会生成随机数

web form 一道，radio、text field、textarea 等都要熟悉，基础的 form validation 要会

DOM 练习没出过，考试也没考

canvas查无此人

client-side storage 考了个简答，local 和 session 存储区别

`localStorage` and `sessionStorage` are two client-side storage mechanisms provided by the Web Storage API. `localStorage` stores data persistently with no expiration date, remaining on the user's device until manually cleared or deleted via JavaScript. In contrast, `sessionStorage` only retains data for the duration of the page session, clearing it once the tab or browser window is closed. `localStorage` allows data sharing across all pages from the same origin, while `sessionStorage` isolates data to the specific browser tab. `localStorage` is ideal for long-term data like user preferences, whereas `sessionStorage` suits temporary data such as shopping cart contents.

卧槽我突然想起来xml和dtd考了代码



 Question 1

Create a good-looking webpage A1-Task1-YourStudentName-YourStudentNumber.html using only HTML (without CSS) to display the following information:

- **Part 1. Personal Information**: Use an <u>unordered list</u> to display your CCNU student number, UOW student number, full name, UOW email address, major, and thesis supervisor.

- **Part 2. Assessment Information**: Use an ordered list to display all assessments of this subject and their due dates. (This information can be found in the Subject Outline on the Moodle site.)

- Part 3. Subject Coordinator Information

  : Use a table with a border to display ALL subject coordinators of ALL the subjects that you are currently taking in this session. (This information can be found in the subject outline of each subject.)

  - There must be table headers: Coordinator Name, Contact Information, Subject Code, Short Description of the Subject.
  - Each coordinator must be displayed in a separate row.
  - Set the vertical alignment of the cells in the first column (Coordinator Name) based on your UOW student number: If the last digit of your UOW student number is odd, i.e., 1, 3, 5, 7, 9, (e.g., for a student number of 612345), set the vertical alignment of the cells in the first column to top. Otherwise, set the vertical alignment of the cells in the first column to bottom.

- Part 4. Your Timetable

  : Use a table with a border to display your own timetable.

  - It must include a table caption with your name and UOW student number.
  - There must be table headers: time, Mon, Tue, Wed, Thu, Fri.
  - Each hour must be displayed in a separate row, starting with row 8:00am - 9:00am and ending with row 7:00pm - 8:00pm.
  - In the table cell where you have a class, write the subject code and class type. For example, if you have a lecture for MATH111 on Monday between 8:00am - 10:00am, then you should merge the two cells for Monday 8:00am - 9:00am and Monday 9:00am - 10:00am and write "MATH111 lecture" in it. (You can omit the 5 or 10 minutes difference while creating the table. For example, if the lecture is between 8:10am - 10:10am, it's considered the same as 8:00am - 10:00am.)
  - Subject code must be in bold.
  - Additionally, if the class is a lecture, you must use a school emoji (before the subject code); if the class is a tutorial, then use a laptop emoji. You can search for the HTML code for the emojis on the Internet.

### Answer 1

```html
<!DOCTYPE html>
<html>

<body>
  <!-- Part 1: Personal Information -->
  <ul>
    <li>CCNU Student Number: [Your CCNU Number]</li>
    <li>UOW Student Number: [Your UOW Number]</li>
    <li>Full Name: [Your Full Name]</li>
    <li>UOW Email Address: [Your UOW Email]</li>
    <li>Major: [Your Major]</li>
    <li>Thesis Supervisor: [Your Supervisor Name]</li>
  </ul>

  <!-- Part 2: Assessment Information -->
  <ol>
    <li>Assessment 1: [Details 1], Due Date: [Date 1]</li>
    <li>Assessment 2: [Details 2], Due Date: [Date 2]</li>
    <!-- Add more assessments as needed -->
  </ol>

  <!-- Part 3: Subject Coordinator Information -->
  <table border="1">
    <tr>
      <th>Coordinator Name</th>
      <th>Contact Information</th>
      <th>Subject Code</th>
      <th>Short Description of the Subject</th>
    </tr>
    <tr>
      <td style="vertical-align: [Set based on UOW number]">Coordinator 1 Name</td>
      <td>Contact 1 Details</td>
      <td>[Subject Code 1]</td>
      <td>Subject 1 Description</td>
    </tr>
    <tr>
      <td style="vertical-align: [Set based on UOW number]">Coordinator 2 Name</td>
      <td>Contact 2 Details</td>
      <td>[Subject Code 2]</td>
      <td>Subject 2 Description</td>
    </tr>
    <!-- Add more coordinators as needed -->
  </table>

  <!-- Part 4: Your Timetable -->
  <table border="1" caption="[Your Name] - [Your UOW Student Number] Timetable">
    <tr>
      <th>time</th>
      <th>Mon</th>
      <th>Tue</th>
      <th>Wed</th>
      <th>Thu</th>
      <th>Fri</th>
    </tr>
    <tr>
      <td>8:00am - 9:00am</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>9:00am - 10:00am</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <!-- Add more rows for each hour -->
    <tr>
      <td>7:00pm - 8:00pm</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </table>
</body>

</html>
```

Replace the placeholders (e.g., [Your CCNU Number], [Your UOW Number], etc.) with your actual information. For emojis, search for the HTML code for the school emoji and laptop emoji and insert them as needed before the subject codes for lecture and tutorial classes respectively.

### Question 2

Create a good-looking webpage A1-Task2-YourStudentName-YourStudentNumber.html using HTML and CSS to display programs and activities for students around UOW campus. To read about these programs and activities, on our subject Moodle site, go to the section "Other Materials", you will see a link "List of programs and activities for students around UOW campus". On the webpage A1-Task2-YourStudentName-YourStudentNumber.html that you created, create a table to display 5 programs/activities of your choice.

- The table must have table headers: Which Students, Program/Activity Name, About.
- The 1st column displays which kind of students that can participate in this program/activity.
- The 2nd column displays the program/activity name with a logo image. You can design your own logo image or you can download a free image from the Internet to use.
- The 3rd column displays a short paragraph describing what this student program/activity is about.
  You must use document CSS with the following CSS properties: font-size, color, background-color, padding, text-align, vertical-align, border-collapse, border-spacing, border-style, border-color, border-width, height (for table cells), width (for table cells).

### Answer 2

### HTML File (A1-Task2-YourStudentName-YourStudentNumber.html)

```html
<!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" href="styles.css">
  <title>UOW Campus Programs and Activities</title>
</head>

<body>
  <table>
    <thead>
      <tr>
        <th>Which Students</th>
        <th>Program/Activity Name</th>
        <th>About</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>All Students</td>
        <td><img src="logo1.jpg" alt="Activity 1 Logo">Activity 1 Name</td>
        <td>This activity focuses on [Short description 1].</td>
      </tr>
      <tr>
        <td>Undergraduate Students</td>
        <td><img src="logo2.jpg" alt="Activity 2 Logo">Activity 2 Name</td>
        <td>It offers [Short description 2] opportunities for undergraduates.</td>
      </tr>
      <tr>
        <td>Graduate Students</td>
        <td><img src="logo3.jpg" alt="Activity 3 Logo">Activity 3 Name</td>
        <td>Designed for graduate students to [Short description 3].</td>
      </tr>
      <tr>
        <td>International Students</td>
        <td><img src="logo4.jpg" alt="Activity 4 Logo">Activity 4 Name</td>
        <td>Helps international students with [Short description 4].</td>
      </tr>
      <tr>
        <td>Students in [Specific Major]</td>
        <td><img src="logo5.jpg" alt="Activity 5 Logo">Activity 5 Name</td>
        <td>Exclusive for [major] students to [Short description 5].</td>
      </tr>
    </tbody>
  </table>
</body>

</html>
```

### CSS File (styles.css)

```css
table {
  font-size: 16px;
  color: #333;
  background-color: #f9f9f9;
  border-collapse: collapse;
  border-spacing: 0;
  border-style: solid;
  border-color: #ccc;
  border-width: 1px;
  text-align: left;
  vertical-align: middle;
}

th,
td {
  padding: 10px;
  height: 50px;
  width: 200px;
}

th {
  background-color: #e0e0e0;
}

td img {
  width: 30px;
  height: 30px;
  margin-right: 10px;
  vertical-align: middle;
}
```

### Explanation

- In the HTML file, the `<link>` tag in the `<head>` section links the external CSS file (`styles.css`) to the HTML document. The table structure is created with appropriate headers and rows to display the student programs and activities information. Each row contains details about the target student group, the activity name with an associated logo image, and a short description.
- The CSS file defines the visual style of the table. The `table` selector sets properties like font size, text color, background color, and border style. The `th, td` selector styles the table cells, including padding and size. The `th` selector further customizes the header cells' background. The `td img` selector is used to style the images within the table cells, specifying their size, margin, and vertical alignment.

Remember to replace the `src` values of the `img` tags with the actual paths to your logo images and fill in the short descriptions accurately for each activity.