print("Finding Inverse of a Matrix\n")

# Get matrix size
matrixSize = 0

while (True):
    matrixSize = input("Enter size of Square Matrix: ")

    if (matrixSize.isdigit()):
        break

    print("Please Enter +ve integers only")

matrixSize = int(matrixSize)

# Get matrix values
matrix = []
row = []

for r in range(matrixSize):
    print(f"\nEnter values of row {r+1}: ")
    row.clear()
    for c in range(matrixSize):
        val = 0
        isFloat = False
        while (isFloat is False):
            val = input(f"Enter v{r+1}{c+1}: ")
            try:
                val = float(val)
                isFloat = True
            except ValueError:
                print("Please Enter numbers only")

        row.append(val)

    matrix.append(list(row))

# Get Matrix Inverse (Matrix * InverseOfMatrix = Identity Matrix)
Inverse = []
if (matrixSize == 1):
    if (matrix[0][0] == 0):
        print("\nMatrix has No Inverse\n")
    else:
        Inverse.append(1/matrix[0][0])
        print('\nThe Inverse Matrix')
        print(Inverse)
        print('\n')
elif (matrixSize == 2):
    determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    if (determinant == 0):
        print("\nMatrix has No Inverse\n")
    else:
        n = 1/determinant
        Inverse = [[n*matrix[1][1], n*-1*matrix[0][1]],
                   [n*-1*matrix[1][0], n*matrix[0][0]]]
        print('\nThe Inverse Matrix')
        for r in Inverse:
            print(r)
        print('\n')
else:
    Identity = []
    row = []
    for r in range(matrixSize):
        row.clear()
        for c in range(matrixSize):
            if (r == c):
                row.append(1.0)
            else:
                row.append(0.0)

        Identity.append(list(row))

    # Create a Full Matrix containing all elements of our Matrix and Identity
    fullMatrix = []
    for i in range(matrixSize):
        row.clear()
        row.extend(matrix[i])
        row.extend(Identity[i])

        fullMatrix.append(list(row))

    # Convert Full Matrix -> Reduced Row Echelon Form
    for level in range(len(fullMatrix)):
        currentRow = -1
        for c in range(len(fullMatrix[0])):
            for r in range(level, len(fullMatrix)):
                if (fullMatrix[r][c] != 0):
                    currentRow = r
                    break

            if (currentRow != -1):
                fullMatrix[level], fullMatrix[currentRow] = fullMatrix[currentRow], fullMatrix[level]

                if (fullMatrix[level][c] != 1):
                    divisor = fullMatrix[level][c]
                    for i in range(len(fullMatrix[level])):
                        fullMatrix[level][i] = fullMatrix[level][i] / divisor

                for i in range(len(fullMatrix)):

                    if (fullMatrix[i][c] == 0 or i == level):
                        continue

                    numOfMultiply = fullMatrix[i][c] * -1

                    for j in range(len(fullMatrix[0])):
                        fullMatrix[i][j] = (
                            fullMatrix[level][j] * numOfMultiply) + fullMatrix[i][j]

                break

    Identity2 = []
    for r in fullMatrix:
        Identity2.append(r[:matrixSize])
        Inverse.append(r[matrixSize:])

    if (Identity != Identity2):
        print("\nMatrix has No Inverse\n")
    else:
        print('\nThe Inverse Matrix')
        for r in Inverse:
            print(r)
        print('\n')
