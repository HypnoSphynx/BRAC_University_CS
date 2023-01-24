doctordict={}
class Hospital:
    def __init__(self,hospital):
        self.hospital=hospital
        self.doctor_dict={}
        self.patient_dict={}

    def addDoctor(self,value):

        self.doctor_dict.update({value.id:[value.name,value.special]})

    def addPatient(self,value):
        self.patient_dict.update({value.id:[value.name,value.age,value.phone]})
    
    def getDoctorByID(self,id):
        for key,value in self.doctor_dict.items():
            if key==id:
                return(f"Doctor's ID: {key}\nName:{value[0]}\nSpeciality:{value[1]}")
    def getPatientByID(self,id):
        for key,value in self.patient_dict.items():
            if key==id:
                return(f"Patients's ID: {key}\nName:{value[0]}\nAge:{value[1]}\nPhone no.:{value[2]}")
    def allDoctors(self):
        print('All Doctors:')
        print(f'Number of Doctors: {len(self.doctor_dict)}')
        print(self.doctor_dict)
    
    def allPatients(self):
        print('All Patients:')
        print(f'Number of Patients: {len(self.patient_dict)}')
        print(self.patient_dict)


class Doctor:
    def __init__(self,*args):
        self.id=args[0]
        self.name=args[2]
        self.special=args[3]

class Patient:
    def __init__(self, *args):
        self.id=args[0]
        self.name=args[2]
        self.age=args[3]
        self.phone=args[4]
   
h = Hospital("Evercare")
d1 = Doctor("1d","Doctor", "Samar Kumar", "Neurologist")
h.addDoctor(d1)
print("=================================")
print(h.getDoctorByID("1d"))
print("=================================")
p1 = Patient("1p","Patient", "Kashem Ahmed", 35, 12345)
h.addPatient(p1)
print("=================================")
print(h.getPatientByID("1p"))
print("=================================")
p2 = Patient ("2p","Patient", "Tanina Haque", 26, 33456)
h.addPatient(p2)
print("=================================")
print(h.getPatientByID("2p"))
print("=================================")
h.allDoctors()
h.allPatients()
 

         
    








