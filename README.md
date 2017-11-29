
# Introduction to Computer Programming for Biomedical Data Science
## BMI 6018/MDCRC 6521

## Instructors                                   
* Brian E. Chapman, Ph.D.: <brian.chapman@utah.edu>
* Nick Consiglio (TA): <nick.consiglio@utah.edu>

## Prerequisite

A basic programming course, such as [codecademy’s Python Course](https://www.codecademy.com/learn/learn-python)

## Course Description

This course will provide students in the biological and medical domains the foundational programming skills to create computer programs to manage and analyze data drawn from clinical, biological, and public health domains. Working with the Python programming language, students will learn how to write procedural and object oriented programs. Mathematical principles relevant to biomedical data science will be reviewed through programming examples and problems. Students will also develop competency in using software version control with git as well as how to work within Linux environments.

## Text Books

### Programming

There is no required textbook for this course. However, I will make a PDF copy of Allen Downey's *Think Python, version 2* available through Canvas. This is book with a Creative Commons license, so if you are interested you can [clone](https://github.com/AllenDowney/ThinkPython2), edit, and build your own copy of the book. For relevant modules, I will provide references to readings in Downey's book.

In addition there are a number of very useful books that are available online through the University of Utah's subscription to the [Safari Technical Books Online](http://proquest.safaribooksonline.com.ezproxy.lib.utah.edu/).

### Mathematics

As part of this class we will be reviewing some foundational mathematics as they related to computational issues in biomedical informatics. Some of the mathematics books that I will be drawing materials from include:

* [Doing Math with Python](https://www.nostarch.com/doingmathwithpython)
* [Mathematics for the Life Sciences](http://www.springer.com/us/book/9781461472759)
* [Mathematics in the Real World](http://www.springer.com/us/book/9781461485285)

##  Learning Objectives

Upon completing this course students will be able to:

1. Use basic mathematical principles (e.g. set theory, first order logic, calculus, linear algebra, probability, and graph theory) to motivate and inform computational problems in biology and healthcare.

1. Follow software engineering principles such as version control, documentation, and testing while developing biomedical software.
1. Develop biomedical software applications in the Python programming language.
1. Develop pipelines for manipulating, analyzing, and visualizing biomedical data.

## Evaluation Methods

1. Quizzes: 15% of grade
1. Class Participation: 15% of grade
    1. I will not keep attendance, but I do expect reasonable attendance and participation with in-class activities, peer review of assignments, etc.
1. Homework Assignments: 40%
1. Term Project: 30%

**No tests will be given**

##  Teaching and Learning Methods                 

This class will follow a “flipped classroom” paradigm. Students will be expected to watch prepared videos and read relevant on-line materials prior to the start of class. Class time will be spent answering questions raised by on-line materials, clarifying topics, and participating in individual and group hands-on activities. Students are encouraged to work in groups.

## Writing

While this course does not include a formal written component, students are required to write documentation for all their code following standard Python conventions.

## Analytical

The analytical component of this course includes review of foundational mathematical concepts that are of importance to biomedical informatics.


## Course Schedule

1. **Crash course**
    1. Working in Linux
    1. Using git
    1. Quick overview of Python

1. **Computational Environments and software engineering**

    1.  **Principles**
        1. Working in the Linux shell
        1. Using Jupyter notebooks
        1. Using git for version control
        1. Terminal editors
        1. Documentation
    1.  **Application:**
        1.  Working within the course framework

1.  **Review of sublanguages (mathematical, computational, medical) and
    their symbols/notation**
    1.  **Principles**
        1.  Common mathematical, computational, and medical symbols (and
            their meaning)

    1.  **Application: Pseudo-code and program design**

1. **Mathematical and Computational Concepts of Numbers**
    1.  **Principles**
        1.  Integer, rational, real, and complex numbers in mathematics
        1. Integer, rational, real, and complex numbers in Python
    1.  **Application: representing biomedical data numerically**

1. **Code Blocks in Python**
    1. **Principles**
        1. If/Else If/Else Blocks
        1. Repeition with For and While Loops
    1. **Applications**
    
1. **Collections**
    1.  **Principles**
        1. Set theory
        1. Strings, lists, tuples, dictionaries, and sets in Python
    1.  **Application:**
        1. Using Python collections to represent laboratory test data
        1. Using sets to analyze biomedical texts
        1. Counting kmers
        1. Dictionaries and ICD-9 codes (MIMIC2)
        
1.  **Functions in Mathematics and Computing**
    1.  **Principles**
        1. Mathematical description of functions
        1. Mutable and immutable function arguments
        1. Functions as arguments to functions
        1. Functions for code-reuse
        1. Recursion
        1. Exceptions
    1.  **Application**
        1. Writing functions to find prime numbers
        1. Computing greatest common denominators
        1. Identifying kmers

1. **Advanced Code Blocks in Python**
    1.  **Principles**
        1. Modules
        1. Packages
        
1. **Calculus and numeric approximations of derivatives**
    1.  **Principles**
        1. Meaning of derivatives
        1. Symbolic differentiation with Sympy
        1. Working with Numpy arrays
            1. Slicing
            1. Vectorized operations
        1. Numerical derivatives of Numpy arrays
        1. Approximation
        1. Optimization
    1.  **Applications:**
        1. Drug delivery timing
        1. QRS identification in ECG signals

1. **Pandas for Data Wrangling and visualization**
    1.  **Principles**
        1. Reading tabular data
        1. Numeric representation standards (locale library)
        1. Working with missing data
        1. Representing dates and times
    1.  **Applications**
        1. Air quality and temporal data
        1. Car accidents and spatial data
        1. Reading lab data
        
1. **Working with Data files**
    1.  **Principles**
        1. Reading and writing data from disk with Python
        1. Data serialization with Pickle
    1.  **Applications**
        1. Parsing radiology report files
        1. Parsing common bioinformatics file formats FASTA, FASTQ
        
1. **Object oriented programming and probability**
    1.  **Principles**
        1. Encapsulation
        1. Polymorphism
        1. Inheritance
        1. Basic principles of counting
        1. Random values

    1.  **Application**
        1. Modeling RGB$\alpha$
        1. Simulating populations of patients

1. **Basic Text Processing with Python**
    1.  **Principles**
        1. Tokenization
        1. Regular expressions
    1.  **Application**
        1. Text de-identification
        1. Extracting gene and protein data
        
1. **Linear Algebra and Text Processing**
    1.  **Principles**
        1. Vectors
        1. Word vectors
        1. Dot products
        1. Vector norms

    1.  **Application**
        1. Cosine similarity of text documents
        1. Rerpesenting sparse vectors with dictionaries
        
1. **Networks, ontologies and graph theory**
    1.  **Principles**
        1. Edges and nodes
        1. Directional graphs
        1. Graph traversal
        1. Shortest paths
    1.  **Applications**
        1. Reasoning with Ontologies
        1. Analyzing Twitter networks
        1. Analyzing collaboration networks with Pubmed data
        
        
1. **Visualization of Biomedical Data**
    1.  **Principles**
        1. Creating graphs with [Matplotlib](https://matplotlib.org/)
        1. Creating graphs with [Holoviews](http://holoviews.org/)

    1.  **Applications:**
        1. Visualizing heart sounds
        1. Visualizaing MIMICII Data

1. **Networks and Probability**
    1.  **Principles**
        1.  Multigraphs
        1. Basic principles of probability
    1.  **Applications**
        1.  Disease transmission in Utah public schools
