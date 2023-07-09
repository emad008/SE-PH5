from storage import Column, Table, Database, Initializer, DataSource
from repository import Repository
from model import TreatmentProcess, Patient, MedicalInfoType, MedicalInfoTypeTreatmentProcessRelation, \
    Treatment, MedicalInfo, Payment, HealthExpert
from parsers import CommandParser
from controller import TreatmentProccessController, TreatmentController


class Main:
    def __init__(self) -> None:
        self.database = Database(
            [
                Table(
                    "treatment_process",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'name'
                        ),
                        Column(
                            'approvement_status'
                        ),
                        Column(
                            'description'
                        ),
                        Column(
                            'reject_reason'
                        ),
                        Column(
                            'price',
                            data_type='integer'
                        )
                    ]
                ),
                Table(
                    "patient",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'first_name'
                        ),
                        Column(
                            'last_name'
                        ),
                        Column(
                            'balance',
                            data_type='integer'
                        )
                    ]
                ),
                Table(
                    "medical_info_type",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'name'
                        ),
                        Column(
                            'type'
                        )
                    ]
                ),
                Table(
                    "medical_info_type_treatment_process_relation",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'treatment_process_id',
                            data_type='integer'
                        ),
                        Column(
                            'medical_info_type_id',
                            data_type='integer'
                        )
                    ]
                ),
                Table(
                    "medical_info",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'patient_id',
                            data_type='integer'
                        ),
                        Column(
                            'medical_information_type_id',
                            data_type='integer'
                        ),
                        Column(
                            'data'
                        )
                    ]
                ),
                Table(
                    "payment",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'patient_id',
                            data_type='integer'
                        ),
                        Column(
                            'amount',
                            data_type='integer'
                        )
                    ]
                ),
                Table(
                    "treatment",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'patient_id',
                            data_type='integer'
                        ),
                        Column(
                            'treatment_process_id',
                            data_type='integer'
                        ),
                        Column(
                            'payment_id',
                            data_type='integer'
                        ),
                        Column(
                            'assigned_health_expert_id',
                            data_type='integer'
                        ),
                        Column(
                            'length',
                            data_type='integer'
                        )
                    ]
                ),
                Table(
                    "health_expert",
                    [
                        Column(
                            'id',
                            data_type='integer'
                        ),
                        Column(
                            'first_name'
                        ),
                        Column(
                            'last_name',
                        ),
                        Column(
                            'is_busy',
                            data_type='boolean'
                        )
                    ]
                )
            ]
        )

        treatment_process_repository = Repository(
            self.database,
            model=TreatmentProcess
        )

        patient_repository = Repository(
            self.database,
            model=Patient
        )

        medical_info_type_repository = Repository(
            self.database,
            model=MedicalInfoType
        )

        medical_info_type_treatment_process_relation_repository = Repository(
            self.database,
            model=MedicalInfoTypeTreatmentProcessRelation
        )

        treatment_repository = Repository(
            self.database,
            model=Treatment
        )

        medical_info_repository = Repository(
            self.database,
            model=MedicalInfo
        )

        payment_repository = Repository(
            self.database,
            model=Payment
        )

        health_expert_repository = Repository(
            self.database,
            model=HealthExpert
        )

        TreatmentProcess.repo = treatment_process_repository
        Patient.repo = patient_repository
        MedicalInfoType.repo = medical_info_type_repository
        MedicalInfoTypeTreatmentProcessRelation.repo = medical_info_type_treatment_process_relation_repository
        Treatment.repo = treatment_repository
        MedicalInfo.repo = medical_info_repository
        Payment.repo = payment_repository
        HealthExpert.repo = health_expert_repository

        self.initializer = Initializer(
            datasource=DataSource()
        )

        treatment_process_controller = TreatmentProccessController()

        treatment_controller = TreatmentController()

        self.command_parser = CommandParser(
            treatment_process_controller=treatment_process_controller,
            treatment_controller=treatment_controller
        )

    def initialize(self):        
        self.initializer.initialize()

    def run(self):
        self.initialize()
        while True:
            try:
                output = self.command_parser.parse(
                    input()
                )
            except Exception as ex:
                print(ex)
                continue
            if output is None:
                continue
            print(
                output
            )

Main().run()
