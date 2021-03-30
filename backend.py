from typing import NoReturn, List, Dict, Union
from functools import reduce
from operator import add
from os import startfile, remove, listdir

class GradeCalcultor():
    def __init__(self, lineEdit: object, tickBox: object, listWidget: object, label1: object, label2: object, label3: object) -> None:
        self.lineEdit: object = lineEdit
        self.tickBox: object = tickBox
        self.listWidget: object = listWidget
        self.label1: object = label1
        self.label2: object = label2
        self.label3: object = label3
        self.pointList: List[float] = []
        self.gradeList: List[int] = []
        self.gradeDict: Dict[int, float] = {15: 1.0, 14: 1.0, 13: 1.3, 12: 1.7, 11: 2.0, 10: 2.3, 9: 2.7, 8: 3.0, 7: 3.3, 6: 3.7, 5: 4.0, 4: 4.3, 3: 4.6, 2: 5.0, 1: 5.3, 0: 6.0}
       
    def getGradeInput(self) -> Union[int, NoReturn]:
        gradeInput: str = self.lineEdit.text()

        if len(gradeInput) != 0:
            return int(gradeInput)

    def getTickBox(self) -> bool:
        mode: bool = self.tickBox.isChecked()

        return mode
    
    def changeLabelText(self, pointAverage: float, points: float, gradeAverage: float, mode: bool, ) -> NoReturn:
        textMode: str = '(LK)' if mode else ''

        self.label1.setText(f'Eingegebener Punkt: {points}{textMode}')
        self.label2.setText(f'Punktedurchschnitt: {round(float(str(pointAverage)[0:4]), 1)}')
        self.label3.setText(f'Notendurchschnitt: {round(float(str(gradeAverage)[0:4]), 1)}')
        self.addPointsToList(points, mode)
    
    def calculateAverage(self, point: float, list: List[Union[int, float]], mode: bool) -> float:
        addedUpPoints: Union[int, float] = 0
       
        if mode and len(list) == 0:
            list.append(point)
        
        if mode:
            list += [point] * 2
            
        else:
            list.append(point)

        gradeAmount: int = len(list)
        
        for point in list:
            addedUpPoints += point

        pointAverage: float = addedUpPoints / gradeAmount

        if pointAverage > 15.0:
            pointAverage: float = 15.0

        return pointAverage
    
    def convertPointsToGrades(self, point: int) -> float:
        grade: float = self.gradeDict[point]
       
        return grade
    
    def addPointsToList(self, point: float, mode: bool) -> NoReturn:
        extraText: str = '' if point < 2 else 'e'

        if mode:
            listText: str = f'{point} Punkt{extraText} LK'

        else:
            listText: str = f'{point} Punkt{extraText}'

        self.listWidget.addItem(listText)

    def clear(self) -> NoReturn:
        self.listWidget.clear()
        self.pointList.clear()
        self.gradeList.clear()
        self.lineEdit.clear()
        self.tickBox.setChecked(False)
        self.label1.setText('Eingegebener Punkt:')
        self.label2.setText(f'Punktedurchschnitt:')
        self.label3.setText(f'Notendurchschnitt:')

        if 'myPoints.txt' in listdir():
            remove('myPoints.txt')
        
    def softReset(self) -> NoReturn:
        self.lineEdit.clear()
        self.tickBox.setChecked(False)
    
    def getListItems(self) -> List[str]:
        itemsInWidget: List[str] = [self.listWidget.item(index).text() for index in range(self.listWidget.count())]

        return itemsInWidget

    def savePoints(self) -> NoReturn:
        if len(self.pointList) != 0:
            with open('myPoints.txt', 'a+') as file:
                classCounter: int = 0
                points: List[str] = self.getListItems()
                pointAverage: str = self.label2.text()
                gradeAverage: str = self.label3.text()

                for point in points:
                    classCounter += 1
                    file.write(f'Kurs {classCounter}: {point}\n')

                file.write(f'\n{gradeAverage}\n{pointAverage}')
            
            startfile('myPoints.txt')
        
    def getValues(self) -> NoReturn:
        point: int = self.getGradeInput()

        if point != None:
            if point > 15:
                self.softReset()

            if not point > 15:
                mode: bool = self.getTickBox()

                pointAverage: float = self.calculateAverage(point, self.pointList, mode)
                grade: int = self.convertPointsToGrades(point)
                gradeAverage: float = self.calculateAverage(grade, self.gradeList, mode)

                self.changeLabelText(pointAverage, point, gradeAverage, mode)
                self.softReset()
                
      
        

