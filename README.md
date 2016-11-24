# Algorithm Design Coursework

The purpose of this project is to solve the **fractional knapsack**, **binary knapsack** and the **knapsack with conflict** problem.


### How to run

```
./trabalho <instance_path> <question>
```

where:
* Question **1** is the fractional knapsack problem
* Question **2** is the binary knapsack problem
* Question **3** is the knapsack with conflicts problem


**Example**
```
./trabalho data 1
```


### Instance Format

**Input format**

The input file should be in the following format:

```
NbItems KnapsackSize
<< And then for each item >>
Index Profit Weight [List_Of_Conflict_Items]
```

**Output format**

The output file should be in the following format:

```
NbItemsUsed TotalWeight TotalProfit
<< And then for each item placed in the knapsack >>
ItemIndex FractionOfItem
```

**Some remarks**
* The second field "FractionOfItem" belongs between [0,1]. For the questions 2 and 3, they should always be set to 1 (item cannot be fractioned).

* The instances are common for all three questions.
They include all the information: weight, profit for the items as well as their conflicts  (for question 3).


