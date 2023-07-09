from controller import TreatmentProccessController, TreatmentController


class CommandParser:
    def __init__(self, treatment_process_controller: TreatmentProccessController, treatment_controller: TreatmentController):
        self.treatment_process_controller = treatment_process_controller
        self.treatment_controller = treatment_controller

    def parse(self, command: str):
        if '@' not in command:
            raise Exception("Unauthorized")

        patient_id = int(command.split('@')[0])
        command = command.split('@')[1]
        if 'list treatment processes' in command:
            return str(self.treatment_process_controller.list_treatment_processes(
                patient_id=patient_id
            ))

        if 'list medical info types ' in command:
            return str(self.treatment_process_controller.get_treatment_process(
                patient_id=patient_id,
                treatment_process_id=int(command.split(' ')[-1])
            ).list_medical_info())

        if 'make new treatment ' in command:
            return str(self.treatment_controller.make_new_treatment(
                patient_id=patient_id,
                treatment_process_id=int(command.split(':')[0].split(' ')[-1]),
                medical_informations=[
                    tuple(namevalue.split('%'))
                    for namevalue in command.split(':')[1].split(' ')
                ]
            ))
