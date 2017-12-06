

```python
from IPython.display import YouTubeVideo

YouTubeVideo("1fEf7T9fGB4")
```





        <iframe
            width="400"
            height="300"
            src="https://www.youtube.com/embed/1fEf7T9fGB4"
            frameborder="0"
            allowfullscreen
        ></iframe>
        



#Model View Controller Architecture
[This is largely drawn from Wikipedia](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

* MVC is a General Principle of User Interface design and is not specific to web applications.
* The general idea is breaking your program into three parts
    * Model
    * View
    * Controller
    

![MVC](http://upload.wikimedia.org/wikipedia/commons/f/fd/MVC-Process.png)

## MVC: Model

* The **model** is the domain problem your program is addressing. What data are you interested in? How are you representing it.
* In Web applications, like Flask, you think of your model in terms of **classes and database tables**
    * A class corresponds to a table in the database
    * An attribute of the class corresponds to a column in the table

## MVC: View

* The **view** is how we present information (e.g. models) to the user.
    * You want to keep logic out of the view.
    * In web applications, the view is the web page
        * We'll use **templates** to create dynamic HTML pages (pages where values are chaned based on the state of the program)
        

## MVC: Controller

* The controller is the logic of the program function.
* The controller asks and answers questions about how the model is modified based on input from the user. It also controls the flow of the program.
    * If the user enters value $Y$, display page $a$ otherwise display page $b$

## Resources
* [Model View Controller tutorial](https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/)


```python

```
