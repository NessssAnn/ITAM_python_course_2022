class Binary:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, other):
        self.other = other
        answer = list()
        numbers = list(map(int, str(self.num)))
        numother = list(map(int, str(self.other)))
        f = 0
        while not len(numbers)==len(numother):
            if len(numbers)<len(numother):
                numbers.insert(0,0)
            elif len(numbers)>len(numother):
                numother.insert(0,0)
        for i in range(len(numbers)-1, -1, -1):
            d = numbers[i]+numother[i]+f
            if d==2:
                answer.append(0)
                f=1
            elif d ==3 :
                answer.append(1)
                f=1
            elif d==1:
                answer.append(1)
                f=0
            elif d==0:
                answer.append(0)
                f=0
        if f==1:
            answer.append(1)
        answer.reverse()
        while answer[0]==0:
            answer.pop(0)
        stranswer = ''.join(str(n) for n in answer)
        self.num = int(stranswer)
        return self.num
    
    def __sub__(self, other):
        self.other = other
        answer = list()
        numbers = list(map(int, str(self.num)))
        numother = list(map(int, str(self.other)))
        f = 0
        while not len(numbers)==len(numother):
            if len(numbers)<len(numother):
                numbers.insert(0,0)
            elif len(numbers)>len(numother):
                numother.insert(0,0)
        for i in range(len(numbers)-1, -1, -1):
            d=numbers[i]-numother[i]-f
            if d==-1:
                answer.append(1)
                f=1
            elif d==0:
                answer.append(0)
                f=0
            elif d==1:
                answer.append(1)
                f=0
            elif d==-2:
                answer.append(0)
                f=1
        answer.reverse()
        if answer[0]==0:
            answer.pop(0)
        stranswer = ''.join(str(n) for n in answer)
        self.num = int(stranswer)
        return self.num

    def __mul__(self, other):
        self.other = other        
        answer = list()
        mas = list()
        numbers = list(map(int, str(self.num)))
        numother = list(map(int, str(self.other)))
        for i in range(len(numother)-1,-1,-1):
            answer.clear()
            for j in range(len(numbers)-1,-1,-1):
                d = numother[i]*numbers[j]
                answer.append(d)
            answer.reverse()
            answer.extend(0 for n in range(i+1))
            stranswer = ''.join(str(n) for n in answer)
            mas.append(stranswer)
        answer.clear()
        mas.reverse()
        dig = int(mas[0])
        mas.pop(0)
        while len(mas)>0:
            dig = Binary(dig).__add__(mas[0])
            mas.pop(0)
        self.num = dig
        return self.num
    
    def __floordiv__(self, other):
        self.other=other
        answer = list()
        mas = list()
        numbers = list(map(int, str(self.num)))
        numother = list(map(int, str(self.other)))
        divisible = list()
        ost = 0
        while self.num>=self.other:
            if not mas:
                for i in range(len(numother)):
                    divisible.append(numbers[0])
                    numbers.pop(0)
            if not divisible:    
                divisible.append(numbers[0])
                numbers.pop(0)
                strdivisible = ''.join(str(n) for n in divisible)
                while int(strdivisible)<self.other:
                    mas.append(0)
                    divisible.append(numbers[0])
                    strdivisible = ''.join(str(n) for n in divisible)
                    numbers.pop(0)
            else:
                strdivisible = ''.join(str(n) for n in divisible)
                flag = 0
                while int(strdivisible)<self.other:
                    flag+=1
                    if flag==1:
                        divisible.append(numbers[0])
                        strdivisible = ''.join(str(n) for n in divisible)
                        numbers.pop(0)
                    elif flag>1:
                        mas.append(0)
                        divisible.append(numbers[0])
                        strdivisible = ''.join(str(n) for n in divisible)
                        numbers.pop(0)
            ost = Binary(int(strdivisible)).__sub__(self.other)
            divisible.clear()
            if ost>0:
                divisible.append(ost)
            mas.append(1)
            answer.clear()
            answer.append(ost)
            for i in range(len(numbers)):
                answer.append(numbers[i])
            stranswer = ''.join(str(n) for n in answer)
            self.num = int(stranswer)
        if len(numbers)>0:
            for i in range(len(numbers)):
                mas.append(0)
        strmas = ''.join(str(n) for n in mas)
        self.num = int(strmas)
        return self.num

    def __str__(self):
        return(str(self.num))
    
a,b = map(int, input().split(" "))

print(Binary(a).__add__(b).__str__())
print(Binary(a).__sub__(b).__str__())
print(Binary(a).__mul__(b).__str__())
print(Binary(a).__floordiv__(b).__str__())






        