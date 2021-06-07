# sale_report

A sale data report generator application with Django 3.1.

---
## *Screenshots of the app*
> All of the web pages are login required

### Home Page
in the home page you can use the search form to find the datas between a certain date and then visulize it with the type of chart you want(Bar chart-Line chart-Pie Chart)
, and the set the "Results By" field to get the results by transaction or their sale's date.
![](images/home-1.png)


Then You can see the data frames according to your search and the selected chart, Then you can Add a report with the given Data.
![](images/home-2.png)


You can add a report based on your given chart.

![](images/add-report.png)

---
### Sales Page
In the sales page you can see all the sale objects list.

![](images/sales-list.png)

Sale objects Detail

![](images/sale-example.png)

---
### Add from file
You can drag and drop your csv files to read the data from them and then add them to the database.

*Drag and drop implemented by dropzone.js*

![](images/from-file.png)

---
### Reports
In reports page you can see all of the created reports and you can see every report's detail and you can generate a pdf for the desired report.

![](images/reports.png)

reports detail page

![](images/reports-detail.png)

generating pdf for reports

![](images/reports-pdf.png)

---
### Profile
You can edit and update your profile in this page.

![](images/profile.png)


---
## Libraries i used for this Django project:
| Name | Description |
| ----------- | ----------- |
| pandas | Dataframe creation |
| Matplotlib | Chart Implementation |
| PyPDF2 | pdf toolkit(creating pdf,...) |
| xhtml2pdf | HTML to PDF converter |
