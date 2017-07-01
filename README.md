# Interpreter
Build on python :blush:
* This interpreter is based on Python Object Oriented Programming. 
  The **`eval`** method in the above interpreter works similar to python **`eval`** method and evaluates the parsed tree/structure of the code.
* Basic **toy language** which is parsed and interpreted using **python3** is as follows:
```
n:=2;
while n>0 do
	a:=n*2+1;
	while a>0 do
		print("yo ",a);
		println();
		a:=a-1;
	done;
	n:=n-1;
done;
if a==1 then
	println("Machaya");
else
	println("Kuch nhi machaya");
fi;	

 
```
  * Each assignment statement should use `:=` for assignment and contains `;` for termination.
  * If-Else Statement:
    - **`Condition`** in between **`if`** and **`then`**
    - Statements in between **`then`** and **`fi`**
    - **`fi`** should be followed by a **`;`**
  * While Statement:
    - **`Condition`** in between **`while`** and **`do`**
    - Statements in between **`do`** and **`done`**
    - **`done`** should be followed by a **`;`**
  * Print Statement:
    - Works same as **`python`** print statement and can print multiple arguments at once.
  * Println Statement:
    - **`println`** statement can be used to print a new line character just like in **Java**
    
