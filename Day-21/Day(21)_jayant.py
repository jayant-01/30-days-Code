class statistics:
    def count(self,ages):
        return len(ages)
    def sum(self,ages):
        sum=0
        for i in ages:
            sum=sum+i
        return sum
    def min(self,ages):
        ages.sort()
        return ages[0]
    def max(self,ages):
        ages.sort()
        return ages[-1]
    def range(self,ages):
        return self.max(ages)-self.min(ages)
    
    def mean(self,ages):
        return self.sum(ages)/self.count(ages)
    
    def median(self,ages):
        ages.sort()
        if self.count(ages)%2==0:
            return (ages[self.count(ages)//2]+ages[self.count(ages)//2-1])/2
        else:
            return ages[self.count(ages)//2]
    def mode(self,ages):
        ages.sort()
        count=0
        mode=ages[0]
        for i in ages:
            if ages.count(i)>count:
                count=ages.count(i)
                mode=i
        return mode
    def var(self,ages):
        mean=self.mean(ages)
        sum=0
        for i in ages:
            sum=sum+(i-mean)**2
        return sum/self.count(ages)
    def std(self,ages):
        return self.var(ages)**0.5
    def z_score(self,ages):
        mean=self.mean(ages)
        std=self.std(ages)
        z_score=[]
        for i in ages:
            z_score.append((i-mean)/std)
        return z_score
    def frequency_distribution(self,ages):
        ages.sort()
        return {i:ages.count(i) for i in ages}
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=statistics()
print('Count:', data.count(ages)) 
print('Sum: ', data.sum(ages)) 
print('Min: ', data.min(ages)) 
print('Max: ', data.max(ages)) 
print('Range: ', data.range(ages))
print('Mean: ', data.mean(ages)) 
print('Median: ', data.median(ages)) 
print('Mode: ', data.mode(ages)) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std(ages)) # 4.2
print('Variance: ', data.var(ages))
#print('Z-Score: ', data.z_score(ages))
print('Frequency: ', data.frequency_distribution(ages))


