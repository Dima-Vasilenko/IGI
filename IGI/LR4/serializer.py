from abc import ABC, abstractmethod
import csv
import pickle
import datahandler



gto_norms = {
    "time": 5.2,
    "distance": 1.9
}

user_results = [
    {
        "time": 4.5,
        "distance": 2
    },
    {
        "time": 5.5,
        "distance": 1.4
    },
    {
        "time": 4.2,
        "distance": 1.54
    },
    {
        "time": 4.8,
        "distance": 1.86
    },
    {
        "time": 5.1,
        "distance": 1.99
    },
    {
        "time": 5.3,
        "distance": 2.1
    },
    {
        "time": 4.44,
        "distance": 1.88
    },
    {
        "time": 4.1,
        "distance": 1.95
    },
    {
        "time": 5,
        "distance": 2
    },
    {
        "time": 4.3,
        "distance": 2.03
    }
]

filename = "data.csv"



class Serializer(ABC):
    
    @abstractmethod
    def serialize_data(self, data):
        """Serialize your data"""
        pass
    
    @abstractmethod
    def deserialize(self):
        """Deserialize your data"""
        pass
    
    @abstractmethod
    def get_unsecesfull_users(self):
        """Return list of users that doesnt pass norms"""
        pass

    @abstractmethod
    def amount_of_succesfull_users(self):
        """Amount of users that pass norms"""
        pass

    @abstractmethod
    def most_succesfull(self):
        """List of 3 most succesfull users"""
        pass

class CsvSerializer(Serializer):
    def __init__(self, filename):
        self.filename = filename
    
    def serialize_data(self, data):
        """Serialize your data in csv"""
        with open(self.filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["time", "distance"])
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def deserialize(self):
        """Deserialize your data in csv"""
        data = []
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                data.append(r)
        return data

    def get_unsecesfull_users(self):
        """Return list of users that doesnt pass norms by csv"""
        data = []
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if ((float(r["time"]) <  gto_norms["time"]) or
                    (float(r["distance"]) <  gto_norms["distance"])):
                    data.append(r)
        return data

    def amount_of_succesfull_users(self):
        """Amount of users that pass norms by csv"""
        amount = 0
        with open(self.filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if ((float(r["time"]) >= gto_norms["time"]) or
                    (float(r["distance"]) >=  gto_norms["distance"])):
                    amount += 1
        return amount
    
    def most_succesfull(self):
        """List of 3 most succesfull users by csv"""
        users = self.deserialize()

        def calculate_score(user):
            time_score = -float(user["time"])  
            distance_score = float(user["distance"])
            return time_score + distance_score
        
        best = sorted(users, key=calculate_score, reverse=True)[:3]
        return best

    

class PickleSerializer(Serializer):

    def __init__(self, filename):
        self.filename = filename

    def serialize_data(self, data):
        """Serialize your data in pickle"""
        with open(self.filename, "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self):
        """Deserialize your data in pickle"""
        data = {}
        with open(self.filename, "rb") as fh:
            data = pickle.load(fh)
        return data
    
    def get_unsecesfull_users(self):
        """Return list of users that doesnt pass norms by pickle"""
        unsuccessful_users = []
        with open(self.filename, "rb") as fh:
            data = pickle.load(fh)

        for r in data:
            if ((float(r["time"]) < gto_norms["time"]) or
                (float(r["distance"]) < gto_norms["distance"])):
                unsuccessful_users.append(r)
        return unsuccessful_users
    
    def amount_of_succesfull_users(self):
        """Amount of users that pass norms by pickle"""
        amount = 0
        with open(self.filename, "rb") as fh:
            data = pickle.load(fh)
            for r in data:
                if ((float(r["time"]) >= gto_norms["time"]) or
                    (float(r["distance"]) >=  gto_norms["distance"])):
                    amount += 1
        return amount
    
    def most_succesfull(self):
        """List of 3 most succesfull pickle"""
        users = self.deserialize()

        def calculate_score(user):
            time_score = -float(user["time"])  
            distance_score = float(user["distance"])
            return time_score + distance_score
        
        best = sorted(users, key=calculate_score, reverse=True)[:3]
        return best





class Data:
    def __init__(self, serializer: Serializer):
        self.serializer = serializer

    def get_user(self, data):
        """Get info about user"""
        print("Добавление рузультатов ученика.")
        time = datahandler.DataHandler.get_float("Введите значение времени которое понадобилось вашему ученику для 100м: ")
        distance = datahandler.DataHandler.get_float("Введите значение длины на которое прыгнял ваш ученик: ")
        data.append({"time": time, "distance": distance})


    def execute(self, data):
        """Execute task"""
        self.get_user(data)
        self.serializer.serialize_data(data)
        unsuccessful_users = self.serializer.get_unsecesfull_users()
        print("Список несдавших учеников: ", unsuccessful_users)
        amount = self.serializer.amount_of_succesfull_users()
        print("Количество людей сдавших нормативы: ", amount)
        best = self.serializer.most_succesfull()
        print("Список самых успешных учеников: ", best)