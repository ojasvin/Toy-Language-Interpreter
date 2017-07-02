# Python Interpreter 
* Python Interpreter for a toy language build in Python3 based on concepts of Object Oriented Programming.Both versions have   their own code.imp files to showcase different functionalities.
 
 
* Functionalities added
   * **Version1** 

        * If-Else Statement:
          - **`Condition`** in between **`if`** and **`then`**
          - Statements in between **`then`** and **`fi`**
          - **`fi`** should be followed by a **`;`**
          - **`if-else`** block can be inside another **`if-else`** block or **`while`** loop as well. 
        * While Statement:
          - **`Condition`** in between **`while`** and **`do`**
          - Statements in between **`do`** and **`done`**
          - **`done`** should be followed by a **`;`**
          - Similarly even the **`while`** loop can be inside an **`if-else`** block or another **`while`** loop.
        * Print Statement:
          - Works same as **`python3`** print statement and can print multiple arguments at once as well.
        * Println Statement:
          - **`println`** statement can be used to print a new line character just like in **Java**

   * **Version2**
   
        * Error and Exception Handling:
          - **`Syntax Errors`** such as missing semicolon,missing fi and done at end of if-else block and 
            while loop respectively,printing or evaluation of variables which have not been assigned yet have been
            included.
          - **`Runtime Errors`** such as division by zero have been included using **raise** keyword inside Errors class
