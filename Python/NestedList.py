if __name__ == '__main__':
    nestedList = []
    secondLowestGrade = []
    newSecondLowestGrade = []
    
    for i in range(int(input())):
        listI = []
        name = input()
        score = float(input())
        listI.extend((name,score))
        nestedList.append(listI)
        
    nestedList.sort(key = lambda x: x[1])
    # secondLowestGrade.append(nestedList[1][0])
    
    for z in range(1, len(nestedList)):
      if nestedList[z][1] != nestedList[0][1]:
        secondLowestGrade.append(nestedList[z])
        break
    
    for index in range(2, len(nestedList)):
      if secondLowestGrade[0][1] == nestedList[index][1]:
        secondLowestGrade.append(nestedList[index])
        
    for elem in secondLowestGrade:
      if elem not in newSecondLowestGrade:
        newSecondLowestGrade.append(elem)
        
    secondLowestGrade = newSecondLowestGrade
    
    for y in sorted(secondLowestGrade):
        print(y[0])