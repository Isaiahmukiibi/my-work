class Patient:
    def __init__(self, id, name, age, gender, contact):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

class Doctor:
    def __init__(self, id, name, specialization, contact):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.contact = contact

class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient '{}' added to the system.".format(patient.name))

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor '{}' added to the system.".format(doctor.name))

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        print("Appointment scheduled for Patient ID '{}' with Doctor ID '{}' on {} at {}.".format(
            appointment.patient_id, appointment.doctor_id, appointment.date, appointment.time))

    def display_patients(self):
        if not self.patients:
            print("No patients found.")
            return

        print("Patient List:")
        for patient in self.patients:
            print("ID: {}, Name: {}, Age: {}, Gender: {}, Contact: {}".format(
                patient.id, patient.name, patient.age, patient.gender, patient.contact))

    def display_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return

        print("Doctor List:")
        for doctor in self.doctors:
            print("ID: {}, Name: {}, Specialization: {}, Contact: {}".format(
                doctor.id, doctor.name, doctor.specialization, doctor.contact))

    def display_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return

        print("Appointment List:")
        for appointment in self.appointments:
            print("Patient ID: {}, Doctor ID: {}, Date: {}, Time: {}".format(
                appointment.patient_id, appointment.doctor_id, appointment.date, appointment.time))


def main():
    hospital = HospitalManagementSystem()

    while True:
        print("\nMENU:")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. Display Patients")
        print("5. Display Doctors")
        print("6. Display Appointments")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            contact = input("Enter patient contact: ")

            patient = Patient(id, name, age, gender, contact)
            hospital.add_patient(patient)
        elif choice == "2":
            id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            contact = input("Enter doctor contact: ")

            doctor = Doctor(id, name, specialization, contact)
            hospital.add_doctor(doctor)
        elif choice == "3":
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date: ")
            time = input("Enter appointment time: ")

            appointment = Appointment(patient_id, doctor_id, date, time)
            hospital.add_appointment(appointment)
        elif choice == "4":
            hospital.display_patients()
        elif choice == "5":
            hospital.display_doctors()
        elif choice == "6":
            hospital.display_appointments()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
