print("Solving Linear System using Augmented Matrix and \"Gauss Jordan Elimination\"\n")

# Get the Linear equations' "Coefficients and Value"
print("Enter number of rows and columns")

rows = 0
columns = 0
while (True):
    rows = input("Enter rows: ")
    columns = input("Enter columns: ")

    if (rows.isdigit() and columns.isdigit()):
        break

    print("Please Enter +ve integers only")

rows = int(rows)
columns = int(columns)
augmentedMatrix = []
linearEq = []
for r in range(1, rows+1):
    print(f"\nEnter values of linear equation {r}: ")
    linearEq.clear()
    for c in range(1, columns+1):
        val = 0
        isFloat = False
        while (isFloat is False):
            val = input(f"Enter v{r}{c}: ")
            try:
                val = float(val)
                isFloat = True
            except ValueError:
                print("Please Enter numbers only")

        linearEq.append(val)

    augmentedMatrix.append(list(linearEq))

print('\n')
for r in augmentedMatrix:
    print(r)
print('\n')

# Convert Augmented Matrix -> Reduced Row-Echelon Form
for level in range(0, len(augmentedMatrix)):
    currentRow = -1
    for c in range(0, len(augmentedMatrix[0])-1):
        for r in range(level, len(augmentedMatrix)):
            if (augmentedMatrix[r][c] != 0):
                currentRow = r
                break

        if (currentRow != -1):
            augmentedMatrix[level], augmentedMatrix[currentRow] = augmentedMatrix[currentRow], augmentedMatrix[level]

            print('\n')
            for r in augmentedMatrix:
                print(r)
            print('\n')

            if (augmentedMatrix[level][c] != 1):
                divisor = augmentedMatrix[level][c]
                for i in range(0, len(augmentedMatrix[level])):
                    augmentedMatrix[level][i] = augmentedMatrix[level][i] / divisor

            for i in range(0, len(augmentedMatrix)):

                if (augmentedMatrix[i][c] == 0 or i == level):
                    continue

                numOfMultiply = augmentedMatrix[i][c] * -1

                for j in range(0, len(augmentedMatrix[0])):
                    augmentedMatrix[i][j] = (augmentedMatrix[level][j] * numOfMultiply) + augmentedMatrix[i][j]

            print('\n')
            for r in augmentedMatrix:
                print(r)
            print('\n')

            break


# Check solutions of our Reduced Row-Echelon Matrix
if (augmentedMatrix[rows-1][columns-2] == 0 and augmentedMatrix[rows-1][columns-1] == 0):
    print("Linear System has Infinite Solutions")
elif (augmentedMatrix[rows-1][columns-2] == 0 and augmentedMatrix[rows-1][columns-1] != 0):
    print("Linear System has No Solutions")
else:
    print("The results are")
    for r in range(0, len(augmentedMatrix)):
        eq = ""
        eq = "X" + str(r+1)

        n = augmentedMatrix[r][-1]
        if (int(n) == float(n)):
            eq = eq + " = " + str(int(n))
        else:
            eq = eq + " = " + str(n)

        print(eq)
